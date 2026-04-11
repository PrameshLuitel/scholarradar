"""
FindUni.online Calculator MCP tools — 3 tools ported from finduni.online:
  1. calculate_education_loan — Financial Capacity Calculator
  2. calculate_nepal_salary_tax — Nepal Salary Tax Calculator (FY 2081/82)
  3. calculate_pr_points — Australian PR Points Calculator (189/190/491)

All calculation logic and data tables embedded directly — no external API calls.
Powered by GYCO Consultants / FindUni.online.
"""
from __future__ import annotations

import math
from datetime import datetime
from typing import Any, Optional

import structlog
from fastmcp import FastMCP

log = structlog.get_logger("mcp_server.tools.finduni_calculators")

# ── Constants ──────────────────────────────────────────────────────────────
AUD_TO_NPR = 106  # Current exchange rate used by FindUni
LIVING_COST_AUD_PER_YEAR = 29_710  # DHA requirement 2025
OSHC_AUD_PER_YEAR = 650  # Approximate
VISA_FEE_AUD = 710  # Subclass 500

# ── Nepal Tax Slabs FY 2081/82 (2024/25) ──────────────────────────────────
# Standard slabs (unmarried individual)
_TAX_SLABS = [
    (500_000, 0.01),     # Up to 5 lakh: 1%
    (200_000, 0.10),     # 5-7 lakh: 10%
    (300_000, 0.20),     # 7-10 lakh: 20%
    (1_000_000, 0.30),   # 10-20 lakh: 30%
    (float("inf"), 0.36),  # Above 20 lakh: 36%
]

# Married individuals get a higher first slab (NPR 6,00,000)
_TAX_SLABS_MARRIED = [
    (600_000, 0.01),
    (200_000, 0.10),
    (300_000, 0.20),
    (1_000_000, 0.30),
    (float("inf"), 0.36),
]

# SSF contribution rates
SSF_EMPLOYEE_PCT = 0.11
SSF_EMPLOYER_PCT = 0.20

# ── PR Points Tables ──────────────────────────────────────────────────────
_AGE_POINTS = [
    # (min_age, max_age, points)
    (18, 24, 25),
    (25, 32, 30),
    (33, 39, 25),
    (40, 44, 15),
    (45, 49, 0),
]

_ENGLISH_POINTS = {
    "superior": 20,      # IELTS 8+, PTE 79+
    "proficient": 10,    # IELTS 7, PTE 65
    "competent": 0,      # IELTS 6, PTE 50
}

_QUALIFICATION_POINTS = {
    "phd": 20,
    "doctorate": 20,
    "masters": 15,
    "bachelors": 15,
    "bachelor": 15,
    "diploma": 10,
    "trade": 10,
    "trade_qualification": 10,
}

_OVERSEAS_WORK_POINTS = [
    # (min_years, max_years, points)
    (0, 2, 0),
    (3, 4, 5),
    (5, 7, 10),
    (8, 99, 15),
]

_AUSTRALIA_WORK_POINTS = [
    (0, 0, 0),
    (1, 2, 5),
    (3, 4, 10),
    (5, 7, 15),
    (8, 99, 20),
]

_PARTNER_POINTS = {
    "skilled_competent_english": 10,  # Partner has competent English + skilled occupation
    "competent_english": 5,           # Partner has competent English only
    "single_or_citizen": 10,          # Single OR partner is AU citizen/PR
    "none": 0,
}


from src.utils.analytics import log_search


def register_tools(mcp: FastMCP):
    """Register all 3 FindUni calculator tools."""

    # ────────────────────────────────────────────────────────────────────
    # 1. calculate_education_loan
    # ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    @log_search("calculate_education_loan")
    async def calculate_education_loan(
        annual_tuition_aud: float,
        course_duration_years: float,
        include_oshc: bool = True,
        include_visa_fee: bool = True,
        include_living_costs: bool = True,
        scholarship_aud_per_year: float = 0,
    ) -> dict[str, Any]:
        """Calculate total funds required for Australian student visa application.
        Use when student asks how much money they need, loan amount, or financial capacity for visa.
        Do not use for monthly budget or cost of living comparison.

        Calculates total AUD needed, converts to NPR, and rounds to nearest lakh.
        Based on FindUni.online Financial Capacity Calculator — powered by GYCO Consultants.

        Args:
            annual_tuition_aud: Annual tuition fee in AUD, e.g. 35000.
            course_duration_years: Course duration in years, e.g. 2.0.
            include_oshc: Include Overseas Student Health Cover (default True).
            include_visa_fee: Include visa application fee (default True).
            include_living_costs: Include DHA mandated living costs — AUD 29,710/yr (default True).
            scholarship_aud_per_year: Annual scholarship amount to deduct from tuition, e.g. 5000.
        """
        try:
            log.info("tool_call", tool="calculate_education_loan")

            years = course_duration_years
            net_tuition_per_year = max(0, annual_tuition_aud - scholarship_aud_per_year)
            total_tuition = net_tuition_per_year * years

            total_living = LIVING_COST_AUD_PER_YEAR * years if include_living_costs else 0
            total_oshc = OSHC_AUD_PER_YEAR * years if include_oshc else 0
            visa_fee = VISA_FEE_AUD if include_visa_fee else 0

            grand_total_aud = total_tuition + total_living + total_oshc + visa_fee
            grand_total_npr = grand_total_aud * AUD_TO_NPR

            # Round to upper lakh (as FindUni does)
            required_savings_npr = math.ceil(grand_total_npr / 100_000) * 100_000

            first_year_aud = net_tuition_per_year + (LIVING_COST_AUD_PER_YEAR if include_living_costs else 0) + (OSHC_AUD_PER_YEAR if include_oshc else 0) + visa_fee
            first_year_npr = first_year_aud * AUD_TO_NPR

            return {
                "breakdown": {
                    "tuition_per_year_aud": round(net_tuition_per_year, 2),
                    "tuition_total_aud": round(total_tuition, 2),
                    "living_costs_total_aud": round(total_living, 2),
                    "living_costs_per_year_aud": LIVING_COST_AUD_PER_YEAR if include_living_costs else 0,
                    "oshc_total_aud": round(total_oshc, 2),
                    "visa_fee_aud": visa_fee,
                    "scholarship_deducted_per_year": scholarship_aud_per_year,
                },
                "grand_total_aud": round(grand_total_aud, 2),
                "grand_total_npr": round(grand_total_npr, 2),
                "required_savings_npr": required_savings_npr,
                "required_savings_display": f"NPR {required_savings_npr:,.0f}",
                "first_year_proof_aud": round(first_year_aud, 2),
                "first_year_proof_npr": round(first_year_npr, 2),
                "exchange_rate": f"1 AUD = {AUD_TO_NPR} NPR",
                "course_duration_years": years,
                "advice": [
                    f"Total funds required: AUD {grand_total_aud:,.0f} (NPR {required_savings_npr:,.0f})",
                    f"For visa application, show at least AUD {first_year_aud:,.0f} for the first year",
                    "Bank statements should show funds held for at least 3-6 months",
                    "Education loan sanction letters from recognized Nepali banks are accepted",
                    "Include FD (Fixed Deposit) certificates as supporting evidence",
                ],
                "banking_partners": [
                    {"bank": "Nabil Bank", "branch": "Maligaun Branch", "contact": "Utsab Shrestha", "phone": "9841339931"},
                    {"bank": "Kumari Bank Limited", "branch": "Kirtipur Branch", "contact": "Bikesh Shrestha", "phone": "9852044433"},
                ],
                "source": "FindUni.online Financial Capacity Calculator — powered by GYCO Consultants",
                "data_freshness": datetime.now().isoformat(),
            }
        except Exception as e:
            log.error("tool_error", tool="calculate_education_loan", error=str(e))
            return {"error": "Failed to calculate education loan.", "error_type": "tool_error"}

    # ────────────────────────────────────────────────────────────────────
    # 2. calculate_nepal_salary_tax
    # ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    @log_search("calculate_nepal_salary_tax")
    async def calculate_nepal_salary_tax(
        annual_salary_npr: float,
        is_married: bool = False,
        is_female: bool = False,
        include_ssf: bool = False,
    ) -> dict[str, Any]:
        """Calculate Nepal income tax on salary for FY 2081/82 (2024/25).
        Use when student or their sponsor asks about Nepal tax calculation, take-home salary, or tax slabs.
        Do not use for Australian or other country tax calculations.

        Calculates slab-wise breakdown, total annual and monthly tax, effective rate.
        Based on FindUni.online Salary Tax Calculator — Nepal Fiscal Year 2081/82.

        Args:
            annual_salary_npr: Annual salary in Nepali Rupees (NPR), e.g. 1200000.
            is_married: Whether the taxpayer is married (higher first slab threshold).
            is_female: Whether the taxpayer is female (10% discount on tax).
            include_ssf: Whether to deduct SSF contribution before tax calculation.
        """
        try:
            log.info("tool_call", tool="calculate_nepal_salary_tax")

            gross_annual = annual_salary_npr
            taxable_income = gross_annual

            ssf_employee = 0
            ssf_employer = 0
            if include_ssf:
                ssf_employee = gross_annual * SSF_EMPLOYEE_PCT
                ssf_employer = gross_annual * SSF_EMPLOYER_PCT
                taxable_income = gross_annual - ssf_employee

            slabs = _TAX_SLABS_MARRIED if is_married else _TAX_SLABS
            remaining = taxable_income
            total_tax = 0.0
            slab_breakdown = []

            slab_names = ["First Slab", "Second Slab", "Third Slab", "Fourth Slab", "Fifth Slab"]
            cumulative_income = 0

            for i, (slab_amount, rate) in enumerate(slabs):
                if remaining <= 0:
                    break
                taxable_in_slab = min(remaining, slab_amount)
                tax_in_slab = taxable_in_slab * rate

                slab_start = cumulative_income
                slab_end = cumulative_income + taxable_in_slab

                slab_breakdown.append({
                    "slab": slab_names[i] if i < len(slab_names) else f"Slab {i+1}",
                    "range": f"NPR {slab_start:,.0f} – {slab_end:,.0f}" if slab_amount != float("inf") else f"NPR {slab_start:,.0f}+",
                    "rate": f"{rate*100:.0f}%",
                    "taxable_amount": round(taxable_in_slab, 2),
                    "tax": round(tax_in_slab, 2),
                })

                total_tax += tax_in_slab
                remaining -= taxable_in_slab
                cumulative_income += taxable_in_slab

            # Female 10% discount
            female_discount = 0
            if is_female and total_tax > 0:
                female_discount = total_tax * 0.10
                total_tax -= female_discount

            monthly_tax = total_tax / 12
            monthly_salary = gross_annual / 12
            effective_rate = (total_tax / gross_annual * 100) if gross_annual > 0 else 0

            return {
                "fiscal_year": "2081/82 (2024/25)",
                "gross_annual_salary": round(gross_annual, 2),
                "gross_monthly_salary": round(monthly_salary, 2),
                "taxable_income": round(taxable_income, 2),
                "slab_breakdown": slab_breakdown,
                "female_discount": round(female_discount, 2) if is_female else None,
                "total_annual_tax": round(total_tax, 2),
                "total_monthly_tax": round(monthly_tax, 2),
                "effective_tax_rate": f"{effective_rate:.1f}%",
                "net_annual_income": round(gross_annual - total_tax - ssf_employee, 2),
                "net_monthly_income": round((gross_annual - total_tax - ssf_employee) / 12, 2),
                "ssf_details": {
                    "employee_contribution": round(ssf_employee, 2),
                    "employer_contribution": round(ssf_employer, 2),
                    "total_ssf": round(ssf_employee + ssf_employer, 2),
                } if include_ssf else None,
                "is_married": is_married,
                "is_female": is_female,
                "source": "FindUni.online Salary Tax Calculator — Nepal FY 2081/82",
                "data_freshness": datetime.now().isoformat(),
            }
        except Exception as e:
            log.error("tool_error", tool="calculate_nepal_salary_tax", error=str(e))
            return {"error": "Failed to calculate Nepal salary tax.", "error_type": "tool_error"}

    # ────────────────────────────────────────────────────────────────────
    # 3. calculate_pr_points
    # ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    @log_search("calculate_pr_points")
    async def calculate_pr_points(
        age: int,
        english_level: str,
        highest_qualification: str,
        overseas_work_years: int = 0,
        australia_work_years: int = 0,
        partner_skills: str = "none",
        visa_subclass: str = "189",
        has_naati: bool = False,
        has_professional_year: bool = False,
        has_stem_qualification: bool = False,
        study_in_regional: bool = False,
    ) -> dict[str, Any]:
        """Calculate Australian PR (Permanent Residency) points for skilled migration.
        Use when student or graduate asks about PR eligibility, points test, or skilled migration prospects.
        Do not use for student visa assessment.

        Calculates points for visa subclasses 189, 190, and 491 based on DHA points table.
        Based on FindUni.online PR Points Calculator — powered by GYCO Consultants.

        Args:
            age: Applicant's age (18-49).
            english_level: One of "superior" (IELTS 8+), "proficient" (IELTS 7), "competent" (IELTS 6).
            highest_qualification: One of "phd", "masters", "bachelors", "diploma", "trade".
            overseas_work_years: Years of skilled work experience outside Australia (0-20).
            australia_work_years: Years of skilled work experience in Australia (0-20).
            partner_skills: One of "skilled_competent_english", "competent_english", "single_or_citizen", "none".
            visa_subclass: One of "189", "190", "491". Affects nomination points.
            has_naati: Has NAATI community language credential (5 points).
            has_professional_year: Completed professional year in Australia (5 points).
            has_stem_qualification: Has STEM qualification from Australian institution (10 points).
            study_in_regional: Studied in regional Australia (5 points).
        """
        try:
            log.info("tool_call", tool="calculate_pr_points")

            points_breakdown = []
            total_points = 0

            # Age points
            age_points = 0
            for min_age, max_age, pts in _AGE_POINTS:
                if min_age <= age <= max_age:
                    age_points = pts
                    break
            points_breakdown.append({"category": "Age", "value": f"{age} years", "points": age_points})
            total_points += age_points

            # English points
            eng_lower = english_level.lower().strip()
            eng_points = _ENGLISH_POINTS.get(eng_lower, 0)
            eng_labels = {"superior": "IELTS 8+ / PTE 79+", "proficient": "IELTS 7 / PTE 65", "competent": "IELTS 6 / PTE 50"}
            points_breakdown.append({"category": "English Language", "value": eng_labels.get(eng_lower, english_level), "points": eng_points})
            total_points += eng_points

            # Qualification points
            qual_lower = highest_qualification.lower().strip()
            qual_points = _QUALIFICATION_POINTS.get(qual_lower, 0)
            points_breakdown.append({"category": "Qualification", "value": highest_qualification.title(), "points": qual_points})
            total_points += qual_points

            # Overseas work experience
            overseas_pts = 0
            for min_y, max_y, pts in _OVERSEAS_WORK_POINTS:
                if min_y <= overseas_work_years <= max_y:
                    overseas_pts = pts
                    break
            points_breakdown.append({"category": "Overseas Work Experience", "value": f"{overseas_work_years} years", "points": overseas_pts})
            total_points += overseas_pts

            # Australian work experience
            aus_pts = 0
            for min_y, max_y, pts in _AUSTRALIA_WORK_POINTS:
                if min_y <= australia_work_years <= max_y:
                    aus_pts = pts
                    break
            points_breakdown.append({"category": "Australian Work Experience", "value": f"{australia_work_years} years", "points": aus_pts})
            total_points += aus_pts

            # Partner skills
            partner_lower = partner_skills.lower().strip()
            partner_pts = _PARTNER_POINTS.get(partner_lower, 0)
            partner_labels = {
                "skilled_competent_english": "Partner has skilled occupation + competent English",
                "competent_english": "Partner has competent English",
                "single_or_citizen": "Single or partner is AU citizen/PR",
                "none": "Partner does not meet criteria",
            }
            points_breakdown.append({"category": "Partner Skills", "value": partner_labels.get(partner_lower, partner_skills), "points": partner_pts})
            total_points += partner_pts

            # Nomination / Sponsorship points
            nom_pts = 0
            if visa_subclass == "190":
                nom_pts = 5
            elif visa_subclass == "491":
                nom_pts = 15
            if nom_pts > 0:
                points_breakdown.append({"category": f"State Nomination ({visa_subclass})", "value": f"Subclass {visa_subclass}", "points": nom_pts})
                total_points += nom_pts

            # Bonus points
            if has_naati:
                points_breakdown.append({"category": "NAATI Community Language", "value": "Yes", "points": 5})
                total_points += 5
            if has_professional_year:
                points_breakdown.append({"category": "Professional Year", "value": "Completed", "points": 5})
                total_points += 5
            if has_stem_qualification:
                points_breakdown.append({"category": "STEM Qualification (AU)", "value": "Yes", "points": 10})
                total_points += 10
            if study_in_regional:
                points_breakdown.append({"category": "Regional Study", "value": "Yes", "points": 5})
                total_points += 5

            # Assessment
            pass_mark = 65
            meets_threshold = total_points >= pass_mark

            if total_points >= 90:
                assessment = "Excellent — very competitive score. Expect quick invitation."
                likelihood = "very_high"
            elif total_points >= 80:
                assessment = "Strong — competitive score. Good chance of invitation within a few months."
                likelihood = "high"
            elif total_points >= 70:
                assessment = "Good — meets threshold comfortably. Invitation likely but may take time depending on occupation."
                likelihood = "moderate"
            elif total_points >= 65:
                assessment = "Meets minimum — eligible but invitation timing depends heavily on occupation demand."
                likelihood = "low_to_moderate"
            else:
                shortfall = pass_mark - total_points
                assessment = f"Below threshold by {shortfall} points. Consider improving English, gaining more work experience, or applying for 491 (regional) visa."
                likelihood = "not_eligible"

            # Improvement suggestions
            improvements = []
            if eng_lower == "competent":
                improvements.append(f"Improve English to Proficient (+10 pts) or Superior (+20 pts)")
            elif eng_lower == "proficient":
                improvements.append(f"Improve English to Superior (+10 pts)")
            if not has_professional_year:
                improvements.append("Complete Professional Year in Australia (+5 pts)")
            if not has_naati:
                improvements.append("Get NAATI community language credential (+5 pts)")
            if visa_subclass == "189" and total_points < 80:
                improvements.append("Consider 190 (state nomination, +5 pts) or 491 (regional, +15 pts)")
            if overseas_work_years < 3 and overseas_work_years > 0:
                improvements.append(f"Gain {3 - overseas_work_years} more years overseas work experience for +5 pts")

            return {
                "visa_subclass": visa_subclass,
                "total_points": total_points,
                "pass_mark": pass_mark,
                "meets_threshold": meets_threshold,
                "assessment": assessment,
                "likelihood": likelihood,
                "points_breakdown": points_breakdown,
                "improvement_suggestions": improvements if not meets_threshold or total_points < 80 else [],
                "comparison": {
                    "points_for_189": total_points - nom_pts,
                    "points_for_190": total_points - nom_pts + 5,
                    "points_for_491": total_points - nom_pts + 15,
                },
                "migration_agent": {
                    "name": "Wilson Sharma",
                    "marn": "1793491",
                    "note": "Registered Migration Agent — contact for professional assessment",
                },
                "source": "FindUni.online PR Points Calculator — powered by GYCO Consultants",
                "data_freshness": datetime.now().isoformat(),
            }
        except Exception as e:
            log.error("tool_error", tool="calculate_pr_points", error=str(e))
            return {"error": "Failed to calculate PR points.", "error_type": "tool_error"}
