"""
University MCP tools — 5 production-quality tools for comparing, profiling,
and analyzing universities from the ScholarRadar database.

Each tool returns structured data with source URLs and data freshness timestamps.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Any, Optional

import structlog
from mcp.server.fastmcp import FastMCP

log = structlog.get_logger("mcp_server.tools.universities")

# ── Helpers ─────────────────────────────────────────────────────────────────


def _get_db():
    from src.database.client import get_db
    return get_db()


def _fetch_universities(
    country: Optional[str] = None,
    name: Optional[str] = None,
) -> list[dict[str, Any]]:
    db = _get_db()
    query = db.table("universities").select("*")
    if country:
        query = query.ilike("country", country.strip())
    if name:
        query = query.ilike("name", f"%{name.strip()}%")
    response = query.execute()
    return response.data or []


def _uni_summary(u: dict[str, Any]) -> dict[str, Any]:
    tuition_display = None
    if u.get("tuition_min") or u.get("tuition_max"):
        currency = u.get("currency", "AUD")
        t_min = u.get("tuition_min")
        t_max = u.get("tuition_max")
        if t_min and t_max and t_min != t_max:
            tuition_display = f"{currency} {t_min:,.0f} – {t_max:,.0f}/year"
        elif t_max:
            tuition_display = f"{currency} {t_max:,.0f}/year"
        elif t_min:
            tuition_display = f"{currency} {t_min:,.0f}/year"

    return {
        "id": u.get("id"),
        "name": u.get("name"),
        "country": u.get("country"),
        "city": u.get("city"),
        "world_ranking": u.get("world_ranking"),
        "subject_rankings": u.get("subject_rankings"),
        "acceptance_rate": u.get("acceptance_rate"),
        "total_students": u.get("total_students"),
        "international_students": u.get("international_students"),
        "tuition_min": u.get("tuition_min"),
        "tuition_max": u.get("tuition_max"),
        "tuition_display": tuition_display,
        "currency": u.get("currency"),
        "ielts_minimum": u.get("ielts_minimum"),
        "popular_subjects": u.get("popular_subjects"),
        "facilities": u.get("facilities"),
        "accommodation_cost_min": u.get("accommodation_cost_min"),
        "accommodation_cost_max": u.get("accommodation_cost_max"),
        "website": u.get("website"),
        "idp_profile_url": u.get("idp_profile_url"),
        "data_freshness": str(u["updated_at"]) if u.get("updated_at") else None,
    }


def _empty_result(message: str) -> dict[str, Any]:
    return {"results": [], "total_count": 0, "message": message}


# ── Tool Registration ──────────────────────────────────────────────────────


def register_tools(mcp: FastMCP):
    """Register all 5 university tools with the MCP server."""

    # ────────────────────────────────────────────────────────────────────
    # 1. compare_universities
    # ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    async def compare_universities(
        university1: str,
        university2: str,
    ) -> dict[str, Any]:
        """Compare two universities side by side across all dimensions.

        Returns structured comparison of rankings, fees, student body,
        IELTS requirements, accommodation costs, facilities, and popular subjects.

        Args:
            university1: Full or partial name of the first university, e.g. "University of Melbourne".
            university2: Full or partial name of the second university, e.g. "University of Sydney".
        """
        try:
            log.info("tool_call", tool="compare_universities", parameters={
                "university1": university1, "university2": university2,
            })

            rows1 = _fetch_universities(name=university1)
            rows2 = _fetch_universities(name=university2)

            if not rows1 and not rows2:
                return _empty_result("Could not find either university. Check spellings.")
            if not rows1:
                return _empty_result(f"Could not find '{university1}'.")
            if not rows2:
                return _empty_result(f"Could not find '{university2}'.")

            u1, u2 = _uni_summary(rows1[0]), _uni_summary(rows2[0])

            comparison = {
                "university_1": u1,
                "university_2": u2,
                "comparison_dimensions": {
                    "world_ranking": {
                        "university_1": u1.get("world_ranking"),
                        "university_2": u2.get("world_ranking"),
                        "better_ranked": u1["name"] if (int(u1.get("world_ranking") or 9999)) < (int(u2.get("world_ranking") or 9999)) else u2["name"],
                    },
                    "tuition_fees": {
                        "university_1": u1.get("tuition_display"),
                        "university_2": u2.get("tuition_display"),
                        "more_affordable": u1["name"] if (float(rows1[0].get("tuition_max") or float("inf"))) < (float(rows2[0].get("tuition_max") or float("inf"))) else u2["name"],
                    },
                    "ielts_minimum": {
                        "university_1": u1.get("ielts_minimum"),
                        "university_2": u2.get("ielts_minimum"),
                        "lower_requirement": u1["name"] if (float(rows1[0].get("ielts_minimum") or 99)) < (float(rows2[0].get("ielts_minimum") or 99)) else u2["name"],
                    },
                    "student_body": {
                        "university_1": {
                            "total": u1.get("total_students"),
                            "international": u1.get("international_students"),
                        },
                        "university_2": {
                            "total": u2.get("total_students"),
                            "international": u2.get("international_students"),
                        },
                    },
                    "acceptance_rate": {
                        "university_1": u1.get("acceptance_rate"),
                        "university_2": u2.get("acceptance_rate"),
                    },
                    "accommodation_cost": {
                        "university_1": {
                            "min": rows1[0].get("accommodation_cost_min"),
                            "max": rows1[0].get("accommodation_cost_max"),
                        },
                        "university_2": {
                            "min": rows2[0].get("accommodation_cost_min"),
                            "max": rows2[0].get("accommodation_cost_max"),
                        },
                    },
                    "popular_subjects": {
                        "university_1": u1.get("popular_subjects"),
                        "university_2": u2.get("popular_subjects"),
                    },
                },
            }

            log.info("tool_result", tool="compare_universities")
            return comparison

        except Exception as e:
            log.error("tool_error", tool="compare_universities", error=str(e))
            return {"error": "Failed to compare universities.", "error_type": "tool_error"}

    # ────────────────────────────────────────────────────────────────────
    # 2. get_university_profile
    # ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    async def get_university_profile(
        university_name: str,
    ) -> dict[str, Any]:
        """Get a comprehensive profile for a single university.

        Returns everything known about the university: rankings, fees,
        admission requirements, student demographics, facilities,
        popular subjects, accommodation costs, and links.

        Args:
            university_name: Full or partial name, e.g. "ANU", "Monash", "University of Queensland".
        """
        try:
            log.info("tool_call", tool="get_university_profile", parameters={
                "university_name": university_name,
            })

            rows = _fetch_universities(name=university_name)
            if not rows:
                return _empty_result(
                    f"No university found matching '{university_name}'. "
                    "Try the full name or a different spelling."
                )

            u = rows[0]
            profile = _uni_summary(u)

            # Enrich with scholarship count
            try:
                db = _get_db()
                scholarship_resp = (
                    db.table("scholarships")
                    .select("id", count="exact")
                    .ilike("university", f"%{u['name']}%")
                    .eq("is_active", True)
                    .limit(0)
                    .execute()
                )
                profile["active_scholarships_count"] = scholarship_resp.count or 0
            except Exception:
                profile["active_scholarships_count"] = None

            # Enrich with course count
            try:
                course_resp = (
                    db.table("courses")
                    .select("id", count="exact")
                    .ilike("university", f"%{u['name']}%")
                    .eq("is_active", True)
                    .limit(0)
                    .execute()
                )
                profile["active_courses_count"] = course_resp.count or 0
            except Exception:
                profile["active_courses_count"] = None

            log.info("tool_result", tool="get_university_profile", university=u["name"])
            return {"profile": profile}

        except Exception as e:
            log.error("tool_error", tool="get_university_profile", error=str(e))
            return {"error": "Failed to get university profile.", "error_type": "tool_error"}

    # ────────────────────────────────────────────────────────────────────
    # 3. find_universities_by_budget
    # ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    async def find_universities_by_budget(
        max_tuition_per_year: float,
        destination_country: str,
        currency: str = "AUD",
    ) -> dict[str, Any]:
        """Find universities with tuition fees under a specified budget.

        Returns universities sorted by tuition (lowest first), with rankings
        and key stats to help find the best value.

        Args:
            max_tuition_per_year: Maximum annual tuition budget, e.g. 30000.
            destination_country: Country to search in, e.g. "australia".
            currency: Currency for comparison (default "AUD"). All amounts assumed same currency.
        """
        try:
            log.info("tool_call", tool="find_universities_by_budget", parameters={
                "max_tuition_per_year": max_tuition_per_year,
                "destination_country": destination_country,
                "currency": currency,
            })

            rows = _fetch_universities(country=destination_country)

            if not rows:
                return _empty_result(
                    f"No universities found in {destination_country}."
                )

            affordable: list[dict[str, Any]] = []
            for u in rows:
                # Use tuition_min for most optimistic check
                fee = u.get("tuition_min") or u.get("tuition_max")
                if fee is None:
                    continue  # Can't determine affordability
                if fee <= max_tuition_per_year:
                    summary = _uni_summary(u)
                    summary["within_budget"] = True
                    affordable.append(summary)

            affordable.sort(key=lambda x: float(x.get("tuition_min") or 0))

            if not affordable:
                # Find the cheapest anyway for reference
                with_fees = [u for u in rows if u.get("tuition_min")]
                if with_fees:
                    cheapest = min(with_fees, key=lambda u: u["tuition_min"])
                    return {
                        "results": [],
                        "total_count": 0,
                        "message": (
                            f"No universities in {destination_country} have tuition under "
                            f"{currency} {max_tuition_per_year:,.0f}. "
                            f"The most affordable option is {cheapest['name']} at "
                            f"{currency} {cheapest['tuition_min']:,.0f}/year."
                        ),
                        "cheapest_available": _uni_summary(cheapest),
                    }
                return _empty_result(
                    f"No universities found in {destination_country} with listed tuition fees."
                )

            log.info("tool_result", tool="find_universities_by_budget",
                     result_count=len(affordable))
            return {
                "results": affordable,
                "total_count": len(affordable),
                "budget": f"{currency} {max_tuition_per_year:,.0f}/year",
                "destination_country": destination_country,
            }

        except Exception as e:
            log.error("tool_error", tool="find_universities_by_budget", error=str(e))
            return {"error": "Failed to find universities by budget.", "error_type": "tool_error"}

    # ────────────────────────────────────────────────────────────────────
    # 4. get_top_universities
    # ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    async def get_top_universities(
        destination_country: str,
        subject: Optional[str] = None,
        limit: int = 10,
    ) -> dict[str, Any]:
        """Get the top-ranked universities in a country, optionally filtered by subject strength.

        Returns universities sorted by world ranking, with tuition fees and
        admission requirements for each.

        Args:
            destination_country: Country to list universities for, e.g. "australia", "uk".
            subject: Optional subject to prioritize, e.g. "engineering", "business". Universities that list this in their popular subjects rank higher.
            limit: Maximum number of universities to return (default 10).
        """
        try:
            log.info("tool_call", tool="get_top_universities", parameters={
                "destination_country": destination_country,
                "subject": subject, "limit": limit,
            })

            rows = _fetch_universities(country=destination_country)

            if not rows:
                return _empty_result(
                    f"No universities found in {destination_country}."
                )

            # Score: world ranking + subject relevance
            scored: list[tuple[int, float, dict[str, Any]]] = []
            for u in rows:
                ranking = u.get("world_ranking") or 9999
                subject_bonus = 0.0

                if subject:
                    popular = u.get("popular_subjects") or []
                    if isinstance(popular, list):
                        for p in popular:
                            if isinstance(p, str) and subject.lower() in p.lower():
                                subject_bonus = 1.0
                                break

                    # Check subject rankings JSON
                    subj_rankings = u.get("subject_rankings") or {}
                    if isinstance(subj_rankings, dict):
                        for subj_name, rank in subj_rankings.items():
                            if subject.lower() in subj_name.lower():
                                subject_bonus = max(subject_bonus, 1.0)
                                break

                scored.append((ranking, subject_bonus, u))

            # Sort: subject bonus descending, then ranking ascending
            scored.sort(key=lambda x: (-x[1], x[0]))
            top_n = list(scored[:limit])

            results = []
            for rank_pos, (ranking, subj_bonus, u) in enumerate(top_n, 1):
                summary = _uni_summary(u)
                summary["list_position"] = rank_pos
                if subject and subj_bonus > 0:
                    summary["subject_strength"] = f"Strong in {subject}"
                results.append(summary)

            log.info("tool_result", tool="get_top_universities", result_count=len(results))
            return {
                "results": results,
                "total_count": len(results),
                "destination_country": destination_country,
                "subject_filter": subject,
            }

        except Exception as e:
            log.error("tool_error", tool="get_top_universities", error=str(e))
            return {"error": "Failed to get top universities.", "error_type": "tool_error"}

    # ────────────────────────────────────────────────────────────────────
    # 5. get_scholarship_rich_universities
    # ────────────────────────────────────────────────────────────────────

    @mcp.tool()
    async def get_scholarship_rich_universities(
        destination_country: str,
        study_level: Optional[str] = None,
        limit: int = 10,
    ) -> dict[str, Any]:
        """Find universities with the most and highest-value scholarships.

        Queries the scholarships table, aggregates by university, and returns
        universities ranked by total scholarship value and count.

        Args:
            destination_country: Country to search, e.g. "australia".
            study_level: Optional level filter: foundation, undergraduate, postgraduate, doctorate.
            limit: Maximum universities to return (default 10).
        """
        try:
            log.info("tool_call", tool="get_scholarship_rich_universities", parameters={
                "destination_country": destination_country,
                "study_level": study_level, "limit": limit,
            })

            db = _get_db()
            query = (
                db.table("scholarships")
                .select("*")
                .eq("is_active", True)
                .ilike("country", destination_country.strip())
            )
            if study_level:
                query = query.ilike("study_level", study_level.strip())
            response = query.execute()
            scholarships = response.data or []

            if not scholarships:
                return _empty_result(
                    f"No scholarships found in {destination_country}"
                    + (f" for {study_level}" if study_level else "")
                    + "."
                )

            # Aggregate by university
            uni_data: dict[str, dict[str, Any]] = {}

            for s in scholarships:
                uni_name = s.get("university") or "Unknown"
                if uni_name not in uni_data:
                    uni_data[uni_name] = {
                        "count": 0,
                        "total_max_value": 0.0,
                        "funding_types": defaultdict(int),
                        "top_scholarship": None,
                        "top_value": 0.0,
                    }
                d = uni_data[uni_name]
                d["count"] += 1

                val = float(s.get("award_value_max") or 0)
                d["total_max_value"] += val

                ft = s.get("funding_type") or "unknown"
                d["funding_types"][ft] += 1

                if val > d["top_value"]:
                    d["top_value"] = val
                    d["top_scholarship"] = s.get("title")

            # Score: weighted combo of count and total value
            scored = []
            for uni_name, d in uni_data.items():
                score = d["count"] * 0.4 + (d["total_max_value"] / 10000) * 0.6
                scored.append((score, uni_name, d))

            scored.sort(key=lambda x: float(x[0]), reverse=True)
            top_n = list(scored[:limit])

            results = []
            for rank, (score, uni_name, d) in enumerate(top_n, 1):
                # Try to get university profile
                uni_rows = _fetch_universities(name=uni_name)
                profile = _uni_summary(uni_rows[0]) if uni_rows else {"name": uni_name}

                results.append({
                    "rank": rank,
                    "university": profile,
                    "scholarship_stats": {
                        "total_scholarships": d["count"],
                        "total_max_value": round(float(d["total_max_value"]), 2),
                        "top_scholarship": d["top_scholarship"],
                        "top_value": d["top_value"],
                        "funding_types": dict(d["funding_types"]),
                    },
                })

            log.info("tool_result", tool="get_scholarship_rich_universities",
                     result_count=len(results))
            return {
                "results": results,
                "total_count": len(results),
                "destination_country": destination_country,
                "study_level": study_level,
            }

        except Exception as e:
            log.error("tool_error", tool="get_scholarship_rich_universities", error=str(e))
            return {"error": "Failed to find scholarship-rich universities.", "error_type": "tool_error"}
