"""
Visa MCP tools — 5 production-quality tools for requirements, financial proof,
checklists, timelines, and visa strength assessment.
Nepal-specific detailed guidance included.
"""
from __future__ import annotations
from datetime import date, datetime, timedelta
from typing import Any, Optional
import structlog
from mcp.server.fastmcp import FastMCP

log = structlog.get_logger("mcp_server.tools.visa")

_HIGH_SCRUTINY = {"nepal","nepalese","bangladesh","bangladeshi","pakistan","pakistani",
                  "india","indian","sri lanka","sri lankan","nigeria","nigerian"}

_AU_DOCS = [
    {"document":"Valid Passport","description":"Valid for 6+ months beyond stay","required":True},
    {"document":"Confirmation of Enrolment (CoE)","description":"From CRICOS-registered provider","required":True},
    {"document":"GTE Statement","description":"Why you're a genuine student, course reasons, plans to return home","required":True},
    {"document":"Financial Evidence","description":"Bank statements showing tuition + AUD 29,710/yr living + travel","required":True},
    {"document":"English Test Results","description":"IELTS Academic / PTE / TOEFL report","required":True},
    {"document":"Academic Transcripts","description":"All qualifications with certified translations","required":True},
    {"document":"OSHC","description":"Overseas Student Health Cover for visa duration","required":True},
    {"document":"Health Examination","description":"From Bupa panel physician","required":True},
    {"document":"Police Clearance","description":"From home country and any 12+ month residence","required":True},
    {"document":"Passport Photos","description":"Meeting AU visa specs","required":True},
    {"document":"Work Experience Proof","description":"Employment letters, payslips — strengthens GTE","required":False},
    {"document":"Statement of Purpose","description":"Course choice, career goals, why this uni/city","required":False},
]

def _get_db():
    from src.database.client import get_db
    return get_db()

def register_tools(mcp: FastMCP):
    """Register all 5 visa tools."""

    @mcp.tool()
    async def get_visa_requirements(nationality:str, destination_country:str) -> dict[str,Any]:
        """Get full student visa requirements for a nationality and destination.
        Returns visa type, financial requirements, processing times, work rights, and source URLs.
        Args:
            nationality: e.g. "nepal", "india".
            destination_country: e.g. "australia".
        """
        try:
            log.info("tool_call",tool="get_visa_requirements",nationality=nationality)
            db = _get_db()
            rows = (db.table("visa_requirements").select("*")
                .ilike("nationality",nationality.strip())
                .ilike("destination_country",destination_country.strip()).execute()).data or []
            if not rows:
                return {"results":[],"total_count":0,
                    "message":f"No visa data for {nationality} → {destination_country}."}
            v = rows[0]
            result = {
                "nationality":v.get("nationality"),"destination_country":v.get("destination_country"),
                "visa_type":v.get("visa_type"),"visa_subclass":v.get("visa_subclass"),
                "financial_requirement_aud_per_year":v.get("financial_requirement_aud"),
                "processing_time":{"min_weeks":v.get("processing_weeks_min"),
                    "max_weeks":v.get("processing_weeks_max"),
                    "typical":f"{v.get('processing_weeks_min','?')}–{v.get('processing_weeks_max','?')} weeks"},
                "work_rights":{"hours_per_fortnight":v.get("work_rights_hours_per_week"),
                    "note":"48 hrs/fortnight during term, unlimited during breaks"},
                "health_requirements":v.get("health_requirements"),
                "notes":v.get("notes"),"source_url":v.get("source_url"),
                "last_updated":str(v["last_updated"]) if v.get("last_updated") else None,
            }
            if nationality.lower().strip() in _HIGH_SCRUTINY:
                result["scrutiny_warning"] = (
                    f"Applications from {nationality} receive enhanced scrutiny. "
                    "Ensure GTE is detailed, financials are robust, all docs certified.")
            return result
        except Exception as e:
            log.error("tool_error",tool="get_visa_requirements",error=str(e))
            return {"error":"Failed to get visa requirements.","error_type":"tool_error"}

    @mcp.tool()
    async def calculate_financial_proof(nationality:str, destination_country:str,
            course_duration_months:int, annual_tuition_aud:float,
            has_scholarship:bool=False, scholarship_value_aud:float=0) -> dict[str,Any]:
        """Calculate exact financial proof needed for student visa.
        Breaks down tuition, living costs, OSHC, visa fees, travel.
        Args:
            nationality: e.g. "nepal".
            destination_country: e.g. "australia".
            course_duration_months: Total duration e.g. 24.
            annual_tuition_aud: Annual tuition in AUD.
            has_scholarship: Has scholarship covering some costs.
            scholarship_value_aud: Annual scholarship value in AUD.
        """
        try:
            log.info("tool_call",tool="calculate_financial_proof")
            db = _get_db()
            vr = (db.table("visa_requirements").select("*")
                .ilike("nationality",nationality.strip())
                .ilike("destination_country",destination_country.strip()).execute()).data or []
            living = vr[0].get("financial_requirement_aud",29710) if vr else 29710
            yrs = course_duration_months/12
            tuition_total = annual_tuition_aud*yrs
            schol_ded = scholarship_value_aud*yrs if has_scholarship else 0
            tuition_net = max(0, tuition_total - schol_ded)
            living_total = living*yrs
            oshc_total = 650*yrs
            visa_fee = 710; travel = 2500
            grand = tuition_net + living_total + oshc_total + visa_fee + travel
            yr1 = max(0, annual_tuition_aud - (scholarship_value_aud if has_scholarship else 0) + living + 650 + visa_fee + travel)
            return {
                "breakdown":{"tuition_total":round(tuition_total,2),
                    "scholarship_deduction":round(schol_ded,2),
                    "tuition_after_scholarship":round(tuition_net,2),
                    "living_costs_total":round(living_total,2),"living_per_year":living,
                    "oshc_total":round(oshc_total,2),"visa_fee":visa_fee,"travel":travel},
                "grand_total_aud":round(float(grand),2),
                "first_year_proof_needed":round(float(yr1),2),
                "advice":[f"Show at least AUD {yr1:,.0f} for visa application.",
                    "Bank statements should show funds held 3-6 months.",
                    "Loan sanction letters from approved banks accepted.",
                    "Scholarship letters reduce proof required."],
                "currency":"AUD"}
        except Exception as e:
            log.error("tool_error",tool="calculate_financial_proof",error=str(e))
            return {"error":"Failed to calculate financial proof.","error_type":"tool_error"}

    @mcp.tool()
    async def get_visa_checklist(nationality:str, destination_country:str) -> dict[str,Any]:
        """Get complete document checklist for student visa application.
        Each document has description and whether mandatory or recommended.
        Args:
            nationality: e.g. "nepal".
            destination_country: e.g. "australia".
        """
        try:
            log.info("tool_call",tool="get_visa_checklist")
            checklist = list(_AU_DOCS)
            nl = nationality.lower().strip()
            if nl in _HIGH_SCRUTINY:
                checklist.append({"document":"Enhanced GTE Statement",
                    "description":f"As {nationality} applicant: specific course reasons, career plan, family ties, property","required":True})
                checklist.append({"document":"Property/Asset Proof",
                    "description":"Land ownership, business registration — home country ties","required":False})
                checklist.append({"document":"Family Sponsor Docs",
                    "description":"Sponsor bank statements, income proof, tax returns","required":False})
            if nl in ("nepal","nepalese"):
                checklist.append({"document":"Employer No-Objection Letter",
                    "description":"If employed — shows career to return to","required":False})
                checklist.append({"document":"Citizenship Certificate",
                    "description":"Nagarikta — may be requested","required":False})
            req = [d for d in checklist if d["required"]]
            rec = [d for d in checklist if not d["required"]]
            return {"nationality":nationality,"destination_country":destination_country,
                "required_documents":req,"recommended_documents":rec,
                "total_required":len(req),"total_recommended":len(rec),
                "tips":["Get all docs certified/notarized","Non-English docs need certified translations",
                    "Keep originals and copies","Start gathering 2+ months before application"]}
        except Exception as e:
            log.error("tool_error",tool="get_visa_checklist",error=str(e))
            return {"error":"Failed to get checklist.","error_type":"tool_error"}

    @mcp.tool()
    async def get_processing_timeline(nationality:str, destination_country:str,
            course_start_date:str) -> dict[str,Any]:
        """Get recommended visa application timeline working backward from course start.
        Args:
            nationality: e.g. "nepal".
            destination_country: e.g. "australia".
            course_start_date: ISO format YYYY-MM-DD.
        """
        try:
            log.info("tool_call",tool="get_processing_timeline")
            try:
                start = datetime.fromisoformat(course_start_date).date()
            except ValueError:
                return {"error":f"Invalid date: {course_start_date}. Use YYYY-MM-DD.","error_type":"validation_error"}
            db = _get_db()
            vr = (db.table("visa_requirements").select("*")
                .ilike("nationality",nationality.strip())
                .ilike("destination_country",destination_country.strip()).execute()).data or []
            proc_max = vr[0].get("processing_weeks_max",12) if vr else 12
            hs = nationality.lower().strip() in _HIGH_SCRUTINY
            buf = 4 if hs else 2
            today = date.today()
            apply_by = start - timedelta(weeks=proc_max+buf)
            health_by = apply_by - timedelta(weeks=2)
            docs_by = health_by - timedelta(weeks=3)
            ielts_by = docs_by - timedelta(weeks=4)
            plan_by = ielts_by - timedelta(weeks=4)
            def _step(n,act,dl):
                d=(dl-today).days
                return {"step":n,"action":act,"deadline":str(dl),"days_from_today":d,
                    "status":"overdue" if today>dl else "upcoming"}
            timeline = [
                _step(1,"Start planning & IELTS prep",plan_by),
                _step(2,"Take IELTS test",ielts_by),
                _step(3,"Gather all documents",docs_by),
                _step(4,"Complete health examination",health_by),
                _step(5,"Submit visa application",apply_by),
                _step(6,f"Expected decision (up to {proc_max} weeks)",start-timedelta(weeks=buf)),
                _step(7,"Course starts — arrive 1-2 weeks early",start),
            ]
            overdue = sum(1 for t in timeline if t["status"]=="overdue")
            return {"course_start_date":course_start_date,"days_until_start":(start-today).days,
                "timeline":timeline,"overdue_steps":overdue,"is_high_scrutiny":hs,
                "warning":f"⚠️ {overdue} steps past deadline. Expedite!" if overdue else None}
        except Exception as e:
            log.error("tool_error",tool="get_processing_timeline",error=str(e))
            return {"error":"Failed to generate timeline.","error_type":"tool_error"}

    @mcp.tool()
    async def assess_visa_strength(nationality:str, destination_country:str, age:int,
            has_financial_proof:bool, financial_amount_aud:float, annual_tuition_aud:float,
            course_duration_months:int, has_ielts:bool, ielts_score:Optional[float]=None,
            has_previous_visa_refusal:bool=False, has_work_experience_years:float=0,
            has_family_property:bool=False, is_employed:bool=False,
            gap_years_after_study:int=0, study_level:str="postgraduate") -> dict[str,Any]:
        """Assess visa application strength with detailed scoring and improvement advice.
        Evaluates financials, English, home ties, academic profile, and risk factors.
        Nepal-specific: includes detailed GTE advice, common refusal reasons, financial tips.
        Args:
            nationality: e.g. "nepal".
            destination_country: e.g. "australia".
            age: Student's age.
            has_financial_proof: Bank statements/loan ready.
            financial_amount_aud: Total proof in AUD.
            annual_tuition_aud: Annual tuition AUD.
            course_duration_months: Course months.
            has_ielts: Has valid IELTS.
            ielts_score: IELTS band if available.
            has_previous_visa_refusal: Prior refusal.
            has_work_experience_years: Work experience years.
            has_family_property: Family owns property.
            is_employed: Currently employed.
            gap_years_after_study: Years gap since last study.
            study_level: undergraduate/postgraduate/doctorate.
        """
        try:
            log.info("tool_call",tool="assess_visa_strength")
            score=0.0; mx=100.0
            strengths=[]; weaknesses=[]; recs=[]; flags=[]
            nl = nationality.lower().strip()
            hs = nl in _HIGH_SCRUTINY; is_np = nl in ("nepal","nepalese")
            yrs = course_duration_months/12
            req_total = (annual_tuition_aud*yrs)+(29710*yrs)
            # Financial (30pts)
            if has_financial_proof and req_total>0:
                cov = financial_amount_aud/req_total
                if cov>=1.2: score+=30; strengths.append(f"Excellent financial coverage: {cov:.0%}")
                elif cov>=1.0: score+=22; strengths.append(f"Adequate: {cov:.0%}"); recs.append("Show 20% more than minimum")
                elif cov>=0.7: score+=12; weaknesses.append(f"Only {cov:.0%} coverage"); recs.append("Add savings/FD/loan letters")
                else: score+=5; weaknesses.append(f"Shortfall: {cov:.0%}"); flags.append("Insufficient funds = top refusal reason"); recs.append(f"Need AUD {req_total-financial_amount_aud:,.0f} more")
            elif not has_financial_proof:
                weaknesses.append("No financial proof yet"); flags.append("Prepare financial evidence first")
            # English (15pts)
            if has_ielts and ielts_score:
                if ielts_score>=7.0: score+=15; strengths.append(f"Strong IELTS: {ielts_score}")
                elif ielts_score>=6.5: score+=12; strengths.append(f"Adequate IELTS: {ielts_score}")
                elif ielts_score>=6.0: score+=8; weaknesses.append(f"IELTS {ielts_score} is lower side"); recs.append("Check specific course req")
                else: score+=3; weaknesses.append(f"IELTS {ielts_score} may be insufficient"); recs.append("Retake or do English pathway")
            else: weaknesses.append("No IELTS"); recs.append("Book IELTS Academic ASAP")
            # Home ties (20pts)
            ties=0
            if has_family_property: ties+=8; strengths.append("Family property — strong home ties")
            if is_employed: ties+=7; strengths.append("Currently employed — career to return to")
            elif has_work_experience_years>=2: ties+=4; strengths.append(f"{has_work_experience_years:.0f}yr work experience")
            if ties==0: weaknesses.append("Limited home ties"); recs.append("Include property docs, business registration")
            score += min(ties,20)
            # Academic (15pts)
            if study_level=="doctorate": score+=15; strengths.append("PhD — strong academic purpose")
            elif study_level=="postgraduate": score+=12; strengths.append("Postgrad — logical progression")
            else: score+=10
            if gap_years_after_study>5: score-=3; weaknesses.append(f"{gap_years_after_study}yr study gap"); recs.append("Address gap in GTE clearly")
            elif gap_years_after_study>2: weaknesses.append(f"{gap_years_after_study}yr gap — prepare explanation")
            # Risk (20pts)
            risk=20
            if has_previous_visa_refusal: risk-=10; flags.append("Previous refusal is significant"); recs.append("Address refusal in GTE")
            if hs: risk-=5; flags.append(f"{nationality} receives enhanced scrutiny")
            if age>35 and study_level in ("undergraduate","foundation"): risk-=3; flags.append("Age vs study level mismatch")
            score += max(0,risk)
            # Overall
            pct = score/mx*100
            if pct>=80: overall,verdict = "strong","Strong application. Focus on well-written GTE."
            elif pct>=60: overall,verdict = "moderate","Some gaps. Address weaknesses before applying."
            elif pct>=40: overall,verdict = "needs_improvement","Several areas need work. Review all recommendations."
            else: overall,verdict = "weak","Significant improvements needed. Consider delaying application."
            result = {"overall_strength":overall,"score":round(float(pct),1),"score_out_of":100,
                "verdict":verdict,"strengths":strengths,"weaknesses":weaknesses,
                "risk_flags":flags,"recommendations":recs}
            if is_np:
                result["nepal_specific_advice"] = {
                    "scrutiny_level":"HIGH",
                    "context":"Nepal is high-risk for AU student visas. Higher-than-average refusal rate. Application must be exceptionally prepared.",
                    "critical_requirements":["GTE must be very specific — generic = rejected",
                        "Bank balance 6+ months — not recent deposits","Clear career path in Nepal post-graduation",
                        "CA-certified sponsor financials","Nepal-specific career opportunities linked to course"],
                    "common_refusal_reasons":["Weak/generic GTE","Fabricated/recent financial evidence",
                        "No clear reason to return","Unexplained study gap","Course misaligned with background",
                        "Choosing low-cost regional course (migration intent signal)"],
                    "gte_tips":["Name specific Nepal employers you'd work for",
                        "Reference Nepal's growing IT/hydropower/tourism sectors",
                        "Mention family business application plans","Explain why AU over India/Malaysia",
                        "Cite specific course features unavailable in Nepal",
                        "Detail family in Nepal (parents, siblings, property)"],
                    "financial_tips":["Show savings 6+ months — avoid sudden deposits",
                        "CA-certified income statement for sponsors",
                        "Include Lalpurja (land certificate) as extra evidence",
                        "Education loan sanction from recognized Nepali bank",
                        "Remittance receipts if family works abroad"]}
            return result
        except Exception as e:
            log.error("tool_error",tool="assess_visa_strength",error=str(e))
            return {"error":"Failed to assess visa strength.","error_type":"tool_error"}
