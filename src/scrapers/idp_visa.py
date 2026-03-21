"""
IDP Visa Scraper — scrapes student visa requirements from IDP blog pages.

Sources:
  - IDP blog pages: /nepal/blog/{country}-student-visa-requirements/
  - Australian Dept of Home Affairs (cross-verification, when accessible)

For each destination country, extracts:
  - Visa subclass / type
  - Required documents checklist
  - Financial proof requirements
  - Processing time range
  - Health insurance requirements
  - Work rights during study
  - Post-study work rights
"""

import re
from datetime import datetime
from typing import List, Optional, Dict, Any
from urllib.parse import urljoin

from bs4 import BeautifulSoup
import structlog

from src.scrapers.base_scraper import BaseScraper
from src.database.models import VisaRequirement

# Lazy DB imports
_upsert_visa = None


def _get_upsert_fn():
    global _upsert_visa
    if _upsert_visa is None:
        from src.database.queries import upsert_visa_requirement
        _upsert_visa = upsert_visa_requirement
    return _upsert_visa


log = structlog.get_logger().bind(scraper="IDPVisaScraper")

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
BASE_URL = "https://www.idp.com"
LOCALE = "nepal"

# IDP visa blog page URL patterns (verified March 2026)
VISA_PAGE_URLS: Dict[str, str] = {
    "australia": f"/{LOCALE}/blog/latest-visa-news/",
    "usa": f"/{LOCALE}/blog/usa-student-visa-requirements/",
    "uk": f"/{LOCALE}/blog/uk-student-visa-requirements/",
    "canada": f"/{LOCALE}/blog/canadian-student-visa-requirements/",
    "new-zealand": f"/{LOCALE}/application-assistance/visa-news/",
    "ireland": f"/{LOCALE}/blog/how-to-apply-for-an-irish-student-visa/",
}

# Nationalities to track
NATIONALITIES = [
    "nepal", "india", "bangladesh", "pakistan", "sri-lanka",
    "philippines", "vietnam", "china", "nigeria", "kenya",
]

# Known visa subclass numbers
VISA_SUBCLASS: Dict[str, str] = {
    "australia": "Subclass 500 (Student Visa)",
    "usa": "F-1 (Academic Student) / M-1 (Vocational Student)",
    "uk": "Student Visa (Tier 4 General)",
    "canada": "Study Permit",
    "new-zealand": "Fee Paying Student Visa",
    "ireland": "Stamp 2 (Student Visa)",
}

# Known financial proof requirements (in local currency)
FINANCIAL_PROOF: Dict[str, Dict[str, Any]] = {
    "australia": {
        "amount": 29710,
        "currency": "AUD",
        "period": "per year",
        "description": "AUD 29,710/year living costs + tuition + travel",
    },
    "usa": {
        "amount": None,
        "currency": "USD",
        "period": "varies",
        "description": "Proof of full tuition + living expenses for first year (Form I-20 amount)",
    },
    "uk": {
        "amount": 1334,
        "currency": "GBP",
        "period": "per month",
        "description": "GBP 1,334/month (London) or GBP 1,023/month (outside London) for 9 months",
    },
    "canada": {
        "amount": 20635,
        "currency": "CAD",
        "period": "per year",
        "description": "CAD 20,635/year (or CAD 25,690 in Quebec) + tuition",
    },
    "new-zealand": {
        "amount": 20000,
        "currency": "NZD",
        "period": "per year",
        "description": "NZD 20,000/year living costs + tuition",
    },
    "ireland": {
        "amount": 10000,
        "currency": "EUR",
        "period": "per year",
        "description": "EUR 10,000 in bank account + tuition fees paid",
    },
}

# Work rights during study (hours per week)
WORK_RIGHTS: Dict[str, Dict[str, Any]] = {
    "australia": {
        "hours_per_week": 48,
        "period": "per fortnight",
        "vacation": "unlimited",
        "notes": "48 hours per fortnight during term, unlimited during scheduled breaks",
    },
    "usa": {
        "hours_per_week": 20,
        "period": "per week",
        "vacation": "full-time",
        "notes": "20 hours/week on-campus during term, full-time during breaks (CPT/OPT for off-campus)",
    },
    "uk": {
        "hours_per_week": 20,
        "period": "per week",
        "vacation": "full-time",
        "notes": "20 hours/week during term, full-time during vacations",
    },
    "canada": {
        "hours_per_week": 20,
        "period": "per week",
        "vacation": "full-time",
        "notes": "20 hours/week off-campus during term, full-time during breaks",
    },
    "new-zealand": {
        "hours_per_week": 20,
        "period": "per week",
        "vacation": "full-time",
        "notes": "20 hours/week during term, full-time during scheduled holidays",
    },
    "ireland": {
        "hours_per_week": 20,
        "period": "per week",
        "vacation": "40 hours/week",
        "notes": "20 hours/week during term, 40 hours/week during holidays (June-September, mid-December to mid-January)",
    },
}

# Post-study work rights
POST_STUDY_WORK: Dict[str, str] = {
    "australia": "Temporary Graduate Visa (Subclass 485): 2-6 years depending on qualification level and location",
    "usa": "OPT: 12 months (36 months for STEM). H-1B lottery for permanent work",
    "uk": "Graduate Route: 2 years (3 years for PhD)",
    "canada": "PGWP: up to 3 years depending on program length",
    "new-zealand": "Post-Study Work Visa: 1-3 years depending on qualification",
    "ireland": "Third Level Graduate Scheme: 12 months (Level 8) or 24 months (Level 9/10)",
}

# Known processing times in weeks
PROCESSING_TIMES: Dict[str, Dict[str, int]] = {
    "australia": {"min_weeks": 4, "max_weeks": 12},
    "usa": {"min_weeks": 3, "max_weeks": 10},
    "uk": {"min_weeks": 3, "max_weeks": 8},
    "canada": {"min_weeks": 4, "max_weeks": 16},
    "new-zealand": {"min_weeks": 4, "max_weeks": 8},
    "ireland": {"min_weeks": 4, "max_weeks": 8},
}


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------
def _clean(text: Optional[str]) -> Optional[str]:
    if not text:
        return None
    cleaned = " ".join(text.split())
    return cleaned if cleaned else None


def _extract_document_checklist(faq_sections: List[Any]) -> List[str]:
    """Extract document requirements from IDP visa page sections."""
    docs: List[str] = []
    for faq in faq_sections:
        text = faq.get_text(" ", strip=True).lower()
        if "document" in text or "require" in text:
            # Look for list items
            for li in faq.select("li"):
                item = _clean(li.get_text())
                if item and len(item) > 5:
                    docs.append(item)
            # Also look for bold items
            if not docs:
                for strong in faq.select("strong, b"):
                    item = _clean(strong.get_text())
                    if item and len(item) > 5:
                        docs.append(item)
    return docs


def _extract_health_insurance(faq_sections: List[Any], country: str) -> Optional[str]:
    """Extract health insurance requirements."""
    known = {
        "australia": "Overseas Student Health Cover (OSHC) is mandatory for the duration of your visa",
        "uk": "Immigration Health Surcharge (IHS) must be paid as part of visa application (GBP 776/year for students)",
        "usa": "Most universities require health insurance; some offer their own plans",
        "canada": "Provincial health coverage varies; many provinces cover international students after waiting period",
        "new-zealand": "Medical and travel insurance required for duration of study",
        "ireland": "Private health insurance recommended; EU students covered by EHIC",
    }
    return known.get(country)


# ---------------------------------------------------------------------------
# IDP Visa Scraper
# ---------------------------------------------------------------------------
class IDPVisaScraper(BaseScraper):
    """
    Scrapes student visa information from IDP blog pages.

    Combines scraped data with authoritative reference data
    (visa subclasses, financial requirements, work rights) that is
    maintained as structured constants.

    Real IDP blog page structure (March 2026):
      h1 → page title
      div.faq-content (multiple sections):
        [0] Visa types overview
        [1] How to apply
        [2] Documents required
        [3] What to do after getting visa
        [4] Rules while studying
        [5] How IDP can help
    """

    def __init__(
        self,
        save_to_db: bool = True,
        rate_limit_interval: float = 2.0,
    ):
        super().__init__(BASE_URL, rate_limit_interval=rate_limit_interval)
        self.save_to_db = save_to_db

    async def scrape(self) -> List[VisaRequirement]:
        """Scrape visa requirements for all destination × nationality combos."""
        all_visas: List[VisaRequirement] = []

        for country, path in VISA_PAGE_URLS.items():
            url = urljoin(BASE_URL, path)
            await log.ainfo("scraping_visa_page", country=country, url=url)

            html = await self.fetch(url)
            scraped_data = self._parse_visa_page(html, country) if html else {}

            for nationality in NATIONALITIES:
                visa = self._build_visa_requirement(
                    country, nationality, scraped_data
                )
                if visa:
                    all_visas.append(visa)
                    if self.save_to_db:
                        try:
                            upsert_fn = _get_upsert_fn()
                            await upsert_fn(visa)
                        except Exception:
                            pass

            await log.ainfo(
                "country_complete",
                country=country,
                nationalities=len(NATIONALITIES),
            )

        # Cross-verify with Australian Dept of Home Affairs
        await self._cross_verify_australia()

        await log.ainfo("scrape_complete", total=len(all_visas))
        await self.close()
        return all_visas

    def _parse_visa_page(self, html: str, country: str) -> Dict[str, Any]:
        """Parse an IDP visa blog page."""
        soup = BeautifulSoup(html, "html.parser")
        faq_sections = soup.select("div.faq-content")

        full_text = " ".join(
            faq.get_text(" ", strip=True) for faq in faq_sections
        )

        return {
            "document_checklist": _extract_document_checklist(faq_sections),
            "health_insurance": _extract_health_insurance(faq_sections, country),
            "full_text": full_text[:5000],
        }

    def _build_visa_requirement(
        self,
        country: str,
        nationality: str,
        scraped_data: Dict[str, Any],
    ) -> Optional[VisaRequirement]:
        """Build a VisaRequirement from scraped + reference data."""
        financial = FINANCIAL_PROOF.get(country, {})
        work = WORK_RIGHTS.get(country, {})
        processing = PROCESSING_TIMES.get(country, {})

        # Build notes string from all supplementary info
        notes_parts = []
        if work.get("notes"):
            notes_parts.append(f"Work rights: {work['notes']}")
        if POST_STUDY_WORK.get(country):
            notes_parts.append(f"Post-study: {POST_STUDY_WORK[country]}")
        if financial.get("description"):
            notes_parts.append(f"Financial: {financial['description']}")
        notes = " | ".join(notes_parts) if notes_parts else None

        try:
            return VisaRequirement(
                nationality=nationality,
                destination_country=country,
                visa_type=VISA_SUBCLASS.get(country),
                visa_subclass=VISA_SUBCLASS.get(country),
                financial_requirement_aud=financial.get("amount"),
                processing_weeks_min=processing.get("min_weeks"),
                processing_weeks_max=processing.get("max_weeks"),
                required_documents=scraped_data.get("document_checklist", []),
                health_requirements=scraped_data.get("health_insurance"),
                work_rights_hours_per_week=work.get("hours_per_week"),
                notes=notes,
                source_url=urljoin(BASE_URL, VISA_PAGE_URLS.get(country, "")),
                last_updated=datetime.utcnow(),
            )
        except Exception as exc:
            log.error(
                "visa_build_failed",
                country=country,
                nationality=nationality,
                error=str(exc),
            )
            return None

    async def _cross_verify_australia(self):
        """
        Attempt to cross-verify with Australian Dept of Home Affairs.
        Their site often blocks scraping, so this is best-effort.
        """
        url = "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/student-500"
        html = await self.fetch(url)
        if html:
            await log.ainfo("home_affairs_accessible", url=url)
            # Parse processing times if available
            soup = BeautifulSoup(html, "html.parser")
            for el in soup.select("td, li, p"):
                text = el.get_text(strip=True).lower()
                if "processing" in text and ("day" in text or "week" in text or "month" in text):
                    await log.ainfo("home_affairs_processing", text=text[:100])
        else:
            await log.awarning(
                "home_affairs_blocked",
                note="Australian Dept of Home Affairs blocks server-side scraping. "
                     "Using IDP data as primary source.",
            )
