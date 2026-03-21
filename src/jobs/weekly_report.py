import asyncio
import os
from datetime import datetime, timedelta
from typing import Any, Dict

import httpx
from structlog import get_logger

from src.database.client import get_db

log = get_logger("jobs.weekly_report")

async def generate_weekly_report_data() -> Dict[str, Any]:
    """Gather metrics from the past 7 days."""
    db = get_db()
    cutoff_date = datetime.utcnow() - timedelta(days=7)
    cutoff_iso = cutoff_date.isoformat()
    
    try:
        # 1. Total Searches
        res_total = db.table("search_analytics").select("id", count="exact").gte("timestamp", cutoff_iso).execute()
        total_searches = res_total.count if res_total else 0

        # 2. Gap Searches (Zero results)
        res_zero = db.table("search_analytics").select("id", count="exact").gte("timestamp", cutoff_iso).eq("zero_results", True).execute()
        zero_results_count = res_zero.count if res_zero else 0

        # 3. Most common destinations (simple aggregation)
        res_trends = db.table("search_analytics").select("destination_country, subject").gte("timestamp", cutoff_iso).execute()
        destinations = {}
        subjects = {}
        for r in (res_trends.data or []):
            dest = r.get("destination_country")
            if dest:
                destinations[dest] = destinations.get(dest, 0) + 1
            subj = r.get("subject")
            if subj:
                subjects[subj] = subjects.get(subj, 0) + 1
        
        # Sort and take top 5
        top_destinations = dict(sorted(destinations.items(), key=lambda item: item[1], reverse=True)[:5])
        top_subjects = dict(sorted(subjects.items(), key=lambda item: item[1], reverse=True)[:5])

        return {
            "report_period": "last_7_days",
            "generated_at": datetime.utcnow().isoformat(),
            "total_searches": total_searches,
            "zero_results_count": zero_results_count,
            "top_destinations": top_destinations,
            "top_subjects": top_subjects,
        }
    except Exception as e:
        log.error("weekly_report_generation_error", error=str(e))
        return {"error": "Failed to generate report"}

async def send_report_to_webhook(data: Dict[str, Any]):
    """Send the generated JSON to the configured webhook."""
    webhook_url = os.getenv("IDP_REPORT_WEBHOOK")
    if not webhook_url:
        log.warning("weekly_report_skipped", reason="IDP_REPORT_WEBHOOK not configured")
        return

    try:
        async with httpx.AsyncClient() as client:
            res = await client.post(webhook_url, json=data, timeout=10.0)
            res.raise_for_status()
            log.info("weekly_report_sent", status=res.status_code)
    except Exception as e:
        log.error("weekly_report_delivery_error", error=str(e))

async def run_weekly_report():
    """Manual trigger for the weekly report."""
    log.info("triggering_weekly_report")
    data = await generate_weekly_report_data()
    await send_report_to_webhook(data)

async def scheduler_loop():
    """Background task to run every Monday at 9AM UTC."""
    log.info("scheduler_loop_started")
    while True:
        now = datetime.utcnow()
        # Check if it's Monday (weekday == 0) and hour is 9
        if now.weekday() == 0 and now.hour == 9:
            log.info("scheduler_running_weekly_report", time=now.isoformat())
            await run_weekly_report()
            # Sleep for exactly 1 hour to avoid running multiple times in the 9AM block
            await asyncio.sleep(3600)
        else:
            # Check every minute
            await asyncio.sleep(60)

def start_scheduler():
    """Launch the background loop (fire and forget)."""
    asyncio.create_task(scheduler_loop())
