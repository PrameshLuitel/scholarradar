"""
Course MCP tools — 5 production-quality tools for searching, comparing,
matching, and analyzing course data from the ScholarRadar database.

Each tool returns structured data with source URLs and data freshness timestamps.
"""

from __future__ import annotations

import re
from datetime import datetime
from difflib import SequenceMatcher
from typing import Any, Optional

import structlog
from fastmcp import FastMCP

log = structlog.get_logger("mcp_server.tools.courses")

# ── Helpers ─────────────────────────────────────────────────────────────────


def _get_db():
    from src.database.client import get_db
    return get_db()


def _fuzzy_score(query: Optional[str], text: Optional[str]) -> float:
    if not query or not text:
        return 0.0
    q, t = query.lower(), text.lower()
    if q in t:
        return 0.95
    tokens_q = set(re.split(r"\W+", q))
    tokens_t = set(re.split(r"\W+", t))
    if tokens_q and tokens_t:
        overlap = len(tokens_q & tokens_t) / len(tokens_q)
        if overlap > 0:
            return 0.5 + overlap * 0.4
    return SequenceMatcher(None, q, t).ratio()


def _fetch_active_courses(
    country: Optional[str] = None,
    level: Optional[str] = None,
    university: Optional[str] = None,
) -> list[dict[str, Any]]:
    db = _get_db()
    query = db.table("courses").select("*").eq("is_active", True)
    if country:
        query = query.ilike("country", country.strip())
    if level:
        query = query.ilike("level", level.strip())
    if university:
        query = query.ilike("university", f"%{university.strip()}%")
    response = query.execute()
    return response.data or []


def _course_summary(c: dict[str, Any]) -> dict[str, Any]:
    fee_display = None
    if c.get("tuition_fee"):
        currency = c.get("currency", "AUD")
        fee_display = f"{currency} {c['tuition_fee']:,.0f}/year"

    duration_display = None
    if c.get("duration_months"):
        months = c["duration_months"]
        if months >= 12:
            years = months / 12
            duration_display = f"{years:.1f} years" if years != int(years) else f"{int(years)} years"
        else:
            duration_display = f"{months} months"

    ielts_display = None
    if c.get("ielts_overall"):
        ielts_display = f"{c['ielts_overall']}"

    return {
        "id": c.get("id"),
        "name": c.get("name"),
        "university": c.get("university"),
        "country": c.get("country"),
        "city": c.get("city"),
        "level": c.get("level"),
        "subject": c.get("subject"),
        "subject_category": c.get("subject_category"),
        "tuition_fee": c.get("tuition_fee"),
        "tuition_display": fee_display,
        "currency": c.get("currency"),
        "duration_months": c.get("duration_months"),
        "duration_display": duration_display,
        "ielts_overall": c.get("ielts_overall"),
        "ielts_display": ielts_display,
        "ielts_reading": c.get("ielts_reading"),
        "ielts_writing": c.get("ielts_writing"),
        "ielts_speaking": c.get("ielts_speaking"),
        "ielts_listening": c.get("ielts_listening"),
        "gpa_requirement": c.get("gpa_requirement"),
        "entry_qualification": c.get("entry_qualification"),
        "start_dates": c.get("start_dates"),
        "apply_url": c.get("apply_url"),
        "source_url": c.get("source_url"),
        "last_verified": str(c["last_verified"]) if c.get("last_verified") else None,
        "data_freshness": str(c["updated_at"]) if c.get("updated_at") else None,
    }


def _empty_result(message: str) -> dict[str, Any]:
    return {"results": [], "total_count": 0, "message": message}


# ── Tool Registration ──────────────────────────────────────────────────────


def register_tools(mcp: FastMCP):
    """Register all 5 course tools with the MCP server."""

    # ────────────────────────────────────────────────────────────────────
    # 1. search_courses
    # ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    async def search_courses(
        subject: str,
        destination_country: str,
        study_level: str,
        max_tuition_aud: Optional[float] = None,
        max_duration_months: Optional[int] = None,
        min_ielts: Optional[float] = None,
    ) -> dict[str, Any]:
        """Search for courses by subject, country, and study level with optional filters.

        Returns the top 20 matching courses ranked by subject relevance,
        with full details including fees, duration, IELTS requirements, and entry criteria.

        Args:
            subject: Subject to search for (fuzzy match), e.g. "computer science", "nursing".
            destination_country: Country where the course is offered, e.g. "australia", "uk".
            study_level: One of: foundation, undergraduate, postgraduate, doctorate, vocational.
            max_tuition_aud: Maximum annual tuition fee in local currency. Only returns courses under this.
            max_duration_months: Maximum course duration in months. E.g. 24 for 2-year programs.
            min_ielts: Minimum IELTS score the student has. Returns courses they qualify for.
        """
        try:
            log.info("tool_call", tool="search_courses", parameters={
                "subject": subject, "destination_country": destination_country,
                "study_level": study_level, "max_tuition_aud": max_tuition_aud,
                "max_duration_months": max_duration_months, "min_ielts": min_ielts,
            })

            rows = _fetch_active_courses(country=destination_country, level=study_level)

            if not rows:
                return _empty_result(
                    f"No active courses found in {destination_country} for {study_level}. "
                    "Try broadening your filters."
                )

            scored: list[tuple[float, dict[str, Any]]] = []
            for c in rows:
                # Filter: tuition
                if max_tuition_aud is not None and c.get("tuition_fee"):
                    if c["tuition_fee"] > max_tuition_aud:
                        continue

                # Filter: duration
                if max_duration_months is not None and c.get("duration_months"):
                    if c["duration_months"] > max_duration_months:
                        continue

                # Filter: IELTS
                if min_ielts is not None and c.get("ielts_overall"):
                    if c["ielts_overall"] > min_ielts:
                        continue  # student doesn't meet requirement

                # Score: subject relevance
                relevance = max(
                    _fuzzy_score(subject, c.get("name") or ""),
                    _fuzzy_score(subject, c.get("subject") or ""),
                    _fuzzy_score(subject, c.get("subject_category") or ""),
                )
                if relevance < 0.2:
                    continue

                scored.append((round(float(relevance), 3), c))

            scored.sort(key=lambda x: x[0], reverse=True)
            top_20 = list(scored[:20])

            results = []
            for relevance, c in top_20:
                item = _course_summary(c)
                item["relevance_score"] = relevance
                results.append(item)

            log.info("tool_result", tool="search_courses", result_count=len(results))
            return {
                "results": results,
                "total_count": len(scored),
                "showing": len(results),
                "filters_applied": {
                    "subject": subject,
                    "destination_country": destination_country,
                    "study_level": study_level,
                    "max_tuition_aud": max_tuition_aud,
                    "max_duration_months": max_duration_months,
                    "min_ielts": min_ielts,
                },
            }

        except Exception as e:
            log.error("tool_error", tool="search_courses", error=str(e))
            return {"error": "Failed to search courses. Please try again.", "error_type": "tool_error"}

    # ────────────────────────────────────────────────────────────────────
    # 2. compare_courses
    # ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    async def compare_courses(
        course1_name: str,
        university1: str,
        course2_name: str,
        university2: str,
    ) -> dict[str, Any]:
        """Compare two specific courses side by side.

        Returns a structured comparison of fees, duration, IELTS requirements,
        entry qualifications, location, and start dates.

        Args:
            course1_name: Name or partial name of the first course, e.g. "Master of Data Science".
            university1: University offering the first course, e.g. "University of Melbourne".
            course2_name: Name or partial name of the second course, e.g. "MSc Computer Science".
            university2: University offering the second course, e.g. "University of Sydney".
        """
        try:
            log.info("tool_call", tool="compare_courses", parameters={
                "course1_name": course1_name, "university1": university1,
                "course2_name": course2_name, "university2": university2,
            })

            def _find_best_match(name: str, university: str) -> Optional[dict]:
                rows = _fetch_active_courses(university=university)
                if not rows:
                    return None
                best_score, best = 0.0, None
                for c in rows:
                    score = _fuzzy_score(name, c.get("name") or "")
                    if score > best_score:
                        best_score, best = score, c
                return best

            c1 = _find_best_match(course1_name, university1)
            c2 = _find_best_match(course2_name, university2)

            if not c1 and not c2:
                return _empty_result(
                    f"Could not find either course. Check the course names and universities."
                )
            if not c1:
                return _empty_result(f"Could not find '{course1_name}' at '{university1}'.")
            if not c2:
                return _empty_result(f"Could not find '{course2_name}' at '{university2}'.")

            s1, s2 = _course_summary(c1), _course_summary(c2)

            # Build comparison dimensions
            comparison = {
                "course_1": s1,
                "course_2": s2,
                "comparison_dimensions": {
                    "tuition_fee": {
                        "course_1": s1.get("tuition_display"),
                        "course_2": s2.get("tuition_display"),
                        "cheaper": s1["name"] if (c1.get("tuition_fee") or float("inf")) < (c2.get("tuition_fee") or float("inf")) else s2["name"],
                    },
                    "duration": {
                        "course_1": s1.get("duration_display"),
                        "course_2": s2.get("duration_display"),
                        "shorter": s1["name"] if (float(c1.get("duration_months") or 999)) < (float(c2.get("duration_months") or 999)) else s2["name"],
                    },
                    "ielts_requirement": {
                        "course_1": s1.get("ielts_overall"),
                        "course_2": s2.get("ielts_overall"),
                        "lower_requirement": s1["name"] if (c1.get("ielts_overall") or 99) < (c2.get("ielts_overall") or 99) else s2["name"],
                    },
                    "entry_qualification": {
                        "course_1": s1.get("entry_qualification"),
                        "course_2": s2.get("entry_qualification"),
                    },
                    "location": {
                        "course_1": f"{s1.get('city', 'N/A')}, {s1.get('country', 'N/A')}",
                        "course_2": f"{s2.get('city', 'N/A')}, {s2.get('country', 'N/A')}",
                    },
                    "start_dates": {
                        "course_1": s1.get("start_dates"),
                        "course_2": s2.get("start_dates"),
                    },
                },
            }

            log.info("tool_result", tool="compare_courses")
            return comparison

        except Exception as e:
            log.error("tool_error", tool="compare_courses", error=str(e))
            return {"error": "Failed to compare courses.", "error_type": "tool_error"}

    # ────────────────────────────────────────────────────────────────────
    # 3. find_courses_for_profile
    # ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    async def find_courses_for_profile(
        current_qualification: str,
        target_subject: str,
        ielts_score: float,
        budget_aud_per_year: float,
        destination_country: Optional[str] = None,
    ) -> dict[str, Any]:
        """Find courses a student can actually get into based on their profile.

        Checks IELTS requirements and tuition budget, then returns qualifying
        courses plus a gap analysis showing what the student needs to improve
        to unlock more options.

        Args:
            current_qualification: Student's current degree, e.g. "bachelors in IT".
            target_subject: Subject they want to study, e.g. "data science".
            ielts_score: Student's overall IELTS band score (e.g. 6.5).
            budget_aud_per_year: Maximum annual tuition budget in local currency.
            destination_country: Optional country filter, e.g. "australia".
        """
        try:
            log.info("tool_call", tool="find_courses_for_profile", parameters={
                "current_qualification": current_qualification,
                "target_subject": target_subject,
                "ielts_score": ielts_score,
                "budget_aud_per_year": budget_aud_per_year,
                "destination_country": destination_country,
            })

            # Infer study level
            qual_lower = current_qualification.lower()
            inferred_level = None
            if any(k in qual_lower for k in ("high school", "secondary", "+2", "12th", "a-level")):
                inferred_level = "undergraduate"
            elif any(k in qual_lower for k in ("bachelor", "bsc", "ba ", "beng", "undergraduate")):
                inferred_level = "postgraduate"
            elif any(k in qual_lower for k in ("master", "msc", "ma ", "mba")):
                inferred_level = "doctorate"

            rows = _fetch_active_courses(country=destination_country, level=inferred_level)

            if not rows:
                return _empty_result(
                    f"No courses found"
                    + (f" in {destination_country}" if destination_country else "")
                    + (f" for {inferred_level}" if inferred_level else "")
                    + ". Try broadening your search."
                )

            qualifying: list[dict[str, Any]] = []
            near_miss: list[dict[str, Any]] = []
            ielts_too_low_count = 0
            budget_too_low_count = 0
            min_ielts_needed_for_more = None

            for c in rows:
                # Subject relevance
                relevance = max(
                    _fuzzy_score(target_subject, c.get("name") or ""),
                    _fuzzy_score(target_subject, c.get("subject") or ""),
                    _fuzzy_score(target_subject, c.get("subject_category") or ""),
                )
                if relevance < 0.25:
                    continue

                meets_ielts = True
                meets_budget = True
                gaps = []

                # Check IELTS
                if c.get("ielts_overall") and c["ielts_overall"] > ielts_score:
                    meets_ielts = False
                    gap = float(c["ielts_overall"]) - ielts_score
                    gaps.append(f"IELTS: need {c['ielts_overall']}, you have {ielts_score} (gap: {gap:.1f})")
                    ielts_too_low_count += 1
                    if min_ielts_needed_for_more is None or c["ielts_overall"] < min_ielts_needed_for_more:
                        min_ielts_needed_for_more = c["ielts_overall"]

                # Check budget
                if c.get("tuition_fee") and c["tuition_fee"] > budget_aud_per_year:
                    meets_budget = False
                    excess = c["tuition_fee"] - budget_aud_per_year
                    currency = c.get("currency", "AUD")
                    gaps.append(f"Budget: costs {currency} {c['tuition_fee']:,.0f}, over budget by {currency} {excess:,.0f}")
                    budget_too_low_count += 1

                summary = _course_summary(c)
                summary["relevance_score"] = round(float(relevance), 3)

                if meets_ielts and meets_budget:
                    qualifying.append(summary)
                elif gaps:
                    summary["gaps"] = gaps
                    near_miss.append(summary)

            qualifying.sort(key=lambda x: x.get("relevance_score", 0), reverse=True)
            near_miss.sort(key=lambda x: len(x.get("gaps", [])))

            # Gap analysis
            gap_analysis = {
                "total_relevant_courses": len(qualifying) + len(near_miss),
                "courses_you_qualify_for": len(qualifying),
                "courses_blocked": len(near_miss),
                "blocked_by_ielts": ielts_too_low_count,
                "blocked_by_budget": budget_too_low_count,
                "recommendations": [],
            }
            if min_ielts_needed_for_more and min_ielts_needed_for_more > ielts_score:
                gap_analysis["recommendations"].append(
                    f"Improving IELTS to {min_ielts_needed_for_more} would unlock more courses."
                )
            if budget_too_low_count > 0:
                gap_analysis["recommendations"].append(
                    "Consider applying for scholarships to offset tuition costs."
                )

            log.info("tool_result", tool="find_courses_for_profile",
                     qualifying=len(qualifying), near_miss=len(near_miss))
            return {
                "qualifying_courses": list(qualifying[:20]),
                "near_miss_courses": list(near_miss[:10]),
                "gap_analysis": gap_analysis,
                "student_profile": {
                    "current_qualification": current_qualification,
                    "inferred_level": inferred_level,
                    "target_subject": target_subject,
                    "ielts_score": ielts_score,
                    "budget_aud_per_year": budget_aud_per_year,
                    "destination_country": destination_country,
                },
            }

        except Exception as e:
            log.error("tool_error", tool="find_courses_for_profile", error=str(e))
            return {"error": "Failed to find courses for profile.", "error_type": "tool_error"}

    # ────────────────────────────────────────────────────────────────────
    # 4. get_pathway_options
    # ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    async def get_pathway_options(
        current_qualification: str,
        target_degree: str,
        target_university: str,
    ) -> dict[str, Any]:
        """Find foundation and pathway courses that lead to a target degree program.

        Useful for students who don't yet meet direct entry requirements.
        Searches for foundation, diploma, and pathway programs at or associated
        with the target university.

        Args:
            current_qualification: What the student currently holds, e.g. "high school diploma".
            target_degree: The degree they ultimately want, e.g. "Bachelor of Engineering".
            target_university: University they want to attend, e.g. "University of Sydney".
        """
        try:
            log.info("tool_call", tool="get_pathway_options", parameters={
                "current_qualification": current_qualification,
                "target_degree": target_degree,
                "target_university": target_university,
            })

            # Search for foundation/pathway courses at the target university
            all_courses = _fetch_active_courses(university=target_university)

            pathway_courses = []
            degree_courses = []

            for c in all_courses:
                level = (c.get("level") or "").lower()
                name = (c.get("name") or "").lower()

                is_pathway = any(k in level or k in name for k in
                                ("foundation", "pathway", "diploma", "preparatory", "bridging"))

                if is_pathway:
                    summary = _course_summary(c)
                    # Check subject relevance to target degree
                    relevance = _fuzzy_score(target_degree, c.get("name") or "")
                    summary["pathway_relevance"] = round(float(relevance), 3)
                    pathway_courses.append(summary)
                else:
                    # Check if this is the target degree
                    relevance = _fuzzy_score(target_degree, c.get("name") or "")
                    if relevance > 0.4:
                        degree_courses.append(_course_summary(c))

            pathway_courses.sort(key=lambda x: x.get("pathway_relevance", 0), reverse=True)

            if not pathway_courses and not degree_courses:
                return _empty_result(
                    f"No pathway or matching degree courses found at '{target_university}'. "
                    "Try the university's full name or check a different institution."
                )

            log.info("tool_result", tool="get_pathway_options",
                     pathways=len(pathway_courses), degrees=len(degree_courses))
            return {
                "pathway_courses": pathway_courses,
                "target_degree_matches": degree_courses[:5],
                "total_pathways": len(pathway_courses),
                "student_context": {
                    "current_qualification": current_qualification,
                    "target_degree": target_degree,
                    "target_university": target_university,
                },
                "advice": (
                    "Foundation/pathway programs typically last 6–12 months and guarantee "
                    "progression to the target degree if you meet the required grades."
                    if pathway_courses else
                    "No specific pathway courses found. Contact the university's "
                    "international admissions office for alternative entry options."
                ),
            }

        except Exception as e:
            log.error("tool_error", tool="get_pathway_options", error=str(e))
            return {"error": "Failed to find pathway options.", "error_type": "tool_error"}

    # ────────────────────────────────────────────────────────────────────
    # 5. get_courses_by_ielts
    # ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    async def get_courses_by_ielts(
        ielts_score: float,
        destination_country: str,
        study_level: str,
    ) -> dict[str, Any]:
        """Find all courses where the student's IELTS score meets the requirement.

        Returns courses grouped by whether the student comfortably meets,
        exactly meets, or is close to meeting the IELTS requirement.

        Args:
            ielts_score: Student's overall IELTS band score (e.g. 6.5).
            destination_country: Country to search in, e.g. "australia".
            study_level: One of: foundation, undergraduate, postgraduate, doctorate.
        """
        try:
            log.info("tool_call", tool="get_courses_by_ielts", parameters={
                "ielts_score": ielts_score, "destination_country": destination_country,
                "study_level": study_level,
            })

            rows = _fetch_active_courses(country=destination_country, level=study_level)

            if not rows:
                return _empty_result(
                    f"No courses found in {destination_country} for {study_level}."
                )

            comfortably_meets = []  # score >= requirement + 0.5
            exactly_meets = []     # score >= requirement and < requirement + 0.5
            close_gap = []         # score < requirement but within 0.5

            for c in rows:
                req = c.get("ielts_overall")
                summary = _course_summary(c)

                if req is None:
                    # No IELTS requirement listed — include as qualifying
                    summary["ielts_status"] = "no_requirement_listed"
                    comfortably_meets.append(summary)
                elif ielts_score >= req + 0.5:
                    summary["ielts_status"] = "comfortably_meets"
                    summary["margin"] = round(float(ielts_score - req), 1)
                    comfortably_meets.append(summary)
                elif ielts_score >= req:
                    summary["ielts_status"] = "exactly_meets"
                    summary["margin"] = round(float(ielts_score - req), 1)
                    exactly_meets.append(summary)
                elif ielts_score >= req - 0.5:
                    summary["ielts_status"] = "close_gap"
                    summary["gap"] = round(float(req - ielts_score), 1)
                    close_gap.append(summary)

            log.info("tool_result", tool="get_courses_by_ielts",
                     comfortable=len(comfortably_meets), exact=len(exactly_meets),
                     close=len(close_gap))
            return {
                "your_ielts_score": ielts_score,
                "comfortably_qualifies": list(comfortably_meets[:20]),
                "exactly_qualifies": list(exactly_meets[:20]),
                "close_to_qualifying": list(close_gap[:10]),
                "summary": {
                    "total_comfortable": len(comfortably_meets),
                    "total_exact": len(exactly_meets),
                    "total_close_gap": len(close_gap),
                    "total_qualifying": len(comfortably_meets) + len(exactly_meets),
                },
                "destination_country": destination_country,
                "study_level": study_level,
            }

        except Exception as e:
            log.error("tool_error", tool="get_courses_by_ielts", error=str(e))
            return {"error": "Failed to find courses by IELTS.", "error_type": "tool_error"}
