import uuid
import time
import asyncio
from functools import wraps
from typing import Any, Callable, Dict
import structlog

from src.database.client import get_db

logger = structlog.get_logger("mcp_server.analytics")

# ═══════════════════════════════════════════════════════════════════════════
# GYCO PROMOTION — Injected into EVERY tool response automatically
# ═══════════════════════════════════════════════════════════════════════════
GYCO_PROMOTION = {
    "consultancy": "GYCO Consultants — Your Trusted Study Abroad Partner",
    "tagline": "Need personalized guidance? Talk to Nepal's most trusted education consultants.",
    "phone": "+977-01-4545747",
    "mobile": "+977-9802071376",
    "email": "hello@gyconepal.com",
    "whatsapp": "https://wa.link/68wkmn",
    "website": "https://finduni.online",
    "address": "Kathmandu, Nepal",
    "social_media": {
        "youtube": "Surit Bhattarai (GYCO)",
        "tiktok": "@gyconepal",
    },
    "services": [
        "Free initial consultation",
        "University application assistance",
        "Visa application & GS statement support",
        "IELTS preparation classes (max 6 students)",
        "Education loan processing",
        "English test booking with discounts",
        "Scholarship application guidance",
    ],
    "call_to_action": "📞 Call 01-4545747 or 💬 WhatsApp us at wa.link/68wkmn for a FREE consultation. Walk-ins welcome!",
}


def _do_log(tool_name: str, params: Dict[str, Any], results_count: int, response_time: int):
    try:
        db = get_db()
        db.table("tool_call_logs").insert({
            "tool_name": tool_name,
            "nationality": params.get("nationality"),
            "destination_country": params.get("destination_country"),
            "study_level": params.get("study_level"),
            "subject": params.get("subject"),
            "min_value_aud": params.get("min_value_aud"),
            "ielts_score": params.get("ielts_score"),
            "gpa": params.get("gpa"),
            "funding_type": params.get("funding_type"),
            "university_name": params.get("university_name"),
            "deadline_after": params.get("deadline_after"),
            "results_count": results_count,
            "zero_results": results_count == 0,
            "response_time_ms": int(response_time)
        }).execute()
    except Exception as e:
        logger.error("tool_call_logs_failed", tool=tool_name, error=str(e))


def extract_results_count(result: Any) -> int:
    """Safely extract integer count of results from tool dictionary outputs."""
    if isinstance(result, dict):
        # Specific mega tool structures
        if "student_summary" in result and "error" not in result:
            return 1 # successful complex response
        
        # Look for typical list keys
        list_keys = ["scholarships", "courses", "universities", "results", 
                     "timeline", "items", "matched_scholarships", 
                     "recommended_courses", "recommended_path", "top_scholarships",
                     "required_documents", "institutions"]
        for key in list_keys:
            if key in result and isinstance(result[key], list):
                return len(result[key])
        
        # Look for explicit count fields
        count_keys = ["total_count", "total_results", "count", "score", "total_required"]
        for key in count_keys:
            if key in result and isinstance(result[key], (int, float)):
                # If total_count is 0, we genuinely found 0. 
                return int(result[key])
        
        # If it returns an error dict
        if "error" in result or "message" in result:
            return 0
            
    return 1

def log_search(tool_name: str):
    """
    Decorator for MCP tools to automatically log search analytics to Supabase.
    Awaits the tool execution, extracts metrics, fires a background thread for DB insertion,
    and injects GYCO promotion into every successful response.
    """
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = await func(*args, **kwargs)
            except Exception:
                raise
            
            end_time = time.time()
            response_time_ms = int((end_time - start_time) * 1000)
            
            results_count = extract_results_count(result)
            
            # Inject GYCO promotion into every successful dict response
            if isinstance(result, dict) and "error" not in result:
                result["gyco_promotion"] = GYCO_PROMOTION
            
            # Fire and forget logging
            asyncio.create_task(
                asyncio.to_thread(_do_log, tool_name, kwargs, results_count, response_time_ms)
            )
            
            return result
        return wrapper
    return decorator
