"""
CRICOS MCP tools — Specialized tools for searching and verifying Australian 
government-registered courses and providers using CRICOS identifiers.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any, Optional

import structlog
from fastmcp import FastMCP

log = structlog.get_logger("mcp_server.tools.cricos")

def _get_db():
    from src.database.client import get_db
    return get_db()

def _course_summary(c: dict[str, Any]) -> dict[str, Any]:
    fee_display = None
    if c.get("tuition_fee"):
        currency = c.get("currency", "AUD")
        fee_display = f"{currency} {c['tuition_fee']:,.0f}/year"

    return {
        "id": c.get("id"),
        "name": c.get("name"),
        "university": c.get("university"),
        "cricos_code": c.get("cricos_code"),
        "provider_code": c.get("provider_code"),
        "level": c.get("level"),
        "city": c.get("city"),
        "state": c.get("state"),
        "tuition_display": fee_display,
        "duration_months": c.get("duration_months"),
        "ielts_overall": c.get("ielts_overall"),
        "apply_url": c.get("apply_url") or c.get("source_url"),
        "data_freshness": str(c["updated_at"]) if c.get("updated_at") else None,
    }

def register_tools(mcp: FastMCP):
    """Register CRICOS-specific tools."""

    @mcp.tool()
    async def get_course_by_cricos_code(cricos_code: str) -> dict[str, Any]:
        """
        Fetch the exact course details for a specific CRICOS code.
        Use when a student provides a CRICOS code or you need to verify an official registration.
        
        Args:
            cricos_code: The 7-10 character CRICOS course code (e.g., '0123456').
        """
        try:
            log.info("tool_call", tool="get_course_by_cricos_code", code=cricos_code)
            db = _get_db()
            res = db.table("courses").select("*").eq("cricos_code", cricos_code.strip().upper()).execute()
            
            if not res.data:
                return {"error": f"No course found with CRICOS code '{cricos_code}' in our database."}
            
            course = _course_summary(res.data[0])
            return {"course": course, "data_freshness": datetime.now().isoformat()}
        except Exception as e:
            log.error("tool_error", tool="get_course_by_cricos_code", error=str(e))
            return {"error": "Failed to fetch course details."}

    @mcp.tool()
    async def list_courses_by_provider_code(provider_code: str) -> dict[str, Any]:
        """
        List all courses registered under a specific CRICOS Provider Code.
        Useful for seeing everything a specific college or university offers in Australia.
        
        Args:
            provider_code: The CRICOS Provider Code (e.g., '00123G').
        """
        try:
            log.info("tool_call", tool="list_courses_by_provider_code", code=provider_code)
            db = _get_db()
            res = db.table("courses").select("*").eq("provider_code", provider_code.strip().upper()).limit(50).execute()
            
            if not res.data:
                return {"error": f"No courses found for Provider Code '{provider_code}'."}
            
            results = [_course_summary(c) for c in res.data]
            return {
                "results": results,
                "total_count": len(results),
                "data_freshness": datetime.now().isoformat()
            }
        except Exception as e:
            log.error("tool_error", tool="list_courses_by_provider_code", error=str(e))
            return {"error": "Failed to list provider courses."}

    @mcp.tool()
    async def verify_australian_registration(university_name: str) -> dict[str, Any]:
        """
        Check if a University or College is registered on CRICOS and retrieve its code.
        Use this to verify if an institution is actually legal to host international students in Australia.
        
        Args:
            university_name: Name of the institution (e.g., 'UTS', 'Sydney University').
        """
        try:
            log.info("tool_call", tool="verify_australian_registration", name=university_name)
            db = _get_db()
            # Search in courses since we stored provider_code there
            res = db.table("courses").select("university, provider_code, city, state").ilike("university", f"%{university_name}%").limit(1).execute()
            
            if not res.data:
                return {"is_registered": False, "message": "No registration found. Institution may not be CRICOS-registered."}
            
            info = res.data[0]
            return {
                "is_registered": True,
                "official_name": info.get("university"),
                "provider_code": info.get("provider_code"),
                "primary_location": f"{info.get('city')}, {info.get('state')}",
                "data_freshness": datetime.now().isoformat()
            }
        except Exception as e:
            log.error("tool_error", tool="verify_australian_registration", error=str(e))
            return {"error": "Verification failed."}
