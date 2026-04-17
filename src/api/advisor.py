"""
FindUni AI Advisor API — The core endpoint that powers skolr.xyz/finduni.

Accepts a student's CV (optional PDF) + profile data, queries the entire
ScholarRadar database for matching opportunities, and streams a deeply
personalized study abroad plan through Groq LLMs.

Architecture:
  1. Parse CV PDF → extract text + structured profile
  2. NEW: /parse-cv endpoint → returns extracted fields for frontend auto-fill
  3. LLM-powered subject expansion for semantic database queries
  4. Smart scholarship matching with eligibility analysis
  5. Stream response via Groq cascade (6 models, guaranteed response)
  6. Return SSE stream to frontend with structured data + AI analysis
"""

from __future__ import annotations

import json
import re
import time
from collections import defaultdict
from datetime import date, datetime, timedelta
from difflib import SequenceMatcher
from typing import Any, Optional

import structlog
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import StreamingResponse, JSONResponse

from src.database.client import get_db as _get_db
from src.utils.groq_cascade import get_model_display_name
from src.utils.agent import AgentRunner

log = structlog.get_logger("api.advisor")

app = FastAPI(title="FindUni AI Advisor")

# Max CV file size: 5MB
MAX_CV_SIZE = 5 * 1024 * 1024


# ── Helpers ─────────────────────────────────────────────────────────────────

def _get_db():
    from src.database.client import get_db
    return get_db()


def _fuzzy(query: Optional[str], text: Optional[str]) -> float:
    if not query or not text:
        return 0.0
    q, t = query.lower(), text.lower()
    if q in t:
        return 0.95
    tq = set(re.split(r"\W+", q))
    tt = set(re.split(r"\W+", t))
    if tq and tt:
        overlap = len(tq & tt) / len(tq)
        if overlap > 0:
            return 0.5 + overlap * 0.4
    return SequenceMatcher(None, q, t).ratio()


def _infer_level(qualification: str) -> Optional[str]:
    q = qualification.lower()
    if any(k in q for k in ("high school", "secondary", "+2", "12th", "a-level", "slc", "ssc", "hsc", "high_school")):
        return "undergraduate"
    if any(k in q for k in ("bachelor", "bsc", "ba ", "beng", "be ", "btech", "undergraduate", "btec", "bachelors")):
        return "postgraduate"
    if any(k in q for k in ("master", "msc", "ma ", "mba", "meng", "ms ", "masters")):
        return "doctorate"
    return None


# ── LLM-Powered Subject Expansion ──────────────────────────────────────────

async def _expand_subject_terms(target_subject: str, cv_text: str = "") -> list[str]:
    """
    Use a fast LLM pass to expand the student's target subject into
    semantically related search terms for database queries.
    
    Example: "IT" → ["Information Technology", "Computer Science", 
             "Software Engineering", "IT Management", "Computing"]
    """
    if not target_subject:
        return []
    
    from src.utils.groq_cascade import non_streaming_groq
    
    cv_context = f"\nStudent's CV context: {cv_text[:2000]}" if cv_text else ""
    
    system = """You are a subject synonym expander for a university course database. 
Given a subject, return 6-10 search terms that would match courses in a database.
Include: exact term, formal name, abbreviations, related fields, and broader category.
Return ONLY a JSON array of strings, nothing else. No code fences."""
    
    user = f"""Subject: "{target_subject}"{cv_context}

Return JSON array of 6-10 search terms. Examples:
- "IT" → ["Information Technology", "Computer Science", "Software Engineering", "Computing", "IT Management", "Digital Technology"]
- "MBA" → ["Master of Business Administration", "Business Administration", "Management", "Business", "MBA", "Business Management"]
- "nursing" → ["Nursing", "Registered Nursing", "Health Science", "Nursing Practice", "Clinical Nursing", "Healthcare", "Nursing Science"]"""
    
    try:
        res = await non_streaming_groq(system, user, max_tokens=200, temperature=0.1)
        content = res.get("content", "").strip()
        # Clean up
        content = re.sub(r'^```(?:json)?\s*', '', content)
        content = re.sub(r'\s*```$', '', content)
        terms = json.loads(content)
        if isinstance(terms, list):
            # Always include the original term
            if target_subject not in terms:
                terms.insert(0, target_subject)
            log.info("subject_expanded", original=target_subject, terms=terms[:8])
            return terms[:10]
    except Exception as e:
        log.warning("subject_expansion_failed", error=str(e))
    
    # Fallback: return original + basic variations
    return [target_subject]


async def _infer_subject_from_cv(cv_text: str) -> str:
    """Use a fast LLM pass to infer the logical next subject for this student."""
    if not cv_text:
        return ""
    
    from src.utils.groq_cascade import non_streaming_groq
    
    system = "You are an expert education counselor. Analyze the CV and return ONLY the most likely subject (2-3 words max) the student should study next. Example: 'Computer Science' or 'MBA' or 'Public Health'. No other text."
    user = f"CV Content:\n{cv_text[:4000]}"
    
    try:
        res = await non_streaming_groq(system, user, max_tokens=10, temperature=0.0)
        subject = res.get("content", "").strip().strip("'\"")
        log.info("inferred_subject", subject=subject)
        return subject
    except Exception:
        return ""


# ── Database Queries ────────────────────────────────────────────────────────

def _query_matching_courses(
    target_subject: str,
    countries: list[str],
    inferred_level: Optional[str],
    ielts_score: Optional[float] = None,
    limit: int = 15,
    preferred_states: Optional[list[str]] = None,
    expanded_terms: Optional[list[str]] = None,
    student_gpa: Optional[float] = None,
) -> list[dict]:
    """Query courses matching the student's profile with rich location data.
    
    Uses LLM-expanded subject terms for semantic matching instead of
    pure fuzzy string matching. Falls back to fuzzy if no expanded terms.
    """
    db = _get_db()
    all_courses = []
    course_groups = {}

    # Use expanded terms for matching if available
    search_terms = expanded_terms or [target_subject] if target_subject else []

    for country in countries:
        query = db.table("courses").select("*").eq("is_active", True).ilike("country", f"%{country.strip()}%")
        if inferred_level and inferred_level.lower() not in ['any', 'none', '']:
            lvl = inferred_level.lower()
            if any(k in lvl for k in ('undergrad', 'high', 'bachelor', 'b.a', 'b.s')):
                query = query.or_("level.ilike.%undergrad%,level.ilike.%bachelor%,level.ilike.%diploma%,level.ilike.%associate%")
            elif any(k in lvl for k in ('postgrad', 'master', 'doctor', 'phd')):
                query = query.or_("level.ilike.%postgrad%,level.ilike.%master%,level.ilike.%doctor%,level.ilike.%phd%,level.ilike.%grad%")
        rows = (query.execute()).data or []

        for c in rows:
            # STATE FILTERING
            state = c.get("state") or ""
            if preferred_states:
                state_match = False
                for pref_state in preferred_states:
                    if (state and pref_state.upper().startswith(state.upper())) or \
                       (state and state.upper() in pref_state.upper()) or \
                       (c.get("city") and c.get("city").upper() in pref_state.upper()):
                        state_match = True
                        break
                if not state_match:
                    continue
                    
            course_name = (c.get("name") or "").lower()
            junk_keywords = ["study abroad", "exchange", "exchange program", "non-award"]
            if any(k in course_name for k in junk_keywords) and not any(k in target_subject.lower() for k in junk_keywords):
                continue

            # Use expanded terms for relevance scoring
            rel = 0.0
            matched_term = None
            for term in search_terms:
                term_rel = max(
                    _fuzzy(term, c.get("name") or ""),
                    _fuzzy(term, c.get("subject") or ""),
                    _fuzzy(term, c.get("subject_category") or ""),
                )
                if term_rel > rel:
                    rel = term_rel
                    matched_term = term
            
            # Also check original target subject
            if target_subject and target_subject not in search_terms:
                orig_rel = max(
                    _fuzzy(target_subject, c.get("name") or ""),
                    _fuzzy(target_subject, c.get("subject") or ""),
                    _fuzzy(target_subject, c.get("subject_category") or ""),
                )
                if orig_rel > rel:
                    rel = orig_rel

            # Lower threshold since we're using expanded terms
            threshold = 0.30 if search_terms else 0.2
            if rel < threshold:
                continue

            ielts_met = True
            ielts_gap = None
            if ielts_score and c.get("ielts_overall"):
                course_ielts = float(c["ielts_overall"])
                ielts_met = course_ielts <= ielts_score
                if not ielts_met:
                    ielts_gap = round(course_ielts - ielts_score, 1)

            # Calculate admission probability
            admission_prob = "Medium"
            if student_gpa:
                gpa_req = c.get("gpa_requirement")
                if gpa_req:
                    try:
                        req_gpa = float(re.search(r'[\d.]+', str(gpa_req)).group())
                        if student_gpa >= req_gpa + 0.3:
                            admission_prob = "High"
                        elif student_gpa >= req_gpa:
                            admission_prob = "Medium"
                        else:
                            admission_prob = "Low"
                    except (ValueError, AttributeError):
                        pass
                else:
                    # No GPA req stated — use general thresholds
                    if student_gpa >= 3.5:
                        admission_prob = "High"
                    elif student_gpa >= 3.0:
                        admission_prob = "Medium"
                    else:
                        admission_prob = "Low"
            
            if ielts_met is False:
                admission_prob = "Low"

            fee = c.get("tuition_fee") or 0
            currency = c.get("currency", "AUD")
            source = (c.get("source") or "").upper()
            city = c.get("city") or ""
            
            location_entry = {
                "city": city,
                "state": state,
                "location": f"{city}, {state}" if (city and state) else (city or state),
                "cricos_code": c.get("cricos_code"),
                "provider_code": c.get("provider_code"),
                "start_dates": c.get("start_dates", []),
            }
            
            # Generate match reason
            match_reason = ""
            if matched_term and matched_term.lower() != target_subject.lower():
                match_reason = f"Matched via '{matched_term}'"
            elif rel >= 0.9:
                match_reason = "Direct subject match"
            elif rel >= 0.6:
                match_reason = "Strong subject match"
            else:
                match_reason = "Related field"
            
            course_key = f"{c.get('name')}|{c.get('university')}"
            if course_key not in course_groups:
                course_groups[course_key] = {
                    "name": c.get("name"),
                    "university": c.get("university"),
                    "country": c.get("country"),
                    "level": c.get("level"),
                    "tuition_fee": fee,
                    "tuition_display": f"{currency} {fee:,.0f}/yr" if fee else "Contact university",
                    "currency": currency,
                    "duration_months": c.get("duration_months"),
                    "duration_years": round(c.get("duration_months", 0) / 12, 1) if c.get("duration_months") else None,
                    "ielts_required": c.get("ielts_overall"),
                    "ielts_breakdown": {
                        "overall": c.get("ielts_overall"),
                        "reading": c.get("ielts_reading"),
                        "writing": c.get("ielts_writing"),
                        "speaking": c.get("ielts_speaking"),
                        "listening": c.get("ielts_listening"),
                    },
                    "ielts_met": ielts_met,
                    "ielts_gap": ielts_gap,
                    "gpa_requirement": c.get("gpa_requirement"),
                    "entry_qualification": c.get("entry_qualification"),
                    "apply_url": c.get("apply_url"),
                    "source_url": c.get("source_url"),
                    "source": source,
                    "relevance": round(float(rel), 3),
                    "match_reason": match_reason,
                    "admission_probability": admission_prob,
                    "city": city,
                    "state": state,
                    "cricos_code": c.get("cricos_code"),
                    "provider_code": c.get("provider_code"),
                    "locations": [location_entry],
                    "is_cricos": source == "CRICOS",
                    "start_dates": c.get("start_dates", []),
                }
            else:
                existing = course_groups[course_key]
                if not any(loc["city"] == city and loc["state"] == state for loc in existing["locations"]):
                    existing["locations"].append(location_entry)
                    if source == "CRICOS":
                        existing["is_cricos"] = True

    all_courses = list(course_groups.values())
    
    def sort_key(x):
        priority = 3
        if x["country"].lower() == "australia":
            if x.get("is_cricos"): priority = 1
            elif "IDP" in x["source"]: priority = 2
        # Boost courses where IELTS is met
        ielts_bonus = 0 if x.get("ielts_met") else 0.1
        return (-float(x["relevance"]) + ielts_bonus, priority, x.get("tuition_fee") or 999999)

    all_courses.sort(key=sort_key)
    return all_courses[:limit]


def _query_matching_scholarships(
    target_subject: str,
    countries: list[str],
    inferred_level: Optional[str],
    nationality: str,
    limit: int = 15,
    expanded_terms: Optional[list[str]] = None,
    student_gpa: Optional[float] = None,
    budget_usd: Optional[int] = None,
) -> list[dict]:
    """Query scholarships with intelligent matching.
    
    Uses expanded subject terms and deep eligibility analysis.
    """
    db = _get_db()
    all_scholarships = []
    today = date.today()

    for country in countries:
        query = db.table("scholarships").select("*").eq("is_active", True).ilike("country", f"%{country.strip()}%")
        if inferred_level and inferred_level.lower() not in ['any', 'none', '']:
            lvl = inferred_level.lower()
            if any(k in lvl for k in ('undergrad', 'high', 'bachelor', 'b.a', 'b.s')):
                query = query.or_("study_level.ilike.%undergrad%,study_level.ilike.%bachelor%,study_level.ilike.%diploma%,study_level.ilike.%all%,study_level.ilike.%any%")
            elif any(k in lvl for k in ('postgrad', 'master', 'doctor', 'phd')):
                query = query.or_("study_level.ilike.%postgrad%,study_level.ilike.%master%,study_level.ilike.%doctor%,study_level.ilike.%phd%,study_level.ilike.%all%,study_level.ilike.%any%")
        rows = (query.execute()).data or []

        for s in rows:
            match_score = 0.0
            reasons = []

            # Subject matching with expanded terms
            search_terms = expanded_terms or [target_subject] if target_subject else []
            best_subj_rel = 0.0
            for term in search_terms:
                subj_rel = max(
                    _fuzzy(term, s.get("subject") or ""),
                    _fuzzy(term, s.get("subject_category") or ""),
                    _fuzzy(term, s.get("description") or ""),
                )
                best_subj_rel = max(best_subj_rel, subj_rel)
            
            if best_subj_rel > 0.25:
                match_score += best_subj_rel * 0.30
                if best_subj_rel > 0.7:
                    reasons.append(f"Strong subject match ({best_subj_rel:.0%})")
                else:
                    reasons.append(f"Subject match: {best_subj_rel:.0%}")

            # Nationality matching — deep eligibility analysis
            elig = (s.get("eligibility") or "").lower()
            nat_lower = nationality.lower()
            
            # Check for direct nationality mention
            nationality_variants = [nat_lower]
            # Add country name variants
            nat_to_country = {
                'nepalese': ['nepal', 'nepali'],
                'indian': ['india'],
                'bangladeshi': ['bangladesh'],
                'pakistani': ['pakistan'],
                'sri lankan': ['sri lanka'],
                'chinese': ['china'],
                'vietnamese': ['vietnam'],
                'filipino': ['philippines'],
                'indonesian': ['indonesia'],
                'nigerian': ['nigeria'],
                'thai': ['thailand'],
            }
            nationality_variants.extend(nat_to_country.get(nat_lower, []))
            
            nat_matched = False
            for variant in nationality_variants:
                if variant in elig:
                    match_score += 0.30
                    reasons.append(f"Open to {nationality} students")
                    nat_matched = True
                    break
            
            if not nat_matched:
                # Check for broader eligibility
                broad_terms = ["all international", "international student", "overseas", 
                              "south asia", "developing countr", "asia", "global"]
                for term in broad_terms:
                    if term in elig:
                        match_score += 0.15
                        reasons.append("Open to international students")
                        nat_matched = True
                        break
                
                if not nat_matched and not elig:
                    # No eligibility criteria specified — assume open
                    match_score += 0.10
                    reasons.append("Open eligibility")

            # Funding type bonus
            if s.get("funding_type") == "full":
                match_score += 0.15
                reasons.append("🌟 Fully funded")
            elif s.get("funding_type") == "partial":
                match_score += 0.05
                reasons.append("Partial funding")

            # Deadline analysis
            if s.get("deadline"):
                try:
                    dl = datetime.fromisoformat(str(s["deadline"])).date()
                    if dl < today:
                        continue  # Skip expired
                    days_left = (dl - today).days
                    if days_left < 14:
                        reasons.append(f"⚡ {days_left} days left!")
                    elif days_left < 30:
                        reasons.append(f"⏰ Deadline in {days_left} days")
                    elif days_left < 90:
                        reasons.append(f"Closes in {days_left} days")
                except (ValueError, TypeError):
                    pass

            # Award value vs budget analysis
            val = s.get("award_value_max") or s.get("award_value_min") or 0
            if val and budget_usd:
                # Convert roughly to USD for comparison
                curr = s.get("award_currency", "AUD")
                conversion = {"AUD": 0.65, "USD": 1.0, "GBP": 1.25, "EUR": 1.10, "CAD": 0.74, "NZD": 0.60}
                val_usd = val * conversion.get(curr, 0.65)
                if val_usd > budget_usd * 0.5:
                    match_score += 0.10
                    reasons.append("Significant financial impact")

            # GPA competitiveness bonus
            if student_gpa and student_gpa >= 3.5:
                match_score += 0.05
                reasons.append("Strong GPA candidate")

            # Minimum threshold to include
            if match_score <= 0.10:
                continue

            curr = s.get("award_currency", "AUD")
            
            all_scholarships.append({
                "title": s.get("title"),
                "university": s.get("university"),
                "country": s.get("country"),
                "city": s.get("city") or "",
                "funding_type": s.get("funding_type"),
                "value": f"{curr} {val:,.0f}" if val else "Contact provider",
                "value_numeric": val,
                "award_min": s.get("award_value_min"),
                "award_max": s.get("award_value_max"),
                "currency": curr,
                "deadline": str(s["deadline"]) if s.get("deadline") else None,
                "eligibility": s.get("eligibility"),
                "description": s.get("description"),
                "match_score": round(float(match_score), 3),
                "why_matched": reasons,
                "apply_url": s.get("apply_url"),
                "source_url": s.get("source_url"),
                "source": s.get("source"),
            })

    all_scholarships.sort(key=lambda x: float(x["match_score"]), reverse=True)
    return all_scholarships[:limit]


def _query_universities(countries: list[str], limit: int = 10) -> list[dict]:
    """Get top universities in preferred countries with complete data."""
    db = _get_db()
    all_unis = []
    for country in countries:
        rows = (db.table("universities").select("*")
                .ilike("country", country.strip())
                .order("world_ranking", nullsfirst=False)
                .limit(20).execute()).data or []
        for u in rows:
            all_unis.append({
                "name": u.get("name"),
                "country": u.get("country"),
                "city": u.get("city"),
                "state": u.get("state"),
                "world_ranking": u.get("world_ranking"),
                "subject_rankings": u.get("subject_rankings", {}),
                "acceptance_rate": u.get("acceptance_rate"),
                "total_students": u.get("total_students"),
                "international_students": u.get("international_students"),
                "tuition_min": u.get("tuition_min"),
                "tuition_max": u.get("tuition_max"),
                "currency": u.get("currency", "AUD"),
                "ielts_minimum": u.get("ielts_minimum"),
                "popular_subjects": u.get("popular_subjects", []),
                "facilities": u.get("facilities", []),
                "accommodation_cost_min": u.get("accommodation_cost_min"),
                "accommodation_cost_max": u.get("accommodation_cost_max"),
                "website": u.get("website"),
                "provider_code": u.get("provider_code"),
            })
    all_unis.sort(key=lambda x: x.get("world_ranking") or 9999)
    return all_unis[:limit]


def _query_visa_data(nationality: str, countries: list[str]) -> list[dict]:
    """Get complete visa requirements for student's nationality → each country."""
    db = _get_db()
    results = []
    for country in countries:
        rows = (db.table("visa_requirements").select("*")
                .ilike("nationality", nationality.strip())
                .ilike("destination_country", country.strip())
                .execute()).data or []
        if rows:
            v = rows[0]
            results.append({
                "country": country,
                "visa_type": v.get("visa_type"),
                "visa_subclass": v.get("visa_subclass"),
                "financial_requirement_aud": v.get("financial_requirement_aud"),
                "processing_weeks": f"{v.get('processing_weeks_min', '?')}–{v.get('processing_weeks_max', '?')}",
                "processing_weeks_min": v.get("processing_weeks_min"),
                "processing_weeks_max": v.get("processing_weeks_max"),
                "work_rights_hours": v.get("work_rights_hours_per_week"),
                "required_documents": v.get("required_documents", []),
                "health_requirements": v.get("health_requirements"),
                "notes": v.get("notes"),
                "source_url": v.get("source_url"),
            })
        else:
            results.append({
                "country": country,
                "message": f"No visa data found for {nationality} → {country}",
            })
    return results


def _query_cost_of_living(countries: list[str]) -> list[dict]:
    """Get comprehensive cost of living data for top cities in each country."""
    db = _get_db()
    results = []
    for country in countries:
        rows = (db.table("cost_of_living").select("*")
                .ilike("country", country.strip())
                .limit(5).execute()).data or []
        for c in rows:
            results.append({
                "city": c.get("city"),
                "country": c.get("country"),
                "rent_shared_min": c.get("rent_shared_min"),
                "rent_shared_max": c.get("rent_shared_max"),
                "rent_private_min": c.get("rent_private_min"),
                "rent_private_max": c.get("rent_private_max"),
                "food_monthly": c.get("food_monthly"),
                "transport_monthly": c.get("transport_monthly"),
                "utilities_monthly": c.get("utilities_monthly"),
                "internet_monthly": c.get("internet_monthly"),
                "total_monthly_min": c.get("total_monthly_min"),
                "total_monthly_max": c.get("total_monthly_max"),
                "part_time_wage_hourly": c.get("part_time_wage_hourly"),
                "currency": c.get("currency", "AUD"),
                "weekly_budget": {
                    "shared_rent_min": round((c.get("rent_shared_min") or 0) / 4.33, 2),
                    "shared_rent_max": round((c.get("rent_shared_max") or 0) / 4.33, 2),
                    "food": round((c.get("food_monthly") or 0) / 4.33, 2),
                    "transport": round((c.get("transport_monthly") or 0) / 4.33, 2),
                },
            })
    return results


# ── System Prompt ───────────────────────────────────────────────────────────

SYSTEM_PROMPT = """You are **ScholarRadar AI** — the world's best study abroad advisor. You have access to REAL, verified data from our database. Your job is to give genuinely life-changing, specific, actionable advice.

## RULES
1. **BE SPECIFIC** - Use exact course names, fees, CRICOS codes, deadlines from the database
2. **BE HONEST** - If admission is unlikely, say so. If IELTS is short, say by how much
3. **USE DATABASE DATA** - NEVER make up courses/scholarships. Only reference what's in the data below
4. **CRICOS PRIORITY** - For Australia, always show CRICOS code
5. **MULTIPLE LOCATIONS** - Show ALL locations if course available in multiple cities
6. **ADMISSION PROBABILITY** - Rate each course High/Medium/Low based on student GPA vs requirements
7. **FINANCIAL REALITY** - Calculate total cost vs their budget. Be brutally honest about gaps

## OUTPUT FORMAT

### 🎯 Your Profile Summary
- Academic: [qualification] + GPA [X/4.0] → admission rating
- English: IELTS [score] → meets/doesn't meet requirements (gap: X.X if applicable)
- Experience: [years] in [field] → [how this helps]
- CV Strengths: [2-3 strengths from CV that boost applications]

### 🎓 Top Course Recommendations
For each course (show top 3-5):
| # | University | Course | Fee/Year | IELTS | Admission |
|---|-----------|--------|----------|-------|-----------|
| 1 | [Name] | [Course Name] | $[X] | [X] | [High/Med/Low] |

For each course, explain:
- **Why this fits you:** [specific reason from CV/profile]
- **CRICOS:** [code] (if Australia)
- **Locations:** [all cities]
- **How to apply:** [direct URL]
- **Start dates:** [intake dates]

### 💰 Scholarship Matches (Your Best Bets)
For each scholarship (top 3-5):
- **[Name]** — [amount] | [funding type]
  - Why you qualify: [specific eligibility match]
  - Deadline: [date] | [days remaining]
  - Apply: [URL]

### 💵 Financial Reality Check
| Item | Annual Cost | Total ([N] years) |
|------|-----------|-------------------|
| Tuition (cheapest match) | $[X] | $[X] |
| Living costs | $[X] | $[X] |
| **Total needed** | **$[X]** | **$[X]** |
| Your budget | $[X] | $[X] |
| **Gap/Surplus** | **$[X]** | **$[X]** |

- Part-time work: $[X]/hr × [Y] hrs/wk = ~$[Z]/month potential
- Scholarship savings: Up to $[X] if you get [scholarship name]

### 🛂 Visa Pathway
- **Type:** [visa subclass + name]
- **Financial proof:** $[amount] required
- **Work rights:** [X] hrs/wk during study
- **Processing:** [X]-[Y] weeks
- **Key documents:** [list]

### 📅 Your Action Plan (This Week)
1. [Specific action] → [direct URL]
2. [Specific action] → [direct URL]
3. [Specific action] → [direct URL]

### ⚠️ Important Disclaimer
- Always verify fees and deadlines on official university websites
- ScholarRadar is an AI data aggregator, not a migration agent
- Source: skolr.xyz

## TONE: Warm but honest. If something won't work, suggest alternatives. Be the advisor every student deserves.
"""


def _build_user_prompt(
    profile: dict,
    cv_text: str,
    cv_analysis: dict,
    courses: list[dict],
    scholarships: list[dict],
    universities: list[dict],
    visa_data: list[dict],
    cost_data: list[dict],
) -> str:
    """Build the comprehensive user prompt with all data."""

    sections = []

    # CV section with analysis
    if cv_text:
        sections.append(f"""## Student's CV/Resume
<cv>
{cv_text[:6000]}
</cv>""")
    
    if cv_analysis:
        analysis_parts = []
        if cv_analysis.get('education_summary'):
            analysis_parts.append(f"- Education: {cv_analysis['education_summary']}")
        if cv_analysis.get('skills'):
            skills = cv_analysis['skills'] if isinstance(cv_analysis['skills'], list) else [cv_analysis['skills']]
            analysis_parts.append(f"- Key Skills: {', '.join(skills[:8])}")
        if cv_analysis.get('strengths'):
            strengths = cv_analysis['strengths'] if isinstance(cv_analysis['strengths'], list) else [cv_analysis['strengths']]
            analysis_parts.append(f"- Strengths: {', '.join(strengths[:4])}")
        if cv_analysis.get('gaps'):
            gaps = cv_analysis['gaps'] if isinstance(cv_analysis['gaps'], list) else [cv_analysis['gaps']]
            analysis_parts.append(f"- Areas to address: {', '.join(gaps[:3])}")
        if cv_analysis.get('career_goal'):
            analysis_parts.append(f"- Career trajectory: {cv_analysis['career_goal']}")
        
        if analysis_parts:
            sections.append("## CV Analysis (Pre-processed)\n" + "\n".join(analysis_parts))

    # Profile section
    profile_lines = []
    field_map = {
        "nationality": "Nationality",
        "current_qualification": "Current Qualification",
        "gpa": "GPA (out of 4.0)",
        "ielts_overall": "IELTS Overall",
        "ielts_reading": "IELTS Reading",
        "ielts_writing": "IELTS Writing",
        "ielts_speaking": "IELTS Speaking",
        "ielts_listening": "IELTS Listening",
        "target_subject": "Target Subject/Field",
        "preferred_countries": "Preferred Countries",
        "budget_usd": "Total Budget (USD/year)",
        "timeline_months": "Timeline (months until start)",
        "career_goal": "Career Goal",
        "work_experience_years": "Work Experience (years)",
        "extra_info": "Additional Information",
    }
    for key, label in field_map.items():
        val = profile.get(key)
        if val is not None and val != "" and val != []:
            if isinstance(val, list):
                val = ", ".join(val)
            profile_lines.append(f"- **{label}**: {val}")

    sections.append("## Student Profile\n" + "\n".join(profile_lines))

    # Database results — pre-annotated with match reasons
    if courses:
        # Trim to essential fields to save tokens
        compact_courses = []
        for c in courses[:10]:
            compact = {
                "name": c["name"],
                "university": c["university"],
                "country": c["country"],
                "level": c.get("level"),
                "fee": c.get("tuition_display"),
                "duration": f"{c.get('duration_months', '?')} months",
                "ielts_required": c.get("ielts_required"),
                "ielts_met": c.get("ielts_met"),
                "ielts_gap": c.get("ielts_gap"),
                "admission_probability": c.get("admission_probability"),
                "match_reason": c.get("match_reason"),
                "relevance": c.get("relevance"),
                "city": c.get("city"),
                "state": c.get("state"),
                "cricos_code": c.get("cricos_code"),
                "apply_url": c.get("apply_url"),
                "start_dates": c.get("start_dates"),
                "locations": [f"{l['city']}, {l['state']}" for l in (c.get("locations") or []) if l.get("city")],
            }
            compact_courses.append(compact)
        
        course_text = json.dumps(compact_courses, indent=2, default=str)
        sections.append(f"""## Matching Courses from Database ({len(courses)} total, showing top {len(compact_courses)})
```json
{course_text}
```""")
    else:
        sections.append("## Matching Courses from Database\nNo matching courses found in our database for this profile. Please suggest the student search more broadly or check official university websites directly.")

    if scholarships:
        compact_scholarships = []
        for s in scholarships[:10]:
            compact = {
                "title": s["title"],
                "university": s["university"],
                "country": s["country"],
                "value": s.get("value"),
                "funding_type": s.get("funding_type"),
                "deadline": s.get("deadline"),
                "match_score": s.get("match_score"),
                "why_matched": s.get("why_matched"),
                "apply_url": s.get("apply_url"),
                "eligibility": (s.get("eligibility") or "")[:200],
            }
            compact_scholarships.append(compact)
        
        schol_text = json.dumps(compact_scholarships, indent=2, default=str)
        sections.append(f"""## Matching Scholarships from Database ({len(scholarships)} total, showing top {len(compact_scholarships)})
```json
{schol_text}
```""")
    else:
        sections.append("## Matching Scholarships from Database\nNo matching scholarships found. Suggest checking university-specific funding pages and government scholarship portals directly.")

    if universities:
        uni_text = json.dumps(universities[:5], indent=2, default=str)
        sections.append(f"""## University Data
```json
{uni_text}
```""")

    if visa_data:
        visa_text = json.dumps(visa_data, indent=2, default=str)
        sections.append(f"""## Visa Requirements Data
```json
{visa_text}
```""")

    if cost_data:
        cost_text = json.dumps(cost_data[:3], indent=2, default=str)
        sections.append(f"""## Cost of Living Data
```json
{cost_text}
```""")

    sections.append("""## Your Task
Based on ALL the data above — the student's CV, their profile, and the real database results — provide the most comprehensive, actionable, and genuinely helpful study abroad guidance possible. Follow the response format specified in your instructions.

CRITICAL: Only recommend courses and scholarships that are in the database data above. Do NOT invent or make up any courses, fees, or scholarship names. If data is limited, be honest about it and suggest where to look for more options.""")

    return "\n\n".join(sections)


# ── CV Parse Endpoint ───────────────────────────────────────────────────────

@app.post("/parse-cv")
async def parse_cv(
    cv_file: UploadFile = File(...),
):
    """
    Parse a CV/PDF and return extracted profile data for frontend auto-fill.
    
    Returns a JSON object with all detected profile fields.
    The frontend uses this to auto-populate the form before analysis.
    """
    log.info("parse_cv_request_received")
    
    # Validate file
    if cv_file.size and cv_file.size > MAX_CV_SIZE:
        return JSONResponse(
            status_code=400,
            content={"error": "CV file too large. Maximum size is 5MB."},
        )
    
    content_type = cv_file.content_type or ""
    if "pdf" not in content_type.lower() and not cv_file.filename.lower().endswith(".pdf"):
        return JSONResponse(
            status_code=400,
            content={"error": "Only PDF files are accepted. Please upload your CV as a PDF."},
        )
    
    try:
        from src.utils.cv_parser import extract_text_from_pdf, extract_structured_profile
        
        pdf_bytes = await cv_file.read()
        cv_text = extract_text_from_pdf(pdf_bytes)
        
        if not cv_text:
            return JSONResponse(
                status_code=400,
                content={"error": "Could not extract text from PDF. The file may be image-based."},
            )
        
        # Extract structured profile using regex + LLM
        profile = await extract_structured_profile(cv_text)
        
        log.info("parse_cv_complete", fields=list(profile.keys()), field_count=len(profile))
        
        return JSONResponse(content={
            "success": True,
            "extracted_fields": profile,
            "cv_text_length": len(cv_text),
        })
        
    except ValueError as e:
        return JSONResponse(status_code=400, content={"error": str(e)})
    except Exception as e:
        log.error("parse_cv_error", error=str(e))
        return JSONResponse(
            status_code=500,
            content={"error": f"CV parsing failed: {str(e)}"},
        )


# ── Main Endpoint ───────────────────────────────────────────────────────────

@app.post("/analyze")
async def analyze_profile(
    profile: str = Form(...),
    cv_file: Optional[UploadFile] = File(None),
):
    """
    Analyze a student's profile and CV, then stream personalized guidance.

    - `profile`: JSON string with student profile fields
    - `cv_file`: Optional PDF file (max 5MB)

    Returns a text/event-stream (SSE) with the AI response.
    """
    started = time.time()
    log.info("advisor_request_received")

    try:
        # Parse profile JSON
        try:
            profile_data = json.loads(profile)
            log.info("profile_parsed", keys=list(profile_data.keys()))
        except json.JSONDecodeError as e:
            log.error("invalid_profile_json", error=str(e))
            return JSONResponse(
                status_code=400,
                content={"error": "Invalid profile JSON"},
            )

        # Validate required fields
        nationality = profile_data.get("nationality", "").strip()
        target_subject = profile_data.get("target_subject", "").strip()
        preferred_countries = profile_data.get("preferred_countries", [])
        preferred_states = profile_data.get("preferred_states", [])

        if not nationality:
            return JSONResponse(status_code=400, content={"error": "Nationality is required"})
        if not preferred_countries:
            return JSONResponse(status_code=400, content={"error": "At least one preferred country is required"})

        if isinstance(preferred_countries, str):
            preferred_countries = [c.strip() for c in preferred_countries.split(",")]
        if isinstance(preferred_states, str):
            preferred_states = [s.strip() for s in preferred_states.split(",")]

        # Parse CV if provided
        cv_text = ""
        cv_analysis = {}
        if cv_file:
            if cv_file.size and cv_file.size > MAX_CV_SIZE:
                return JSONResponse(
                    status_code=400,
                    content={"error": "CV file too large. Maximum size is 5MB."},
                )

            content_type = cv_file.content_type or ""
            if "pdf" not in content_type.lower() and not cv_file.filename.lower().endswith(".pdf"):
                return JSONResponse(
                    status_code=400,
                    content={"error": "Only PDF files are accepted. Please upload your CV as a PDF."},
                )

            try:
                from src.utils.cv_parser import extract_text_from_pdf, extract_structured_profile
                pdf_bytes = await cv_file.read()
                cv_text = extract_text_from_pdf(pdf_bytes)
                
                # Full structured extraction
                if cv_text:
                    cv_analysis = await extract_structured_profile(cv_text)
                    
                    # Fill in missing profile fields from CV analysis
                    auto_filled = []
                    fill_fields = [
                        'gpa', 'ielts_overall', 'ielts_reading', 'ielts_writing',
                        'ielts_speaking', 'ielts_listening', 'current_qualification',
                        'nationality', 'work_experience_years', 'career_goal',
                    ]
                    for field in fill_fields:
                        if cv_analysis.get(field) and not profile_data.get(field):
                            profile_data[field] = cv_analysis[field]
                            auto_filled.append(field)
                    
                    # Infer subject from CV if not provided
                    if not target_subject and cv_analysis.get('target_subject'):
                        target_subject = cv_analysis['target_subject']
                        profile_data['target_subject'] = target_subject
                        auto_filled.append('target_subject')
                    
                    if auto_filled:
                        log.info("cv_auto_filled_fields", fields=auto_filled)
                        # Update nationality if it was auto-filled
                        if 'nationality' in auto_filled:
                            nationality = profile_data['nationality']
                        
            except ValueError as e:
                return JSONResponse(status_code=400, content={"error": str(e)})
            except Exception as e:
                log.error("cv_parse_error", error=str(e))
                cv_text = ""

        # Extract profile fields
        current_qualification = profile_data.get("current_qualification", "")
        ielts_score = profile_data.get("ielts_overall")
        if ielts_score:
            try:
                ielts_score = float(ielts_score)
            except (ValueError, TypeError):
                ielts_score = None

        student_gpa = None
        if profile_data.get("gpa"):
            try:
                student_gpa = float(profile_data["gpa"])
            except (ValueError, TypeError):
                pass

        budget_usd = profile_data.get("budget_usd")
        if budget_usd:
            try:
                budget_usd = int(budget_usd)
            except (ValueError, TypeError):
                budget_usd = None

        # Level selection: User Choice > Inferred
        target_level = profile_data.get("target_level")
        if not target_level:
            target_level = _infer_level(current_qualification) if current_qualification else None

        log.info(
            "advisor_analyze",
            nationality=nationality,
            subject=target_subject,
            countries=preferred_countries,
            has_cv=bool(cv_text),
            target_level=target_level,
            gpa=student_gpa,
        )

        # ── Expand subject terms using LLM ──
        expanded_terms = []
        if target_subject:
            expanded_terms = await _expand_subject_terms(target_subject, cv_text)
            log.info("subject_terms_expanded", count=len(expanded_terms))

        # ── Query database for matching data ──
        log.info("querying_database", countries=preferred_countries)
        
        courses = _query_matching_courses(
            target_subject=target_subject,
            countries=preferred_countries,
            inferred_level=target_level,
            ielts_score=ielts_score,
            limit=15,
            preferred_states=preferred_states,
            expanded_terms=expanded_terms,
            student_gpa=student_gpa,
        )
        
        scholarships = _query_matching_scholarships(
            target_subject=target_subject,
            countries=preferred_countries,
            inferred_level=target_level,
            nationality=nationality,
            limit=15,
            expanded_terms=expanded_terms,
            student_gpa=student_gpa,
            budget_usd=budget_usd,
        )
        
        universities = _query_universities(
            countries=preferred_countries,
            limit=10,
        )
        
        visa_data = _query_visa_data(
            nationality=nationality,
            countries=preferred_countries,
        )
        
        cost_data = _query_cost_of_living(
            countries=preferred_countries,
        )
        
        log.info(
            "database_query_complete",
            courses=len(courses),
            scholarships=len(scholarships),
            universities=len(universities),
        )

        # ── Build comprehensive user prompt ──
        user_prompt = _build_user_prompt(
            profile=profile_data,
            cv_text=cv_text,
            cv_analysis=cv_analysis,
            courses=courses,
            scholarships=scholarships,
            universities=universities,
            visa_data=visa_data,
            cost_data=cost_data,
        )

        # Stream response
        async def event_stream():
            try:
                # Send metadata first
                log.info("sending_metadata", courses=len(courses), scholarships=len(scholarships))
                yield f"data: {json.dumps({'type': 'metadata', 'courses_found': len(courses), 'scholarships_found': len(scholarships)})}\n\n"
                
                # Send CV analysis if available (for frontend auto-fill confirmation)
                if cv_analysis:
                    yield f"data: {json.dumps({'type': 'cv_extracted', 'data': cv_analysis})}\n\n"
                
                # Send courses data
                if courses:
                    log.info("sending_courses", count=len(courses))
                    yield f"data: {json.dumps({'type': 'courses', 'data': courses})}\n\n"
                
                # Send scholarships data
                if scholarships:
                    log.info("sending_scholarships", count=len(scholarships))
                    yield f"data: {json.dumps({'type': 'scholarships', 'data': scholarships})}\n\n"
                
                yield f"data: {json.dumps({'type': 'status', 'content': 'Generating your personalized analysis...'})}\n\n"

                # Use simple streaming
                from src.utils.groq_cascade import stream_groq_response
                
                log.info("starting_llm_stream", prompt_length=len(user_prompt))
                
                async for event in stream_groq_response(
                    system_prompt=SYSTEM_PROMPT,
                    user_prompt=user_prompt,
                    max_tokens=4096,
                    temperature=0.7,
                ):
                    if event["type"] == "model":
                        yield f"data: {json.dumps({'type': 'model', 'model': event['model'], 'display_name': get_model_display_name(event['model'])})}\n\n"
                    elif event["type"] == "chunk":
                        yield f"data: {json.dumps({'type': 'chunk', 'content': event['content']})}\n\n"
                    elif event["type"] == "done":
                        total_time = round(time.time() - started, 2)
                        done_payload = {
                            'type': 'done',
                            'model': event['model'],
                            'display_name': get_model_display_name(event['model']),
                            'usage': event.get('usage', {}),
                            'cost_usd': event.get('cost_usd', 0),
                            'total_time_seconds': total_time
                        }
                        yield f"data: {json.dumps(done_payload)}\n\n"
                        log.info("stream_complete", total_time=total_time)
                    elif event["type"] == "error":
                        yield f"data: {json.dumps({'type': 'error', 'message': event['message']})}\n\n"
                        log.error("stream_error", message=event['message'])

                yield "data: [DONE]\n\n"
                log.info("advisor_stream_finished")
                
            except Exception as e:
                log.error("advisor_stream_failed", error=str(e), exc_info=True)
                yield f"data: {json.dumps({'type': 'error', 'message': f'Analysis failed: {str(e)}'})}\n\n"

        return StreamingResponse(
            event_stream(),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "X-Accel-Buffering": "no",
            },
        )

    except Exception as e:
        log.error("advisor_analyze_error", error=str(e))
        return JSONResponse(
            status_code=500,
            content={"error": f"Analysis failed: {str(e)}"},
        )

# force render update
