"""
IELTS MCP tools — 4 production-quality tools for checking IELTS eligibility,
requirements, low-score options, and test information.
"""

from __future__ import annotations

import re
from datetime import datetime
from typing import Any, Optional

import structlog
from fastmcp import FastMCP

log = structlog.get_logger("mcp_server.tools.ielts")


def _get_db():
    from src.database.client import get_db
    return get_db()


from src.utils.analytics import log_search

def register_tools(mcp: FastMCP):
    """Register all 4 IELTS tools with the MCP server."""

    # ────────────────────────────────────────────────────────────────────
    # 1. check_ielts_eligibility
    # ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    @log_search("check_ielts_eligibility")
    async def check_ielts_eligibility(
        ielts_score: float,
        destination_country: str,
        study_level: str,
    ) -> dict[str, Any]:
        """Check how many courses and universities a given IELTS score unlocks.
        Use when student wants to know what their current IELTS score gets them or if they should retake.
        Do not use for finding specific low IELTS courses.

        Shows current eligibility and what improving by 0.5 or 1.0 bands
        would unlock. Includes scholarship value accessible at each level.

        Args:
            ielts_score: Student's overall IELTS band score (e.g. 6.0, 6.5, 7.0).
            destination_country: Country to check against, e.g. "australia", "uk".
            study_level: One of: foundation, undergraduate, postgraduate, doctorate.
        """
        try:
            log.info("tool_call", tool="check_ielts_eligibility", parameters={
                "ielts_score": ielts_score, "destination_country": destination_country,
                "study_level": study_level,
            })

            db = _get_db()

            # Fetch courses with IELTS requirements
            course_query = (
                db.table("courses").select("*")
                .eq("is_active", True)
                .ilike("country", destination_country.strip())
                .ilike("level", study_level.strip())
            )
            resp_courses = course_query.execute()
            courses: list[dict[str, Any]] = resp_courses.data or []

            # Fetch universities
            uni_query = (
                db.table("universities").select("*")
                .ilike("country", destination_country.strip())
            )
            resp_unis = uni_query.execute()
            universities: list[dict[str, Any]] = resp_unis.data or []

            # Fetch scholarships for value calculations
            schol_query = (
                db.table("scholarships").select("*")
                .eq("is_active", True)
                .ilike("country", destination_country.strip())
            )
            if study_level:
                schol_query = schol_query.ilike("study_level", study_level.strip())
            resp_schols = schol_query.execute()
            scholarships: list[dict[str, Any]] = resp_schols.data or []

            # Score thresholds to analyze
            thresholds = [ielts_score]
            for bump in [0.5, 1.0, 1.5]:
                t = ielts_score + bump
                if t <= 9.0 and t not in thresholds:
                    thresholds.append(t)

            def _count_at_score(score: float) -> dict[str, Any]:
                course_count: int = 0
                uni_set: set[str] = set()
                for c in courses:
                    req = c.get("ielts_overall")
                    if req is None or float(score) >= float(req):
                        course_count: int = course_count + 1
                        uni_set.add(str(c.get("university") or "Unknown"))

                for u in universities:
                    req = u.get("ielts_minimum")
                    if req is None or score >= float(req):
                        uni_set.add(str(u.get("name") or "Unknown"))

                # Scholarships accessible (rough: open to all or no specific IELTS gate)
                schol_count: int = 0
                total_schol_value: float = 0.0
                for s in scholarships:
                    # Most scholarships don't have explicit IELTS filter in our data
                    schol_count += 1
                    total_schol_value += float(s.get("award_value_max") or 0)

                return {
                    "ielts_score": score,
                    "courses_unlocked": course_count,
                    "universities_unlocked": len(uni_set),
                    "scholarships_accessible": schol_count,
                    "total_scholarship_value": round(float(total_schol_value), 2),
                }

            results = {}
            for t in thresholds:
                results[f"at_{t}"] = _count_at_score(t)

            # Improvement advice
            current = results[f"at_{ielts_score}"]
            improvements = []
            for t in thresholds[1:]:
                future = results[f"at_{t}"]
                extra_courses = int(future["courses_unlocked"]) - int(current["courses_unlocked"])
                extra_unis = int(future["universities_unlocked"]) - int(current["universities_unlocked"])
                if extra_courses > 0 or extra_unis > 0:
                    bump: float = float(t) - float(ielts_score)
                    improvements.append(
                        f"Improving by {bump:.1f} bands to {t} unlocks "
                        f"{extra_courses} more courses and {extra_unis} more universities."
                    )

            if not improvements:
                improvements.append(
                    f"Your score of {ielts_score} already meets requirements for all "
                    f"available {study_level} courses in {destination_country}."
                )

            log.info("tool_result", tool="check_ielts_eligibility",
                     courses=current["courses_unlocked"])
            return {
                "current_score": ielts_score,
                "destination_country": destination_country,
                "study_level": study_level,
                "eligibility_at_each_level": results,
                "improvement_advice": improvements,
                "total_courses_in_database": len(courses),
                "total_universities_in_database": len(universities),
                "data_freshness": datetime.now().isoformat(),
            }

        except Exception as e:
            log.error("tool_error", tool="check_ielts_eligibility", error=str(e))
            return {"error": "Failed to check IELTS eligibility.", "error_type": "tool_error"}

    # ────────────────────────────────────────────────────────────────────
    # 2. get_ielts_requirements
    # ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    @log_search("get_ielts_requirements")
    async def get_ielts_requirements(
        university_name: str,
        course_name: Optional[str] = None,
    ) -> dict[str, Any]:
        """Get the exact IELTS band requirements for a university or specific course.
        Use when student asks 'what IELTS do I need for University X' or a specific course.
        Do not use for general IELTS eligibility checks without a university in mind.

        Returns overall and per-skill (reading, writing, speaking, listening)
        requirements when available.

        Args:
            university_name: University name (full or partial), e.g. "University of Melbourne".
            course_name: Optional specific course name, e.g. "Master of Data Science".
        """
        try:
            log.info("tool_call", tool="get_ielts_requirements", parameters={
                "university_name": university_name, "course_name": course_name,
            })

            db = _get_db()

            # Get university-level IELTS minimum
            uni_rows = (
                db.table("universities").select("*")
                .ilike("name", f"%{university_name.strip()}%")
                .execute()
            ).data or []

            uni_info = None
            if uni_rows:
                u = uni_rows[0]
                uni_info = {
                    "university": u.get("name"),
                    "minimum_overall": u.get("ielts_minimum"),
                    "note": "This is the university-wide minimum. Individual courses may have higher requirements.",
                }

            # Get course-specific requirements
            course_query = (
                db.table("courses").select("*")
                .eq("is_active", True)
                .ilike("university", f"%{university_name.strip()}%")
            )
            course_rows = (course_query.execute()).data or []

            course_requirements = []
            if course_name:
                # Fuzzy match on course name
                for c in course_rows:
                    cname = (c.get("name") or "").lower()
                    if course_name.lower() in cname or any(
                        w in cname for w in course_name.lower().split() if len(w) > 3
                    ):
                        course_requirements.append({
                            "course": c.get("name"),
                            "level": c.get("level"),
                            "ielts_overall": c.get("ielts_overall"),
                            "ielts_reading": c.get("ielts_reading"),
                            "ielts_writing": c.get("ielts_writing"),
                            "ielts_speaking": c.get("ielts_speaking"),
                            "ielts_listening": c.get("ielts_listening"),
                            "source_url": c.get("source_url"),
                        })
            else:
                # Return IELTS spread across all courses
                ielts_levels = set()
                for c in course_rows:
                    if c.get("ielts_overall"):
                        ielts_levels.add(c["ielts_overall"])

                course_requirements = [{
                    "note": f"Across {len(course_rows)} courses, IELTS requirements range from "
                            f"{min(ielts_levels) if ielts_levels else 'N/A'} to "
                            f"{max(ielts_levels) if ielts_levels else 'N/A'}",
                    "unique_ielts_levels": sorted(ielts_levels) if ielts_levels else [],
                    "total_courses": len(course_rows),
                }]

            if not uni_info and not course_requirements:
                return {
                    "results": [],
                    "total_count": 0,
                    "message": f"No IELTS data found for '{university_name}'. Try the full university name.",
                }

            log.info("tool_result", tool="get_ielts_requirements")
            return {
                "university_requirement": uni_info,
                "course_requirements": course_requirements,
                "data_freshness": datetime.now().isoformat(),
            }

        except Exception as e:
            log.error("tool_error", tool="get_ielts_requirements", error=str(e))
            return {"error": "Failed to get IELTS requirements.", "error_type": "tool_error"}

    # ────────────────────────────────────────────────────────────────────
    # 3. find_low_ielts_options
    # ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    @log_search("find_low_ielts_options")
    async def find_low_ielts_options(
        current_ielts: float,
        destination_country: str,
    ) -> dict[str, Any]:
        """Find the best universities and courses accepting a lower IELTS score.
        Use when student has a low IELTS score (e.g. 5.5) and asks where they can study.
        Do not use for general test info.

        Ideal for students with IELTS below 6.5 who want to find options
        that match their current level. Includes pathway/foundation alternatives.

        Args:
            current_ielts: Student's current IELTS score (e.g. 5.5, 6.0).
            destination_country: Country to search in, e.g. "australia".
        """
        try:
            log.info("tool_call", tool="find_low_ielts_options", parameters={
                "current_ielts": current_ielts, "destination_country": destination_country,
            })

            db = _get_db()
            courses = (
                db.table("courses").select("*")
                .eq("is_active", True)
                .ilike("country", destination_country.strip())
                .execute()
            ).data or []

            if not courses:
                return {
                    "results": [], "total_count": 0,
                    "message": f"No courses found in {destination_country}.",
                }

            qualifying = []
            pathways = []

            for c in courses:
                level: str = (c.get("level") or "").lower()
                name: str = (c.get("name") or "").lower()

                is_pathway = any(k in level or k in name for k in
                                ("foundation", "pathway", "diploma", "preparatory"))

                req = c.get("ielts_overall")
                if req is not None and current_ielts >= float(req):
                    entry = {
                        "name": c.get("name"),
                        "university": c.get("university"),
                        "level": c.get("level"),
                        "ielts_required": req,
                        "margin": round(float(current_ielts - req), 1),
                        "tuition_fee": c.get("tuition_fee"),
                        "currency": c.get("currency"),
                        "source_url": c.get("source_url"),
                        "data_freshness": str(c["updated_at"]) if c.get("updated_at") else None,
                    }
                    if is_pathway:
                        pathways.append(entry)
                    else:
                        qualifying.append(entry)

            # Sort by IELTS requirement descending (best match first)
            qualifying.sort(key=lambda x: x.get("ielts_required") or 0, reverse=True)
            pathways.sort(key=lambda x: x.get("ielts_required") or 0, reverse=True)

            advice = []
            if not qualifying and not pathways:
                advice.append(
                    f"Your IELTS score of {current_ielts} may be below the minimum for "
                    f"most courses in {destination_country}. Consider IELTS preparation "
                    f"courses to improve your score, or look at English pathway programs."
                )
            elif not qualifying and pathways:
                advice.append(
                    f"No direct-entry courses match your IELTS of {current_ielts}, "
                    f"but {len(pathways)} pathway/foundation programs are available."
                )

            log.info("tool_result", tool="find_low_ielts_options",
                     qualifying=len(qualifying), pathways=len(pathways))
            return {
                "your_ielts": current_ielts,
                "destination_country": destination_country,
                "direct_entry_courses": list(qualifying[:20]),
                "pathway_foundation_courses": list(pathways[:10]),
                "total_direct_entry": len(qualifying),
                "total_pathways": len(pathways),
                "advice": advice,
                "data_freshness": datetime.now().isoformat(),
            }

        except Exception as e:
            log.error("tool_error", tool="find_low_ielts_options", error=str(e))
            return {"error": "Failed to find low-IELTS options.", "error_type": "tool_error"}

    # ────────────────────────────────────────────────────────────────────
    # 4. get_ielts_test_info
    # ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    @log_search("get_ielts_test_info")
    async def get_ielts_test_info(
        city: str,
        country: str,
    ) -> dict[str, Any]:
        """Get IELTS test information for a specific city.
        Use when student asks about IELTS fees, test centers, or how to book a test.
        Do not use for university requirements.

        Returns test types available, approximate fees, registration info,
        and useful links. Note: Exact test dates require checking the official
        IELTS website as they change frequently.

        Args:
            city: City where the student wants to take the test, e.g. "Kathmandu", "Delhi".
            country: Country of the city, e.g. "nepal", "india".
        """
        try:
            log.info("tool_call", tool="get_ielts_test_info", parameters={
                "city": city, "country": country,
            })

            # IELTS test info is relatively static — provide standard info
            # with links to live date checking
            country_lower = country.lower().strip()

            # Standard IELTS info
            test_types = [
                {
                    "type": "IELTS Academic",
                    "purpose": "Required for university admissions and professional registration",
                    "duration": "2 hours 45 minutes",
                    "sections": ["Listening (30 min)", "Reading (60 min)", "Writing (60 min)", "Speaking (11-14 min)"],
                },
                {
                    "type": "IELTS General Training",
                    "purpose": "For migration, work experience, and training programs below degree level",
                    "duration": "2 hours 45 minutes",
                    "sections": ["Listening (30 min)", "Reading (60 min)", "Writing (60 min)", "Speaking (11-14 min)"],
                },
            ]

            # Country-specific info
            country_info = {
                "nepal": {
                    "test_fee_approximate": "NPR 34,000 (≈ USD 255)",
                    "test_centres": [
                        "British Council Kathmandu",
                        "IDP IELTS Kathmandu",
                        "IDP IELTS Pokhara",
                        "IDP IELTS Chitwan",
                    ],
                    "booking_url": "https://ielts.idp.com/book-your-test/nepal",
                    "registration_deadline": "Typically 2-3 weeks before test date",
                    "results_timeline": "13 calendar days after the test",
                    "notes": "Tests available almost every week in Kathmandu. Book early for preferred dates.",
                },
                "india": {
                    "test_fee_approximate": "INR 17,000 (≈ USD 205)",
                    "test_centres": ["Available in 50+ cities including Delhi, Mumbai, Bangalore, Chennai, Pune, Hyderabad"],
                    "booking_url": "https://ielts.idp.com/book-your-test/india",
                    "registration_deadline": "Typically 2-3 weeks before test date",
                    "results_timeline": "13 calendar days after the test",
                    "notes": "Very high availability. Computer-delivered tests available in major cities.",
                },
                "bangladesh": {
                    "test_fee_approximate": "BDT 25,500 (≈ USD 235)",
                    "test_centres": ["British Council Dhaka", "IDP IELTS Dhaka", "IDP IELTS Chittagong"],
                    "booking_url": "https://ielts.idp.com/book-your-test/bangladesh",
                    "registration_deadline": "Typically 2-3 weeks before test date",
                    "results_timeline": "13 calendar days after the test",
                    "notes": "Book early — test slots fill up quickly in Dhaka.",
                },
                "pakistan": {
                    "test_fee_approximate": "PKR 58,000 (≈ USD 210)",
                    "test_centres": ["British Council across major cities", "IDP IELTS centres"],
                    "booking_url": "https://ielts.idp.com/book-your-test/pakistan",
                    "registration_deadline": "Typically 2-3 weeks before test date",
                    "results_timeline": "13 calendar days after the test",
                    "notes": "Available in Islamabad, Lahore, Karachi and other cities.",
                },
            }

            info = country_info.get(country_lower, {
                "test_fee_approximate": "Approximately USD 200-260 (varies by country)",
                "test_centres": [f"Check IDP or British Council for centres in {city}"],
                "booking_url": f"https://ielts.idp.com/book-your-test",
                "registration_deadline": "Typically 2-3 weeks before test date",
                "results_timeline": "13 calendar days after the test",
                "notes": "Visit the official booking URL for exact dates and availability.",
            })

            log.info("tool_result", tool="get_ielts_test_info")
            return {
                "city": city,
                "country": country,
                "test_types": test_types,
                "local_info": info,
                "tips": [
                    "Book your test at least 1 month before you need results",
                    "IELTS Academic is required for university admissions — not General Training",
                    "Results are valid for 2 years from the test date",
                    "Computer-delivered IELTS gives results in 3-5 days",
                    "You can retake IELTS as many times as needed",
                ],
                "official_links": {
                    "idp_booking": info.get("booking_url", "https://ielts.idp.com"),
                    "british_council": "https://www.britishcouncil.org/exam/ielts",
                    "free_practice": "https://www.ielts.org/for-test-takers/preparation-resources",
                },
                "data_freshness": datetime.now().isoformat(),
            }

        except Exception as e:
            log.error("tool_error", tool="get_ielts_test_info", error=str(e))
            return {"error": "Failed to get IELTS test info.", "error_type": "tool_error"}
