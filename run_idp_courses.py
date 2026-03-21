"""
Fast IDP Course Scraper runner.

Scrapes all courses concurrently and saves to scraped_data/idp_courses.json.

Usage:
    cd /Users/prameshluitel/Documents/ScholarRadar
    PYTHONPATH=. python run_idp_courses.py
"""

import asyncio
import json
import os
import time
from datetime import datetime

from src.scrapers.idp_courses import IDPCourseScraper

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "scraped_data")


def save_courses_json(courses, filepath):
    """Save Course models to a JSON file."""
    data = []
    for c in courses:
        d = c.model_dump(exclude_none=True)
        for k, v in d.items():
            if isinstance(v, datetime):
                d[k] = v.isoformat()
            elif not isinstance(v, (str, int, float, bool, list, dict, type(None))):
                d[k] = str(v)
        data.append(d)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2, default=str)
    size_mb = os.path.getsize(filepath) / (1024 * 1024)
    print(f"💾 Saved {len(data)} courses → {filepath} ({size_mb:.1f} MB)")


async def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("🚀 IDP Fast Course Scraper")
    print(f"   Concurrency: 5 combos × 3 pages = 15 concurrent requests max")
    print(f"   Rate limit: 0.5s per request")
    print(f"   Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    start = time.time()

    scraper = IDPCourseScraper(save_to_db=False, rate_limit_interval=0.5)
    try:
        courses = await scraper.scrape()
    except Exception as e:
        print(f"\n❌ Scraper failed: {e}")
        import traceback
        traceback.print_exc()
        return
    finally:
        await scraper.close()

    elapsed = time.time() - start

    # Save to JSON
    output_path = os.path.join(OUTPUT_DIR, "idp_courses.json")
    save_courses_json(courses, output_path)

    # Summary
    print(f"\n{'='*60}")
    print(f"✅ SCRAPE COMPLETE")
    print(f"   Total courses: {len(courses):,}")
    if elapsed > 3600:
        print(f"   Elapsed: {elapsed/3600:.1f} hours")
    elif elapsed > 60:
        print(f"   Elapsed: {elapsed/60:.1f} minutes")
    else:
        print(f"   Elapsed: {elapsed:.0f} seconds")
    print(f"   Rate: {len(courses)/max(elapsed,1):.0f} courses/second")
    print(f"{'='*60}")


if __name__ == "__main__":
    asyncio.run(main())
