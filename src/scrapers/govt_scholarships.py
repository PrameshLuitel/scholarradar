"""
Government Scholarship Scrapers.

Sources (reverse-engineered March 2026):
  1. StudyAustralia.gov.au  — aggregator page with all Australian govt scholarships
  2. DFAT Australia Awards    — scraped via StudyAustralia (DFAT blocks direct scraping)
  3. Education.gov.au RTP     — scraped via StudyAustralia (education.gov.au blocks too)

Strategy: StudyAustralia is the only .gov.au site that allows scraping.
It aggregates all Australian Government scholarships on a single page with
structured sections and outbound links. We scrape that page and extract
scholarships from each <h2> section.
"""

import re
from datetime import datetime
from typing import List, Optional, Dict, Any
from urllib.parse import urljoin

from bs4 import BeautifulSoup, Tag
import structlog

from src.scrapers.base_scraper import BaseScraper
from src.database.models import Scholarship

# Lazy imports — supabase may not be installed
_upsert_scholarship = None
_deactivate_stale = None


def _get_db_fns():
    global _upsert_scholarship, _deactivate_stale
    if _upsert_scholarship is None:
        from src.database.queries import upsert_scholarship, deactivate_stale_scholarships
        _upsert_scholarship = upsert_scholarship
        _deactivate_stale = deactivate_stale_scholarships
    return _upsert_scholarship, _deactivate_stale


log = structlog.get_logger().bind(scraper="GovtScholarships")


def _clean(text: Optional[str]) -> Optional[str]:
    if not text:
        return None
    cleaned = " ".join(text.split())
    return cleaned if cleaned else None


# ---------------------------------------------------------------------------
# StudyAustralia Scholarships Scraper (single aggregator page)
# ---------------------------------------------------------------------------
class StudyAustraliaScholarshipScraper(BaseScraper):
    """
    Scrapes https://www.studyaustralia.gov.au/en/plan-your-studies/scholarships

    This page contains multiple <h2> sections, each describing a different
    Australian Government scholarship program:
      - Australia Awards
      - Australia for ASEAN scholarships
      - Australian Government Research Training Program (RTP)
      - Education provider scholarships
      - The Quad Fellowship (STEM)
      - Scholarships for smaller cities and regional areas
      - Scholarships for UK students
      - Scholarships for US students

    Each section has descriptive text and links to external apply/info pages.
    """

    SOURCE_URL = "https://www.studyaustralia.gov.au/en/plan-your-studies/scholarships"

    # Map section heading → our source enum value
    SOURCE_MAP = {
        "australia awards": "australia_awards",
        "australia for asean": "australia_awards",
        "research training program": "rtp",
        "education provider": "university_direct",
        "quad fellowship": "australia_awards",
        "smaller cities": "state_govt",
        "regional": "state_govt",
        "united kingdom": "state_govt",
        "united states": "state_govt",
    }

    # Map section heading → study level
    LEVEL_MAP = {
        "australia awards": "postgraduate",
        "australia for asean": "postgraduate",
        "research training program": "doctorate",
        "quad fellowship": "postgraduate",
    }

    def __init__(self, save_to_db: bool = True, rate_limit_interval: float = 2.0):
        # Explicit call to BaseScraper's init to avoid confusion with object.__init__
        BaseScraper.__init__(self, self.SOURCE_URL, rate_limit_interval=rate_limit_interval)
        self.save_to_db = save_to_db
        self._seen_ids: List[str] = []

    async def scrape(self) -> List[Scholarship]:
        await log.ainfo("studyaustralia_scrape_start")
        scholarships: List[Scholarship] = []

        try:
            from bs4 import BeautifulSoup, Tag
        except ImportError:
            log.error("missing_dependency", package="beautifulsoup4")
            return []

        html = await self.fetch(self.SOURCE_URL)
        if not html:
            await log.aerror("studyaustralia_fetch_failed")
            await self.close()
            return scholarships

        soup = BeautifulSoup(html, "html.parser")

        # Each <h2> is a scholarship program section
        for h2 in soup.select("h2"):
            heading = _clean(h2.get_text())
            if not heading:
                continue

            # Gather text from siblings until next <h2>
            description_parts: List[str] = []
            links: List[Dict[str, str]] = []

            sibling = h2.find_next_sibling()
            while sibling and sibling.name != "h2":
                if isinstance(sibling, Tag):
                    text = _clean(sibling.get_text())
                    if text:
                        description_parts.append(text)

                    # Extract links
                    for a in sibling.select("a[href]"):
                        href = a.get("href", "")
                        link_text = _clean(a.get_text())
                        if href and link_text and href.startswith("http"):
                            links.append({"text": link_text, "url": href})

                sibling = sibling.find_next_sibling()

            description = " ".join(description_parts) if description_parts else None

            # Skip navigation/footer headings
            heading_lower = heading.lower()
            if any(skip in heading_lower for skip in ["on this page", "discover more", "footer", "quick links", "apply for a scholarship today"]):
                continue

            # Determine source and level from heading
            source = "state_govt"
            study_level = None
            for key, val in self.SOURCE_MAP.items():
                if key in heading_lower:
                    source = val
                    break
            for key, val in self.LEVEL_MAP.items():
                if key in heading_lower:
                    study_level = val
                    break

            # Primary apply/info link
            apply_url = links[0]["url"] if links else None

            scholarship = self._build(
                title=heading,
                description=description,
                apply_url=apply_url,
                source=source,
                study_level=study_level,
            )
            if not scholarship:
                continue

            scholarships.append(scholarship)

            if self.save_to_db:
                try:
                    upsert_fn, _ = _get_db_fns()
                    result = await upsert_fn(scholarship)
                    if result and result.get("id"):
                        self._seen_ids.append(result["id"])
                except Exception:
                    pass

            # Also create entries for sub-links (e.g. regional scholarships)
            for link in links[1:]:  # skip the first, already used
                sub_scholarship = self._build(
                    title=link["text"],
                    description=f"Part of: {heading}",
                    apply_url=link["url"],
                    source=source,
                    study_level=study_level,
                )
                if not sub_scholarship:
                    continue
                scholarships.append(sub_scholarship)
                if self.save_to_db:
                    try:
                        upsert_fn, _ = _get_db_fns()
                        result = await upsert_fn(sub_scholarship)
                        if result and result.get("id"):
                            self._seen_ids.append(result["id"])
                    except Exception:
                        pass

        # Deactivate stale records across all govt sources
        if self.save_to_db and self._seen_ids:
            _, deactivate_fn = _get_db_fns()
            for src in set(self.SOURCE_MAP.values()):
                source_ids = [sid for sid in self._seen_ids]  # all IDs
                await deactivate_fn(src, source_ids)

        await log.ainfo("studyaustralia_scrape_complete", count=len(scholarships))
        await self.close()
        return scholarships

    def _build(
        self,
        title: str,
        description: Optional[str],
        apply_url: Optional[str],
        source: str,
        study_level: Optional[str],
    ) -> Optional[Scholarship]:
        try:
            return Scholarship(
                title=title,
                university="Australian Government",
                country="australia",
                study_level=study_level,
                description=description,
                apply_url=apply_url,
                source=source,
                source_url=self.SOURCE_URL,
                funding_type="full",
                is_active=True,
                last_verified=datetime.utcnow(),
            )
        except Exception as exc:
            log.error("validation_failed", title=title, error=str(exc))
            return None


# ---------------------------------------------------------------------------
# Legacy aliases — these all delegate to StudyAustraliaScholarshipScraper
# since the individual .gov.au sites block scraping.
# ---------------------------------------------------------------------------
class AustraliaAwardsScraper(StudyAustraliaScholarshipScraper):
    """Alias for backwards compatibility."""
    pass


class RTPScholarshipScraper(StudyAustraliaScholarshipScraper):
    """Alias for backwards compatibility."""
    pass


class DestinationAustraliaScraper(StudyAustraliaScholarshipScraper):
    """Alias for backwards compatibility."""
    pass
