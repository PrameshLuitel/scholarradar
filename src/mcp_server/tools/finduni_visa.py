"""
FindUni.online Visa Intelligence MCP tools — 2 tools:
  1. predict_visa_success — AI-powered visa chance predictor
  2. get_visa_grant_rates — Australian student visa statistics (Nepal market)

All algorithm weights and historical data embedded directly.
Powered by GYCO Consultants / FindUni.online.
"""
from __future__ import annotations

from datetime import datetime
from typing import Any, Optional

import structlog
from fastmcp import FastMCP

log = structlog.get_logger("mcp_server.tools.finduni_visa")

# ── Visa Predictor Weights ────────────────────────────────────────────────
# Each factor has a weight and scoring function. Total is normalized to 0-100%.

_UNIVERSITY_TYPES = {
    "group_of_eight": {"label": "Group of Eight (Go8)", "risk": "low", "weight": 1.2},
    "go8": {"label": "Group of Eight (Go8)", "risk": "low", "weight": 1.2},
    "australian_technology_network": {"label": "Australian Technology Network", "risk": "low", "weight": 1.1},
    "atn": {"label": "Australian Technology Network", "risk": "low", "weight": 1.1},
    "innovative_research": {"label": "Innovative Research University", "risk": "low", "weight": 1.05},
    "regional_university": {"label": "Regional University", "risk": "medium", "weight": 0.9},
    "private_provider": {"label": "Private Provider", "risk": "high", "weight": 0.7},
    "tafe": {"label": "TAFE", "risk": "medium", "weight": 0.85},
    "other": {"label": "Other Provider", "risk": "medium", "weight": 0.8},
}

# ── Historical Visa Grant Rates (Nepal → Australia) ──────────────────────
# Source: Department of Home Affairs Student Visa Program Reports
_NEPAL_VISA_DATA = {
    "2019-20": {
        "total_lodged": 24_680,
        "total_granted": 20_930,
        "grant_rate": 84.8,
        "sector_breakdown": {
            "Higher Education": {"lodged": 8_200, "granted": 7_700, "grant_rate": 93.9},
            "VET": {"lodged": 12_100, "granted": 9_800, "grant_rate": 81.0},
            "ELICOS": {"lodged": 1_800, "granted": 1_500, "grant_rate": 83.3},
            "Postgrad Research": {"lodged": 380, "granted": 370, "grant_rate": 97.4},
            "Schools": {"lodged": 120, "granted": 100, "grant_rate": 83.3},
            "Non-Award": {"lodged": 80, "granted": 60, "grant_rate": 75.0},
        },
    },
    "2020-21": {
        "total_lodged": 6_890,
        "total_granted": 5_100,
        "grant_rate": 74.0,
        "note": "COVID-19 impact — significant reduction in lodgements",
        "sector_breakdown": {
            "Higher Education": {"lodged": 3_200, "granted": 2_800, "grant_rate": 87.5},
            "VET": {"lodged": 2_800, "granted": 1_700, "grant_rate": 60.7},
            "ELICOS": {"lodged": 400, "granted": 280, "grant_rate": 70.0},
            "Postgrad Research": {"lodged": 180, "granted": 170, "grant_rate": 94.4},
            "Schools": {"lodged": 30, "granted": 20, "grant_rate": 66.7},
            "Non-Award": {"lodged": 20, "granted": 10, "grant_rate": 50.0},
        },
    },
    "2021-22": {
        "total_lodged": 18_450,
        "total_granted": 13_200,
        "grant_rate": 71.5,
        "note": "Post-COVID recovery — lodgements rebounding but grant rates lower",
        "sector_breakdown": {
            "Higher Education": {"lodged": 6_500, "granted": 5_600, "grant_rate": 86.2},
            "VET": {"lodged": 9_200, "granted": 5_800, "grant_rate": 63.0},
            "ELICOS": {"lodged": 1_200, "granted": 800, "grant_rate": 66.7},
            "Postgrad Research": {"lodged": 300, "granted": 280, "grant_rate": 93.3},
            "Schools": {"lodged": 80, "granted": 50, "grant_rate": 62.5},
            "Non-Award": {"lodged": 40, "granted": 25, "grant_rate": 62.5},
        },
    },
    "2022-23": {
        "total_lodged": 32_500,
        "total_granted": 19_800,
        "grant_rate": 60.9,
        "note": "Record lodgements — DHA imposed stricter scrutiny on Nepal",
        "sector_breakdown": {
            "Higher Education": {"lodged": 10_800, "granted": 8_500, "grant_rate": 78.7},
            "VET": {"lodged": 17_200, "granted": 8_600, "grant_rate": 50.0},
            "ELICOS": {"lodged": 2_100, "granted": 1_200, "grant_rate": 57.1},
            "Postgrad Research": {"lodged": 450, "granted": 420, "grant_rate": 93.3},
            "Schools": {"lodged": 100, "granted": 60, "grant_rate": 60.0},
            "Non-Award": {"lodged": 50, "granted": 30, "grant_rate": 60.0},
        },
    },
    "2023-24": {
        "total_lodged": 28_900,
        "total_granted": 15_200,
        "grant_rate": 52.6,
        "note": "Genuine Student requirement introduced — significant tightening",
        "sector_breakdown": {
            "Higher Education": {"lodged": 11_500, "granted": 8_200, "grant_rate": 71.3},
            "VET": {"lodged": 13_800, "granted": 5_100, "grant_rate": 37.0},
            "ELICOS": {"lodged": 1_600, "granted": 700, "grant_rate": 43.8},
            "Postgrad Research": {"lodged": 500, "granted": 460, "grant_rate": 92.0},
            "Schools": {"lodged": 90, "granted": 50, "grant_rate": 55.6},
            "Non-Award": {"lodged": 60, "granted": 25, "grant_rate": 41.7},
        },
    },
    "2024-25": {
        "total_lodged": 22_100,
        "total_granted": 10_600,
        "grant_rate": 48.0,
        "note": "YTD estimate — GS requirement fully operational, lowest grant rate in decade",
        "sector_breakdown": {
            "Higher Education": {"lodged": 9_800, "granted": 6_600, "grant_rate": 67.3},
            "VET": {"lodged": 9_500, "granted": 2_800, "grant_rate": 29.5},
            "ELICOS": {"lodged": 1_200, "granted": 450, "grant_rate": 37.5},
            "Postgrad Research": {"lodged": 420, "granted": 390, "grant_rate": 92.9},
            "Schools": {"lodged": 70, "granted": 35, "grant_rate": 50.0},
            "Non-Award": {"lodged": 40, "granted": 15, "grant_rate": 37.5},
        },
    },
}

# Global comparison rates
_GLOBAL_GRANT_RATES = {
    "2022-23": 82.1,
    "2023-24": 76.5,
    "2024-25": 72.0,
}


from src.utils.analytics import log_search


def register_tools(mcp: FastMCP):
    """Register all 2 FindUni visa intelligence tools."""

    # ────────────────────────────────────────────────────────────────────
    # 1. predict_visa_success
    # ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    @log_search("predict_visa_success")
    async def predict_visa_success(
        nationality: str,
        age: int,
        education_level: str,
        course_level: str,
        university_type: str = "other",
        ielts_score: float = 6.0,
        has_previous_refusal: bool = False,
        study_gap_years: int = 0,
        financial_coverage_pct: float = 100,
        has_work_experience: bool = False,
        work_experience_years: float = 0,
        has_family_in_australia: bool = False,
        marital_status: str = "single",
        has_dependents: bool = False,
        has_property_in_home_country: bool = False,
    ) -> dict[str, Any]:
        """Predict Australian student visa success probability using weighted scoring.
        Use when student asks about their visa chances, likelihood of approval, or wants a visa assessment.
        Do not use for checking document requirements or financial calculations.

        Uses an advanced scoring algorithm calibrated against Nepal market visa grant rates.
        Based on FindUni.online Visa Chance Predictor — powered by GYCO Consultants.

        Args:
            nationality: e.g. "nepalese", "indian", "bangladeshi".
            age: Student's age.
            education_level: Current education: "high_school", "bachelors", "masters", "phd".
            course_level: Course applying for: "foundation", "diploma", "bachelors", "masters", "phd".
            university_type: One of "go8", "atn", "innovative_research", "regional_university", "private_provider", "tafe", "other".
            ielts_score: Overall IELTS band (e.g. 6.5).
            has_previous_refusal: Any previous Australian visa refusal.
            study_gap_years: Years gap since last formal education.
            financial_coverage_pct: Financial proof as percentage of DHA requirement (100 = exactly meeting, 120 = 20% above).
            has_work_experience: Currently employed or has relevant work experience.
            work_experience_years: Total years of work experience.
            has_family_in_australia: Close family members living in Australia.
            marital_status: "single", "married", "divorced".
            has_dependents: Has children or financial dependents.
            has_property_in_home_country: Family owns property/land in home country.
        """
        try:
            log.info("tool_call", tool="predict_visa_success")

            score = 0.0
            max_score = 100.0
            factors = []

            # ── Factor 1: Course Level & Progression Logic (max 15 pts) ──
            course_scores = {
                "phd": 15, "doctorate": 15,
                "masters": 13,
                "bachelors": 10, "bachelor": 10,
                "diploma": 6,
                "foundation": 5,
            }
            course_pts = course_scores.get(course_level.lower(), 7)

            # Progression logic bonus/penalty
            edu_lower = education_level.lower()
            course_lower = course_level.lower()
            progression_ok = False
            if edu_lower in ("high_school", "secondary", "+2") and course_lower in ("foundation", "diploma", "bachelors"):
                progression_ok = True
            elif edu_lower in ("bachelors", "bachelor") and course_lower in ("masters", "postgraduate"):
                progression_ok = True
            elif edu_lower in ("masters", "postgraduate") and course_lower in ("phd", "doctorate"):
                progression_ok = True
            elif edu_lower == course_lower:
                course_pts -= 3  # Same level = suspicious
            
            if progression_ok:
                course_pts = min(15, course_pts + 2)

            score += course_pts
            factors.append({"factor": "Course Level & Progression", "points": course_pts, "max": 15,
                           "detail": f"{education_level} → {course_level}" + (" ✓ logical progression" if progression_ok else "")})

            # ── Factor 2: University Type (max 12 pts) ──
            uni_info = _UNIVERSITY_TYPES.get(university_type.lower(), _UNIVERSITY_TYPES["other"])
            uni_pts = round(12 * uni_info["weight"])
            uni_pts = min(12, max(0, uni_pts))
            score += uni_pts
            factors.append({"factor": "University Type", "points": uni_pts, "max": 12,
                           "detail": f"{uni_info['label']} (risk: {uni_info['risk']})"})

            # ── Factor 3: IELTS Score (max 12 pts) ──
            if ielts_score >= 7.5:
                ielts_pts = 12
            elif ielts_score >= 7.0:
                ielts_pts = 10
            elif ielts_score >= 6.5:
                ielts_pts = 8
            elif ielts_score >= 6.0:
                ielts_pts = 5
            else:
                ielts_pts = 2
            score += ielts_pts
            factors.append({"factor": "English Proficiency (IELTS)", "points": ielts_pts, "max": 12,
                           "detail": f"IELTS {ielts_score}"})

            # ── Factor 4: Financial Coverage (max 15 pts) ──
            if financial_coverage_pct >= 150:
                fin_pts = 15
            elif financial_coverage_pct >= 120:
                fin_pts = 13
            elif financial_coverage_pct >= 100:
                fin_pts = 10
            elif financial_coverage_pct >= 80:
                fin_pts = 5
            else:
                fin_pts = 2
            score += fin_pts
            factors.append({"factor": "Financial Evidence", "points": fin_pts, "max": 15,
                           "detail": f"{financial_coverage_pct:.0f}% of DHA requirement"})

            # ── Factor 5: Work Experience & Home Ties (max 12 pts) ──
            ties_pts = 0
            ties_detail = []
            if has_work_experience:
                if work_experience_years >= 5:
                    ties_pts += 5
                    ties_detail.append(f"{work_experience_years:.0f}yr work experience")
                elif work_experience_years >= 2:
                    ties_pts += 3
                    ties_detail.append(f"{work_experience_years:.0f}yr work experience")
                else:
                    ties_pts += 1
                    ties_detail.append("Some work experience")

            if has_property_in_home_country:
                ties_pts += 4
                ties_detail.append("Family property in home country")

            if marital_status == "married" and not has_dependents:
                ties_pts += 2
                ties_detail.append("Married without dependents")
            elif marital_status == "married" and has_dependents:
                ties_pts += 1
                ties_detail.append("Married with dependents (complex case)")

            ties_pts = min(12, ties_pts)
            score += ties_pts
            factors.append({"factor": "Home Ties & Work Experience", "points": ties_pts, "max": 12,
                           "detail": ", ".join(ties_detail) if ties_detail else "Limited home ties"})

            # ── Factor 6: Age Appropriateness (max 8 pts) ──
            age_pts = 8
            age_detail = "Age appropriate for course"
            if course_lower in ("bachelors", "bachelor", "foundation", "diploma"):
                if age > 30:
                    age_pts = 3
                    age_detail = "Age may raise questions for undergraduate study"
                elif age > 25:
                    age_pts = 5
                    age_detail = "Slightly above typical age for this level"
            elif course_lower in ("masters", "postgraduate"):
                if age > 40:
                    age_pts = 4
                    age_detail = "Above typical age — strong GTE needed"
                elif age < 21:
                    age_pts = 5
                    age_detail = "Young for postgraduate — ensure strong academic record"
            elif course_lower in ("phd", "doctorate"):
                age_pts = 8  # Any age is fine for PhD

            score += age_pts
            factors.append({"factor": "Age Appropriateness", "points": age_pts, "max": 8,
                           "detail": f"Age {age} — {age_detail}"})

            # ── Factor 7: Study Gap (max 8 pts, can be negative) ──
            if study_gap_years <= 1:
                gap_pts = 8
                gap_detail = "No significant study gap"
            elif study_gap_years <= 3:
                gap_pts = 5
                gap_detail = f"{study_gap_years}yr gap — explain in GTE"
            elif study_gap_years <= 5:
                gap_pts = 2
                gap_detail = f"{study_gap_years}yr gap — must justify clearly in GTE"
            else:
                gap_pts = 0
                gap_detail = f"{study_gap_years}yr gap — significant red flag, requires very strong explanation"

            score += gap_pts
            factors.append({"factor": "Study Gap", "points": gap_pts, "max": 8,
                           "detail": gap_detail})

            # ── Factor 8: Risk Factors (max 18 pts — deductions) ──
            risk_pts = 18
            risk_flags = []

            if has_previous_refusal:
                risk_pts -= 8
                risk_flags.append("Previous visa refusal (-8 pts)")

            nat_lower = nationality.lower().strip()
            high_scrutiny = nat_lower in ("nepal", "nepalese", "bangladesh", "bangladeshi",
                                          "pakistan", "pakistani", "india", "indian",
                                          "nigeria", "nigerian", "sri lanka", "sri lankan")
            if high_scrutiny:
                risk_pts -= 5
                risk_flags.append(f"{nationality} applications receive enhanced scrutiny (-5 pts)")

            if has_family_in_australia:
                risk_pts -= 3
                risk_flags.append("Family in Australia — DHA may question intent to return (-3 pts)")

            if has_dependents and course_lower in ("diploma", "foundation"):
                risk_pts -= 2
                risk_flags.append("Dependents + lower-level course — migration intent signal (-2 pts)")

            risk_pts = max(0, risk_pts)
            score += risk_pts
            factors.append({"factor": "Risk Assessment", "points": risk_pts, "max": 18,
                           "detail": "; ".join(risk_flags) if risk_flags else "No significant risk factors"})

            # ── Final Probability ──
            raw_pct = (score / max_score) * 100

            # Calibrate against Nepal baseline (~48% grant rate in 2024-25)
            if high_scrutiny:
                # Map our 0-100 score to a realistic range (20-85%) for high-scrutiny nationals
                calibrated_pct = 20 + (raw_pct / 100) * 65
            else:
                calibrated_pct = 30 + (raw_pct / 100) * 65

            calibrated_pct = round(min(95, max(10, calibrated_pct)), 1)

            if calibrated_pct >= 75:
                risk_level = "low"
                verdict = "Strong application — good chance of approval with well-prepared documentation."
            elif calibrated_pct >= 55:
                risk_level = "medium"
                verdict = "Moderate application — address identified weaknesses before applying."
            elif calibrated_pct >= 35:
                risk_level = "high"
                verdict = "Challenging application — significant improvements needed. Consider seeking professional help."
            else:
                risk_level = "very_high"
                verdict = "Very difficult — multiple major issues. Strongly recommend consulting a registered migration agent."

            # Improvement tips
            tips = []
            if ielts_pts < 10:
                tips.append(f"Improve IELTS from {ielts_score} to 7.0+ to strengthen your application")
            if fin_pts < 13:
                tips.append("Show financial evidence at least 120% of DHA requirement")
            if ties_pts < 6:
                tips.append("Strengthen home ties — include property documents, employment letters, family ties evidence")
            if gap_pts < 5:
                tips.append("Address study gap clearly in your GTE statement with specific career progression narrative")
            if has_previous_refusal:
                tips.append("Address previous refusal directly in GTE — explain what has changed since then")
            if uni_pts < 10:
                tips.append("Consider applying to a Go8 or ATN university for stronger visa case")
            if not progression_ok:
                tips.append("Consider a course that shows clear academic progression from your current qualification")

            # Get Nepal-specific rates for context
            latest_rate = _NEPAL_VISA_DATA.get("2024-25", {}).get("grant_rate", 48.0)
            global_rate = _GLOBAL_GRANT_RATES.get("2024-25", 72.0)

            return {
                "success_probability": calibrated_pct,
                "risk_level": risk_level,
                "verdict": verdict,
                "raw_score": round(score, 1),
                "max_score": max_score,
                "factor_breakdown": factors,
                "improvement_tips": tips,
                "context": {
                    "nepal_current_grant_rate": f"{latest_rate}%",
                    "global_current_grant_rate": f"{global_rate}%",
                    "your_predicted_vs_national": f"{'Above' if calibrated_pct > latest_rate else 'Below'} Nepal average ({latest_rate}%)",
                },
                "disclaimer": "This prediction is based on statistical analysis and current market trends. "
                              "Actual results depend on individual circumstances and DHA assessment. "
                              "This tool provides an estimate only.",
                "source": "FindUni.online Visa Chance Predictor — powered by GYCO Consultants",
                "data_freshness": datetime.now().isoformat(),
            }
        except Exception as e:
            log.error("tool_error", tool="predict_visa_success", error=str(e))
            return {"error": "Failed to predict visa success.", "error_type": "tool_error"}

    # ────────────────────────────────────────────────────────────────────
    # 2. get_visa_grant_rates
    # ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    @log_search("get_visa_grant_rates")
    async def get_visa_grant_rates(
        sector: str = "all",
        year: Optional[str] = None,
    ) -> dict[str, Any]:
        """Get Australian student visa grant rate statistics for Nepal market.
        Use when student asks about current visa success rates, trends, how many Nepali students get visas, or sector-specific grant rates.
        Do not use for individual visa assessment.

        Shows lodgements, grants, grant rates by year and education sector.
        Based on DHA Student Visa Program Reports — curated by FindUni.online.

        Args:
            sector: Education sector filter. One of: "Higher Education", "VET", "ELICOS", "Postgrad Research", "Schools", "all" (default).
            year: Specific financial year, e.g. "2024-25". Leave empty for all years.
        """
        try:
            log.info("tool_call", tool="get_visa_grant_rates")

            if year and year in _NEPAL_VISA_DATA:
                # Single year
                data = _NEPAL_VISA_DATA[year]
                if sector.lower() != "all" and sector in data.get("sector_breakdown", {}):
                    sector_data = data["sector_breakdown"][sector]
                    return {
                        "year": year,
                        "sector": sector,
                        "lodged": sector_data["lodged"],
                        "granted": sector_data["granted"],
                        "grant_rate": sector_data["grant_rate"],
                        "global_grant_rate": _GLOBAL_GRANT_RATES.get(year),
                        "note": data.get("note"),
                        "source": "DHA Student Visa Program Reports — curated by FindUni.online",
                        "data_freshness": datetime.now().isoformat(),
                    }
                else:
                    result = {
                        "year": year,
                        "total_lodged": data["total_lodged"],
                        "total_granted": data["total_granted"],
                        "grant_rate": data["grant_rate"],
                        "global_grant_rate": _GLOBAL_GRANT_RATES.get(year),
                        "note": data.get("note"),
                        "sector_breakdown": data.get("sector_breakdown", {}),
                        "source": "DHA Student Visa Program Reports — curated by FindUni.online",
                        "data_freshness": datetime.now().isoformat(),
                    }
                    return result

            # All years — trend view
            trend = []
            for yr, data in sorted(_NEPAL_VISA_DATA.items()):
                entry: dict[str, Any] = {
                    "year": yr,
                    "total_lodged": data["total_lodged"],
                    "total_granted": data["total_granted"],
                    "grant_rate": data["grant_rate"],
                    "global_grant_rate": _GLOBAL_GRANT_RATES.get(yr),
                }
                if data.get("note"):
                    entry["note"] = data["note"]

                if sector.lower() != "all" and sector in data.get("sector_breakdown", {}):
                    s = data["sector_breakdown"][sector]
                    entry["sector_lodged"] = s["lodged"]
                    entry["sector_granted"] = s["granted"]
                    entry["sector_grant_rate"] = s["grant_rate"]

                trend.append(entry)

            # Summary stats
            years_sorted = sorted(_NEPAL_VISA_DATA.keys())
            latest_year = years_sorted[-1]
            latest = _NEPAL_VISA_DATA[latest_year]
            first_year = years_sorted[0]
            first = _NEPAL_VISA_DATA[first_year]

            grant_rate_change = latest["grant_rate"] - first["grant_rate"]
            peak_year = max(years_sorted, key=lambda y: _NEPAL_VISA_DATA[y]["grant_rate"])
            peak_rate = _NEPAL_VISA_DATA[peak_year]["grant_rate"]
            low_year = min(years_sorted, key=lambda y: _NEPAL_VISA_DATA[y]["grant_rate"])
            low_rate = _NEPAL_VISA_DATA[low_year]["grant_rate"]

            # Sector ranking for latest year
            sector_ranking = []
            for sec_name, sec_data in sorted(
                latest.get("sector_breakdown", {}).items(),
                key=lambda x: x[1].get("grant_rate", 0),
                reverse=True,
            ):
                sector_ranking.append({
                    "sector": sec_name,
                    "grant_rate": sec_data["grant_rate"],
                    "lodged": sec_data["lodged"],
                    "granted": sec_data["granted"],
                })

            return {
                "country": "Nepal",
                "destination": "Australia",
                "trend_data": trend,
                "summary": {
                    "latest_year": latest_year,
                    "latest_grant_rate": latest["grant_rate"],
                    "latest_lodged": latest["total_lodged"],
                    "latest_granted": latest["total_granted"],
                    "rate_change_since_2019": round(grant_rate_change, 1),
                    "peak": {"year": peak_year, "grant_rate": peak_rate},
                    "lowest": {"year": low_year, "grant_rate": low_rate},
                    "global_comparison": f"Nepal ({latest['grant_rate']}%) vs Global ({_GLOBAL_GRANT_RATES.get(latest_year, 'N/A')}%)",
                },
                "sector_ranking": sector_ranking,
                "key_insights": [
                    f"Nepal's visa grant rate has declined from {first['grant_rate']}% ({first_year}) to {latest['grant_rate']}% ({latest_year})",
                    "Postgrad Research has the highest grant rate (~93%) — PhD students are least affected",
                    "VET (Vocational Education) has seen the sharpest decline — now below 30%",
                    "Higher Education remains relatively stable at ~67% — choose degree programs for better chances",
                    "The Genuine Student (GS) requirement introduced in 2023-24 caused a significant drop",
                    f"Nepal's rate ({latest['grant_rate']}%) is well below the global average ({_GLOBAL_GRANT_RATES.get(latest_year, 72)}%)",
                ],
                "advice": [
                    "Apply for Higher Education or Postgrad Research for best approval chances",
                    "Avoid VET/ELICOS unless your GTE case is extremely strong",
                    "Choose Group of Eight or ATN universities to strengthen your application",
                    "Ensure GS statement is detailed, specific, and addresses DHA concerns directly",
                ],
                "source": "DHA Student Visa Program Reports — curated by FindUni.online",
                "data_freshness": datetime.now().isoformat(),
            }
        except Exception as e:
            log.error("tool_error", tool="get_visa_grant_rates", error=str(e))
            return {"error": "Failed to get visa grant rates.", "error_type": "tool_error"}
