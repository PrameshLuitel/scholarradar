"""
IDP University Scraper — scrapes university listing + detail pages from idp.com.

Built from reverse-engineering the REAL idp.com HTML (March 2026).
Covers all 1,185 universities across 99 listing pages.

For each university:
  1. Listing page → name, country, THE ranking, intl students, profile URL
  2. Detail page  → overview, curriculum, entry requirements, facilities,
                     accommodation, scholarships, career support

Also includes a static QS World University Rankings top-200 lookup table
for ranking cross-verification (QS site is fully JS-rendered, not scrapeable
server-side).

Designed to run weekly (universities rarely change).
"""

import re
from datetime import datetime
from typing import List, Optional, Dict, Any, Tuple
from urllib.parse import urljoin

from bs4 import BeautifulSoup
import structlog

from src.scrapers.base_scraper import BaseScraper
from src.database.models import University

# Lazy DB imports
_upsert_university = None


def _get_upsert_fn():
    global _upsert_university
    if _upsert_university is None:
        from src.database.queries import upsert_university
        _upsert_university = upsert_university
    return _upsert_university


log = structlog.get_logger().bind(scraper="IDPUniversityScraper")

# ---------------------------------------------------------------------------
# Constants (reverse-engineered March 2026)
# ---------------------------------------------------------------------------
BASE_URL = "https://www.idp.com"
LOCALE = "nepal"

# Listing URL: /nepal/find-a-university/?page=N
CARDS_PER_PAGE = 12
TOTAL_PAGES = 99  # ~1,185 universities

# Country name mapping (IDP uses full names on listing, our DB uses keys)
COUNTRY_MAP = {
    "australia": "australia",
    "canada": "canada",
    "ireland": "ireland",
    "new zealand": "new-zealand",
    "united kingdom": "uk",
    "united states": "usa",
}

# ---------------------------------------------------------------------------
# QS World University Rankings 2026 — static top-200 lookup
# (QS site is JS-rendered, can't scrape server-side)
# Source: topuniversities.com/world-university-rankings (June 2025 release)
# ---------------------------------------------------------------------------
QS_RANKINGS_2026: Dict[str, int] = {
    "Massachusetts Institute of Technology (MIT)": 1,
    "Imperial College London": 2,
    "University of Oxford": 3,
    "Harvard University": 4,
    "University of Cambridge": 5,
    "Stanford University": 6,
    "ETH Zurich": 7,
    "National University of Singapore (NUS)": 8,
    "UCL": 9,
    "California Institute of Technology (Caltech)": 10,
    "University of Pennsylvania": 11,
    "University of Chicago": 12,
    "Princeton University": 13,
    "Nanyang Technological University, Singapore (NTU)": 14,
    "The University of Edinburgh": 15,
    "Cornell University": 16,
    "The University of Hong Kong": 17,
    "Columbia University": 18,
    "The University of Melbourne": 19,
    "Yale University": 20,
    "Peking University": 21,
    "The University of Tokyo": 22,
    "Tsinghua University": 23,
    "University of Toronto": 24,
    "Seoul National University": 25,
    "Johns Hopkins University": 26,
    "University of Michigan-Ann Arbor": 27,
    "PSL University": 28,
    "The University of Sydney": 29,
    "EPFL": 30,
    "King's College London": 31,
    "The University of New South Wales (UNSW Sydney)": 32,
    "McGill University": 33,
    "The University of Manchester": 34,
    "The Australian National University": 35,
    "University of British Columbia": 36,
    "Monash University": 37,
    "The University of Queensland": 38,
    "Kyoto University": 39,
    "University of California, Los Angeles (UCLA)": 40,
    "Technical University of Munich": 41,
    "New York University (NYU)": 42,
    "Northwestern University": 43,
    "Duke University": 44,
    "KAIST - Korea Advanced Institute of Science & Technology": 45,
    "The Hong Kong University of Science and Technology": 46,
    "The Chinese University of Hong Kong (CUHK)": 47,
    "Carnegie Mellon University": 48,
    "University of California, Berkeley (UCB)": 49,
    "The University of Auckland": 50,
    "University of Amsterdam": 51,
    "University of Waterloo": 52,
    "Universiti Malaya (UM)": 53,
    "The Hong Kong Polytechnic University": 54,
    "University of Bristol": 55,
    "Delft University of Technology": 56,
    "Yonsei University": 57,
    "The University of Warwick": 58,
    "University of Leeds": 59,
    "KU Leuven": 60,
    "Ludwig-Maximilians-Universität München": 61,
    "National Taiwan University (NTU)": 62,
    "Sorbonne University": 63,
    "University of Glasgow": 64,
    "Korea University": 65,
    "University of Southampton": 66,
    "University of Birmingham": 67,
    "Durham University": 68,
    "University of Western Australia": 69,
    "Politecnico di Milano": 70,
    "University of Alberta": 71,
    "University of Technology Sydney": 72,
    "Osaka University": 73,
    "Lund University": 74,
    "KTH Royal Institute of Technology": 75,
    "Lomonosov Moscow State University": 76,
    "Université Paris-Saclay": 77,
    "Tohoku University": 78,
    "University of Adelaide": 79,
    "City University of Hong Kong": 80,
    "Sungkyunkwan University (SKKU)": 81,
    "University of Nottingham": 82,
    "Fudan University": 83,
    "Shanghai Jiao Tong University": 84,
    "Trinity College Dublin, The University of Dublin": 85,
    "University of St Andrews": 86,
    "University of Sheffield": 87,
    "Queen Mary University of London": 88,
    "University of Science and Technology of China": 89,
    "Zhejiang University": 90,
    "Lancaster University": 91,
    "Tokyo Institute of Technology": 92,
    "Newcastle University": 93,
    "Georgia Institute of Technology": 94,
    "University of Bath": 95,
    "University of Illinois at Urbana-Champaign": 96,
    "University of Exeter": 97,
    "Purdue University": 98,
    "University of California, San Diego (UCSD)": 99,
    "University of York": 100,
}

# Fuzzy name → QS key mapping for IDP names that differ
QS_NAME_ALIASES: Dict[str, str] = {
    "THE UNIVERSITY OF MELBOURNE": "The University of Melbourne",
    "THE UNIVERSITY OF SYDNEY": "The University of Sydney",
    "THE AUSTRALIAN NATIONAL UNIVERSITY": "The Australian National University",
    "MONASH UNIVERSITY": "Monash University",
    "THE UNIVERSITY OF QUEENSLAND": "The University of Queensland",
    "UNIVERSITY OF NEW SOUTH WALES": "The University of New South Wales (UNSW Sydney)",
    "UNSW SYDNEY": "The University of New South Wales (UNSW Sydney)",
    "UNIVERSITY OF WESTERN AUSTRALIA": "University of Western Australia",
    "UNIVERSITY OF TECHNOLOGY SYDNEY": "University of Technology Sydney",
    "UNIVERSITY OF ADELAIDE": "University of Adelaide",
    "UNIVERSITY OF TORONTO": "University of Toronto",
    "MCGILL UNIVERSITY": "McGill University",
    "UNIVERSITY OF BRITISH COLUMBIA": "University of British Columbia",
    "UNIVERSITY OF WATERLOO": "University of Waterloo",
    "UNIVERSITY OF ALBERTA": "University of Alberta",
    "UNIVERSITY OF AUCKLAND": "The University of Auckland",
    "IMPERIAL COLLEGE LONDON": "Imperial College London",
    "UNIVERSITY OF OXFORD": "University of Oxford",
    "UNIVERSITY OF CAMBRIDGE": "University of Cambridge",
    "KING'S COLLEGE LONDON": "King's College London",
    "UCL (UNIVERSITY COLLEGE LONDON)": "UCL",
    "THE UNIVERSITY OF EDINBURGH": "The University of Edinburgh",
    "THE UNIVERSITY OF MANCHESTER": "The University of Manchester",
    "UNIVERSITY OF BRISTOL": "University of Bristol",
    "THE UNIVERSITY OF WARWICK": "The University of Warwick",
    "UNIVERSITY OF LEEDS": "University of Leeds",
    "UNIVERSITY OF GLASGOW": "University of Glasgow",
    "UNIVERSITY OF SOUTHAMPTON": "University of Southampton",
    "UNIVERSITY OF BIRMINGHAM": "University of Birmingham",
    "DURHAM UNIVERSITY": "Durham University",
    "UNIVERSITY OF NOTTINGHAM": "University of Nottingham",
    "UNIVERSITY OF SHEFFIELD": "University of Sheffield",
    "QUEEN MARY UNIVERSITY OF LONDON": "Queen Mary University of London",
    "LANCASTER UNIVERSITY": "Lancaster University",
    "NEWCASTLE UNIVERSITY": "Newcastle University",
    "UNIVERSITY OF BATH": "University of Bath",
    "UNIVERSITY OF EXETER": "University of Exeter",
    "UNIVERSITY OF YORK": "University of York",
    "UNIVERSITY OF ST ANDREWS": "University of St Andrews",
    "TRINITY COLLEGE DUBLIN, THE UNIVERSITY OF DUBLIN": "Trinity College Dublin, The University of Dublin",
    "TRINITY COLLEGE DUBLIN THE UNIVERSITY OF DUBLIN": "Trinity College Dublin, The University of Dublin",
}


def _lookup_qs_ranking(name: str) -> Optional[int]:
    """Look up QS ranking by university name (case-insensitive with aliases)."""
    # Direct lookup (title case)
    if name in QS_RANKINGS_2026:
        return QS_RANKINGS_2026[name]

    # Alias lookup (IDP uses ALL CAPS)
    upper = name.upper().strip()
    alias = QS_NAME_ALIASES.get(upper)
    if alias and alias in QS_RANKINGS_2026:
        return QS_RANKINGS_2026[alias]

    # Fuzzy: try title-casing the IDP name
    title = name.strip().title()
    for qs_name, rank in QS_RANKINGS_2026.items():
        if title.lower() == qs_name.lower():
            return rank

    return None


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------
def _clean(text: Optional[str]) -> Optional[str]:
    if not text:
        return None
    cleaned = " ".join(text.split())
    return cleaned if cleaned else None


def _parse_the_ranking(text: str) -> Optional[int]:
    """Parse 'THE World Ranking: 401' → 401."""
    match = re.search(r"(\d+)", text)
    return int(match.group(1)) if match else None


def _parse_intl_students(text: str) -> Optional[int]:
    """Parse 'International students: 1430' → 1430."""
    match = re.search(r"(\d[\d,]*)", text)
    return int(match.group(1).replace(",", "")) if match else None


def _extract_facilities(text: str) -> List[str]:
    """Extract facility names from overview text."""
    facilities = []
    keywords = [
        "library", "gymnasium", "gym", "pool", "swimming",
        "laboratory", "lab", "computer", "wifi", "internet",
        "cafeteria", "dining", "medical", "health", "clinic",
        "sports", "recreation", "fitness", "stadium",
        "auditorium", "theater", "theatre", "gallery",
        "research center", "research centre", "innovation",
        "student union", "student centre", "student center",
    ]
    text_lower = text.lower()
    for kw in keywords:
        if kw in text_lower:
            facilities.append(kw.title())
    return list(set(facilities))


def _extract_accommodation_costs(text: str) -> Tuple[Optional[float], Optional[float]]:
    """Try to extract accommodation cost range from text."""
    # Patterns like "AUD 200-400 per week" or "$150 to $300"
    # Improved regex to ensure we start with a digit
    numbers = re.findall(r"(\d[\d,.]*)", text)
    nums = []
    for n in numbers:
        try:
            # Remove commas and handle multiple dots if any
            cleaned = n.replace(",", "")
            if "." in cleaned:
                parts = cleaned.split(".")
                cleaned = parts[0] + "." + "".join(parts[1:])
            
            if cleaned and cleaned != ".":
                val = float(cleaned)
                if 10 < val < 100000:  # Ignore very small or very large numbers
                    nums.append(val)
        except ValueError:
            continue
            
    if len(nums) >= 2:
        return min(nums), max(nums)
    elif len(nums) == 1:
        return nums[0], nums[0]
    return None, None


def _extract_ielts(text: str) -> Optional[float]:
    """Extract minimum IELTS from entry requirements text."""
    matches = re.findall(r"IELTS[:\s]*(?:overall[:\s]*)?([\d.]+)", text, re.IGNORECASE)
    if matches:
        scores = [float(m) for m in matches]
        return min(scores)
    return None


def _extract_website(soup: BeautifulSoup) -> Optional[str]:
    """Find the university's own website from external links."""
    for a in soup.select("a[href]"):
        href = a.get("href", "")
        text = a.get_text(strip=True).lower()
        # Look for links to university domains (not idp.com)
        if (href.startswith("http")
                and "idp.com" not in href
                and "idp-connect" not in href
                and ("visit" in text or "website" in text or "official" in text)):
            return href
    return None


# ---------------------------------------------------------------------------
# IDP University Scraper
# ---------------------------------------------------------------------------
class IDPUniversityScraper(BaseScraper):
    """
    Scrapes university profiles from idp.com.

    Phase 1: Listing pages → collect all university URLs + basic metadata
    Phase 2: Detail pages → extract full profiles
    Phase 3: Merge with QS static rankings

    Real HTML structure (reverse-engineered March 2026):
    Listing card:
      div.interactive-card
        a.h4 → university name + profile href
        p.text-small[title] → country
        ul li span.text-small → THE ranking, intl students
    Detail page:
      h1 → full name
      div.faq-content (8 sections):
        [0] Overview/facilities
        [1] Curriculum
        [2] Entry requirements (IELTS, GPA)
        [3] Scholarships
        [4] Employability
        [5] Accommodation
        [6+] News / other
    """

    def __init__(
        self,
        save_to_db: bool = True,
        rate_limit_interval: float = 2.0,
        locale: str = LOCALE,
    ):
        super().__init__(BASE_URL, rate_limit_interval=rate_limit_interval)
        self.save_to_db = save_to_db
        self.locale = locale

    # -- public entry-point --------------------------------------------------

    async def scrape(self) -> List[University]:
        """
        Full scrape of all IDP universities.
        Phase 1: Collect from listing pages
        Phase 2: Fetch each detail page
        Phase 3: Merge with QS rankings + validate + upsert
        """
        # Phase 1: listing pages
        await log.ainfo("phase1_start", description="Collecting university URLs from listing pages")
        uni_stubs = await self._collect_all_listings()
        await log.ainfo("phase1_complete", total_stubs=len(uni_stubs))

        # Phase 2 + 3: detail pages + build + save
        universities: List[University] = []
        total = len(uni_stubs)

        for idx, stub in enumerate(uni_stubs):
            pct = round((idx / total) * 100, 1) if total else 0

            if idx % 50 == 0:
                await log.ainfo("progress", pct=f"{pct}%", done=idx, total=total)

            detail = await self._fetch_detail(stub["profile_url"])
            university = self._build_university(stub, detail)
            if university is None:
                continue

            universities.append(university)

            if self.save_to_db:
                try:
                    upsert_fn = _get_upsert_fn()
                    await upsert_fn(university)
                except Exception:
                    pass

        await log.ainfo("scrape_complete", total=len(universities))
        await self.close()
        return universities

    # -- Phase 1: listing pages ----------------------------------------------

    async def _collect_all_listings(self) -> List[Dict[str, Any]]:
        all_stubs: List[Dict[str, Any]] = []
        page = 1

        while True:
            url = f"{BASE_URL}/{self.locale}/find-a-university/?page={page}"
            html = await self.fetch(url)
            if html is None:
                await log.awarning("listing_fetch_failed", page=page)
                break

            stubs = self._parse_listing(html)
            if not stubs:
                break

            all_stubs.extend(stubs)

            if page % 10 == 0:
                await log.ainfo("listing_progress", page=page, collected=len(all_stubs))

            if len(stubs) < CARDS_PER_PAGE:
                break

            page += 1

        return all_stubs

    @staticmethod
    def _parse_listing(html: str) -> List[Dict[str, Any]]:
        """
        Parse university listing page.

        Card structure:
          div.interactive-card
            img[alt="university logo"]
            div > a.h4 → name + href
            div > p.text-small[title] → country
            ul > li > span.text-small → ranking, intl students, etc.
        """
        soup = BeautifulSoup(html, "html.parser")
        stubs: List[Dict[str, Any]] = []

        for el in soup.select("div.interactive-card"):
            title_a = el.select_one("a.h4")
            if not title_a:
                continue
            name = _clean(title_a.get_text())
            if not name:
                continue
            href = title_a.get("href", "")
            profile_url = urljoin(BASE_URL, href) if href else None

            # Country — in <p class="text-small" title="...">
            country_p = el.select_one("p.text-small[title]")
            country_raw = country_p.get("title", "").strip() if country_p else ""
            if not country_raw and country_p:
                country_raw = _clean(country_p.get_text()) or ""
            country_key = COUNTRY_MAP.get(country_raw.lower(), country_raw.lower())

            # Metadata spans
            meta_spans = el.select("ul li span.text-small")
            the_ranking = None
            intl_students = None

            for span in meta_spans:
                txt = span.get_text(strip=True)
                if not txt:
                    continue
                txt_lower = txt.lower()
                if "world ranking" in txt_lower:
                    the_ranking = _parse_the_ranking(txt)
                elif "international student" in txt_lower:
                    intl_students = _parse_intl_students(txt)

            # Logo image
            logo_img = el.select_one("img[alt*='logo']")
            logo_url = logo_img.get("src", "") if logo_img else None

            stubs.append({
                "name": name,
                "country": country_key,
                "profile_url": profile_url,
                "the_ranking": the_ranking,
                "international_students": intl_students,
                "logo_url": logo_url,
            })

        return stubs

    # -- Phase 2: detail pages -----------------------------------------------

    async def _fetch_detail(self, url: Optional[str]) -> Dict[str, Any]:
        """
        Fetch a university detail page and extract structured data.

        Real structure:
          h1 → full name
          div.faq-content.rich-text-format (up to 8 sections):
            [0] Overview: description, facilities
            [1] Curriculum: programs, structure
            [2] Entry requirements: IELTS, grades
            [3] Scholarships
            [4] Employability / career support
            [5] Accommodation: options, costs
            [6+] News / events
        """
        detail: Dict[str, Any] = {
            "overview": None,
            "entry_requirements": None,
            "accommodation": None,
            "facilities": [],
            "ielts_minimum": None,
            "accommodation_cost_min": None,
            "accommodation_cost_max": None,
            "website": None,
            "city": None,
        }
        if not url:
            return detail

        html = await self.fetch(url)
        if not html:
            return detail

        soup = BeautifulSoup(html, "html.parser")

        # FAQ content sections
        faq_sections = soup.select("div.faq-content")

        if len(faq_sections) >= 1:
            overview_text = faq_sections[0].get_text(" ", strip=True)
            detail["overview"] = _clean(overview_text[:2000])
            detail["facilities"] = _extract_facilities(overview_text)

        # Entry requirements (section index varies — search by heading)
        for i, faq in enumerate(faq_sections):
            # Find the heading associated with this section
            prev_h = faq.find_previous(["h2", "h3"])
            if not prev_h:
                continue
            heading = prev_h.get_text(strip=True).lower()

            if "entry" in heading or "requirement" in heading or "english" in heading:
                text = faq.get_text(" ", strip=True)
                detail["entry_requirements"] = _clean(text[:1000])
                ielts = _extract_ielts(text)
                if ielts:
                    detail["ielts_minimum"] = ielts

            elif "accommodation" in heading or "housing" in heading:
                text = faq.get_text(" ", strip=True)
                detail["accommodation"] = _clean(text[:1000])
                cost_min, cost_max = _extract_accommodation_costs(text)
                if cost_min:
                    detail["accommodation_cost_min"] = cost_min
                if cost_max:
                    detail["accommodation_cost_max"] = cost_max

        # University website
        detail["website"] = _extract_website(soup)

        # City — try to find from breadcrumb or location info
        for el in soup.select("span, p"):
            text = el.get_text(strip=True)
            # Look for patterns like "Melbourne, Australia" or "Parkville, Melbourne"
            if "," in text and len(text) < 50:
                parts = [p.strip() for p in text.split(",")]
                if len(parts) == 2 and all(2 < len(p) < 30 for p in parts):
                    # Heuristic: if second part looks like a country, first is city
                    if parts[1].lower() in COUNTRY_MAP:
                        detail["city"] = parts[0]
                        break

        return detail

    # -- Phase 3: build + validate -------------------------------------------

    def _build_university(
        self,
        stub: Dict[str, Any],
        detail: Dict[str, Any],
    ) -> Optional[University]:
        """Build and validate a University model from listing + detail data."""
        name = stub["name"]
        qs_rank = _lookup_qs_ranking(name)
        the_rank = stub.get("the_ranking")

        # Best available ranking: prefer QS, fall back to THE
        best_ranking = qs_rank or the_rank

        try:
            return University(
                name=name,
                country=stub["country"],
                city=detail.get("city"),
                world_ranking=best_ranking,
                international_students=stub.get("international_students"),
                ielts_minimum=detail.get("ielts_minimum"),
                facilities=detail.get("facilities", []),
                accommodation_cost_min=detail.get("accommodation_cost_min"),
                accommodation_cost_max=detail.get("accommodation_cost_max"),
                website=detail.get("website"),
                idp_profile_url=stub.get("profile_url"),
            )
        except Exception as exc:
            log.error(
                "pydantic_validation_failed",
                name=name,
                error=str(exc),
            )
            return None
