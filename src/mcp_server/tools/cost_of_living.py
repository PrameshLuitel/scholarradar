"""
Cost of Living MCP tools — 4 production-quality tools for city budgets,
destination comparisons, total cost calculations, and affordable city finding.
"""
from __future__ import annotations
from typing import Any, Optional
from datetime import datetime
import structlog
from fastmcp import FastMCP

log = structlog.get_logger("mcp_server.tools.cost_of_living")

def _get_db():
    from src.database.client import get_db
    return get_db()

def _city_summary(c: dict[str, Any]) -> dict[str, Any]:
    return {
        "city": c.get("city"), "country": c.get("country"),
        "currency": c.get("currency", "AUD"),
        "monthly_costs": {
            "rent_shared": {"min": c.get("rent_shared_min"), "max": c.get("rent_shared_max")},
            "rent_private": {"min": c.get("rent_private_min"), "max": c.get("rent_private_max")},
            "food": c.get("food_monthly"),
            "transport": c.get("transport_monthly"),
            "utilities": c.get("utilities_monthly"),
            "internet": c.get("internet_monthly"),
        },
        "total_monthly": {"min": c.get("total_monthly_min"), "max": c.get("total_monthly_max")},
        "part_time_wage_hourly": c.get("part_time_wage_hourly"),
        "data_freshness": str(c["last_updated"]) if c.get("last_updated") else None,
    }

from src.utils.analytics import log_search

def register_tools(mcp: FastMCP):
    """Register all 4 cost of living tools."""

    @mcp.tool()
    @log_search("get_city_budget")
    async def get_city_budget(city: str, country: str) -> dict[str, Any]:
        """Get detailed monthly cost breakdown for a specific city.
        Use when student asks about living expenses, rent, or part-time wages in a particular city.
        Do not use for calculating total course cost including tuition.

        Includes rent (shared/private), food, transport, utilities, internet,
        and part-time wage earning potential.
        Args:
            city: City name, e.g. "Sydney", "Melbourne", "Brisbane".
            country: Country, e.g. "australia".
        """
        try:
            log.info("tool_call", tool="get_city_budget", city=city, country=country)
            db = _get_db()
            rows = (db.table("cost_of_living").select("*")
                .ilike("city", city.strip())
                .ilike("country", country.strip()).execute()).data or []
            if not rows:
                return {"results": [], "total_count": 0,
                    "message": f"No cost data for {city}, {country}. Try a major city."}
            c = rows[0]
            result = _city_summary(c)
            # Earning potential
            wage = c.get("part_time_wage_hourly") or 0
            if wage > 0:
                weekly_20h = wage * 20
                monthly_income = weekly_20h * 4
                result["earning_potential"] = {
                    "hourly_wage": wage,
                    "weekly_20hrs": round(weekly_20h, 2),
                    "monthly_estimate": round(monthly_income, 2),
                    "note": "Based on 20hrs/week part-time (student visa limit during term)",
                }
                min_cost = c.get("total_monthly_min") or 0
                if min_cost > 0:
                    coverage = monthly_income / min_cost * 100
                    result["earning_potential"]["covers_expenses_pct"] = round(float(coverage), 1)
                    result["earning_potential"]["summary"] = (
                        f"Part-time work covers ~{coverage:.0f}% of minimum monthly expenses"
                    )
            # Budget tips
            result["budget_tips"] = [
                "Shared accommodation is 40-50% cheaper than private",
                "Cook at home to reduce food costs by 40-60%",
                "Get a student concession card for transport discounts",
                "Many universities offer free/subsidized meals and services",
            ]
            log.info("tool_result", tool="get_city_budget")
            result["data_freshness"] = datetime.now().isoformat()
            return result
        except Exception as e:
            log.error("tool_error", tool="get_city_budget", error=str(e))
            return {"error": "Failed to get city budget.", "error_type": "tool_error"}

    @mcp.tool()
    @log_search("compare_study_destinations")
    async def compare_study_destinations(
        city1: str, country1: str,
        city2: str, country2: str,
    ) -> dict[str, Any]:
        """Compare cost of living between two cities side by side.
        Use when student wants to know which city is cheaper or comparing rent between two places.
        Do not use for broad affordability searches across a whole country.

        Shows rent, food, transport, total monthly, and earning potential for each.
        Args:
            city1: First city, e.g. "Sydney".
            country1: First country, e.g. "australia".
            city2: Second city, e.g. "Melbourne".
            country2: Second country, e.g. "australia".
        """
        try:
            log.info("tool_call", tool="compare_study_destinations")
            db = _get_db()
            r1 = (db.table("cost_of_living").select("*")
                .ilike("city", city1.strip()).ilike("country", country1.strip())
                .execute()).data or []
            r2 = (db.table("cost_of_living").select("*")
                .ilike("city", city2.strip()).ilike("country", country2.strip())
                .execute()).data or []
            if not r1 and not r2:
                return {"results": [], "total_count": 0,
                    "message": "No cost data for either city."}
            if not r1:
                return {"results": [], "total_count": 0,
                    "message": f"No data for {city1}, {country1}."}
            if not r2:
                return {"results": [], "total_count": 0,
                    "message": f"No data for {city2}, {country2}."}
            s1, s2 = _city_summary(r1[0]), _city_summary(r2[0])
            c1_min = r1[0].get("total_monthly_min") or 0
            c2_min = r2[0].get("total_monthly_min") or 0
            cheaper = f"{city1}" if c1_min < c2_min and c1_min > 0 else f"{city2}"
            savings = abs(c1_min - c2_min)
            return {
                "city_1": s1, "city_2": s2,
                "comparison": {
                    "cheaper_city": cheaper,
                    "monthly_savings": round(float(savings), 2),
                    "annual_savings": round(float(savings * 12), 2),
                    "rent_shared_cheaper": city1 if (float(r1[0].get("rent_shared_min") or 9999)) < (float(r2[0].get("rent_shared_min") or 9999)) else city2,
                    "food_cheaper": city1 if (float(r1[0].get("food_monthly") or 9999)) < (float(r2[0].get("food_monthly") or 9999)) else city2,
                    "transport_cheaper": city1 if (float(r1[0].get("transport_monthly") or 9999) < float(r2[0].get("transport_monthly") or 9999)) else city2,
                },
                "data_freshness": datetime.now().isoformat(),
            }
        except Exception as e:
            log.error("tool_error", tool="compare_study_destinations", error=str(e))
            return {"error": "Failed to compare destinations.", "error_type": "tool_error"}

    @mcp.tool()
    @log_search("calculate_total_cost")
    async def calculate_total_cost(
        city: str, country: str,
        course_duration_months: int,
        annual_tuition_aud: float,
        accommodation_type: str = "shared",
        nationality: Optional[str] = None,
    ) -> dict[str, Any]:
        """Calculate total cost for entire course duration including living, visa, OSHC, flights.
        Use when student asks for the grand total, total budget needed, or 'how much will it cost to study'.
        Do not use for finding cheap universities; use find_universities_by_budget instead.

        Args:
            city: Study city, e.g. "Sydney".
            country: Study country, e.g. "australia".
            course_duration_months: Total months, e.g. 24.
            annual_tuition_aud: Annual tuition in AUD.
            accommodation_type: "shared" or "private" (default shared).
            nationality: Optional, for visa fee calculation, e.g. "nepal".
        """
        try:
            log.info("tool_call", tool="calculate_total_cost")
            db = _get_db()
            rows = (db.table("cost_of_living").select("*")
                .ilike("city", city.strip()).ilike("country", country.strip())
                .execute()).data or []
            if not rows:
                return {"results": [], "total_count": 0,
                    "message": f"No cost data for {city}. Try a major city."}
            c = rows[0]
            months = course_duration_months
            years = months / 12
            # Tuition
            tuition_total = annual_tuition_aud * years
            # Living
            if accommodation_type == "private":
                rent_monthly = (c.get("rent_private_min") or 0 + (c.get("rent_private_max") or 0)) / 2
            else:
                rent_monthly = ((c.get("rent_shared_min") or 0) + (c.get("rent_shared_max") or 0)) / 2
            food = c.get("food_monthly") or 0
            transport = c.get("transport_monthly") or 0
            utilities = c.get("utilities_monthly") or 0
            internet = c.get("internet_monthly") or 0
            monthly_living = rent_monthly + food + transport + utilities + internet
            total_living = monthly_living * months
            # Fixed costs
            visa_fee = 710
            oshc_total = 650 * years  # approx
            flights = 2500  # return from South Asia
            setup_costs = 2000  # initial deposit, bedding, etc.
            grand_total = tuition_total + total_living + visa_fee + oshc_total + flights + setup_costs
            # Earning offset
            wage = c.get("part_time_wage_hourly") or 0
            monthly_income = wage * 20 * 4 if wage else 0
            total_earnings = monthly_income * months
            net_cost = grand_total - total_earnings
            return {
                "city": city, "country": country,
                "course_duration_months": months,
                "cost_breakdown": {
                    "tuition_total": round(tuition_total, 2),
                    "living_total": round(total_living, 2),
                    "living_monthly": round(monthly_living, 2),
                    "living_detail": {
                        "rent_monthly": round(rent_monthly, 2),
                        "food_monthly": food, "transport_monthly": transport,
                        "utilities_monthly": utilities, "internet_monthly": internet,
                    },
                    "visa_fee": visa_fee,
                    "oshc_total": round(oshc_total, 2),
                    "flights": flights,
                    "setup_costs": setup_costs,
                },
                "grand_total_aud": round(float(grand_total), 2),
                "earning_potential": {
                    "monthly_part_time": round(float(monthly_income), 2),
                    "total_earnings_estimate": round(float(total_earnings), 2),
                },
                "net_cost_after_earnings": round(float(net_cost), 2),
                "accommodation_type": accommodation_type,
                "currency": "AUD",
                "data_freshness": datetime.now().isoformat(),
            }
        except Exception as e:
            log.error("tool_error", tool="calculate_total_cost", error=str(e))
            return {"error": "Failed to calculate total cost.", "error_type": "tool_error"}

    @mcp.tool()
    @log_search("find_affordable_destinations")
    async def find_affordable_destinations(
        monthly_budget_aud: float,
        destination_country: str,
    ) -> dict[str, Any]:
        """Find the most affordable cities for study within a monthly budget.
        Use when student specifies a living budget and asks where they can afford to live.
        Do not use for comparing two specific cities.

        Returns cities sorted by total monthly cost (cheapest first),
        with budget fit analysis.
        Args:
            monthly_budget_aud: Maximum monthly budget including rent and living, e.g. 2500.
            destination_country: Country to search, e.g. "australia".
        """
        try:
            log.info("tool_call", tool="find_affordable_destinations")
            db = _get_db()
            rows = (db.table("cost_of_living").select("*")
                .ilike("country", destination_country.strip())
                .execute()).data or []
            if not rows:
                return {"results": [], "total_count": 0,
                    "message": f"No cost data for {destination_country}."}
            cities = []
            for c in rows:
                min_cost = c.get("total_monthly_min") or 0
                max_cost = c.get("total_monthly_max") or 0
                fits = min_cost <= monthly_budget_aud
                summary = _city_summary(c)
                summary["within_budget"] = fits
                summary["budget_surplus"] = round(float(monthly_budget_aud - min_cost), 2) if fits else None
                summary["budget_shortfall"] = round(float(min_cost - monthly_budget_aud), 2) if not fits else None
                cities.append((min_cost, summary))
            cities.sort(key=lambda x: x[0])
            affordable = [s for _, s in cities if s["within_budget"]]
            over_budget = [s for _, s in cities if not s["within_budget"]]
            return {
                "budget_aud_monthly": monthly_budget_aud,
                "destination_country": destination_country,
                "affordable_cities": list(affordable),
                "over_budget_cities": list(over_budget[:5]),
                "total_affordable": len(affordable),
                "total_cities": len(cities),
                "advice": (
                    f"{len(affordable)} cities fit your AUD {monthly_budget_aud:,.0f}/month budget."
                    if affordable else
                    f"No cities in {destination_country} fit AUD {monthly_budget_aud:,.0f}/month. "
                    f"Cheapest is {cities[0][1]['city']} at AUD {cities[0][0]:,.0f}/month."
                ),
                "data_freshness": datetime.now().isoformat(),
            }
        except Exception as e:
            log.error("tool_error", tool="find_affordable_destinations", error=str(e))
            return {"error": "Failed to find affordable destinations.", "error_type": "tool_error"}
