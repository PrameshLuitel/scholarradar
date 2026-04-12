"""
IDP Course Scraper — FAST concurrent version.

Scrapes the live idp.com course search using concurrent processing.
Covers all countries × study levels, paginates every page, validates
with Pydantic, and optionally upserts to Supabase.

Speed optimizations:
  - 5 concurrent country/level combos (via asyncio.Semaphore)
  - Page batches of 3 via asyncio.gather
  - 0.5s rate limit (down from 2s)
  - Early total-page detection from pagination HTML

Features:
  - Checkpoint/resume: saves progress to a JSON file, resumes on crash
  - Progress logging with percentage and ETA
  - Handles "Contact for fees" → null, "No IELTS required" → 0.0
  - Returns list of Course objects for JSON saving
"""

import asyncio
import json
import os
import re
import time
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Dict, Any, Tuple
from urllib.parse import urljoin

from bs4 import BeautifulSoup
import structlog

from src.scrapers.base_scraper import BaseScraper
from src.database.models import Course

# Lazy DB imports (supabase may not be installed in test env)
_upsert_course = None
_bulk_upsert_course = None


def _get_upsert_fn():
    global _upsert_course
    if _upsert_course is None:
        from src.database.queries import upsert_course
        _upsert_course = upsert_course
    return _upsert_course


def _get_bulk_upsert_fn():
    global _bulk_upsert_course
    if _bulk_upsert_course is None:
        from src.database.queries import bulk_upsert_courses
        _bulk_upsert_course = bulk_upsert_courses
    return _bulk_upsert_course


log = structlog.get_logger().bind(scraper="IDPCourseScraper")

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
BASE_URL = "https://www.idp.com"
LOCALE = "nepal"

COUNTRIES = {
    "australia": "australia",
    "uk": "united-kingdom",
    "canada": "canada",
    "usa": "united-states",
    "ireland": "ireland",
    "new-zealand": "new-zealand",
}

STUDY_LEVELS = [
    "undergraduate",
    "postgraduate",
    "doctorate",
]

LEVEL_MAP = {
    "undergraduate": "undergraduate",
    "postgraduate": "postgraduate",
    "doctorate": "doctorate",
}

CARDS_PER_PAGE = 12
CHECKPOINT_FILE = ".course_scraper_checkpoint.json"

# Concurrency settings
MAX_CONCURRENT_COMBOS = 5   # Number of country/level combos to scrape at once
PAGE_BATCH_SIZE = 2          # Pages to fetch concurrently within a combo
RATE_LIMIT_INTERVAL = 0.5    # Seconds between requests (down from 0.5)


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------
def _clean(text: Optional[str]) -> Optional[str]:
    if not text:
        return None
    cleaned = " ".join(text.split())
    return cleaned if cleaned else None


def _parse_tuition(text: str) -> Dict[str, Any]:
    result: Dict[str, Any] = {"tuition_fee": None, "currency": None}
    if not text:
        return result
    text = text.strip()
    if "contact" in text.lower():
        return result
    match = re.match(r"([A-Z]{3})\s*([\d,]+)", text)
    if match:
        result["currency"] = match.group(1)
        result["tuition_fee"] = float(match.group(2).replace(",", ""))
        return result
    cur_match = re.search(r"(AUD|USD|GBP|EUR|CAD|NZD|£|\$|€)", text, re.IGNORECASE)
    nums = re.findall(r"[\d,]+\.?\d*", text)
    if cur_match and nums:
        symbol_map = {"£": "GBP", "$": "USD", "€": "EUR"}
        raw = cur_match.group(1)
        result["currency"] = symbol_map.get(raw, raw.upper())
        result["tuition_fee"] = float(nums[0].replace(",", ""))
    return result


def _parse_ielts(text: str) -> Optional[float]:
    if not text:
        return None
    text = text.strip()
    if "no ielts" in text.lower() or "not required" in text.lower():
        return 0.0
    match = re.search(r"IELTS\s*([\d.]+)", text, re.IGNORECASE)
    if match:
        return float(match.group(1))
    return None


def _parse_duration(text: str) -> Dict[str, Any]:
    result: Dict[str, Any] = {"duration_months": None}
    if not text:
        return result
    text = text.lower().strip()
    total = 0
    year_match = re.search(r"(\d+(?:\.\d+)?)\s*(?:-\s*\d+(?:\.\d+)?\s*)?year", text)
    if year_match:
        total += int(float(year_match.group(1)) * 12)
    month_match = re.search(r"(\d+)\s*month", text)
    if month_match:
        total += int(month_match.group(1))
    week_match = re.search(r"(\d+)\s*week", text)
    if week_match:
        total += max(1, int(int(week_match.group(1)) / 4))
    result["duration_months"] = total if total > 0 else None
    return result


def _parse_intake_date(text: str) -> Optional[str]:
    if not text:
        return None
    text = re.sub(r"^Next intake:\s*", "", text, flags=re.IGNORECASE).strip()
    match = re.match(r"(\d{2})\.(\d{2})\.(\d{4})", text)
    if match:
        day, month, year = match.groups()
        return f"{year}-{month}-{day}"
    return text


def _parse_city_country(text: str) -> Tuple[Optional[str], Optional[str]]:
    if not text:
        return None, None
    parts = [p.strip() for p in text.split(",", 1)]
    if len(parts) == 2:
        return parts[0] or None, parts[1] or None
    return None, parts[0] or None


def _extract_total_pages(html: str) -> Optional[int]:
    """Extract total page count from pagination links in the HTML."""
    soup = BeautifulSoup(html, "html.parser")
    # Look for pagination links with page numbers
    max_page = 1
    for link in soup.find_all("a", href=True):
        href = link["href"]
        match = re.search(r"[?&]page=(\d+)", href)
        if match:
            page_num = int(match.group(1))
            if page_num > max_page:
                max_page = page_num
    return max_page if max_page > 1 else None


# ---------------------------------------------------------------------------
# Checkpoint manager
# ---------------------------------------------------------------------------
class CheckpointManager:
    """Saves/loads scrape progress so we can resume after crashes."""

    def __init__(self, filepath: str = CHECKPOINT_FILE):
        self.filepath = filepath
        self._data: Dict[str, Any] = {"completed": {}, "total_scraped": 0}
        self._lock = asyncio.Lock()
        self._load()

    def _load(self):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as f:
                self._data = json.load(f)
            log.info("checkpoint_loaded", completed=len(self._data.get("completed", {})))

    def save(self):
        with open(self.filepath, "w") as f:
            json.dump(self._data, f, indent=2)

    def is_done(self, combo_key: str) -> bool:
        return combo_key in self._data.get("completed", {})

    async def mark_done(self, combo_key: str, count: int):
        async with self._lock:
            self._data.setdefault("completed", {})[combo_key] = {
                "count": count,
                "timestamp": datetime.utcnow().isoformat(),
            }
            self._data["total_scraped"] = sum(
                v["count"] for v in self._data["completed"].values()
            )
            self.save()

    @property
    def total_scraped(self) -> int:
        return self._data.get("total_scraped", 0)

    @property
    def completed_combos(self) -> int:
        return len(self._data.get("completed", {}))

    def clear(self):
        self._data = {"completed": {}, "total_scraped": 0}
        if os.path.exists(self.filepath):
            os.remove(self.filepath)


# ---------------------------------------------------------------------------
# IDP Course Scraper — Concurrent
# ---------------------------------------------------------------------------
class IDPCourseScraper(BaseScraper):
    """
    Fast concurrent IDP course scraper.

    Scrapes all country × level combos concurrently using asyncio.Semaphore
    and batches page fetches for maximum throughput.
    """

    def __init__(
        self,
        save_to_db: bool = True,
        rate_limit_interval: float = RATE_LIMIT_INTERVAL,
        locale: str = LOCALE,
        checkpoint_file: str = CHECKPOINT_FILE,
        max_concurrent_combos: int = MAX_CONCURRENT_COMBOS,
        page_batch_size: int = PAGE_BATCH_SIZE,
    ):
        super().__init__(BASE_URL, rate_limit_interval=rate_limit_interval)
        self.save_to_db = save_to_db
        self.locale = locale
        self._checkpoint = CheckpointManager(checkpoint_file)
        self._combo_semaphore = asyncio.Semaphore(max_concurrent_combos)
        self._page_batch_size = page_batch_size
        self._all_courses: List[Course] = []
        self._courses_lock = asyncio.Lock()
        self._start_time: float = 0

    # -- public entry-point --------------------------------------------------

    async def scrape(self) -> List[Course]:
        """
        Scrape all country × level combos concurrently.
        Returns list of all Course objects scraped.
        """
        self._start_time = time.monotonic()
        combos = [
            (country_key, country_slug, level)
            for country_key, country_slug in COUNTRIES.items()
            for level in STUDY_LEVELS
        ]
        total_combos = len(combos)

        await log.ainfo(
            "scrape_start",
            total_combos=total_combos,
            max_concurrent=self._combo_semaphore._value,
            rate_limit=self._rate_limiter.interval,
        )

        # Launch all combos concurrently (semaphore limits parallelism)
        tasks = [
            self._scrape_combo_with_semaphore(
                country_key, country_slug, level, idx, total_combos
            )
            for idx, (country_key, country_slug, level) in enumerate(combos)
        ]
        await asyncio.gather(*tasks)

        elapsed = time.monotonic() - self._start_time
        await log.ainfo(
            "scrape_complete",
            total_courses=len(self._all_courses),
            elapsed_seconds=round(elapsed, 1),
            elapsed_minutes=round(elapsed / 60, 1),
        )

        await self.close()
        return self._all_courses

    # -- semaphore wrapper ---------------------------------------------------

    async def _scrape_combo_with_semaphore(
        self,
        country_key: str,
        country_slug: str,
        level: str,
        idx: int,
        total: int,
    ):
        combo_key = f"{country_slug}:{level}"
        pct = round((idx / total) * 100, 1)

        if self._checkpoint.is_done(combo_key):
            await log.ainfo("combo_skipped", combo=combo_key, progress=f"{pct}%")
            return

        async with self._combo_semaphore:
            await log.ainfo(
                "combo_start",
                combo=combo_key,
                progress=f"{pct}%",
                elapsed=f"{round(time.monotonic() - self._start_time, 0)}s",
            )

            combo_start = time.monotonic()
            courses = await self._scrape_combination(country_key, country_slug, level)

            if self.save_to_db and courses:
                try:
                    bulk_upsert_fn = _get_bulk_upsert_fn()
                    await bulk_upsert_fn(courses)
                except Exception as e:
                    await log.aerror("combo_bulk_upsert_failed", combo=combo_key, error=str(e))

            async with self._courses_lock:
                self._all_courses.extend(courses)

            await self._checkpoint.mark_done(combo_key, len(courses))
            combo_elapsed = time.monotonic() - combo_start

            await log.ainfo(
                "combo_complete",
                combo=combo_key,
                found=len(courses),
                total_so_far=len(self._all_courses),
                combo_seconds=round(combo_elapsed, 1),
                progress=f"{round(((idx + 1) / total) * 100, 1)}%",
            )

    # -- per combo (paginated with batching) ---------------------------------

    async def _scrape_combination(
        self, country_key: str, country_slug: str, level: str
    ) -> List[Course]:
        courses: List[Course] = []
        page = 1
        total_pages: Optional[int] = None

        while True:
            # Determine how many pages to fetch in this batch
            batch_end = page + self._page_batch_size
            if total_pages is not None:
                batch_end = min(batch_end, total_pages + 1)

            page_range = list(range(page, batch_end))
            if not page_range:
                break

            # Fetch pages concurrently
            urls = [self._build_url(country_slug, level, p) for p in page_range]
            fetch_tasks = [self.fetch(url) for url in urls]
            results = await asyncio.gather(*fetch_tasks)

            any_cards = False
            for p, html in zip(page_range, results):
                if html is None:
                    continue

                # Try to detect total pages from first page
                if total_pages is None and p == 1:
                    total_pages = _extract_total_pages(html)
                    if total_pages:
                        await log.ainfo(
                            "total_pages_detected",
                            combo=f"{country_slug}:{level}",
                            total_pages=total_pages,
                            estimated_courses=total_pages * CARDS_PER_PAGE,
                        )

                cards = self._parse_listing(html)
                if not cards:
                    continue

                any_cards = True
                for card_data in cards:
                    course = self._build_course(card_data, country_key, level)
                    if course is not None:
                        courses.append(course)

                # If this page had fewer cards than expected, it's the last page
                if len(cards) < CARDS_PER_PAGE:
                    return courses

            if not any_cards:
                break

            page = batch_end

            # Check if we've gone past total pages
            if total_pages is not None and page > total_pages:
                break

            # Log progress every 30 pages
            if page % 30 == 0:
                await log.ainfo(
                    "pagination_progress",
                    combo=f"{country_slug}:{level}",
                    page=page,
                    total_pages=total_pages or "unknown",
                    courses_so_far=len(courses),
                )

        return courses

    # -- URL builder ---------------------------------------------------------

    def _build_url(self, country_slug: str, level: str, page: int = 1) -> str:
        base = f"{BASE_URL}/{self.locale}/find-a-course/all-subject/{level}/{country_slug}/"
        if page > 1:
            return f"{base}?page={page}"
        return base

    # -- listing parser (JSON-based) ------------------------------------------

    def _parse_listing(self, html: str) -> List[Dict[str, Any]]:
        """Parse IDP course search results from Next.js __NEXT_DATA__."""
        soup = BeautifulSoup(html, "html.parser")
        script = soup.find("script", id="__NEXT_DATA__")
        if not script:
            return []

        try:
            data = json.loads(script.string)
            results = data.get("props", {}).get("pageProps", {}).get("courseSearchResult", [])
            return results if isinstance(results, list) else []
        except Exception as exc:
            log.error("json_parse_failed", error=str(exc))
            return []

    # -- build + validate with Pydantic --------------------------------------

    def _build_course(
        self,
        item: Dict[str, Any],
        country_key: str,
        level_slug: str,
    ) -> Optional[Course]:
        try:
            # Tuition
            tuition_fee = None
            raw_fee = item.get("total_fee")
            if raw_fee and str(raw_fee).isdigit():
                tuition_fee = float(raw_fee)

            # IELTS
            ielts_score = None
            raw_ielts = item.get("ielts_score")
            if raw_ielts:
                try:
                    ielts_score = float(raw_ielts)
                except ValueError:
                    pass

            # Duration
            duration_months = None
            dur = item.get("duration")
            unit = item.get("duration_unit", "").lower()
            if dur and str(dur).replace(".", "").isdigit():
                if "year" in unit:
                    duration_months = int(float(dur) * 12)
                elif "month" in unit:
                    duration_months = int(float(dur))

            # Intake Date
            start_dates = []
            raw_date = item.get("intake_date")
            if raw_date:
                match = re.match(r"(\d{2})\.(\d{2})\.(\d{4})", raw_date)
                if match:
                    day, month, year = match.groups()
                    start_dates.append(f"{year}-{month}-{day}")

            # URLs
            detail_slug = item.get("url_slug", {}).get("detail_page_slug", "")
            apply_url = urljoin(BASE_URL, detail_slug) if detail_slug else None

            # Normalized level
            study_level = LEVEL_MAP.get(level_slug, level_slug)

            return Course(
                name=item["course_name"],
                university=item.get("institution_name", {}).get("key") or "Unknown",
                country=country_key,
                city=item.get("nearest_city"),
                level=study_level,
                duration_months=duration_months,
                tuition_fee=tuition_fee,
                currency=item.get("currency"),
                ielts_overall=ielts_score,
                start_dates=start_dates,
                apply_url=apply_url,
                source_url=apply_url,
                is_active=True,
                last_verified=datetime.utcnow(),
            )
        except Exception as exc:
            log.error(
                "pydantic_validation_failed",
                name=item.get("course_name"),
                error=str(exc),
            )
            return None
