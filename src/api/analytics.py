import os
from datetime import datetime, timedelta
from typing import Any, Optional

from fastapi import APIRouter, Depends, HTTPException, Header, Request
from structlog import get_logger

from src.database.client import get_db

log = get_logger()

# Require API Key for Analytics endpoints
async def verify_analytics_key(x_analytics_key: str = Header(None)):
    expected_key = os.getenv("ANALYTICS_API_KEY")
    if not expected_key:
        log.warning("auth_warning", message="ANALYTICS_API_KEY is not set in environment")
        raise HTTPException(status_code=500, detail="Analytics authentication not configured")
    if x_analytics_key != expected_key:
        raise HTTPException(status_code=403, detail="Invalid Analytics API Key")
    return x_analytics_key

router = APIRouter(
    prefix="/analytics",
    tags=["analytics"],
    dependencies=[Depends(verify_analytics_key)]
)

@router.get("/overview")
async def get_overview(days: int = 7) -> dict[str, Any]:
    """Get high-level summary of search volume and performance."""
    db = get_db()
    
    # Calculate cutoff
    cutoff_date = datetime.utcnow() - timedelta(days=days)
    
    try:
        # Example overview logic
        res = db.table("search_analytics").select("id", count="exact").gte("timestamp", cutoff_date.isoformat()).execute()
        total_searches = res.count if res else 0
        
        # Zero results
        zero_res = db.table("search_analytics").select("id", count="exact").gte("timestamp", cutoff_date.isoformat()).eq("zero_results", True).execute()
        zero_count = zero_res.count if zero_res else 0
        
        return {
            "time_period_days": days,
            "total_searches": total_searches,
            "zero_results_count": zero_count,
            "zero_results_percentage": round((zero_count / total_searches * 100), 2) if total_searches > 0 else 0,
        }
    except Exception as e:
        log.error("analytics_error", error=str(e), endpoint="overview")
        raise HTTPException(status_code=500, detail="Failed to retrieve analytics overview")

@router.get("/gaps")
async def get_gaps(days: int = 30) -> dict[str, Any]:
    """Analyze searches that returned zero results (supply gaps)."""
    db = get_db()
    cutoff_date = datetime.utcnow() - timedelta(days=days)
    try:
        res = db.table("search_analytics").select("*").gte("timestamp", cutoff_date.isoformat()).eq("zero_results", True).execute()
        return {"time_period_days": days, "gaps_found": len(res.data) if res and res.data else 0, "details": res.data if res else []}
    except Exception as e:
        log.error("analytics_error", error=str(e), endpoint="gaps")
        raise HTTPException(status_code=500, detail="Failed to retrieve analytics gaps")

@router.get("/trends")
async def get_trends(days: int = 7) -> dict[str, Any]:
    """Analyze high-demand destination countries or subjects."""
    db = get_db()
    cutoff_date = datetime.utcnow() - timedelta(days=days)
    try:
        res = db.table("search_analytics").select("destination_country, subject").gte("timestamp", cutoff_date.isoformat()).execute()
        # Aggregation can be done in memory
        destinations = {}
        for r in (res.data or []):
            dest = r.get("destination_country")
            if dest:
                destinations[dest] = destinations.get(dest, 0) + 1
        
        return {"time_period_days": days, "top_destinations": destinations}
    except Exception as e:
        log.error("analytics_error", error=str(e), endpoint="trends")
        raise HTTPException(status_code=500, detail="Failed to retrieve analytics trends")

@router.get("/nationality/{nationality}")
async def get_nationality_stats(nationality: str, days: int = 30) -> dict[str, Any]:
    """Get Deep-dive into student profiles from a specific nationality."""
    db = get_db()
    cutoff_date = datetime.utcnow() - timedelta(days=days)
    try:
        res = db.table("search_analytics").select("*").eq("nationality", nationality).gte("timestamp", cutoff_date.isoformat()).execute()
        return {"nationality": nationality, "total_searches": len(res.data) if res and res.data else 0, "details": res.data if res else []}
    except Exception as e:
        log.error("analytics_error", error=str(e), endpoint="nationality")
        raise HTTPException(status_code=500, detail="Failed to retrieve nationality stats")
