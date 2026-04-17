"""
FindUni AI Advisor API — The core endpoint that powers skolr.xyz/finduni.

Accepts a student's CV (optional PDF) + profile data, queries the entire
ScholarRadar database for matching opportunities, and streams a deeply
personalized study abroad plan through Groq LLMs.

Architecture:
  1. Parse CV PDF → extract text
  2. Query Supabase for matching courses, scholarships, universities, visa, costs
  3. Build a mega-prompt with all real data
  4. Stream response via Groq cascade (5 models, guaranteed response)
  5. Return SSE stream to frontend
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
    if any(k in q for k in ("high school", "secondary", "+2", "12th", "a-level", "slc", "ssc", "hsc")):
        return "undergraduate"
    if any(k in q for k in ("bachelor", "bsc", "ba ", "beng", "be ", "btech", "undergraduate", "btec")):
        return "postgraduate"
    if any(k in q for k in ("master", "msc", "ma ", "mba", "meng", "ms ")):
        return "doctorate"
    return None


async def _infer_subject_from_cv(cv_text: str) -> str:
    """Use a fast LLM pass to infer the logical next subject for this student."""
    if not cv_text:
        return ""
    
    from src.utils.groq_cascade import non_streaming_groq
    
    system = "You are an expert education counselor. Analyze the CV and return ONLY the most likely subject (2-3 words max) the student should study next. Example: 'Computer Science' or 'MBA' or 'Public Health'. No other text."
    user = f"CV Content:\n{cv_text[:4000]}" # First 4k chars is enough for subject
    
    try:
        # Use a very fast model for this pre-pass
        res = await non_streaming_groq(system, user, max_tokens=10, temperature=0.0)
        subject = res.get("content", "").strip().strip("'\"")
        log.info("inferred_subject", subject=subject)
        return subject
    except Exception:
        return ""


async def _extract_cv_details(cv_text: str) -> dict:
    """Extract qualification, GPA, and IELTS scores from CV using pattern matching + LLM."""
    if not cv_text:
        return {}
    
    details = {}
    cv_lower = cv_text.lower()
    
    # 1. Extract GPA using pattern matching
    import re
    gpa_patterns = [
        r'gpa[:\s]*([0-4]\.?\d{0,2})\s*(?:out of|/)?\s*4',
        r'([0-4]\.?\d{0,2})\s*/\s*4',
        r'cumulative\s*gpa[:\s]*([0-4]\.?\d{0,2})',
        r'cgpa[:\s]*([0-4]\.?\d{0,2})',
    ]
    for pattern in gpa_patterns:
        match = re.search(pattern, cv_text, re.IGNORECASE)
        if match:
            try:
                gpa = float(match.group(1))
                if 0.0 <= gpa <= 4.0:
                    details['gpa'] = str(gpa)
                    break
            except ValueError:
                pass
    
    # 2. Extract IELTS scores
    ielts_patterns = [
        r'ielts[:\s]*(overall[:\s]*)?([6-9]\.?\d{0,1})',
        r'ielts\s*score[:\s]*([6-9]\.?\d{0,1})',
        r'english\s*proficiency[:\s]*ielts[:\s]*([6-9]\.?\d{0,1})',
    ]
    for pattern in ielts_patterns:
        match = re.search(pattern, cv_text, re.IGNORECASE)
        if match:
            try:
                ielts = float(match.group(2) if len(match.groups()) > 1 else match.group(1))
                if 0.0 <= ielts <= 9.0:
                    details['ielts_overall'] = str(ielts)
                    break
            except (ValueError, IndexError):
                pass
    
    # 3. Extract qualification/degree
    qual_keywords = [
        ('bachelor', 'bachelors'),
        ('master', 'masters'),
        ('phd', 'doctorate'),
        ('high school', 'high_school'),
        ('+2', 'high_school'),
        ('12th', 'high_school'),
        ('bsc', 'bachelors'),
        ('ba ', 'bachelors'),
        ('btech', 'bachelors'),
        ('be ', 'bachelors'),
        ('beng', 'bachelors'),
        ('msc', 'masters'),
        ('ma ', 'masters'),
        ('mba', 'masters'),
    ]
    
    for keyword, qual_type in qual_keywords:
        if keyword in cv_lower:
            details['current_qualification'] = qual_type
            break
    
    # 4. Use LLM to fill in any missing details
    if len(details) < 3:  # If we didn't find everything
        try:
            from src.utils.groq_cascade import non_streaming_groq
            
            system_prompt = """You are an expert CV parser. Extract these details from the CV as JSON:
- gpa: GPA out of 4.0 (number only, or null if not found)
- ielts_overall: IELTS score (number only, or null if not found)
- current_qualification: One of: 'high_school', 'bachelors', 'masters', 'doctorate' (or null)

Return ONLY valid JSON, no other text. Example: {"gpa": "3.5", "ielts_overall": "7.0", "current_qualification": "bachelors"}"""
            
            user_prompt = f"CV Content:\n{cv_text[:3000]}"
            
            res = await non_streaming_groq(system_prompt, user_prompt, max_tokens=100, temperature=0.0)
            import json
            llm_details = json.loads(res.get("content", "{}"))
            
            # Merge LLM results with pattern matching (pattern matching takes priority)
            for key in ['gpa', 'ielts_overall', 'current_qualification']:
                if key not in details and key in llm_details and llm_details[key]:
                    details[key] = str(llm_details[key])
        except Exception as e:
            log.warning("cv_llm_extraction_failed", error=str(e))
    
    if details:
        log.info("cv_details_extracted", details=details)
    
    return details


# ── Database Queries ────────────────────────────────────────────────────────

def _query_matching_courses(
    target_subject: str,
    countries: list[str],
    inferred_level: Optional[str],
    ielts_score: Optional[float] = None,
    limit: int = 15,
    preferred_states: Optional[list[str]] = None,
) -> list[dict]:
    """Query courses matching the student's profile with rich location data.
    
    For Australia, prioritizes CRICOS data and groups courses by name+university
    to show all available locations.
    """
    db = _get_db()
    all_courses = []
    course_groups = {}  # Group by (name, university) to show multiple locations

    for country in countries:
        # For Australia, prioritize CRICOS data
        query = db.table("courses").select("*").eq("is_active", True).ilike("country", country.strip())
        # Only filter by level if explicitly provided, otherwise get all courses
        if inferred_level and inferred_level.lower() not in ['any', 'none', '']:
            query = query.ilike("level", inferred_level)
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

            rel = max(
                _fuzzy(target_subject, c.get("name") or ""),
                _fuzzy(target_subject, c.get("subject") or ""),
                _fuzzy(target_subject, c.get("subject_category") or ""),
            )
            threshold = 0.35 if target_subject else 0.2
            if rel < threshold:
                continue

            ielts_met = True
            if ielts_score and c.get("ielts_overall"):
                ielts_met = c["ielts_overall"] <= ielts_score

            fee = c.get("tuition_fee") or 0
            currency = c.get("currency", "AUD")
            source = (c.get("source") or "").upper()
            city = c.get("city") or ""
            
            # Create location entry
            location_entry = {
                "city": city,
                "state": state,
                "location": f"{city}, {state}" if (city and state) else (city or state),
                "cricos_code": c.get("cricos_code"),
                "provider_code": c.get("provider_code"),
                "start_dates": c.get("start_dates", []),
            }
            
            # Group courses by name + university
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
                    "gpa_requirement": c.get("gpa_requirement"),
                    "entry_qualification": c.get("entry_qualification"),
                    "apply_url": c.get("apply_url"),
                    "source_url": c.get("source_url"),
                    "source": source,
                    "relevance": round(float(rel), 3),
                    "city": city,        # Flattened primary location
                    "state": state,      # Flattened primary location
                    "cricos_code": c.get("cricos_code"),   # Flattened primary location
                    "provider_code": c.get("provider_code"), # Flattened primary location
                    "locations": [location_entry],
                    "is_cricos": source == "CRICOS",
                }
            else:
                existing = course_groups[course_key]
                # Only add if location is different
                if not any(loc["city"] == city and loc["state"] == state for loc in existing["locations"]):
                    existing["locations"].append(location_entry)
                    if source == "CRICOS":
                        existing["is_cricos"] = True

    # Convert to list and apply rich sorting
    all_courses = list(course_groups.values())
    
    # Sort logic: 
    # 1. Relevance (desc)
    # 2. Source priority (CRICOS > IDP > Others) if Australia
    # 3. Cost (lower first)
    def sort_key(x):
        priority = 3
        if x["country"].lower() == "australia":
            if x.get("is_cricos"): priority = 1
            elif "IDP" in x["source"]: priority = 2
        return (-float(x["relevance"]), priority, x.get("tuition_fee") or 999999)

    all_courses.sort(key=sort_key)
    return all_courses[:limit]


def _query_matching_scholarships(
    target_subject: str,
    countries: list[str],
    inferred_level: Optional[str],
    nationality: str,
    limit: int = 15,
) -> list[dict]:
    """Query scholarships matching the student's profile with rich location data."""
    db = _get_db()
    all_scholarships = []
    today = date.today()

    for country in countries:
        query = db.table("scholarships").select("*").eq("is_active", True).ilike("country", country.strip())
        if inferred_level:
            query = query.ilike("study_level", inferred_level)
        rows = (query.execute()).data or []

        for s in rows:
            match_score = 0.0
            reasons = []

            subj_rel = max(
                _fuzzy(target_subject, s.get("subject") or ""),
                _fuzzy(target_subject, s.get("subject_category") or ""),
                _fuzzy(target_subject, s.get("description") or ""),
            )
            if subj_rel > 0.3:
                match_score += subj_rel * 0.3
                reasons.append(f"Subject match: {subj_rel:.0%}")

            elig = (s.get("eligibility") or "").lower()
            if nationality.lower() in elig:
                match_score += 0.25
                reasons.append(f"Open to {nationality} students")
            elif "all international" in elig or not elig:
                match_score += 0.1
                reasons.append("Open to all international students")

            if s.get("funding_type") == "full":
                match_score += 0.15
                reasons.append("Fully funded")

            if s.get("deadline"):
                try:
                    dl = datetime.fromisoformat(str(s["deadline"])).date()
                    if dl < today:
                        continue
                    days_left = (dl - today).days
                    if days_left < 30:
                        reasons.append(f"Deadline in {days_left} days!")
                except (ValueError, TypeError):
                    pass

            if match_score <= 0.15:
                continue

            val = s.get("award_value_max") or s.get("award_value_min") or 0
            curr = s.get("award_currency", "AUD")
            
            # Get location data
            city = s.get("city") or ""
            state = ""  # Scholarships table doesn't have state, but we can infer from universities if needed

            all_scholarships.append({
                "title": s.get("title"),
                "university": s.get("university"),
                "country": s.get("country"),
                "city": city,
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

SYSTEM_PROMPT = """You are **ScholarRadar AI** — expert study abroad advisor.

## RULES
1. **BE CONCISE** - Max 2-3 sentences per section
2. **USE BULLETS** - No paragraphs, only lists
3. **BE SPECIFIC** - Exact names, costs, URLs from database
4. **NO FLUFF** - Skip generic advice
5. **CRICOS PRIORITY** - For Australia, always show CRICOS code
6. **MULTIPLE LOCATIONS** - Show ALL locations if course available in multiple cities

## OUTPUT FORMAT

### 🎯 Profile (3 bullets)
- Academic: [qualification] + [GPA]
- English: IELTS [score] → [meets/not meets]
- Experience: [years] in [field]

### 🎓 Top 3 Courses
| Uni | Course | CRICOS | Locations | Fee/Year | IELTS |
|-----|--------|--------|-----------|----------|-------|
| [Name] | [Course] | [code] | [City1], [City2] | $[X] | [X] |

- **Why:** [1 reason per course]
- **Admission:** [High/Med/Low]

### 💰 Scholarships (top 3)
- **[Name]** - $[amount] | Deadline: [date] | [URL]

### 💵 Costs
- **Total:** $[X] tuition + $[Y] living = $[Z] for [N] years
- **Budget:** $[budget] → [OK/Short $X]
- **Work:** $[X]/hr × [Y] hrs/wk = ~$[Z]/mo

### 🛂 Visa
- **Type:** [subclass]
- **Proof:** $[amount]
- **Work:** [X] hrs/wk

### 📅 This Week
1. [action] → [URL]
2. [action] → [URL]
3. [action] → [URL]

### ⚠️ Note
- Verify on official websites
- ScholarRadar = AI advisor, NOT migration agent

## TONE: Direct, honest, specific
## MAX: 3000 characters total
"""


def _build_user_prompt(
    profile: dict,
    cv_text: str,
    courses: list[dict],
    scholarships: list[dict],
    universities: list[dict],
    visa_data: list[dict],
    cost_data: list[dict],
) -> str:
    """Build the comprehensive user prompt with all data."""

    sections = []

    # CV section
    if cv_text:
        sections.append(f"""## Student's CV/Resume
<cv>
{cv_text}
</cv>""")

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
        "budget_usd": "Total Budget (USD)",
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

    # Database results
    if courses:
        course_text = json.dumps(courses, indent=2, default=str)
        sections.append(f"""## Matching Courses from Database ({len(courses)} results)
```json
{course_text}
```""")
    else:
        sections.append("## Matching Courses from Database\nNo matching courses found in our database for this profile. Please suggest the student search more broadly or check official university websites directly.")

    if scholarships:
        schol_text = json.dumps(scholarships, indent=2, default=str)
        sections.append(f"""## Matching Scholarships from Database ({len(scholarships)} results)
```json
{schol_text}
```""")
    else:
        sections.append("## Matching Scholarships from Database\nNo matching scholarships found. Suggest checking university-specific funding pages and government scholarship portals directly.")

    if universities:
        uni_text = json.dumps(universities, indent=2, default=str)
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
        cost_text = json.dumps(cost_data, indent=2, default=str)
        sections.append(f"""## Cost of Living Data
```json
{cost_text}
```""")

    sections.append("""## Your Task
Based on ALL the data above — the student's CV, their profile, and the real database results — provide the most comprehensive, actionable, and genuinely helpful study abroad guidance possible. Follow the response format specified in your instructions. Make this genuinely life-changing advice.""")

    return "\n\n".join(sections)


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
        preferred_states = profile_data.get("preferred_states", [])  # NEW: State filtering

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
                from src.utils.cv_parser import extract_text_from_pdf
                pdf_bytes = await cv_file.read()
                cv_text = extract_text_from_pdf(pdf_bytes)
                
                # Auto-detect profile details from CV
                if cv_text:
                    cv_details = await _extract_cv_details(cv_text)
                    
                    # Fill in missing profile fields from CV
                    if cv_details.get('gpa') and not profile_data.get('gpa'):
                        profile_data['gpa'] = cv_details['gpa']
                        log.info("cv_auto_filled_gpa", gpa=cv_details['gpa'])
                    
                    if cv_details.get('ielts_overall') and not profile_data.get('ielts_overall'):
                        profile_data['ielts_overall'] = cv_details['ielts_overall']
                        log.info("cv_auto_filled_ielts", ielts=cv_details['ielts_overall'])
                    
                    if cv_details.get('current_qualification') and not profile_data.get('current_qualification'):
                        profile_data['current_qualification'] = cv_details['current_qualification']
                        log.info("cv_auto_filled_qualification", qual=cv_details['current_qualification'])
                    
                    # If subject is missing, infer it from the CV
                    if not target_subject:
                        target_subject = await _infer_subject_from_cv(cv_text)
                        profile_data["target_subject"] = target_subject
            except ValueError as e:
                return JSONResponse(status_code=400, content={"error": str(e)})
            except Exception as e:
                log.error("cv_parse_error", error=str(e))
                cv_text = ""  # Continue without CV

        # Extract profile fields
        current_qualification = profile_data.get("current_qualification", "")
        ielts_score = profile_data.get("ielts_overall")
        if ielts_score:
            try:
                ielts_score = float(ielts_score)
            except (ValueError, TypeError):
                ielts_score = None

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
        )

        # ── Query database for matching data ──
        log.info("querying_database", countries=preferred_countries)
        
        # Get matching courses
        courses = _query_matching_courses(
            target_subject=target_subject,
            countries=preferred_countries,
            inferred_level=target_level,
            ielts_score=ielts_score,
            limit=15,
            preferred_states=preferred_states,  # NEW: State filtering
        )
        
        # Get matching scholarships
        scholarships = _query_matching_scholarships(
            target_subject=target_subject,
            countries=preferred_countries,
            inferred_level=target_level,
            nationality=nationality,
            limit=15,
        )
        
        # Get universities
        universities = _query_universities(
            countries=preferred_countries,
            limit=10,
        )
        
        # Get visa data
        visa_data = _query_visa_data(
            nationality=nationality,
            countries=preferred_countries,
        )
        
        # Get cost of living
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
            courses=courses,
            scholarships=scholarships,
            universities=universities,
            visa_data=visa_data,
            cost_data=cost_data,
        )

        # Stream response directly - no complex agent loop
        async def event_stream():
            try:
                # Send metadata first so frontend can display results
                log.info("sending_metadata", courses=len(courses), scholarships=len(scholarships))
                yield f"data: {json.dumps({'type': 'metadata', 'courses_found': len(courses), 'scholarships_found': len(scholarships)})}\n\n"
                
                # Send courses data
                if courses:
                    log.info("sending_courses", count=len(courses))
                    yield f"data: {json.dumps({'type': 'courses', 'data': courses})}\n\n"
                
                # Send scholarships data
                if scholarships:
                    log.info("sending_scholarships", count=len(scholarships))
                    yield f"data: {json.dumps({'type': 'scholarships', 'data': scholarships})}\n\n"
                
                yield f"data: {json.dumps({'type': 'status', 'content': 'Generating your personalized analysis...'})}\n\n"

                # Use simple streaming instead of complex agent
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
