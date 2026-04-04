"""
ScholarRadar Production Scheduler — daily live scraper and maintenance jobs.

Runs as a separate worker process alongside the MCP server.
Start: python -m src.scheduler.jobs

Jobs:
  1. scrape_all_databases   — every 24 hours from deploy/startup
  2. verify_urls            — every 24 hours
  3. health_report          — every 6 hours
  4. scholarship_alert      — every 12 hours
"""
from __future__ import annotations

import asyncio
import os
import random
import signal
import sys
import time
from datetime import datetime, timedelta, timezone
from typing import Any

import httpx
import structlog
from apscheduler.schedulers.asyncio import AsyncIOScheduler

log = structlog.get_logger("scheduler")

# ── Config ──────────────────────────────────────────────────────────────────

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")
URL_VERIFY_SAMPLE_SIZE = int(os.getenv("URL_VERIFY_SAMPLE", "100"))
HEALTH_DROP_THRESHOLD = float(os.getenv("HEALTH_DROP_PCT", "0.10"))  # 10%

# Track previous health counts for anomaly detection
_prev_health: dict[str, int] = {}


# ── Helpers ─────────────────────────────────────────────────────────────────

def _get_db():
    from src.database.client import get_db
    return get_db()


async def _post_slack(text: str, blocks: list[dict] | None = None):
    """Post a message to Slack webhook. No-op if webhook not configured."""
    if not SLACK_WEBHOOK_URL:
        log.info("slack_skip", reason="SLACK_WEBHOOK_URL not set", text=text)
        return
    try:
        payload: dict[str, Any] = {"text": text}
        if blocks:
            payload["blocks"] = blocks
        async with httpx.AsyncClient(timeout=10) as client:
            resp = await client.post(SLACK_WEBHOOK_URL, json=payload)
            log.info("slack_posted", status=resp.status_code, text=text[:80])
    except Exception as e:
        log.error("slack_error", error=str(e))


async def _run_async_scraper(scraper_name: str, scraper, clear_checkpoint: bool = False) -> int:
    """Run an async scraper and return the count of scraped items."""
    if clear_checkpoint and hasattr(scraper, "_checkpoint"):
        try:
            scraper._checkpoint.clear()
            log.info("checkpoint_cleared", scraper=scraper_name)
        except Exception as exc:
            log.warning("checkpoint_clear_failed", scraper=scraper_name, error=str(exc))

    try:
        items = await scraper.scrape()
        count = len(items) if isinstance(items, list) else 0
        log.info("scraper_complete", scraper=scraper_name, count=count)
        return count
    except Exception as e:
        log.error("scraper_failed", scraper=scraper_name, error=str(e))
        return 0
    finally:
        if hasattr(scraper, "close"):
            try:
                await scraper.close()
            except Exception:
                pass


async def _run_sync_scraper(scraper_name: str, fn, *args, **kwargs) -> int:
    """Run a synchronous scraper on a thread and return the final saved count."""
    try:
        result = await asyncio.to_thread(fn, *args, **kwargs)
        count = len(result) if isinstance(result, list) else 0
        log.info("sync_scraper_complete", scraper=scraper_name, count=count)
        return count
    except Exception as e:
        log.error("sync_scraper_failed", scraper=scraper_name, error=str(e))
        return 0


async def _save_phd_seeker_data(scraper) -> int:
    """Save PhD-Seeker output to Supabase."""
    try:
        positions = await asyncio.to_thread(scraper.scrape)
        if not positions:
            log.info("phd_seeker_no_positions")
            return 0
        saved = await asyncio.to_thread(scraper.save_to_database, positions)
        log.info("phd_seeker_saved", count=saved)
        return saved
    except Exception as e:
        log.error("phd_seeker_save_failed", error=str(e))
        return 0


# ════════════════════════════════════════════════════════════════════════════
# JOB 1: scrape_all_databases — every 24 hours from deploy/startup
# ════════════════════════════════════════════════════════════════════════════

async def scrape_all_databases():
    """Run the full live scraper once and keep Supabase updated."""
    job_start = time.time()
    log.info("job_start", job="scrape_all_databases")

    try:
        from src.scrapers.idp_scholarships import IDPScholarshipScraper
        from src.scrapers.idp_courses import IDPCourseScraper
        from src.scrapers.idp_universities import IDPUniversityScraper
        from src.scrapers.idp_visa import IDPVisaScraper
        from src.scrapers.idp_cost_of_living import CostOfLivingScraper
        from src.scrapers.govt_scholarships import StudyAustraliaScholarshipScraper
        from src.scrapers.phd_seeker_scraper import PhDSeekerScraper

        counts: dict[str, int] = {}

        scholarships_scraper = IDPScholarshipScraper(save_to_db=True)
        counts["idp_scholarships"] = await _run_async_scraper(
            "idp_scholarships", scholarships_scraper
        )

        courses_scraper = IDPCourseScraper(save_to_db=True)
        counts["idp_courses"] = await _run_async_scraper(
            "idp_courses", courses_scraper, clear_checkpoint=True
        )

        universities_scraper = IDPUniversityScraper(save_to_db=True)
        counts["idp_universities"] = await _run_async_scraper(
            "idp_universities", universities_scraper
        )

        visa_scraper = IDPVisaScraper(save_to_db=True)
        counts["visa_requirements"] = await _run_async_scraper(
            "visa_requirements", visa_scraper
        )

        cost_scraper = CostOfLivingScraper(save_to_db=True)
        counts["cost_of_living"] = await _run_async_scraper(
            "cost_of_living", cost_scraper
        )

        govt_scraper = StudyAustraliaScholarshipScraper(save_to_db=True)
        counts["govt_scholarships"] = await _run_async_scraper(
            "govt_scholarships", govt_scraper
        )

        phd_scraper = PhDSeekerScraper()
        counts["phd_seeker"] = await _save_phd_seeker_data(phd_scraper)

        total = sum(counts.values())
        elapsed = round(time.time() - job_start, 1)
        log.info(
            "job_complete",
            job="scrape_all_databases",
            counts=counts,
            total=total,
            elapsed_seconds=elapsed,
        )

    except Exception as e:
        elapsed = round(time.time() - job_start, 1)
        log.error(
            "job_failed",
            job="scrape_all_databases",
            error=str(e),
            elapsed_seconds=elapsed,
        )


# ════════════════════════════════════════════════════════════════════════════
# Helper: scrape_courses
# ════════════════════════════════════════════════════════════════════

async def scrape_courses():
    """Run IDP course scraper."""
    job_start = time.time()
    log.info("job_start", job="scrape_courses")
    try:
        from src.scrapers.idp_courses import IDPCourseScraper

        scraper = IDPCourseScraper(save_to_db=True)
        results = await scraper.scrape()
        await scraper.close()

        scraped_count = len(results) if isinstance(results, list) else 0
        elapsed = round(time.time() - job_start, 1)
        log.info("job_complete", job="scrape_courses",
                 scraped=scraped_count, elapsed_seconds=elapsed)

    except Exception as e:
        elapsed = round(time.time() - job_start, 1)
        log.error("job_failed", job="scrape_courses",
                  error=str(e), elapsed_seconds=elapsed)


# ════════════════════════════════════════════════════════════════════════════
# Helper: scrape_universities
# ════════════════════════════════════════════════════════════════════════════

async def scrape_universities():
    """Run IDP university scraper."""
    job_start = time.time()
    log.info("job_start", job="scrape_universities")
    try:
        from src.scrapers.idp_universities import IDPUniversityScraper

        scraper = IDPUniversityScraper(save_to_db=True)
        results = await scraper.scrape()
        await scraper.close()

        scraped_count = len(results) if isinstance(results, list) else 0
        elapsed = round(time.time() - job_start, 1)
        log.info("job_complete", job="scrape_universities",
                 scraped=scraped_count, elapsed_seconds=elapsed)

    except Exception as e:
        elapsed = round(time.time() - job_start, 1)
        log.error("job_failed", job="scrape_universities",
                  error=str(e), elapsed_seconds=elapsed)


# ════════════════════════════════════════════════════════════════════════════
# JOB 4: verify_urls — every 24 hours
# ════════════════════════════════════════════════════════════════════════════

async def verify_urls():
    """Check random sample of scholarship apply_urls. Deactivate dead links."""
    job_start = time.time()
    log.info("job_start", job="verify_urls")
    try:
        db = _get_db()
        # Get all active scholarship URLs
        response = (
            db.table("scholarships")
            .select("id,apply_url,source_url")
            .eq("is_active", True)
            .execute()
        )
        all_rows = response.data or []
        urls_to_check = [
            r for r in all_rows
            if r.get("apply_url") and r["apply_url"].startswith("http")
        ]

        # Random sample
        sample = random.sample(urls_to_check, min(URL_VERIFY_SAMPLE_SIZE, len(urls_to_check)))
        log.info("verify_urls_sample", total=len(urls_to_check), sample_size=len(sample))

        dead_ids: list[str] = []
        checked = 0

        async with httpx.AsyncClient(
            timeout=15,
            follow_redirects=True,
            limits=httpx.Limits(max_connections=10),
        ) as client:
            for row in sample:
                url = row["apply_url"]
                try:
                    resp = await client.head(url, headers={
                        "User-Agent": "ScholarRadar-LinkChecker/1.0",
                    })
                    if resp.status_code >= 400:
                        dead_ids.append(row["id"])
                        log.warning("dead_link", url=url, status=resp.status_code)
                except Exception:
                    dead_ids.append(row["id"])
                    log.warning("dead_link_timeout", url=url)
                checked += 1
                # Don't hammer servers
                await asyncio.sleep(0.5)

        # Deactivate dead links
        if dead_ids:
            for dead_id in dead_ids:
                db.table("scholarships").update({"is_active": False}).eq("id", dead_id).execute()

        elapsed = round(time.time() - job_start, 1)
        log.info("job_complete", job="verify_urls",
                 checked=checked, dead=len(dead_ids),
                 elapsed_seconds=elapsed)

    except Exception as e:
        elapsed = round(time.time() - job_start, 1)
        log.error("job_failed", job="verify_urls",
                  error=str(e), elapsed_seconds=elapsed)


# ════════════════════════════════════════════════════════════════════════════
# JOB 5: health_report — every 6 hours
# ════════════════════════════════════════════════════════════════════════════

async def health_report():
    """Count active records, check freshness, alert on anomalies."""
    global _prev_health
    job_start = time.time()
    log.info("job_start", job="health_report")
    try:
        db = _get_db()

        tables = {
            "scholarships": {"filter": ("is_active", True)},
            "courses": {"filter": ("is_active", True)},
            "universities": {"filter": None},
            "visa_requirements": {"filter": None},
            "cost_of_living": {"filter": None},
        }

        counts: dict[str, int] = {}
        for table, cfg in tables.items():
            q = db.table(table).select("id", count="exact")
            if cfg["filter"]:
                col, val = cfg["filter"]
                q = q.eq(col, val)
            result = q.execute()
            counts[table] = result.count or 0

        # Data freshness — average age of scholarships
        recent = (
            db.table("scholarships")
            .select("updated_at")
            .eq("is_active", True)
            .order("updated_at", desc=True)
            .limit(100)
            .execute()
        )
        now = datetime.now(timezone.utc)
        ages_hours = []
        for row in (recent.data or []):
            if row.get("updated_at"):
                try:
                    updated = datetime.fromisoformat(str(row["updated_at"]).replace("Z", "+00:00"))
                    age = (now - updated).total_seconds() / 3600
                    ages_hours.append(age)
                except (ValueError, TypeError):
                    pass
        avg_age_hours = round(sum(ages_hours) / len(ages_hours), 1) if ages_hours else None

        # Anomaly detection — compare to previous run
        alerts: list[str] = []
        for table, count in counts.items():
            prev = _prev_health.get(table)
            if prev and prev > 0:
                drop_pct = (prev - count) / prev
                if drop_pct > HEALTH_DROP_THRESHOLD:
                    alerts.append(
                        f"⚠️ {table}: dropped from {prev:,} to {count:,} ({drop_pct:.0%} decrease)"
                    )
        _prev_health = counts.copy()

        # Log report
        log.info("health_report",
                 counts=counts,
                 avg_data_age_hours=avg_age_hours,
                 alerts=alerts or None)

        # Slack alert if anomalies
        if alerts:
            alert_text = (
                f"🚨 *ScholarRadar Data Anomaly Alert*\n"
                + "\n".join(alerts)
                + f"\n\n📊 Counts: {counts}"
            )
            await _post_slack(alert_text)

        elapsed = round(time.time() - job_start, 1)
        log.info("job_complete", job="health_report",
                 counts=counts, elapsed_seconds=elapsed)

    except Exception as e:
        elapsed = round(time.time() - job_start, 1)
        log.error("job_failed", job="health_report",
                  error=str(e), elapsed_seconds=elapsed)


# ════════════════════════════════════════════════════════════════════════════
# JOB 6: scholarship_alert — every 12 hours
# ════════════════════════════════════════════════════════════════════════════

async def scholarship_alert():
    """Find high-value scholarships added in the last 12 hours, post to Slack."""
    job_start = time.time()
    log.info("job_start", job="scholarship_alert")
    try:
        db = _get_db()
        cutoff = (datetime.now(timezone.utc) - timedelta(hours=12)).isoformat()

        # New high-value scholarships
        response = (
            db.table("scholarships").select("*")
            .eq("is_active", True)
            .gte("created_at", cutoff)
            .gte("award_value_max", 10000)
            .order("award_value_max", desc=True)
            .limit(20)
            .execute()
        )
        new_high = response.data or []

        if new_high:
            lines = [f"🎓 *{len(new_high)} new high-value scholarships added*\n"]
            for s in new_high[:10]:
                val = s.get("award_value_max") or 0
                lines.append(
                    f"• *{s.get('title', 'Unknown')}* at {s.get('university', 'Unknown')} — "
                    f"AUD {val:,.0f} ({s.get('funding_type', '')})"
                )
            if len(new_high) > 10:
                lines.append(f"_...and {len(new_high) - 10} more_")

            text = "\n".join(lines)
            await _post_slack(text)
            log.info("scholarship_alert_sent", count=len(new_high))
        else:
            log.info("scholarship_alert_none", message="No new high-value scholarships in last 12h")

        elapsed = round(time.time() - job_start, 1)
        log.info("job_complete", job="scholarship_alert",
                 new_scholarships=len(new_high), elapsed_seconds=elapsed)

    except Exception as e:
        elapsed = round(time.time() - job_start, 1)
        log.error("job_failed", job="scholarship_alert",
                  error=str(e), elapsed_seconds=elapsed)


# ════════════════════════════════════════════════════════════════════════════
# Main — scheduler entry point
# ════════════════════════════════════════════════════════════════════════════

async def main():
    """Start the APScheduler with the live daily scraper and support jobs."""

    scheduler = AsyncIOScheduler(timezone="UTC")

    # JOB 1: Scrape all configured databases once immediately, then every 24 hours.
    scheduler.add_job(
        scrape_all_databases,
        "interval",
        hours=24,
        next_run_time=datetime.now(timezone.utc),
        id="scrape_all_databases",
        name="Scrape All ScholarRadar Databases",
        max_instances=1,
        coalesce=True,
        misfire_grace_time=3600,
    )

    # JOB 2: URL verification — every 24 hours
    scheduler.add_job(
        verify_urls,
        "interval",
        hours=24,
        id="verify_urls",
        name="Verify Scholarship URLs",
        max_instances=1,
        coalesce=True,
    )

    # JOB 3: Health report — every 6 hours
    scheduler.add_job(
        health_report,
        "interval",
        hours=6,
        id="health_report",
        name="Data Health Report",
        max_instances=1,
        coalesce=True,
    )

    # JOB 4: Scholarship alerts — every 12 hours
    scheduler.add_job(
        scholarship_alert,
        "interval",
        hours=12,
        id="scholarship_alert",
        name="High-Value Scholarship Alert",
        max_instances=1,
        coalesce=True,
    )

    scheduler.start()
    log.info("scheduler_started", jobs=len(scheduler.get_jobs()))

    # Print job schedule
    for job in scheduler.get_jobs():
        log.info("job_scheduled", job_id=job.id, next_run=str(job.next_run_time))

    # Run health report immediately on startup
    await health_report()

    # Graceful shutdown
    loop = asyncio.get_event_loop()
    stop_event = asyncio.Event()

    def _shutdown(sig):
        log.info("scheduler_shutdown", signal=sig.name)
        scheduler.shutdown(wait=False)
        stop_event.set()

    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, lambda s=sig: _shutdown(s))

    log.info("scheduler_running", message="Waiting for jobs... Press Ctrl+C to stop.")
    await stop_event.wait()
    log.info("scheduler_stopped")


if __name__ == "__main__":
    asyncio.run(main())
