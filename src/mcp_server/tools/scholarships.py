"""
Scholarship MCP tools — 7 production-quality tools for searching, matching,
comparing, and analyzing scholarship data from the ScholarRadar database.

Each tool returns structured data with source URLs and handles empty results
gracefully. All parameters are validated via Pydantic-style type hints.
"""

from __future__ import annotations

import re
from collections import defaultdict
from datetime import date, datetime, timedelta
from difflib import SequenceMatcher
from typing import Any, Optional

import structlog
from mcp.server.fastmcp import FastMCP

log = structlog.get_logger("mcp_server.tools.scholarships")

# ── Helpers ─────────────────────────────────────────────────────────────────

_VALID_STUDY_LEVELS = {"foundation", "undergraduate", "postgraduate", "doctorate", "vocational"}
_VALID_FUNDING_TYPES = {"full", "partial", "fee_waiver", "stipend", "accommodation"}


def _get_db():
    """Lazy import to avoid startup crash if Supabase isn't configured."""
    from src.database.client import get_db
    return get_db()


def _fetch_active_scholarships(
    country: Optional[str] = None,
    study_level: Optional[str] = None,
    funding_type: Optional[str] = None,
    university: Optional[str] = None,
) -> list[dict[str, Any]]:
    """Fetch active scholarships from Supabase with optional exact-match filters."""
    db = _get_db()
    query = db.table("scholarships").select("*").eq("is_active", True)
    if country:
        query = query.ilike("country", country.strip())
    if study_level:
        query = query.ilike("study_level", study_level.strip())
    if funding_type:
        query = query.ilike("funding_type", funding_type.strip())
    if university:
        query = query.ilike("university", f"%{university.strip()}%")
    response = query.execute()
    data: list[dict[str, Any]] = response.data or []
    return data


def _fuzzy_score(query: Optional[str], text: Optional[str]) -> float:
    """Return a 0.0–1.0 fuzzy-match score between query and text."""
    if query is None or text is None:
        return 0.0
    query_str: str = query.lower()
    text_str: str = text.lower()
    # Exact substring match gets a high score
    if query_str in text_str:
        return 0.95
    # Token overlap
    query_tokens = set(re.split(r"\W+", query_str))
    text_tokens = set(re.split(r"\W+", text_str))
    if query_tokens and text_tokens:
        overlap = len(query_tokens & text_tokens) / len(query_tokens)
        if overlap > 0:
            return 0.5 + overlap * 0.4
    # Sequence matcher fallback
    return SequenceMatcher(None, query_str, text_str).ratio()


def _scholarship_summary(s: dict[str, Any]) -> dict[str, Any]:
    """Create a clean summary dict for one scholarship record."""
    value_display = None
    if s.get("award_value_min") or s.get("award_value_max"):
        currency = s.get("award_currency", "AUD")
        v_min = s.get("award_value_min")
        v_max = s.get("award_value_max")
        if v_min and v_max and v_min != v_max:
            value_display = f"{currency} {v_min:,.0f} – {v_max:,.0f}"
        elif v_max:
            value_display = f"{currency} {v_max:,.0f}"
        elif v_min:
            value_display = f"{currency} {v_min:,.0f}"

    days_remaining = None
    if s.get("deadline"):
        try:
            dl = s["deadline"] if isinstance(s["deadline"], date) else datetime.fromisoformat(str(s["deadline"])).date()
            days_remaining = (dl - date.today()).days
        except (ValueError, TypeError):
            pass

    return {
        "id": s.get("id"),
        "title": s.get("title"),
        "university": s.get("university"),
        "country": s.get("country"),
        "city": s.get("city"),
        "study_level": s.get("study_level"),
        "subject": s.get("subject"),
        "subject_category": s.get("subject_category"),
        "funding_type": s.get("funding_type"),
        "value": value_display,
        "award_value_min": s.get("award_value_min"),
        "award_value_max": s.get("award_value_max"),
        "award_currency": s.get("award_currency"),
        "deadline": str(s["deadline"]) if s.get("deadline") else None,
        "days_remaining": days_remaining,
        "eligibility": s.get("eligibility"),
        "description": s.get("description"),
        "apply_url": s.get("apply_url"),
        "source": s.get("source"),
        "source_url": s.get("source_url"),
    }


def _empty_result(message: str) -> dict[str, Any]:
    """Return a structured empty-result response with a helpful message."""
    return {
        "results": [],
        "total_count": 0,
        "message": message,
    }


# ── Tool Registration ──────────────────────────────────────────────────────


def register_tools(mcp: FastMCP):
    """Register all 7 scholarship tools with the MCP server."""

    # ────────────────────────────────────────────────────────────────────
    # 1. search_scholarships
    # ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    async def search_scholarships(
        nationality: str,
        destination_country: Optional[str] = None,
        study_level: Optional[str] = None,
        subject: Optional[str] = None,
        min_value_aud: Optional[float] = None,
        deadline_after: Optional[str] = None,
        funding_type: Optional[str] = None,
    ) -> dict[str, Any]:
        """Search for scholarships available to students of a given nationality.

        Filters by destination country, study level, subject (fuzzy match),
        minimum award value, upcoming deadlines, and funding type.
        Returns the top 20 matches ranked by relevance score.

        Args:
            nationality: Student's nationality, e.g. "nepalese", "indian", "chinese".
            destination_country: Country where the scholarship is offered, e.g. "australia", "uk".
            study_level: One of: foundation, undergraduate, postgraduate, doctorate, vocational.
            subject: Subject area to match (fuzzy), e.g. "computer science", "engineering".
            min_value_aud: Minimum scholarship value in AUD. Only returns awards >= this amount.
            deadline_after: ISO date string (YYYY-MM-DD). Only returns scholarships with deadlines after this date.
            funding_type: One of: full, partial, fee_waiver, stipend, accommodation.
        """
        try:
            log.info("tool_call", tool="search_scholarships", parameters={
                "nationality": nationality, "destination_country": destination_country,
                "study_level": study_level, "subject": subject,
                "min_value_aud": min_value_aud, "deadline_after": deadline_after,
                "funding_type": funding_type,
            })

            rows = _fetch_active_scholarships(
                country=destination_country,
                study_level=study_level,
                funding_type=funding_type,
            )

            if not rows:
                return _empty_result(
                    f"No active scholarships found"
                    + (f" in {destination_country}" if destination_country else "")
                    + ". Try broadening your filters."
                )

            # Parse deadline_after
            cutoff_date = None
            if deadline_after:
                try:
                    cutoff_date = datetime.fromisoformat(deadline_after).date()
                except ValueError:
                    return {"error": f"Invalid date format: {deadline_after}. Use YYYY-MM-DD.", "error_type": "validation_error"}

            scored: list[tuple[float, dict[str, Any]]] = []
            for s in rows:
                score = 0.5  # base relevance

                # Filter: deadline
                if cutoff_date and s.get("deadline"):
                    try:
                        dl = datetime.fromisoformat(str(s["deadline"])).date()
                        if dl < cutoff_date:
                            continue
                    except (ValueError, TypeError):
                        pass

                # Filter: min value
                if min_value_aud is not None:
                    max_val: float = float(s.get("award_value_max") or s.get("award_value_min") or 0)
                    if max_val < min_value_aud:
                        continue

                # Score: subject fuzzy match
                if subject:
                    subj_score = max(
                        _fuzzy_score(subject, s.get("subject") or ""),
                        _fuzzy_score(subject, s.get("subject_category") or ""),
                        _fuzzy_score(subject, s.get("description") or ""),
                    )
                    if subj_score < 0.2:
                        continue  # not relevant enough
                    score += subj_score * 0.3

                # Score: nationality mention in eligibility
                if nationality and s.get("eligibility"):
                    if nationality.lower() in s["eligibility"].lower():
                        score += 0.2
                    elif "all international" in s["eligibility"].lower():
                        score += 0.1

                # Score: funding type bonus (full funding = higher relevance)
                if s.get("funding_type") == "full":
                    score += 0.1

                # Score: has deadline (more concrete = more relevant)
                if s.get("deadline"):
                    score += 0.05

                # Score: has value info
                final_score = float(min(score, 1.0))
                scored.append((round(final_score, 3), s))

            scored.sort(key=lambda x: x[0], reverse=True)
            top_20 = scored[:20]

            results = []
            for relevance, s in top_20:
                item = _scholarship_summary(s)
                item["relevance_score"] = relevance
                results.append(item)

            log.info("tool_result", tool="search_scholarships", result_count=len(results))
            return {
                "results": results,
                "total_count": len(scored),
                "showing": len(results),
                "filters_applied": {
                    "nationality": nationality,
                    "destination_country": destination_country,
                    "study_level": study_level,
                    "subject": subject,
                    "min_value_aud": min_value_aud,
                    "deadline_after": deadline_after,
                    "funding_type": funding_type,
                },
            }

        except Exception as e:
            log.error("tool_error", tool="search_scholarships", error=str(e))
            return {"error": "Failed to search scholarships. Please try again.", "error_type": "tool_error"}

    # ────────────────────────────────────────────────────────────────────
    # 2. match_profile
    # ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    async def match_profile(
        nationality: str,
        current_qualification: str,
        target_subject: str,
        target_country: str,
        ielts_score: float,
        gpa: Optional[float] = None,
    ) -> dict[str, Any]:
        """Find the top 10 scholarships that best match a specific student profile.

        Scores each scholarship on eligibility fit and returns match reasons
        plus an estimated likelihood of success.

        Args:
            nationality: Student's nationality, e.g. "nepalese", "bangladeshi".
            current_qualification: Student's current degree, e.g. "bachelors in computer science".
            target_subject: Subject they want to study, e.g. "data science", "MBA".
            target_country: Country they want to study in, e.g. "australia", "uk".
            ielts_score: Student's overall IELTS band score (e.g. 7.0).
            gpa: Student's GPA on a 4.0 scale (optional).
        """
        try:
            log.info("tool_call", tool="match_profile", parameters={
                "nationality": nationality, "current_qualification": current_qualification,
                "target_subject": target_subject, "target_country": target_country,
                "ielts_score": ielts_score, "gpa": gpa,
            })

            # Infer study level from current qualification
            qual_lower = current_qualification.lower()
            inferred_level = None
            if any(k in qual_lower for k in ("high school", "secondary", "a-level", "slc", "+2", "12th")):
                inferred_level = "undergraduate"
            elif any(k in qual_lower for k in ("bachelor", "undergraduate", "bsc", "ba ", "beng")):
                inferred_level = "postgraduate"
            elif any(k in qual_lower for k in ("master", "msc", "ma ", "mba", "meng")):
                inferred_level = "doctorate"

            rows = _fetch_active_scholarships(country=target_country)

            if not rows:
                return _empty_result(
                    f"No active scholarships found in {target_country}. "
                    "Try a different destination country."
                )

            scored: list[tuple[float, dict, list[str]]] = []
            for s in rows:
                match_score = 0.0
                reasons: list[str] = []

                # Study level match
                if inferred_level and s.get("study_level"):
                    if s["study_level"].lower() == inferred_level:
                        match_score += 0.25
                        reasons.append(f"Study level matches ({s['study_level']})")
                    else:
                        continue  # Wrong level, skip

                # Subject match
                subj_score = max(
                    _fuzzy_score(target_subject, s.get("subject") or ""),
                    _fuzzy_score(target_subject, s.get("subject_category") or ""),
                    _fuzzy_score(target_subject, s.get("description") or ""),
                )
                if subj_score > 0.3:
                    match_score += subj_score * 0.25
                    reasons.append(f"Subject relevance: {subj_score:.0%}")

                # Nationality eligibility
                elig = (s.get("eligibility") or "").lower()
                if nationality.lower() in elig:
                    match_score += 0.2
                    reasons.append(f"Explicitly mentions {nationality} students")
                elif "all international" in elig:
                    match_score += 0.1
                    reasons.append("Open to all international students")
                elif elig and nationality.lower() not in elig and "all" not in elig:
                    # Nationality is specifically excluded
                    match_score -= 0.3
                    reasons.append("May have nationality restrictions — check eligibility")

                # Funding type bonus
                if s.get("funding_type") == "full":
                    match_score += 0.1
                    reasons.append("Fully funded scholarship")
                elif s.get("funding_type") == "partial":
                    match_score += 0.05
                    reasons.append("Partial funding")

                # Deadline check (still open?)
                if s.get("deadline"):
                    try:
                        dl = datetime.fromisoformat(str(s["deadline"])).date()
                        if dl < date.today():
                            continue  # Expired
                        days_left = (dl - date.today()).days
                        if days_left < 30:
                            reasons.append(f"⚠️ Deadline in {days_left} days — apply soon!")
                    except (ValueError, TypeError):
                        pass

                # Academic merit indicators
                if gpa is not None and gpa >= 3.5:
                    if "academic" in elig or "merit" in elig or "excellence" in elig:
                        match_score += 0.1
                        reasons.append("GPA qualifies for merit-based criteria")

                if match_score <= 0:
                    continue

                # Estimate likelihood
                likelihood = "low"
                if match_score >= 0.7:
                    likelihood = "high"
                elif match_score >= 0.4:
                    likelihood = "medium"

                final_mscore = float(min(match_score, 1.0))
                scored.append((round(final_mscore, 3), s, reasons, likelihood))

            scored.sort(key=lambda x: x[0], reverse=True)
            top_10 = scored[:10]

            results = []
            for match_score, s, reasons, likelihood in top_10:
                item = _scholarship_summary(s)
                item["match_score"] = match_score
                item["match_reasons"] = reasons
                item["likelihood_of_success"] = likelihood
                results.append(item)

            log.info("tool_result", tool="match_profile", result_count=len(results))
            return {
                "results": results,
                "total_matches": len(scored),
                "showing": len(results),
                "student_profile": {
                    "nationality": nationality,
                    "current_qualification": current_qualification,
                    "inferred_target_level": inferred_level,
                    "target_subject": target_subject,
                    "target_country": target_country,
                    "ielts_score": ielts_score,
                    "gpa": gpa,
                },
            }

        except Exception as e:
            log.error("tool_error", tool="match_profile", error=str(e))
            return {"error": "Failed to match profile. Please try again.", "error_type": "tool_error"}

    # ────────────────────────────────────────────────────────────────────
    # 3. get_closing_soon
    # ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    async def get_closing_soon(
        days: int = 30,
        destination_country: Optional[str] = None,
    ) -> dict[str, Any]:
        """Get scholarships with deadlines closing within the next N days.

        Results are sorted by deadline ascending (soonest first).
        Each result includes a days_remaining field.

        Args:
            days: Number of days to look ahead (default 30). E.g. 14 for next two weeks.
            destination_country: Optional country filter, e.g. "australia", "canada".
        """
        try:
            log.info("tool_call", tool="get_closing_soon", parameters={
                "days": days, "destination_country": destination_country,
            })

            rows = _fetch_active_scholarships(country=destination_country)
            today = date.today()
            cutoff = today + timedelta(days=days)

            closing: list[tuple[int, dict]] = []
            for s in rows:
                if not s.get("deadline"):
                    continue
                try:
                    dl = datetime.fromisoformat(str(s["deadline"])).date()
                except (ValueError, TypeError):
                    continue
                if today <= dl <= cutoff:
                    days_remaining = (dl - today).days
                    closing.append((days_remaining, s))

            closing.sort(key=lambda x: x[0])

            if not closing:
                return _empty_result(
                    f"No scholarships closing within the next {days} days"
                    + (f" in {destination_country}" if destination_country else "")
                    + ". Try increasing the number of days."
                )

            results = []
            for days_remaining, s in closing:
                item = _scholarship_summary(s)
                item["days_remaining"] = days_remaining
                item["urgency"] = "critical" if days_remaining <= 7 else ("urgent" if days_remaining <= 14 else "upcoming")
                results.append(item)

            log.info("tool_result", tool="get_closing_soon", result_count=len(results))
            return {
                "results": results,
                "total_count": len(results),
                "period_days": days,
                "destination_country": destination_country,
            }

        except Exception as e:
            log.error("tool_error", tool="get_closing_soon", error=str(e))
            return {"error": "Failed to fetch closing scholarships.", "error_type": "tool_error"}

    # ────────────────────────────────────────────────────────────────────
    # 4. get_fully_funded
    # ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    async def get_fully_funded(
        destination_country: str,
        study_level: Optional[str] = None,
    ) -> dict[str, Any]:
        """Get only fully-funded scholarships that cover full tuition and living expenses.

        Fully funded means the funding_type is 'full'. These typically cover
        tuition fees, living allowance, and sometimes travel costs.

        Args:
            destination_country: Country where the scholarship is offered, e.g. "australia".
            study_level: Optional level filter: foundation, undergraduate, postgraduate, doctorate.
        """
        try:
            log.info("tool_call", tool="get_fully_funded", parameters={
                "destination_country": destination_country, "study_level": study_level,
            })

            rows = _fetch_active_scholarships(
                country=destination_country,
                study_level=study_level,
                funding_type="full",
            )

            if not rows:
                return _empty_result(
                    f"No fully-funded scholarships found in {destination_country}"
                    + (f" for {study_level} level" if study_level else "")
                    + ". Try checking partial scholarships or fee waivers too."
                )

            results = [_scholarship_summary(s) for s in rows]
            # Sort: those with deadlines first, then by value
            results.sort(key=lambda x: (
                x["deadline"] is None,
                x["deadline"] or "9999",
            ))

            log.info("tool_result", tool="get_fully_funded", result_count=len(results))
            return {
                "results": results,
                "total_count": len(results),
                "destination_country": destination_country,
                "study_level": study_level,
            }

        except Exception as e:
            log.error("tool_error", tool="get_fully_funded", error=str(e))
            return {"error": "Failed to fetch fully funded scholarships.", "error_type": "tool_error"}

    # ────────────────────────────────────────────────────────────────────
    # 5. get_by_university
    # ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    async def get_by_university(
        university_name: str,
    ) -> dict[str, Any]:
        """Get all active scholarships offered by a specific university.

        Uses fuzzy matching on the university name so partial names work
        (e.g. "Melbourne" will match "University of Melbourne").

        Args:
            university_name: Full or partial university name, e.g. "University of Sydney", "ANU".
        """
        try:
            log.info("tool_call", tool="get_by_university", parameters={
                "university_name": university_name,
            })

            rows = _fetch_active_scholarships(university=university_name)

            if not rows:
                return _empty_result(
                    f"No active scholarships found for '{university_name}'. "
                    "Try a different spelling or the university's full name."
                )

            results = [_scholarship_summary(s) for s in rows]
            # Sort by value descending
            results.sort(key=lambda x: x.get("award_value_max") or 0, reverse=True)

            # Summary of unique values
            universities_found = list({r["university"] for r in results})

            log.info("tool_result", tool="get_by_university", result_count=len(results))
            return {
                "results": results,
                "total_count": len(results),
                "universities_matched": universities_found,
                "university_query": university_name,
            }

        except Exception as e:
            log.error("tool_error", tool="get_by_university", error=str(e))
            return {"error": "Failed to fetch university scholarships.", "error_type": "tool_error"}

    # ────────────────────────────────────────────────────────────────────
    # 6. compare_scholarship_options
    # ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    async def compare_scholarship_options(
        nationality: str,
        country1: str,
        country2: str,
        study_level: str,
    ) -> dict[str, Any]:
        """Compare scholarship availability between two countries side by side.

        Shows total count, funding types, value ranges, and deadline summary
        for each country so the student can make an informed decision.

        Args:
            nationality: Student's nationality, e.g. "nepalese".
            country1: First country to compare, e.g. "australia".
            country2: Second country to compare, e.g. "uk".
            study_level: Study level: foundation, undergraduate, postgraduate, doctorate.
        """
        try:
            log.info("tool_call", tool="compare_scholarship_options", parameters={
                "nationality": nationality, "country1": country1,
                "country2": country2, "study_level": study_level,
            })

            def _analyze_country(rows: list[dict[str, Any]], country: str) -> dict[str, Any]:
                if not rows:
                    return {
                        "country": country,
                        "total_scholarships": 0,
                        "message": f"No scholarships found in {country} for {study_level}.",
                    }

                funding_breakdown: defaultdict[str, int] = defaultdict(int)
                values: list[float] = []
                deadlines: list[str] = []
                nationality_eligible = 0
                sources: defaultdict[str, int] = defaultdict(int)

                for s in rows:
                    ft_key: str = str(s.get("funding_type") or "unknown")
                    funding_breakdown[ft_key] += 1

                    if s.get("award_value_max"):
                        values.append(float(s["award_value_max"]))

                    if s.get("deadline"):
                        deadlines.append(str(s["deadline"]))

                    elig = (s.get("eligibility") or "").lower()
                    if nationality.lower() in elig or "all international" in elig or not elig:
                        nationality_eligible += 1

                    src_key: str = str(s.get("source") or "unknown")
                    sources[src_key] += 1

                avg_value = sum(values) / len(values) if values else 0.0
                next_deadline = min(deadlines) if deadlines else None

                top_3 = list(sorted(rows, key=lambda x: x.get("award_value_max") or 0.0, reverse=True)[:3])

                return {
                    "country": country,
                    "total_scholarships": len(rows),
                    "eligible_for_nationality": nationality_eligible,
                    "funding_breakdown": dict(funding_breakdown),
                    "value_range": {
                        "min": min(values) if values else None,
                        "max": max(values) if values else None,
                        "average_value": round(float(avg_value), 2) if avg_value > 0 else None,
                        "currency": rows[0].get("award_currency", "AUD") if rows else None,
                    },
                    "deadlines": {
                        "total_with_deadline": len(deadlines),
                        "next_deadline": next_deadline,
                    },
                    "sources": dict(sources),
                    "top_scholarships": [_scholarship_summary(s) for s in top_3],
                }

            rows1 = _fetch_active_scholarships(country=country1, study_level=study_level)
            rows2 = _fetch_active_scholarships(country=country2, study_level=study_level)

            analysis1 = _analyze_country(rows1, country1)
            analysis2 = _analyze_country(rows2, country2)

            # Recommendation
            total1 = analysis1.get("total_scholarships", 0)
            total2 = analysis2.get("total_scholarships", 0)
            recommendation = None
            if total1 > total2 * 1.5:
                recommendation = f"{country1} has significantly more scholarship options ({total1} vs {total2})."
            elif total2 > total1 * 1.5:
                recommendation = f"{country2} has significantly more scholarship options ({total2} vs {total1})."
            else:
                recommendation = f"Both countries have similar scholarship availability ({total1} vs {total2}). Compare values and eligibility."

            log.info("tool_result", tool="compare_scholarship_options",
                     count1=total1, count2=total2)
            return {
                "comparison": {country1: analysis1, country2: analysis2},
                "recommendation": recommendation,
                "student_profile": {
                    "nationality": nationality,
                    "study_level": study_level,
                },
            }

        except Exception as e:
            log.error("tool_error", tool="compare_scholarship_options", error=str(e))
            return {"error": "Failed to compare scholarship options.", "error_type": "tool_error"}

    # ────────────────────────────────────────────────────────────────────
    # 7. get_scholarship_statistics
    # ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    async def get_scholarship_statistics(
        destination_country: str,
        nationality: str,
    ) -> dict[str, Any]:
        """Get aggregated statistics about available scholarships for a country.

        Returns total available, total value, average award amount,
        breakdown by study level and funding type, and deadline distribution.

        Args:
            destination_country: Country to analyze, e.g. "australia", "uk".
            nationality: Student's nationality to check eligibility counts, e.g. "nepalese".
        """
        try:
            log.info("tool_call", tool="get_scholarship_statistics", parameters={
                "destination_country": destination_country, "nationality": nationality,
            })

            rows = _fetch_active_scholarships(country=destination_country)

            if not rows:
                return _empty_result(
                    f"No active scholarships found in {destination_country}. "
                    "Statistics cannot be generated."
                )

            # Aggregations
            values: list[float] = []
            by_level: defaultdict[str, int] = defaultdict(int)
            by_funding: defaultdict[str, int] = defaultdict(int)
            by_source: defaultdict[str, int] = defaultdict(int)
            nationality_eligible = 0
            deadline_buckets: dict[str, int] = {
                "closing_within_7_days": 0,
                "closing_within_30_days": 0,
                "closing_within_90_days": 0,
                "closing_later": 0,
                "no_deadline_specified": 0,
            }
            today = date.today()

            for s in rows:
                # Values
                if s.get("award_value_max"):
                    values.append(float(s["award_value_max"]))
                elif s.get("award_value_min"):
                    values.append(float(s["award_value_min"]))

                # Level breakdown
                level_key = str(s.get("study_level") or "unspecified")
                by_level[level_key] += 1

                # Funding breakdown
                ft_key = str(s.get("funding_type") or "unspecified")
                by_funding[ft_key] += 1

                # Source breakdown
                src_key = str(s.get("source") or "unknown")
                by_source[src_key] += 1

                # Nationality eligibility
                elig = (s.get("eligibility") or "").lower()
                if nationality.lower() in elig or "all international" in elig or not elig:
                    nationality_eligible += 1

                # Deadline distribution
                if s.get("deadline"):
                    try:
                        dl = datetime.fromisoformat(str(s["deadline"])).date()
                        days_left = (dl - today).days
                        if days_left < 0:
                            pass  # expired, still counted in total
                        elif days_left <= 7:
                            deadline_buckets["closing_within_7_days"] += 1
                        elif days_left <= 30:
                            deadline_buckets["closing_within_30_days"] += 1
                        elif days_left <= 90:
                            deadline_buckets["closing_within_90_days"] += 1
                        else:
                            deadline_buckets["closing_later"] += 1
                    except (ValueError, TypeError):
                        deadline_buckets["no_deadline_specified"] += 1
                else:
                    deadline_buckets["no_deadline_specified"] += 1

            total_value = sum(values) if values else 0.0
            avg_value = total_value / len(values) if values else 0.0

            log.info("tool_result", tool="get_scholarship_statistics",
                     total=len(rows), eligible=nationality_eligible)
            return {
                "destination_country": destination_country,
                "nationality": nationality,
                "total_available": len(rows),
                "eligible_for_nationality": nationality_eligible,
                "value_statistics": {
                    "total_value": round(float(total_value), 2),
                    "average_award": round(float(avg_value), 2),
                    "min_award": round(float(min(values)), 2) if values else None,
                    "max_award": round(float(max(values)), 2) if values else None,
                    "scholarships_with_value": len(values),
                    "currency": "AUD",
                },
                "by_study_level": dict(sorted(by_level.items(), key=lambda x: x[1], reverse=True)),
                "by_funding_type": dict(sorted(by_funding.items(), key=lambda x: x[1], reverse=True)),
                "by_source": dict(sorted(by_source.items(), key=lambda x: x[1], reverse=True)),
                "deadline_distribution": deadline_buckets,
            }

        except Exception as e:
            log.error("tool_error", tool="get_scholarship_statistics", error=str(e))
            return {"error": "Failed to generate statistics.", "error_type": "tool_error"}
