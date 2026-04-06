"""
IDP Scholarship Scraper — scrapes the live idp.com scholarship search.

Built from reverse-engineering the REAL idp.com HTML (March 2026).
Covers all countries × all study levels, paginates every page, visits
each detail page, validates with Pydantic, upserts to Supabase, and
deactivates stale records.
"""

import asyncio
import re
import time
from datetime import datetime, date
from typing import List, Optional, Dict, Any
from urllib.parse import urljoin, urlencode, urlparse

from bs4 import BeautifulSoup
import structlog

from src.scrapers.base_scraper import BaseScraper
from src.database.models import Scholarship

# Lazy imports — database queries require supabase which may not
# be installed in test environments.  Import at call site instead.
_upsert_scholarship = None
_deactivate_stale_scholarships = None


def _get_db_functions():
    global _upsert_scholarship, _deactivate_stale_scholarships
    if _upsert_scholarship is None:
        from src.database.queries import upsert_scholarship, deactivate_stale_scholarships
        _upsert_scholarship = upsert_scholarship
        _deactivate_stale_scholarships = deactivate_stale_scholarships
    return _upsert_scholarship, _deactivate_stale_scholarships

log = structlog.get_logger().bind(scraper="IDPScholarshipScraper")

# ---------------------------------------------------------------------------
# Real IDP site constants (reverse-engineered March 2026)
# ---------------------------------------------------------------------------
BASE_URL = "https://www.idp.com"

# IDP localises URLs based on visitor country.  We use /nepal/ as the locale
# prefix because it returns English content for all destinations.
# Change this if you need a different locale.
LOCALE = "nepal"

SEARCH_PATH = f"/{LOCALE}/find-a-scholarship/"

# Countries available in IDP's filter dropdown
COUNTRIES = [
    "australia",
    "uk",
    "canada",
    "usa",
    "ireland",
    "new-zealand",
]

# Study levels available in IDP's filter dropdown
STUDY_LEVELS = [
    "undergraduate",
    "postgraduate",
    "doctorate",
    "foundation",
    "pre-degree-vocational",
    "school",
]

# Map IDP filter slugs → our normalised DB values
LEVEL_MAP = {
    "undergraduate": "undergraduate",
    "postgraduate": "postgraduate",
    "doctorate": "doctorate",
    "foundation": "foundation",
    "pre-degree-vocational": "vocational",
    "school": "foundation",
}

# IDP shows 12 scholarship cards per page
CARDS_PER_PAGE = 12


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------
def _parse_award_value(text: str) -> Dict[str, Any]:
    """
    Parse real IDP award strings:
      'Value of award: 2000 EUR'
      'Value of award: 2000 to 5000 EUR'
      'Value of award: Up to AUD 40,000'
    """
    result: Dict[str, Any] = {
        "award_value_min": None,
        "award_value_max": None,
        "award_currency": None,
    }
    if not text:
        return result

    # Strip the label prefix
    text = re.sub(r"^Value of award:\s*", "", text, flags=re.IGNORECASE).strip()
    if not text:
        return result

    # Extract currency
    currency_match = re.search(
        r"(AUD|USD|GBP|EUR|CAD|NZD|INR|£|\$|€)", text, re.IGNORECASE
    )
    if currency_match:
        symbol_map = {"£": "GBP", "$": "USD", "€": "EUR"}
        raw = currency_match.group(1)
        result["award_currency"] = symbol_map.get(raw, raw.upper())

    # Extract numbers
    numbers = [float(n.replace(",", "")) for n in re.findall(r"[\d,]+\.?\d*", text)]

    if len(numbers) >= 2:
        result["award_value_min"] = min(numbers)
        result["award_value_max"] = max(numbers)
    elif len(numbers) == 1:
        if "up to" in text.lower():
            result["award_value_max"] = numbers[0]
        else:
            result["award_value_min"] = numbers[0]
            result["award_value_max"] = numbers[0]

    return result


def _parse_deadline(text: str) -> Optional[date]:
    """
    Parse real IDP deadline strings like 'Deadline:01 Apr 2026'.
    """
    if not text:
        return None
    # Strip label prefix
    text = re.sub(r"^Deadline:\s*", "", text, flags=re.IGNORECASE).strip()
    if not text:
        return None

    for fmt in ("%d %b %Y", "%d %B %Y", "%B %d, %Y", "%Y-%m-%d", "%d/%m/%Y"):
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            continue
    return None


def _parse_funding_type(text: str) -> Optional[str]:
    """
    Extract funding type from 'Funding type: Fee waiver/discount'.
    Maps to our enum values.
    """
    if not text:
        return None
    text = re.sub(r"^Funding type:\s*", "", text, flags=re.IGNORECASE).strip().lower()
    mapping = {
        "fee waiver/discount": "fee_waiver",
        "fee waiver": "fee_waiver",
        "full tuition": "full",
        "full": "full",
        "partial": "partial",
        "stipend": "stipend",
        "accommodation": "accommodation",
    }
    return mapping.get(text, text)


def _clean(text: Optional[str]) -> Optional[str]:
    if not text:
        return None
    cleaned = " ".join(text.split())
    return cleaned if cleaned else None


# ---------------------------------------------------------------------------
# IDP Scholarship Scraper
# ---------------------------------------------------------------------------
class IDPScholarshipScraper(BaseScraper):
    """
    Scrapes the live IDP scholarship search at idp.com.

    FAST concurrent version:
    - 8 country×level combos run concurrently via asyncio.Semaphore
    - 12 detail pages fetched concurrently per listing page via asyncio.gather
    - Checkpoint/resume: saves progress, skips completed combos on restart

    Real HTML structure (reverse-engineered March 2026):
    - Cards: div.interactive-card
    - Title: a.h4 (inside card)
    - University: p.text-small > a (inside card)
    - Metadata: ul > li > span.text-small (country, level, funding, deadline, award)
    - Pagination: a[href*="page="]
    - Detail page: 3 × div.faq-content (overview, eligibility, how to apply)
    """

    # Concurrency settings
    MAX_CONCURRENT_COMBOS = 8
    DETAIL_BATCH_SIZE = 12
    CHECKPOINT_FILE = ".scholarship_scraper_checkpoint.json"

    def __init__(
        self,
        save_to_db: bool = True,
        rate_limit_interval: float = 0.15,
        locale: str = LOCALE,
    ):
        super().__init__(BASE_URL, rate_limit_interval=rate_limit_interval)
        self.save_to_db = save_to_db
        self.locale = locale
        self._seen_ids: List[str] = []
        self._seen_ids_lock = asyncio.Lock()
        self._combo_semaphore = asyncio.Semaphore(self.MAX_CONCURRENT_COMBOS)
        self._all_scholarships: List[Scholarship] = []
        self._results_lock = asyncio.Lock()
        self._checkpoint = self._load_checkpoint()
        self._start_time: float = 0

    # -- checkpoint helpers --------------------------------------------------

    def _load_checkpoint(self) -> Dict[str, Any]:
        import json, os
        if os.path.exists(self.CHECKPOINT_FILE):
            with open(self.CHECKPOINT_FILE, "r") as f:
                data = json.load(f)
                log.info("checkpoint_loaded", completed=len(data.get("completed", {})))
                return data
        return {"completed": {}, "total_scraped": 0}

    def _save_checkpoint(self):
        import json
        with open(self.CHECKPOINT_FILE, "w") as f:
            json.dump(self._checkpoint, f, indent=2)

    def _is_combo_done(self, key: str) -> bool:
        return key in self._checkpoint.get("completed", {})

    def _mark_combo_done(self, key: str, count: int):
        self._checkpoint.setdefault("completed", {})[key] = {
            "count": count,
            "timestamp": datetime.utcnow().isoformat(),
        }
        self._checkpoint["total_scraped"] = sum(
            v["count"] for v in self._checkpoint["completed"].values()
        )
        self._save_checkpoint()

    def clear_checkpoint(self):
        import os
        self._checkpoint = {"completed": {}, "total_scraped": 0}
        if os.path.exists(self.CHECKPOINT_FILE):
            os.remove(self.CHECKPOINT_FILE)

    # -- public entry-point --------------------------------------------------

    async def scrape(self) -> List[Scholarship]:
        self._start_time = time.monotonic()
        combos = [
            (country, level)
            for country in COUNTRIES
            for level in STUDY_LEVELS
        ]
        total_combos = len(combos)

        await log.ainfo(
            "scrape_start",
            total_combos=total_combos,
            max_concurrent=self.MAX_CONCURRENT_COMBOS,
            rate_limit=self._rate_limiter.interval,
        )

        tasks = [
            self._scrape_combo_with_semaphore(country, level, idx, total_combos)
            for idx, (country, level) in enumerate(combos)
        ]
        await asyncio.gather(*tasks)

        if self.save_to_db and self._seen_ids:
            _, deactivate_fn = _get_db_functions()
            deactivated = await deactivate_fn("idp", self._seen_ids)
            await log.ainfo("stale_records_deactivated", count=deactivated)

        elapsed = time.monotonic() - self._start_time
        await log.ainfo(
            "scrape_complete",
            total=len(self._all_scholarships),
            elapsed_minutes=round(elapsed / 60, 1),
        )
        await self.close()

        # Clean up checkpoint on successful complete run
        self.clear_checkpoint()
        return self._all_scholarships

    # -- semaphore wrapper ---------------------------------------------------

    async def _scrape_combo_with_semaphore(
        self, country: str, level: str, idx: int, total: int
    ):
        combo_key = f"{country}:{level}"
        pct = round((idx / total) * 100, 1)

        if self._is_combo_done(combo_key):
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
            combo_results = await self._scrape_combination(country, level)

            async with self._results_lock:
                self._all_scholarships.extend(combo_results)

            self._mark_combo_done(combo_key, len(combo_results))
            combo_elapsed = time.monotonic() - combo_start

            await log.ainfo(
                "combo_complete",
                combo=combo_key,
                found=len(combo_results),
                total_so_far=len(self._all_scholarships),
                combo_seconds=round(combo_elapsed, 1),
                progress=f"{round(((idx + 1) / total) * 100, 1)}%",
            )

    # -- per combination (paginated) -----------------------------------------

    async def _scrape_combination(
        self, country: str, level: str
    ) -> List[Scholarship]:
        scholarships: List[Scholarship] = []
        page = 1

        while True:
            url = self._build_url(country, level, page)
            html = await self.fetch(url)
            if html is None:
                await log.awarning("page_fetch_failed", url=url, page=page)
                break

            cards = self._parse_listing(html)
            if not cards:
                break  # no more results

            # Batch-fetch all detail pages for this page's cards concurrently
            detail_tasks = [self._fetch_detail(card) for card in cards]
            details = await asyncio.gather(*detail_tasks)

            for card, detail in zip(cards, details):
                scholarship = self._build_scholarship(card, detail, country, level)
                if scholarship is None:
                    continue

                scholarships.append(scholarship)

                if self.save_to_db:
                    try:
                        upsert_fn, _ = _get_db_functions()
                        result = await upsert_fn(scholarship)
                        if result and result.get("id"):
                            async with self._seen_ids_lock:
                                self._seen_ids.append(result["id"])
                    except Exception:
                        pass  # already logged

            # If we got fewer than a full page, we've hit the last page
            if len(cards) < CARDS_PER_PAGE:
                break

            page += 1

        return scholarships

    # -- URL builder ---------------------------------------------------------

    def _build_url(self, country: str, level: str, page: int = 1) -> str:
        """
        Real IDP URL pattern:
        https://www.idp.com/nepal/find-a-scholarship/?country=australia&level=postgraduate&page=2
        """
        params: Dict[str, str] = {"country": country, "level": level}
        if page > 1:
            params["page"] = str(page)
        return f"{BASE_URL}/{self.locale}/find-a-scholarship/?{urlencode(params)}"

    # -- listing page parser (REAL selectors) --------------------------------

    @staticmethod
    def _parse_listing(html: str) -> List[Dict[str, Any]]:
        """
        Parse real IDP search results HTML.

        Real structure per card:
          div.interactive-card
            div > a.h4  → title + href
            p.text-small > a → university name
            ul > li > span.text-small → metadata lines:
              [0] country, [1] study_level, [2] funding_type,
              [3] deadline OR value, [4] value (if deadline present)
        """
        soup = BeautifulSoup(html, "html.parser")
        cards: List[Dict[str, Any]] = []

        for el in soup.select("div.interactive-card"):
            # Title — the <a> with class h4
            title_a = el.select_one("a.h4")
            if not title_a:
                continue
            title = _clean(title_a.get_text())
            if not title:
                continue
            detail_href = title_a.get("href", "")
            detail_url = urljoin(BASE_URL, detail_href) if detail_href else None

            # University — the <a> inside <p class="text-small">
            uni_el = el.select_one("p.text-small a")
            university = _clean(uni_el.get_text()) if uni_el else "Unknown"

            # Metadata lines — inside <ul> <li> <span class="text-small">
            meta_spans = el.select("ul li span.text-small")
            meta_texts = [_clean(s.get_text()) for s in meta_spans]

            # Parse metadata lines (order: country, level, funding, deadline, value)
            country_text = meta_texts[0] if len(meta_texts) > 0 else None
            level_text = meta_texts[1] if len(meta_texts) > 1 else None
            funding_text = None
            deadline_text = None
            award_text = None

            for mt in meta_texts[2:]:
                if mt is None:
                    continue
                mt_lower = mt.lower()
                if mt_lower.startswith("funding type"):
                    funding_text = mt
                elif mt_lower.startswith("deadline"):
                    deadline_text = mt
                elif mt_lower.startswith("value of award"):
                    award_text = mt

            cards.append(
                {
                    "title": title,
                    "university": university,
                    "detail_url": detail_url,
                    "country_text": country_text,
                    "level_text": level_text,
                    "funding_text": funding_text,
                    "deadline_text": deadline_text,
                    "award_text": award_text,
                }
            )

        return cards

    # -- detail page (REAL selectors) ----------------------------------------

    async def _fetch_detail(self, card: Dict[str, Any]) -> Dict[str, Any]:
        """
        Fetch a scholarship detail page.

        Real structure:
          3 × div.faq-content.rich-text-format
            [0] Overview: awarding institution, value, study mode, etc.
            [1] Eligibility: criteria, nationality requirements, etc.
            [2] How to apply: application process, deadlines, etc.
        """
        detail: Dict[str, Any] = {
            "description": None,
            "eligibility": None,
            "application_process": None,
            "apply_url": None,
        }
        url = card.get("detail_url")
        if not url:
            return detail

        html = await self.fetch(url)
        if not html:
            return detail

        soup = BeautifulSoup(html, "html.parser")

        # The 3 faq-content sections
        faq_sections = soup.select("div.faq-content.rich-text-format")

        if len(faq_sections) >= 1:
            detail["description"] = _clean(faq_sections[0].get_text())
        if len(faq_sections) >= 2:
            detail["eligibility"] = _clean(faq_sections[1].get_text())
        if len(faq_sections) >= 3:
            detail["application_process"] = _clean(faq_sections[2].get_text())

        # Apply URL — look for links to university application pages
        for a in soup.select("a[href]"):
            href = a.get("href", "")
            if "apply" in href.lower() and "idp.com" not in href:
                detail["apply_url"] = href
                break

        return detail

    # -- build + validate with Pydantic --------------------------------------

    def _build_scholarship(
        self,
        card: Dict[str, Any],
        detail: Dict[str, Any],
        country: str,
        level_slug: str,
    ) -> Optional[Scholarship]:
        award = _parse_award_value(card.get("award_text", ""))
        deadline = _parse_deadline(card.get("deadline_text", ""))
        funding = _parse_funding_type(card.get("funding_text", ""))
        study_level = LEVEL_MAP.get(level_slug, level_slug)

        # Merge description + application process into description
        desc_parts = []
        if detail.get("description"):
            desc_parts.append(detail["description"])
        if detail.get("application_process"):
            desc_parts.append(f"Application process: {detail['application_process']}")
        full_description = "\n\n".join(desc_parts) if desc_parts else None

        try:
            return Scholarship(
                title=card["title"],
                university=card["university"],
                country=country,
                study_level=study_level,
                funding_type=funding,
                deadline=deadline,
                award_value_min=award["award_value_min"],
                award_value_max=award["award_value_max"],
                award_currency=award["award_currency"],
                description=full_description,
                eligibility=detail.get("eligibility"),
                apply_url=detail.get("apply_url") or card.get("detail_url"),
                source="idp",
                source_url=card.get("detail_url"),
                is_active=True,
                last_verified=datetime.utcnow(),
            )
        except Exception as exc:
            log.error(
                "pydantic_validation_failed",
                title=card.get("title"),
                error=str(exc),
            )
            return None
