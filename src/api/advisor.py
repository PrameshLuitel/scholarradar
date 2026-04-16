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


# ── Database Queries ────────────────────────────────────────────────────────

def _query_matching_courses(
    target_subject: str,
    countries: list[str],
    inferred_level: Optional[str],
    ielts_score: Optional[float] = None,
    limit: int = 15,
) -> list[dict]:
    """Query courses matching the student's profile."""
    db = _get_db()
    all_courses = []

    for country in countries:
        query = db.table("courses").select("*").eq("is_active", True).ilike("country", country.strip())
        if inferred_level:
            query = query.ilike("level", inferred_level)
        rows = (query.execute()).data or []

        for c in rows:
            course_name = (c.get("name") or "").lower()
            # Filter out junk 6-month study abroad / non-degree programs unless specifically relevant
            junk_keywords = ["study abroad", "exchange", "exchange program", "non-award"]
            if any(k in course_name for k in junk_keywords) and not any(k in target_subject.lower() for k in junk_keywords):
                continue

            rel = max(
                _fuzzy(target_subject, c.get("name") or ""),
                _fuzzy(target_subject, c.get("subject") or ""),
                _fuzzy(target_subject, c.get("subject_category") or ""),
            )
            # If subject is provided, be strict. If not, we provide more top courses for AI to filter via CV.
            threshold = 0.35 if target_subject else 0.2
            if rel < threshold:
                continue

            ielts_met = True
            if ielts_score and c.get("ielts_overall"):
                ielts_met = c["ielts_overall"] <= ielts_score

            fee = c.get("tuition_fee") or 0
            currency = c.get("currency", "AUD")
            source = (c.get("source") or "").upper()
            
            # Basic match reasoning
            match_reasons = []
            if rel >= 0.8: match_reasons.append("Perfect subject match")
            elif rel >= 0.5: match_reasons.append("Strong subject alignment")
            
            if ielts_met: match_reasons.append("Meets English requirements")
            
            # If university is high-ranked (world_ranking is in universities table, but we don't have it here yet,
            # we can add a generic high-quality tag if relevance is high and fee is standard)

            all_courses.append({
                "name": c.get("name"),
                "university": c.get("university"),
                "country": c.get("country"),
                "city": c.get("city"),
                "state": c.get("state"),
                "level": c.get("level"),
                "tuition_fee": fee,
                "tuition_display": f"{currency} {fee:,.0f}/yr" if fee else "Contact university",
                "duration_months": c.get("duration_months"),
                "ielts_required": c.get("ielts_overall"),
                "ielts_met": ielts_met,
                "gpa_requirement": c.get("gpa_requirement"),
                "entry_qualification": c.get("entry_qualification"),
                "apply_url": c.get("apply_url"),
                "source_url": c.get("source_url"),
                "cricos_code": c.get("cricos_code"),
                "provider_code": c.get("provider_code"),
                "source": source,
                "relevance": round(float(rel), 3),
                "match_reason": " • ".join(match_reasons) if match_reasons else "Relevance match",
            })

    # Sort logic: 
    # 1. Relevance
    # 2. Source priority (CRICOS > IDP > Others) if Australia
    # 3. Cost (lower first)
    def sort_key(x):
        priority = 3
        if x["country"].lower() == "australia":
            if "CRICOS" in x["source"]: priority = 1
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
    """Query scholarships matching the student's profile."""
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

            all_scholarships.append({
                "title": s.get("title"),
                "university": s.get("university"),
                "country": s.get("country"),
                "funding_type": s.get("funding_type"),
                "value": f"{curr} {val:,.0f}" if val else "Contact provider",
                "value_numeric": val,
                "deadline": str(s["deadline"]) if s.get("deadline") else None,
                "eligibility": s.get("eligibility"),
                "match_score": round(float(match_score), 3),
                "why_matched": reasons,
                "apply_url": s.get("apply_url"),
                "source_url": s.get("source_url"),
            })

    all_scholarships.sort(key=lambda x: float(x["match_score"]), reverse=True)
    return all_scholarships[:limit]


def _query_universities(countries: list[str], limit: int = 10) -> list[dict]:
    """Get top universities in preferred countries."""
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
                "world_ranking": u.get("world_ranking"),
                "acceptance_rate": u.get("acceptance_rate"),
                "ielts_minimum": u.get("ielts_minimum"),
                "tuition_min": u.get("tuition_min"),
                "tuition_max": u.get("tuition_max"),
                "website": u.get("website"),
            })
    all_unis.sort(key=lambda x: x.get("world_ranking") or 9999)
    return all_unis[:limit]


def _query_visa_data(nationality: str, countries: list[str]) -> list[dict]:
    """Get visa requirements for student's nationality → each country."""
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
                "financial_requirement_aud": v.get("financial_requirement_aud"),
                "processing_weeks": f"{v.get('processing_weeks_min', '?')}–{v.get('processing_weeks_max', '?')}",
                "work_rights_hours": v.get("work_rights_hours_per_week"),
                "health_requirements": v.get("health_requirements"),
            })
        else:
            results.append({
                "country": country,
                "message": f"No visa data found for {nationality} → {country}",
            })
    return results


def _query_cost_of_living(countries: list[str]) -> list[dict]:
    """Get cost of living data for top cities in each country."""
    db = _get_db()
    results = []
    for country in countries:
        rows = (db.table("cost_of_living").select("*")
                .ilike("country", country.strip())
                .limit(3).execute()).data or []
        for c in rows:
            results.append({
                "city": c.get("city"),
                "country": c.get("country"),
                "rent_shared_range": f"{c.get('rent_shared_min', '?')}–{c.get('rent_shared_max', '?')}",
                "food_monthly": c.get("food_monthly"),
                "transport_monthly": c.get("transport_monthly"),
                "total_monthly_min": c.get("total_monthly_min"),
                "total_monthly_max": c.get("total_monthly_max"),
                "part_time_wage_hourly": c.get("part_time_wage_hourly"),
                "currency": c.get("currency", "AUD"),
            })
    return results


# ── System Prompt ───────────────────────────────────────────────────────────

SYSTEM_PROMPT = """You are **ScholarRadar AI** — the world's most advanced study abroad advisor. You help students worldwide find their perfect university match based on their unique profile, goals, and circumstances.

## YOUR MISSION
Your goal is to provide genuinely life-changing guidance that helps students make informed decisions about their education abroad. Every recommendation must be personalized, actionable, and honest.

## CORE PRINCIPLES

### 1. DEEP PROFILE ANALYSIS
- Read their CV carefully if provided - reference specific projects, skills, work experience, achievements
- Understand their background, not just their grades
- Identify their strengths and areas for improvement
- Connect their past experiences to their future goals
- Consider their financial reality - this is often their family's life savings

### 2. HONEST & TRANSPARENT
- If their budget is too low, say it clearly and provide specific alternatives
- If their IELTS/GPA is insufficient, tell them exactly what they need
- Never sugarcoat challenges - students need truth to make good decisions
- Provide realistic admission probabilities with reasoning
- Be upfront about visa challenges for their nationality

### 3. HYPER-PERSONALIZED
- Every recommendation must explain WHY it fits THEIR specific background
- Reference their CV details, work experience, projects, skills
- Connect their career goals to specific courses and universities
- Provide tailored advice for their nationality's visa situation
- Suggest scholarships they actually qualify for based on their profile

### 4. ACTIONABLE & SPECIFIC
- Every recommendation needs: exact name, cost, deadline, apply URL
- Provide specific next steps, not generic advice
- Include month-by-month timeline from NOW to their intake
- Give exact test score targets if they need to improve
- List concrete action items they can do THIS WEEK

### 5. COUNTRY STRICT
- ONLY recommend universities/courses/scholarships in their selected countries
- Never suggest countries they didn't choose
- Respect their preferences completely

### 6. FINANCIAL REALITY CHECK
- Calculate total costs (tuition + living) for full course duration
- Compare directly to their stated budget
- Show scholarship impact on affordability
- Include part-time work opportunities and realistic earnings
- Provide cheaper alternatives if budget is insufficient

## DATA USAGE RULES
1. **Use tools extensively** - search_courses, search_scholarships, get_visa_requirements, get_universities, etc.
2. **Never hallucinate** - every fact must come from tool results
3. **Quote exact data** - use exact names, fees, URLs from database
4. **If data missing** - say "Check official website" rather than guessing
5. **Multiple tool calls** - call tools for each country they selected

## RESPONSE STRUCTURE
Use these exact section headers. Write 2-4 substantial paragraphs per section:

### 🎯 Your Profile Analysis
Analyze their complete profile in detail:
- Academic background and performance
- Work experience and skills (from CV if provided)
- Strengths and competitive advantages
- Areas needing attention (gaps, low scores, etc.)
- How their background aligns with their goals
- Specific insights that show you truly understand them

### 🎓 Best-Match Universities & Courses
Recommend 3-5 specific courses from database results. For EACH:
- **Why it's perfect for them** (reference their CV/background specifically)
- University name, course name, location
- Annual tuition fee AND total course cost
- Entry requirements vs their actual qualifications
- IELTS requirement vs their score (or what they need)
- Direct application URL from database
- Admission probability: High/Medium/Low with honest reasoning
- What makes this course stand out for their career

### 💰 Scholarships You Can Win
Highlight 3-5 scholarships from results. For EACH:
- Exact award value and what it covers
- Why THEY specifically qualify (reference their profile)
- Application deadline — mark ⚠️ URGENT if <30 days
- Direct application link
- Specific tips to strengthen their application
- Realistic probability of winning it

### 💵 Complete Financial Breakdown
Be brutally honest with numbers:
- Total cost for top 3 choices (tuition × years + living costs)
- Their budget vs actual costs — is it realistic?
- Scholarships that could reduce costs and by how much
- Part-time work: hourly wage, max hours/week, monthly earnings potential
- If budget insufficient: specific cheaper alternatives in their countries
- Simple cost comparison table
- Honest assessment: "Your budget of $X is/isn't sufficient because..."

### 🛂 Your Visa Pathway
For their nationality to each destination:
- Exact visa subclass/type and requirements
- Financial proof required (specific amount in local currency)
- Processing time and when to apply
- Work rights during and after study
- Post-study work visa duration
- Honest visa approval likelihood for their nationality
- Specific red flags to avoid in their application
- Documents they need to start preparing NOW

### 📝 Test Score Strategy
If they have IELTS/test scores:
- Which recommended courses they qualify for now
- What a 0.5 improvement would unlock (specific courses)
- Whether retaking is worth time/money for their goals
If no scores yet:
- Target scores for their recommended courses
- Preparation timeline and resources
- Alternative tests accepted (TOEFL, PTE, etc.)

### 📅 Your Month-by-Month Action Plan
Create specific timeline from NOW to their target intake:
- Each month: primary task + specific action items
- Hard deadlines they cannot miss
- What to prepare for following month
- Buffer time for unexpected delays
- Final checklist before departure

### 🚀 Your Career Pathway After Graduation
- Specific career outcomes for their field in destination country
- Average graduate salary (cite real figures from data)
- Job market demand level and growth trends
- Post-study work visa duration and PR pathway
- How this connects to their stated career goal
- Companies/employers that hire graduates from their recommended courses
- Skills they should build during study to maximize job prospects

### ⚡ 5 Things to Do THIS WEEK
Number 1-5, most urgent first. Be hyper-specific:
- NOT "research universities" 
- BUT "Apply to MSc Computer Science at University of Melbourne before March 15 at apply.unimelb.edu.au"
- Include exact URLs, deadlines, amounts
- Prioritize time-sensitive actions

### ⚠️ Important Notes
- ScholarRadar is an AI data aggregator, NOT a migration agent or legal advisor
- All fees, deadlines, visa rules must be verified on official websites
- Data sourced from ScholarRadar/FindUni databases — always double-check
- Immigration rules change frequently — verify before making decisions
- This guidance is personalized but not a guarantee of admission

## TONE & STYLE
- Professional but warm and encouraging
- Direct and honest — students appreciate truth over fluff
- Use specific numbers, names, URLs everywhere
- Reference their personal details to show genuine understanding
- Balance optimism with realistic expectations
- Write like an expert counselor who genuinely cares about their success
- Avoid generic statements — everything must be specific to THEM

## CRITICAL REMINDERS
- You are their trusted advisor — treat their future seriously
- Every recommendation must be backed by actual tool data
- Personalization is your superpower — use their CV details
- Financial honesty protects them from bad decisions
- Specific action items are more valuable than general advice
- Your guidance could change their life — make it count
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

    try:
        # Parse profile JSON
        try:
            profile_data = json.loads(profile)
        except json.JSONDecodeError:
            return JSONResponse(
                status_code=400,
                content={"error": "Invalid profile JSON"},
            )

        # Validate required fields
        nationality = profile_data.get("nationality", "").strip()
        target_subject = profile_data.get("target_subject", "").strip()
        preferred_countries = profile_data.get("preferred_countries", [])

        if not nationality:
            return JSONResponse(status_code=400, content={"error": "Nationality is required"})
        if not preferred_countries:
            return JSONResponse(status_code=400, content={"error": "At least one preferred country is required"})

        if isinstance(preferred_countries, str):
            preferred_countries = [c.strip() for c in preferred_countries.split(",")]

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
                
                # If subject is missing, infer it from the CV
                if not target_subject and cv_text:
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

        # Stream response via Agentic Loop
        async def event_stream():
            agent = AgentRunner(system_prompt=SYSTEM_PROMPT, max_iterations=6)
            
            # Send metadata first so frontend can display results
            yield f"data: {json.dumps({'type': 'metadata', 'courses_found': len(courses), 'scholarships_found': len(scholarships)})}\n\n"
            
            # Send courses data
            if courses:
                yield f"data: {json.dumps({'type': 'courses', 'data': courses})}\n\n"
            
            # Send scholarships data
            if scholarships:
                yield f"data: {json.dumps({'type': 'scholarships', 'data': scholarships})}\n\n"
            
            yield f"data: {json.dumps({'type': 'status', 'content': 'Analyzing your profile...'})}\n\n"

            try:
                async for event in agent.run(user_prompt):
                    if event["type"] == "model":
                        yield f"data: {json.dumps({'type': 'model', 'model': event['model'], 'display_name': get_model_display_name(event['model'])})}\n\n"
                    elif event["type"] == "chunk":
                        yield f"data: {json.dumps({'type': 'chunk', 'content': event['content']})}\n\n"
                    elif event["type"] == "status":
                        yield f"data: {json.dumps({'type': 'status', 'content': event['message']})}\n\n"
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
                    elif event["type"] == "error":
                        yield f"data: {json.dumps({'type': 'error', 'message': event['message']})}\n\n"

                yield "data: [DONE]\n\n"
            except Exception as e:
                log.error("agent_run_failed", error=str(e))
                yield f"data: {json.dumps({'type': 'error', 'message': f'Agent execution failed: {str(e)}'})}\n\n"

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
