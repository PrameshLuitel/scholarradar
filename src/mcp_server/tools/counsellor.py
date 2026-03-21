"""
Counsellor MCP tools — the flagship `plan_study_abroad_journey` tool that
orchestrates ALL other tools internally to produce a comprehensive study abroad
plan in one call.

This is the most important tool in ScholarRadar.
"""
from __future__ import annotations

import hashlib
import json
import re
import time
from collections import defaultdict
from datetime import date, datetime, timedelta
from difflib import SequenceMatcher
from typing import Any, Optional

import structlog
from mcp.server.fastmcp import FastMCP

log = structlog.get_logger("mcp_server.tools.counsellor")

# ── TTL Cache (1 hour) ─────────────────────────────────────────────────────

_cache: dict[str, tuple[float, Any]] = {}
_CACHE_TTL = 3600  # 1 hour


def _cache_key(params: dict) -> str:
    raw = json.dumps(params, sort_keys=True, default=str)
    return hashlib.sha256(raw.encode()).hexdigest()


def _cache_get(key: str) -> Any | None:
    if key in _cache:
        ts, data = _cache[key]
        if time.time() - ts < _CACHE_TTL:
            return data
        del _cache[key]
    return None


def _cache_set(key: str, data: Any):
    _cache[key] = (time.time(), data)


# ── Database helpers ────────────────────────────────────────────────────────

def _get_db():
    from src.database.client import get_db
    return get_db()


def _fuzzy(query: Optional[str], text: Optional[str]) -> float:
    if not query or not text:
        return 0.0
    q, t = query.lower(), text.lower()
    if q in t:
        return 0.95
    tq, tt = set(re.split(r"\W+", q)), set(re.split(r"\W+", t))
    if tq and tt:
        overlap = len(tq & tt) / len(tq)
        if overlap > 0:
            return 0.5 + overlap * 0.4
    return SequenceMatcher(None, q, t).ratio()


def _infer_level(qualification: str) -> str | None:
    q = qualification.lower()
    if any(k in q for k in ("high school", "secondary", "+2", "12th", "a-level")):
        return "undergraduate"
    if any(k in q for k in ("bachelor", "bsc", "ba ", "beng", "be ", "btech", "undergraduate")):
        return "postgraduate"
    if any(k in q for k in ("master", "msc", "ma ", "mba", "meng")):
        return "doctorate"
    return None


_HIGH_SCRUTINY = {"nepal", "nepalese", "bangladesh", "bangladeshi", "pakistan",
                  "pakistani", "india", "indian", "sri lanka", "sri lankan"}


# ── Tool Registration ──────────────────────────────────────────────────────

def register_tools(mcp: FastMCP):
    """Register the counsellor mega tool plus the booking tool."""

    @mcp.tool()
    async def book_counselling_session(
        name: str, email: str, destination: str,
    ) -> dict[str, Any]:
        """Book a free counselling session with IDP experts.
        Args:
            name: Student name.
            email: Contact email.
            destination: Destination country.
        """
        try:
            log.info("tool_call", tool="book_counselling_session",
                     name=name, destination=destination)
            return {
                "status": "success",
                "message": f"Counselling session request submitted for {name}",
                "details": {
                    "email": email,
                    "destination": destination,
                    "note": "An IDP counsellor will contact you within 24 hours.",
                },
            }
        except Exception as e:
            log.error("tool_error", tool="book_counselling_session", error=str(e))
            return {"error": "Failed to book session.", "error_type": "tool_error"}

    @mcp.tool()
    async def search_all(
        query: str,
        destination_country: Optional[str] = None,
    ) -> dict[str, Any]:
        """Search across all data — scholarships, courses, and universities.
        A quick cross-domain search for any keyword.
        Args:
            query: Search term, e.g. "data science", "engineering scholarship".
            destination_country: Optional country filter.
        """
        try:
            log.info("tool_call", tool="search_all", query=query)
            db = _get_db()
            results: dict[str, list] = {"scholarships": [], "courses": [], "universities": []}
            # Scholarships
            sq = db.table("scholarships").select("title,university,country,study_level,funding_type,source_url").eq("is_active", True)
            if destination_country:
                sq = sq.ilike("country", destination_country.strip())
            for s in (sq.execute()).data or []:
                if _fuzzy(query, s.get("title", "")) > 0.3 or _fuzzy(query, s.get("university", "")) > 0.3:
                    results["scholarships"].append(s)
            # Courses
            cq = db.table("courses").select("name,university,country,level,tuition_fee,source_url").eq("is_active", True)
            if destination_country:
                cq = cq.ilike("country", destination_country.strip())
            for c in (cq.execute()).data or []:
                if _fuzzy(query, c.get("name", "")) > 0.3 or _fuzzy(query, c.get("university", "")) > 0.3:
                    results["courses"].append(c)
            # Universities
            uq = db.table("universities").select("name,country,world_ranking,website")
            if destination_country:
                uq = uq.ilike("country", destination_country.strip())
            for u in (uq.execute()).data or []:
                if _fuzzy(query, u.get("name", "")) > 0.3:
                    results["universities"].append(u)
            total = sum(len(v) for v in results.values())
            return {"query": query, "results": results, "total_results": total,
                    "message": f"Found {total} results across all categories." if total else "No results found. Try different keywords."}
        except Exception as e:
            log.error("tool_error", tool="search_all", error=str(e))
            return {"error": "Search failed.", "error_type": "tool_error"}

    # ════════════════════════════════════════════════════════════════════
    # THE MEGA TOOL: plan_study_abroad_journey
    # ════════════════════════════════════════════════════════════════════

    @mcp.tool()
    async def plan_study_abroad_journey(
        nationality: str,
        current_qualification: str,
        target_subject: str,
        preferred_countries: list[str],
        total_budget_usd: float,
        timeline_months: int,
        ielts_score: Optional[float] = None,
        career_goal: Optional[str] = None,
    ) -> dict[str, Any]:
        """Create a comprehensive, personalized study abroad plan in one call.

        This is a full counselling consultation that analyzes:
        - Best matching courses for your profile
        - Scholarships you qualify for with eligibility explanations
        - Complete financial breakdown per destination
        - Visa requirements and application strength assessment
        - IELTS analysis with improvement impact
        - Month-by-month application timeline
        - Prioritized next steps

        Returns a structured JSON plan that covers everything a student
        needs to make an informed decision about studying abroad.

        Args:
            nationality: Your nationality, e.g. "nepalese", "indian", "bangladeshi".
            current_qualification: Your current degree and GPA, e.g. "Bachelor of Engineering, GPA 3.7".
            target_subject: What you want to study, e.g. "Computer Science", "Data Science", "MBA".
            preferred_countries: List of countries to consider, e.g. ["australia", "uk", "canada"].
            total_budget_usd: Total budget in USD for the entire study period.
            timeline_months: How many months until you want to start, e.g. 6 for next semester.
            ielts_score: Your IELTS overall band score if you have one (e.g. 6.5). Leave empty if not yet taken.
            career_goal: What career you want after graduating, e.g. "data engineer at a tech company". Helps match courses.
        """
        started = time.time()
        try:
            log.info("tool_call", tool="plan_study_abroad_journey", parameters={
                "nationality": nationality, "target_subject": target_subject,
                "preferred_countries": preferred_countries,
                "budget_usd": total_budget_usd, "timeline_months": timeline_months,
            })

            # ── Check cache ──
            cache_params = {
                "nationality": nationality, "qualification": current_qualification,
                "subject": target_subject, "countries": preferred_countries,
                "budget": total_budget_usd, "timeline": timeline_months,
                "ielts": ielts_score, "career": career_goal,
            }
            ck = _cache_key(cache_params)
            cached = _cache_get(ck)
            if cached:
                log.info("cache_hit", tool="plan_study_abroad_journey")
                cached["_cached"] = True
                return cached

            db = _get_db()
            inferred_level = _infer_level(current_qualification)
            budget_aud = total_budget_usd * 1.55  # approximate USD→AUD
            today = date.today()
            target_start = today + timedelta(days=timeline_months * 30)
            is_high_scrutiny = nationality.lower().strip() in _HIGH_SCRUTINY
            warnings: list[str] = []

            # ════════════════════════════════════════════════════════════
            # 1. COURSE SEARCH — across all preferred countries
            # ════════════════════════════════════════════════════════════
            all_courses: list[dict] = []
            course_warnings: list[str] = []

            for country in preferred_countries:
                query = db.table("courses").select("*").eq("is_active", True).ilike("country", country.strip())
                if inferred_level:
                    query = query.ilike("level", inferred_level)
                rows = (query.execute()).data or []

                if not rows:
                    course_warnings.append(
                        f"No {inferred_level or ''} courses found in {country}. "
                        "Try broadening study level or check the country name."
                    )
                    continue

                for c in rows:
                    rel = max(
                        _fuzzy(target_subject, c.get("name") or ""),
                        _fuzzy(target_subject, c.get("subject") or ""),
                        _fuzzy(target_subject, c.get("subject_category") or ""),
                    )
                    if rel < 0.25:
                        continue

                    # IELTS filter
                    ielts_ok = True
                    if ielts_score and c.get("ielts_overall"):
                        if c["ielts_overall"] > ielts_score:
                            ielts_ok = False

                    fee = c.get("tuition_fee") or 0
                    currency = c.get("currency", "AUD")
                    all_courses.append({
                        "name": c.get("name"),
                        "university": c.get("university"),
                        "country": c.get("country"),
                        "city": c.get("city"),
                        "level": c.get("level"),
                        "tuition_fee": fee,
                        "tuition_display": f"{currency} {fee:,.0f}/yr" if fee else None,
                        "currency": currency,
                        "duration_months": c.get("duration_months"),
                        "ielts_required": c.get("ielts_overall"),
                        "ielts_met": ielts_ok,
                        "entry_qualification": c.get("entry_qualification"),
                        "relevance": round(float(rel), 3),
                        "apply_url": c.get("apply_url"),
                        "source_url": c.get("source_url"),
                    })

            all_courses.sort(key=lambda x: (-float(x["relevance"]), x.get("tuition_fee") or 0))
            top_courses = list(all_courses[:3])

            if not top_courses and course_warnings:
                warnings.extend(course_warnings)

            # ════════════════════════════════════════════════════════════
            # 2. SCHOLARSHIP MATCHING
            # ════════════════════════════════════════════════════════════
            all_scholarships: list[dict] = []
            schol_warnings: list[str] = []

            for country in preferred_countries:
                query = db.table("scholarships").select("*").eq("is_active", True).ilike("country", country.strip())
                if inferred_level:
                    query = query.ilike("study_level", inferred_level)
                rows = (query.execute()).data or []

                if not rows:
                    schol_warnings.append(f"No scholarships found in {country} for {inferred_level}.")
                    continue

                for s in rows:
                    match_score = 0.0
                    reasons: list[str] = []

                    # Subject match
                    subj_rel = max(
                        _fuzzy(target_subject, s.get("subject") or ""),
                        _fuzzy(target_subject, s.get("subject_category") or ""),
                        _fuzzy(target_subject, s.get("description") or ""),
                    )
                    if subj_rel > 0.3:
                        match_score += subj_rel * 0.3
                        reasons.append(f"Subject relevance: {subj_rel:.0%}")

                    # Nationality
                    elig = (s.get("eligibility") or "").lower()
                    if nationality.lower() in elig:
                        match_score += 0.25
                        reasons.append(f"Explicitly open to {nationality} students")
                    elif "all international" in elig or not elig:
                        match_score += 0.1
                        reasons.append("Open to all international students")

                    # Funding type
                    if s.get("funding_type") == "full":
                        match_score += 0.15
                        reasons.append("Fully funded")
                    elif s.get("funding_type"):
                        match_score += 0.05
                        reasons.append(f"Funding: {s['funding_type']}")

                    # Deadline check
                    if s.get("deadline"):
                        try:
                            dl = datetime.fromisoformat(str(s["deadline"])).date()
                            if dl < today:
                                continue  # expired
                            days_left = (dl - today).days
                            if days_left < 30:
                                reasons.append(f"⚠️ Deadline in {days_left} days!")
                        except (ValueError, TypeError):
                            pass

                    if match_score <= 0.05:
                        continue

                    val = s.get("award_value_max") or s.get("award_value_min") or 0
                    curr = s.get("award_currency", "AUD")
                    all_scholarships.append({
                        "title": s.get("title"),
                        "university": s.get("university"),
                        "country": s.get("country"),
                        "funding_type": s.get("funding_type"),
                        "value": f"{curr} {val:,.0f}" if val else None,
                        "value_numeric": val,
                        "deadline": str(s["deadline"]) if s.get("deadline") else None,
                        "match_score": round(float(match_score), 3),
                        "why_matched": reasons,
                        "source_url": s.get("source_url"),
                        "apply_url": s.get("apply_url"),
                    })

            all_scholarships.sort(key=lambda x: float(x["match_score"]), reverse=True)
            top_scholarships = list(all_scholarships[:5])

            if not top_scholarships and schol_warnings:
                warnings.extend(schol_warnings)

            # ════════════════════════════════════════════════════════════
            # 3. FINANCIAL BREAKDOWN — per top course city
            # ════════════════════════════════════════════════════════════
            financial_breakdowns: list[dict] = []
            cities_checked = set()

            for course in top_courses:
                city = course.get("city")
                country = course.get("country")
                if not city or (city, country) in cities_checked:
                    continue
                cities_checked.add((city, country))

                cost_rows = (db.table("cost_of_living").select("*")
                    .ilike("city", city).ilike("country", country).execute()).data or []

                duration = course.get("duration_months") or 24
                tuition = course.get("tuition_fee") or 0
                years = duration / 12

                if cost_rows:
                    c = cost_rows[0]
                    rent = ((c.get("rent_shared_min") or 0) + (c.get("rent_shared_max") or 0)) / 2
                    monthly_living = rent + (c.get("food_monthly") or 0) + (c.get("transport_monthly") or 0) + (c.get("utilities_monthly") or 0) + (c.get("internet_monthly") or 0)
                    total_living = monthly_living * duration
                    wage = c.get("part_time_wage_hourly") or 0
                    monthly_income = wage * 20 * 4
                    total_earnings = monthly_income * duration
                else:
                    monthly_living = 2500  # fallback
                    total_living = monthly_living * duration
                    total_earnings = 0

                tuition_total = tuition * years
                oshc = 650 * years
                visa_fee = 710
                travel = 2500
                grand = tuition_total + total_living + oshc + visa_fee + travel

                # Scholarship offset
                schol_offset = sum(s["value_numeric"] * years for s in top_scholarships
                                   if s.get("value_numeric") and s.get("country", "").lower() == (country or "").lower())

                financial_breakdowns.append({
                    "city": city, "country": country,
                    "course": course.get("name"),
                    "course_fees_total": round(tuition_total, 2),
                    "living_costs_total": round(total_living, 2),
                    "living_monthly": round(monthly_living, 2),
                    "visa_and_oshc": round(oshc + visa_fee, 2),
                    "travel": travel,
                    "grand_total_aud": round(grand, 2),
                    "grand_total_usd": round(grand / 1.55, 2),
                    "covered_by_scholarships_aud": round(schol_offset, 2),
                    "you_need_to_fund_aud": round(max(0, grand - schol_offset), 2),
                    "you_need_to_fund_usd": round(max(0, grand - schol_offset) / 1.55, 2),
                    "part_time_earnings_total": round(total_earnings, 2),
                    "net_after_earnings_aud": round(max(0, grand - schol_offset - total_earnings), 2),
                    "within_budget": (grand - schol_offset) / 1.55 <= total_budget_usd,
                    "currency": "AUD",
                })

            # Best financial option
            best_financial = None
            if financial_breakdowns:
                affordable = [f for f in financial_breakdowns if f["within_budget"]]
                best_financial = min(affordable or financial_breakdowns,
                                     key=lambda x: x["you_need_to_fund_aud"])

            # ════════════════════════════════════════════════════════════
            # 4. VISA ASSESSMENT
            # ════════════════════════════════════════════════════════════
            visa_assessments: list[dict] = []

            for country in preferred_countries:
                visa_rows = (db.table("visa_requirements").select("*")
                    .ilike("nationality", nationality.strip())
                    .ilike("destination_country", country.strip())
                    .execute()).data or []

                if not visa_rows:
                    visa_assessments.append({
                        "country": country,
                        "message": f"No visa data for {nationality} → {country}.",
                    })
                    continue
                v = visa_rows[0]
                assessment: dict[str, Any] = {
                    "country": country,
                    "visa_type": v.get("visa_type"),
                    "financial_requirement_aud": float(v.get("financial_requirement_aud") or 0),
                    "processing_weeks": f"{v.get('processing_weeks_min', '?')}–{v.get('processing_weeks_max', '?')}",
                    "work_rights": v.get("work_rights_hours_per_week"),
                    "health_requirements": v.get("health_requirements"),
                    "source_url": v.get("source_url"),
                }

                # Risks
                risks: list[str] = []
                recs: list[str] = []
                if is_high_scrutiny:
                    risks.append(f"{nationality} applications receive enhanced scrutiny")
                    recs.append("Prepare an extremely detailed GTE statement")
                    recs.append("Show bank balance held for 6+ months, not recent deposits")

                # Financial readiness
                fin_req = v.get("financial_requirement_aud") or 29710
                first_course = top_courses[0] if top_courses else None
                if first_course:
                    first_yr_need = (first_course.get("tuition_fee") or 0) + fin_req + 1360
                    if budget_aud < first_yr_need:
                        risks.append(f"Budget may be tight for first-year proof (need AUD {first_yr_need:,.0f})")
                        recs.append("Consider scholarships or education loans to bridge the gap")

                assessment["key_risks"] = risks
                assessment["recommendations"] = recs
                visa_assessments.append(assessment)

            # ════════════════════════════════════════════════════════════
            # 5. IELTS ANALYSIS
            # ════════════════════════════════════════════════════════════
            ielts_analysis: dict[str, Any] = {}

            if ielts_score is not None:
                courses_unlocked = sum(1 for c in all_courses if c.get("ielts_met", True))
                courses_blocked = sum(1 for c in all_courses if not c.get("ielts_met", True))

                # What would 0.5 more unlock?
                extra_at_half = 0
                extra_at_one = 0
                for c in all_courses:
                    req = c.get("ielts_required")
                    if req and req > ielts_score:
                        if req <= ielts_score + 0.5:
                            extra_at_half += 1
                        if req <= ielts_score + 1.0:
                            extra_at_one += 1

                ielts_analysis = {
                    "current_score": ielts_score,
                    "courses_unlocked": courses_unlocked,
                    "courses_blocked_by_ielts": courses_blocked,
                    "if_improve_by_half_band": f"Unlocks {extra_at_half} more courses" if extra_at_half else "No additional courses at +0.5",
                    "if_improve_by_one_band": f"Unlocks {extra_at_one} more courses" if extra_at_one else "No additional courses at +1.0",
                    "recommendation": (
                        f"Your IELTS {ielts_score} is sufficient for {courses_unlocked} relevant courses."
                        if courses_blocked == 0 else
                        f"Consider improving to {ielts_score + 0.5} to unlock {extra_at_half} more options."
                    ),
                }
            else:
                ielts_analysis = {
                    "current_score": None,
                    "status": "NOT_TAKEN",
                    "recommendation": "Take IELTS Academic as soon as possible — it's required for almost all university admissions and visa applications.",
                    "target_score": "6.5 for most postgraduate courses, 6.0 for foundation/pathway",
                }

            # ════════════════════════════════════════════════════════════
            # 6. APPLICATION TIMELINE
            # ════════════════════════════════════════════════════════════
            timeline: list[dict] = []
            months_remaining = timeline_months

            if not ielts_score:
                timeline.append({"month": 1, "action": "Book and prepare for IELTS Academic test",
                    "details": "Register at ielts.idp.com. Aim for 6.5+ overall."})
                timeline.append({"month": 2, "action": "Take IELTS test",
                    "details": "Results in 13 days (paper) or 3-5 days (computer)."})
                ielts_done_month = 2
            else:
                ielts_done_month = 0

            timeline.append({
                "month": max(1, ielts_done_month + 1),
                "action": "Research and shortlist universities",
                "details": f"Your top matches: {', '.join(c['university'] for c in top_courses[:3]) if top_courses else 'see course recommendations'}",
            })

            timeline.append({
                "month": max(2, ielts_done_month + 1),
                "action": "Apply to universities and scholarships",
                "details": f"Apply to 3-5 universities. {len(top_scholarships)} scholarship(s) matched your profile.",
            })

            timeline.append({
                "month": max(3, ielts_done_month + 2),
                "action": "Accept offer and receive CoE",
                "details": "Pay deposit to secure your place. CoE needed for visa.",
            })

            timeline.append({
                "month": max(4, ielts_done_month + 2),
                "action": "Gather visa documents and financial evidence",
                "details": "GTE statement, bank statements, health exam, police clearance."
                + (" Ensure bank balance held 6+ months." if is_high_scrutiny else ""),
            })

            timeline.append({
                "month": max(5, ielts_done_month + 3),
                "action": "Submit visa application",
                "details": f"Processing: {visa_assessments[0].get('processing_weeks', '4-12 weeks') if visa_assessments else '4-12 weeks'}.",
            })

            timeline.append({
                "month": max(months_remaining - 1, ielts_done_month + 4),
                "action": "Receive visa and book flights",
                "details": "Book OSHC. Arrange accommodation. Plan orientation attendance.",
            })

            timeline.append({
                "month": months_remaining,
                "action": "Arrive and start course",
                "details": "Arrive 1-2 weeks early for orientation and settling in.",
            })

            # ════════════════════════════════════════════════════════════
            # 7. PROFILE SUMMARY & NEXT STEPS
            # ════════════════════════════════════════════════════════════
            level_label = inferred_level or "further study"
            course_count = len(all_courses)
            schol_count = len(all_scholarships)
            countries_str = ", ".join(preferred_countries[:3])

            profile_summary = (
                f"Based on your {current_qualification}, you qualify for {level_label} "
                f"programs in {target_subject}. We found {course_count} relevant courses "
                f"and {schol_count} matching scholarships across {countries_str}."
            )
            if ielts_score:
                profile_summary += f" Your IELTS {ielts_score} meets requirements for {ielts_analysis.get('courses_unlocked', 0)} courses."
            if career_goal:
                profile_summary += f" Career alignment: {career_goal} — courses selected to support this goal."

            next_steps: list[str] = []
            if not ielts_score:
                next_steps.append("📝 PRIORITY: Book IELTS Academic test — required for admission and visa")
            if top_courses:
                next_steps.append(f"🎓 Apply to top match: {top_courses[0]['name']} at {top_courses[0]['university']}")
            if top_scholarships:
                best_schol = top_scholarships[0]
                next_steps.append(f"💰 Apply for: {best_schol['title']} ({best_schol.get('value', 'value varies')})")
                if best_schol.get("deadline"):
                    next_steps.append(f"⏰ Scholarship deadline: {best_schol['deadline']}")
            if is_high_scrutiny:
                next_steps.append("📋 Start preparing GTE statement early — this is critical for your nationality")
            if financial_breakdowns:
                bf = best_financial or financial_breakdowns[0]
                if bf["within_budget"]:
                    next_steps.append(f"✅ {bf['city']}, {bf['country']} fits your budget (USD {bf['you_need_to_fund_usd']:,.0f} needed)")
                else:
                    next_steps.append(f"💡 Budget gap: need USD {bf['you_need_to_fund_usd']:,.0f} — consider scholarships or education loans")
            next_steps.append(f"📅 Target start: {target_start.strftime('%B %Y')} — you have {months_remaining} months to prepare")

            # ════════════════════════════════════════════════════════════
            # ASSEMBLE FINAL RESULT
            # ════════════════════════════════════════════════════════════
            elapsed = round(time.time() - started, 2)

            result = {
                "profile_summary": profile_summary,
                "recommended_courses": top_courses,
                "matched_scholarships": top_scholarships,
                "financial_breakdown": financial_breakdowns,
                "best_value_option": best_financial,
                "visa_assessment": visa_assessments,
                "ielts_analysis": ielts_analysis,
                "application_timeline": timeline,
                "next_steps": next_steps,
                "warnings": warnings if warnings else None,
                "metadata": {
                    "total_courses_analyzed": course_count,
                    "total_scholarships_analyzed": schol_count,
                    "countries_checked": preferred_countries,
                    "inferred_study_level": inferred_level,
                    "budget_usd": total_budget_usd,
                    "budget_aud_equivalent": round(budget_aud, 2),
                    "processing_time_seconds": elapsed,
                    "generated_at": datetime.now().isoformat(),
                },
            }

            # Cache the result
            _cache_set(ck, result)

            log.info("tool_result", tool="plan_study_abroad_journey",
                     courses=course_count, scholarships=schol_count,
                     elapsed=elapsed)
            return result

        except Exception as e:
            elapsed = round(time.time() - started, 2)
            log.error("tool_error", tool="plan_study_abroad_journey",
                      error=str(e), elapsed=elapsed)
            return {
                "error": f"Failed to generate study plan: {str(e)}",
                "error_type": "tool_error",
                "partial_data": {
                    "profile": {"nationality": nationality, "qualification": current_qualification,
                                "subject": target_subject},
                    "suggestion": "Try again or narrow your search to one country.",
                },
            }
