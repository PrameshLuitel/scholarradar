"""
ScholarRadar — Full overnight scrape runner.

Saves ALL scraped data to local JSON files in scraped_data/ folder.
Resume-capable: if it crashes, re-run and it skips completed scrapers.

Usage:
    cd /Users/prameshluitel/Documents/ScholarRadar
    PYTHONPATH=. nohup python run_all_scrapers.py > scrape_log.txt 2>&1 &
"""

import asyncio
import json
import os
import sys
import time
from datetime import datetime

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "scraped_data")
PROGRESS_FILE = os.path.join(OUTPUT_DIR, ".progress.json")


def ensure_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE) as f:
            return json.load(f)
    return {"completed": [], "started_at": None}


def save_progress(progress):
    progress["last_run"] = datetime.utcnow().isoformat()
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)


def mark_done(progress, name, count, elapsed):
    progress["completed"].append({
        "scraper": name,
        "count": count,
        "elapsed_seconds": round(elapsed, 1),
        "finished_at": datetime.utcnow().isoformat(),
    })
    save_progress(progress)


def is_done(progress, name):
    return any(s["scraper"] == name for s in progress.get("completed", []))


def save_json(filename, records):
    """Save a list of Pydantic models to a JSON file."""
    path = os.path.join(OUTPUT_DIR, filename)
    data = []
    for r in records:
        if hasattr(r, "model_dump"):
            d = r.model_dump(exclude_none=True)
            # Convert non-serializable types
            for k, v in d.items():
                if isinstance(v, datetime):
                    d[k] = v.isoformat()
                elif not isinstance(v, (str, int, float, bool, list, dict, type(None))):
                    d[k] = str(v)
            data.append(d)
        elif isinstance(r, dict):
            # Also handle dicts with datetimes
            d_copy = r.copy()
            for k, v in d_copy.items():
                if isinstance(v, datetime):
                    d_copy[k] = v.isoformat()
            data.append(d_copy)
    with open(path, "w") as f:
        json.dump(data, f, indent=2, default=str)
    size_mb = os.path.getsize(path) / (1024 * 1024)
    print(f"   💾 Saved {len(data)} records → {path} ({size_mb:.1f} MB)")


# ---------------------------------------------------------------------------
# Scraper runners
# ---------------------------------------------------------------------------
async def run_govt_scholarships(progress):
    name = "govt_scholarships"
    if is_done(progress, name):
        print(f"✅ {name} — already done, skipping")
        return
    print(f"\n{'='*60}")
    print(f"🔄 Government Scholarships (~5 sec)")
    print(f"{'='*60}")
    t = time.time()
    from src.scrapers.govt_scholarships import StudyAustraliaScholarshipScraper
    s = StudyAustraliaScholarshipScraper(save_to_db=False)
    results = await s.scrape()
    elapsed = time.time() - t
    save_json("govt_scholarships.json", results)
    print(f"✅ Done: {len(results)} records in {elapsed:.1f} sec")
    mark_done(progress, name, len(results), elapsed)


async def run_visa(progress):
    name = "visa_requirements"
    if is_done(progress, name):
        print(f"✅ {name} — already done, skipping")
        return
    print(f"\n{'='*60}")
    print(f"🔄 Visa Requirements (60 records, ~15 sec)")
    print(f"{'='*60}")
    t = time.time()
    from src.scrapers.idp_visa import IDPVisaScraper
    s = IDPVisaScraper(save_to_db=False)
    results = await s.scrape()
    elapsed = time.time() - t
    save_json("visa_requirements.json", results)
    print(f"✅ Done: {len(results)} records in {elapsed:.1f} sec")
    mark_done(progress, name, len(results), elapsed)


async def run_cost_of_living(progress):
    name = "cost_of_living"
    if is_done(progress, name):
        print(f"✅ {name} — already done, skipping")
        return
    print(f"\n{'='*60}")
    print(f"🔄 Cost of Living (23 cities, ~1.5 min)")
    print(f"{'='*60}")
    t = time.time()
    from src.scrapers.idp_cost_of_living import CostOfLivingScraper
    s = CostOfLivingScraper(save_to_db=False)
    results = await s.scrape()
    elapsed = time.time() - t
    save_json("cost_of_living.json", results)
    print(f"✅ Done: {len(results)} records in {elapsed:.1f} sec")
    mark_done(progress, name, len(results), elapsed)


async def run_universities(progress):
    name = "universities"
    if is_done(progress, name):
        print(f"✅ {name} — already done, skipping")
        return
    print(f"\n{'='*60}")
    print(f"🔄 IDP Universities (~1,185 records, ~40 min)")
    print(f"{'='*60}")
    t = time.time()
    from src.scrapers.idp_universities import IDPUniversityScraper
    s = IDPUniversityScraper(save_to_db=False)
    results = await s.scrape()
    elapsed = time.time() - t
    save_json("universities.json", results)
    print(f"✅ Done: {len(results)} records in {elapsed/60:.1f} min")
    mark_done(progress, name, len(results), elapsed)


async def run_scholarships(progress):
    name = "idp_scholarships"
    if is_done(progress, name):
        print(f"✅ {name} — already done, skipping")
        return
    print(f"\n{'='*60}")
    print(f"🔄 IDP Scholarships (~6,288 records, ~4-5 hours)")
    print(f"{'='*60}")
    t = time.time()
    from src.scrapers.idp_scholarships import IDPScholarshipScraper
    s = IDPScholarshipScraper(save_to_db=False)
    results = await s.scrape()
    elapsed = time.time() - t
    save_json("idp_scholarships.json", results)
    print(f"✅ Done: {len(results)} records in {elapsed/3600:.1f} hours")
    mark_done(progress, name, len(results), elapsed)


async def run_phd_seeker(progress):
    name = "phd_seeker"
    if is_done(progress, name):
        print(f"✅ {name} — already done, skipping")
        return
    print(f"\n{'='*60}")
    print(f"🔄 PhD-Seeker Scholarships (~500-1000 records, ~5-10 min)")
    print(f"{'='*60}")
    t = time.time()
    from src.scrapers.phd_seeker_scraper import PhDSeekerScraper
    s = PhDSeekerScraper()
    results = s.scrape()
    elapsed = time.time() - t
    save_json("phd_seeker.json", results)
    print(f"✅ Done: {len(results)} records in {elapsed/60:.1f} min")
    mark_done(progress, name, len(results), elapsed)


async def run_courses(progress):
    name = "idp_courses"
    if is_done(progress, name):
        print(f"✅ {name} — already done, skipping")
        return
    print(f"\n{'='*60}")
    print(f"🔄 IDP Courses (~50,000+ records, ~20-40 min with concurrency)")
    print(f"   5 concurrent combos × 3 page batches, 0.5s rate limit")
    print(f"   Has internal checkpoint — resumes if crashed")
    print(f"{'='*60}")
    t = time.time()
    from src.scrapers.idp_courses import IDPCourseScraper
    s = IDPCourseScraper(save_to_db=False)
    courses = await s.scrape()
    elapsed = time.time() - t
    count = len(courses) if isinstance(courses, list) else 0
    save_json("idp_courses.json", courses if isinstance(courses, list) else [])
    print(f"✅ Done: {count:,} records in {elapsed/60:.1f} min")
    mark_done(progress, name, count, elapsed)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
async def main():
    ensure_output_dir()
    progress = load_progress()

    if not progress.get("started_at"):
        progress["started_at"] = datetime.utcnow().isoformat()
        save_progress(progress)

    completed_list = progress.get("completed", [])
    done_count = len(completed_list) if isinstance(completed_list, list) else 0
    total_scrapers = 7

    print(f"🚀 ScholarRadar Full Scrape")
    print(f"   Output: {OUTPUT_DIR}/")
    print(f"   Progress: {done_count}/{total_scrapers} scrapers done")
    print(f"   Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"   💡 Crash? Just re-run to resume from where it stopped\n")

    total_start = time.time()

    # Fast scrapers first, heavy ones last
    scrapers = [
        ("Government Scholarships", run_govt_scholarships),
        ("Visa Requirements", run_visa),
        ("Cost of Living", run_cost_of_living),
        ("PhD-Seeker Scholarships", run_phd_seeker),
        ("IDP Universities", run_universities),
        ("IDP Scholarships", run_scholarships),
        ("IDP Courses", run_courses),
    ]

    for label, func in scrapers:
        try:
            await func(progress)
        except Exception as e:
            print(f"\n❌ CRITICAL ERROR in {label}: {str(e)}")
            import traceback
            traceback.print_exc()
            print(f"⏩ Skipping {label} and continuing with next...\n")

    total_elapsed = time.time() - total_start

    print(f"\n{'='*60}")
    print(f"🎉 ALL SCRAPERS COMPLETE!")
    print(f"⏱️  Total: {total_elapsed/3600:.1f} hours")
    print(f"{'='*60}")

    # Summary
    print(f"\n📊 Summary:")
    total_records = 0
    completed = progress.get("completed")
    if isinstance(completed, list):
        for s in completed:
            if not isinstance(s, dict):
                continue
            count = s.get("count", 0)
            total_records += count
            t = s.get("elapsed_seconds", 0)
            label = f"{t/3600:.1f} hrs" if t > 3600 else f"{t/60:.1f} min" if t > 60 else f"{t:.0f} sec"
            print(f"  {s.get('scraper')}: {count:,} records ({label})")
    print(f"\n  TOTAL: {total_records:,} records")

    # Show file sizes
    print(f"\n📁 Files in {OUTPUT_DIR}/:")
    for f in sorted(os.listdir(OUTPUT_DIR)):
        if f.endswith(".json") and not f.startswith("."):
            path = os.path.join(OUTPUT_DIR, f)
            size_mb = os.path.getsize(path) / (1024 * 1024)
            print(f"  {f}: {size_mb:.1f} MB")


if __name__ == "__main__":
    asyncio.run(main())
