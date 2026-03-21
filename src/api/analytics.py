import os
from collections import Counter
from datetime import datetime, timedelta
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, Header
from structlog import get_logger

from src.database.client import get_db

log = get_logger()

async def verify_analytics_key(x_analytics_key: str = Header(None)):
    expected_key = os.getenv("ANALYTICS_API_KEY")
    if not expected_key:
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
async def get_overview() -> dict[str, Any]:
    db = get_db()
    now = datetime.utcnow()
    
    try:
        # Get counts for today, week, month
        # In a high volume production app, we would use raw SQL RPCs for these standard aggregations.
        # But for Supabase REST we can pull counts via exact count.
        today_iso = (now - timedelta(days=1)).isoformat()
        week_iso = (now - timedelta(days=7)).isoformat()
        month_iso = (now - timedelta(days=30)).isoformat()

        today_res = db.table("tool_call_logs").select("id", count="exact").gte("called_at", today_iso).execute()
        week_res = db.table("tool_call_logs").select("id", count="exact").gte("called_at", week_iso).execute()
        month_res = db.table("tool_call_logs").select("id", count="exact").gte("called_at", month_iso).execute()

        total_today = today_res.count if today_res else 0
        total_week = week_res.count if week_res else 0
        total_month = month_res.count if month_res else 0

        # We need historical data for tops, let's fetch last 1000 rows to aggregate in-memory
        recent = db.table("tool_call_logs").select("*").order("called_at", desc=True).limit(2000).execute()
        rows = recent.data if recent and recent.data else []

        nats = Counter([r.get("nationality") for r in rows if r.get("nationality")])
        dests = Counter([r.get("destination_country") for r in rows if r.get("destination_country")])
        subjects = Counter([r.get("subject") for r in rows if r.get("subject")])
        
        # zero result rate
        zero_results_count = sum(1 for r in rows if r.get("zero_results") is True)
        zero_result_rate = round((zero_results_count / len(rows) * 100), 2) if len(rows) > 0 else 0

        # busiest hour (aggregate by hour from called_at)
        hours = Counter()
        for r in rows:
            called_at_str = r.get("called_at")
            if called_at_str:
                # Naive parsing
                try:
                    dt = datetime.fromisoformat(called_at_str.replace('Z', '+00:00'))
                    hours[dt.hour] += 1
                except ValueError:
                    pass
        
        busiest_hour = hours.most_common(1)[0][0] if hours else None

        return {
            "total_calls": {
                "today": total_today,
                "week": total_week,
                "month": total_month
            },
            "top_nationalities": [dict(zip(["name", "count"], item)) for item in nats.most_common(5)],
            "top_destinations": [dict(zip(["name", "count"], item)) for item in dests.most_common(5)],
            "top_subjects": [dict(zip(["name", "count"], item)) for item in subjects.most_common(5)],
            "zero_result_rate_percentage": zero_result_rate,
            "busiest_hour_utc": busiest_hour
        }
    except Exception as e:
        log.error("analytics_overview_error", error=str(e))
        raise HTTPException(status_code=500, detail="Failed to load overview.")

@router.get("/gaps")
async def get_gaps() -> dict[str, Any]:
    db = get_db()
    try:
        # Fetch last 1000 zero-result searches
        res = db.table("tool_call_logs").select("*").eq("zero_results", True).order("called_at", desc=True).limit(2000).execute()
        rows = res.data if res and res.data else []
        
        # Group by nationality + country + subject
        gaps = Counter()
        for r in rows:
            nat = r.get("nationality") or "Any"
            dest = r.get("destination_country") or "Any"
            subj = r.get("subject") or "Any"
            # Ignore searches that were entirely empty params
            if nat == "Any" and dest == "Any" and subj == "Any":
                continue
            
            key = f"{nat} | {dest} | {subj}"
            gaps[key] += 1
            
        sorted_gaps = [{"combo": k, "frequency": v} for k, v in gaps.most_common()]
        
        return {
            "total_gap_searches_analyzed": len(rows),
            "unfilled_requirements": sorted_gaps
        }
    except Exception as e:
        log.error("analytics_gaps_error", error=str(e))
        raise HTTPException(status_code=500, detail="Failed to load gaps.")

@router.get("/realtime")
async def get_realtime() -> dict[str, Any]:
    db = get_db()
    try:
        res = db.table("tool_call_logs").select("*").order("called_at", desc=True).limit(50).execute()
        return {
            "latest_calls": res.data if res and res.data else []
        }
    except Exception as e:
        log.error("analytics_realtime_error", error=str(e))
        raise HTTPException(status_code=500, detail="Failed to load realtime stats.")
