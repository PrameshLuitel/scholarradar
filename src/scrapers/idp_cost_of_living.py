"""
Cost of Living Scraper — scrapes Numbeo for real-time cost data
and merges with IDP reference data.

Sources:
  - Numbeo.com: table.data_wide_table with 70+ price rows per city
  - IDP reference data: minimum wage, student budget estimates

Covers all major student cities:
  Australia: Sydney, Melbourne, Brisbane, Perth, Adelaide, Gold Coast, Canberra
  UK: London, Manchester, Edinburgh, Birmingham, Glasgow
  Canada: Toronto, Vancouver, Montreal, Calgary
  USA: New York, Los Angeles, Boston, Chicago
  Ireland: Dublin, Cork, Galway
"""

import re
from datetime import datetime
from typing import List, Optional, Dict, Any, Tuple

from bs4 import BeautifulSoup
import structlog

from src.scrapers.base_scraper import BaseScraper
from src.database.models import CostOfLiving

# Lazy DB imports
_get_living_costs = None
_upsert_cost = None


def _get_db_fns():
    global _upsert_cost
    if _upsert_cost is None:
        from src.database.queries import get_living_costs
        _upsert_cost = get_living_costs  # reuse existing
    return _upsert_cost


log = structlog.get_logger().bind(scraper="CostOfLivingScraper")

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
NUMBEO_BASE = "https://www.numbeo.com"

# City → (country_key, Numbeo city slug, currency)
STUDENT_CITIES: Dict[str, Dict[str, str]] = {
    # Australia
    "Sydney": {"country": "australia", "slug": "Sydney", "currency": "AUD"},
    "Melbourne": {"country": "australia", "slug": "Melbourne", "currency": "AUD"},
    "Brisbane": {"country": "australia", "slug": "Brisbane", "currency": "AUD"},
    "Perth": {"country": "australia", "slug": "Perth", "currency": "AUD"},
    "Adelaide": {"country": "australia", "slug": "Adelaide", "currency": "AUD"},
    "Gold Coast": {"country": "australia", "slug": "Gold-Coast", "currency": "AUD"},
    "Canberra": {"country": "australia", "slug": "Canberra", "currency": "AUD"},
    # UK
    "London": {"country": "uk", "slug": "London", "currency": "GBP"},
    "Manchester": {"country": "uk", "slug": "Manchester", "currency": "GBP"},
    "Edinburgh": {"country": "uk", "slug": "Edinburgh", "currency": "GBP"},
    "Birmingham": {"country": "uk", "slug": "Birmingham", "currency": "GBP"},
    "Glasgow": {"country": "uk", "slug": "Glasgow", "currency": "GBP"},
    # Canada
    "Toronto": {"country": "canada", "slug": "Toronto", "currency": "CAD"},
    "Vancouver": {"country": "canada", "slug": "Vancouver", "currency": "CAD"},
    "Montreal": {"country": "canada", "slug": "Montreal", "currency": "CAD"},
    "Calgary": {"country": "canada", "slug": "Calgary", "currency": "CAD"},
    # USA
    "New York": {"country": "usa", "slug": "New-York", "currency": "USD"},
    "Los Angeles": {"country": "usa", "slug": "Los-Angeles", "currency": "USD"},
    "Boston": {"country": "usa", "slug": "Boston", "currency": "USD"},
    "Chicago": {"country": "usa", "slug": "Chicago", "currency": "USD"},
    # Ireland
    "Dublin": {"country": "ireland", "slug": "Dublin", "currency": "EUR"},
    "Cork": {"country": "ireland", "slug": "Cork", "currency": "EUR"},
    "Galway": {"country": "ireland", "slug": "Galway", "currency": "EUR"},
}

# Minimum wages (hourly, from government sources, 2026)
MIN_WAGES: Dict[str, float] = {
    "australia": 24.10,     # Fair Work Commission (July 2025): AUD 24.10/hr
    "uk": 12.21,            # National Living Wage (April 2025): GBP 12.21/hr (21+)
    "canada": 17.20,        # Federal: CAD 17.20/hr (varies by province)
    "usa": 15.00,           # Federal: USD 7.25 but most student cities have USD 15+
    "ireland": 13.50,       # National: EUR 13.50/hr (2025)
}


# ---------------------------------------------------------------------------
# Numbeo price row mappings
# Map Numbeo item names → our CostOfLiving model fields
# ---------------------------------------------------------------------------
RENT_SHARED_KEYS = [
    "1 Bedroom Apartment Outside of City Centre",
]
RENT_PRIVATE_KEYS = [
    "1 Bedroom Apartment in City Centre",
]
RENT_3BED_KEYS = [
    "3 Bedroom Apartment in City Centre",
    "3 Bedroom Apartment Outside of City Centre",
]
TRANSPORT_KEY = "Monthly Public Transport Pass (Regular Price)"
UTILITIES_KEY = "Basic Utilities for 85 m2Apartment (Electricity, Heatin"  # truncated in Numbeo
INTERNET_KEY = "Broadband Internet (Unlimited Data, 60 Mbps or Higher)"
MEAL_KEY = "Meal at an Inexpensive Restaurant"
SALARY_KEY = "Average Monthly Net Salary (After Tax)"


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------
def _parse_numbeo_price(text: str) -> Optional[float]:
    """
    Parse Numbeo price strings:
      '30.00 A$'  → 30.0
      '3,695.12 A$' → 3695.12
      '217.39 A$' → 217.39
      '?' → None
    """
    if not text or text.strip() == "?":
        return None
    # Remove currency symbols and whitespace
    cleaned = re.sub(r"[A-Z$€£¥\s]+$", "", text.strip())
    cleaned = cleaned.replace(",", "")
    try:
        return float(cleaned)
    except ValueError:
        return None


def _estimate_food_monthly(meal_price: Optional[float]) -> Optional[float]:
    """
    Estimate monthly food cost for a student from meal prices.
    Assume: 50% home cooking (60% of restaurant cost) + 50% eating out.
    ~3 meals/day × 30 days = ~90 meals.
    Budget: 60 home-cooked ($meal * 0.4 each) + 30 cheap eats ($meal each).
    """
    if not meal_price:
        return None
    home = 60 * (meal_price * 0.4)
    out = 30 * meal_price
    return round(home + out, 2)


def _estimate_shared_rent(private_rent: Optional[float]) -> Optional[float]:
    """Estimate shared room rent as ~55-65% of a 1-bed apartment rent."""
    if not private_rent:
        return None
    return round(private_rent * 0.55, 2)


# ---------------------------------------------------------------------------
# Cost of Living Scraper
# ---------------------------------------------------------------------------
class CostOfLivingScraper(BaseScraper):
    """
    Scrapes cost of living data from Numbeo for all major student cities.

    Numbeo structure (verified March 2026):
      table.data_wide_table
        tr > td[0] = item name
        tr > td[1] = price in local currency
        tr > td[2] = range (optional)

    Key rows for students:
      - Rent: "1 Bedroom Apartment in/outside City Centre"
      - Transport: "Monthly Public Transport Pass"
      - Utilities: "Basic Utilities for 85 m2 Apartment"
      - Internet: "Broadband Internet"
      - Meals: "Meal at an Inexpensive Restaurant"
      - Salary: "Average Monthly Net Salary"
    """

    def __init__(
        self,
        save_to_db: bool = True,
        rate_limit_interval: float = 3.0,  # Be nice to Numbeo
    ):
        BaseScraper.__init__(self, NUMBEO_BASE, rate_limit_interval=rate_limit_interval)
        self.save_to_db = save_to_db

    async def scrape(self) -> List[CostOfLiving]:
        """Scrape all student cities."""
        all_costs: List[CostOfLiving] = []
        total = len(STUDENT_CITIES)
        
        try:
            from bs4 import BeautifulSoup
        except ImportError:
            log.error("missing_dependency", package="beautifulsoup4")
            return []

        for idx, (city, info) in enumerate(STUDENT_CITIES.items()):
            pct = round((idx / total) * 100, 1)
            await log.ainfo("scraping_city", city=city, progress=f"{pct}%")

            numbeo_data = await self._scrape_numbeo(info["slug"])
            cost = self._build_cost(city, info, numbeo_data)

            if cost:
                all_costs.append(cost)

                if self.save_to_db:
                    try:
                        await self._upsert_cost(cost)
                    except Exception:
                        pass

            await log.ainfo(
                "city_complete",
                city=city,
                country=info["country"],
                has_data=cost is not None,
            )

        await log.ainfo("scrape_complete", total=len(all_costs))
        await self.close()
        return all_costs

    async def _scrape_numbeo(self, city_slug: str) -> Dict[str, Optional[float]]:
        """Scrape Numbeo cost-of-living page for a city."""
        url = f"{NUMBEO_BASE}/cost-of-living/in/{city_slug}"
        html = await self.fetch(url)
        if not html:
            return {}

        return self._parse_numbeo_table(html)

    @staticmethod
    def _parse_numbeo_table(html: str) -> Dict[str, Optional[float]]:
        """
        Parse Numbeo's data_wide_table into a price dictionary.

        Each row: td[0]=item name, td[1]=price with currency symbol
        """
        soup = BeautifulSoup(html, "html.parser")
        table = soup.select_one("table.data_wide_table")
        if not table:
            return {}

        prices: Dict[str, Optional[float]] = {}
        for row in table.select("tr"):
            tds = row.select("td")
            if len(tds) < 2:
                continue
            item = tds[0].get_text(strip=True)
            price_text = tds[1].get_text(strip=True)
            if item:
                prices[item] = _parse_numbeo_price(price_text)

        return prices

    def _build_cost(
        self,
        city: str,
        info: Dict[str, str],
        numbeo: Dict[str, Optional[float]],
    ) -> Optional[CostOfLiving]:
        """Build CostOfLiving from Numbeo + reference data."""
        country = info["country"]
        currency = info["currency"]

        # Extract prices from Numbeo data
        rent_private = None
        rent_outside = None
        for key, val in numbeo.items():
            if "1 Bedroom" in key and "City Centre" in key and "Outside" not in key:
                rent_private = val
            elif "1 Bedroom" in key and "Outside" in key:
                rent_outside = val

        transport = numbeo.get(TRANSPORT_KEY)

        # Utilities — key may be truncated
        utilities = None
        for key, val in numbeo.items():
            if "Basic Utilities" in key:
                utilities = val
                break

        # Internet
        internet = None
        for key, val in numbeo.items():
            if "Broadband Internet" in key or "Internet" in key:
                internet = val
                break

        # Meal price for food estimate
        meal_price = numbeo.get(MEAL_KEY)
        food = _estimate_food_monthly(meal_price)

        # Salary
        salary = None
        for key, val in numbeo.items():
            if "Average Monthly Net Salary" in key:
                salary = val
                break

        # Shared rent estimate (split a 1-bed outside city)
        rent_shared_min = _estimate_shared_rent(rent_outside)
        rent_shared_max = rent_outside  # worst case: paying full rent alone

        # Part-time hourly wage
        wage = MIN_WAGES.get(country)

        # Budget calculations
        monthly_min = sum(filter(None, [
            rent_shared_min,            # cheapest rent option
            food * 0.7 if food else 0,  # frugal food budget
            transport,
            utilities * 0.5 if utilities else 0,  # split with flatmate
            internet * 0.5 if internet else 0,     # split with flatmate
        ])) or None

        monthly_max = sum(filter(None, [
            rent_private,    # private 1-bed in city
            food,            # normal food budget
            transport,
            utilities,
            internet,
        ])) or None

        try:
            return CostOfLiving(
                city=city,
                country=country,
                rent_shared_min=rent_shared_min,
                rent_shared_max=rent_shared_max,
                rent_private_min=rent_outside,
                rent_private_max=rent_private,
                food_monthly=food,
                transport_monthly=transport,
                utilities_monthly=utilities,
                internet_monthly=internet,
                total_monthly_min=round(monthly_min, 2) if monthly_min else None,
                total_monthly_max=round(monthly_max, 2) if monthly_max else None,
                currency=currency,
                part_time_wage_hourly=wage,
                last_updated=datetime.utcnow(),
            )
        except Exception as exc:
            log.error(
                "cost_build_failed",
                city=city,
                error=str(exc),
            )
            return None

    async def _upsert_cost(self, cost: CostOfLiving):
        """Upsert cost of living into Supabase."""
        try:
            from src.database.client import get_db
            db = get_db()
            data = cost.model_dump(exclude_none=True)
            data.pop("id", None)
            db.table("cost_of_living").upsert(
                data, on_conflict="city,country"
            ).execute()
        except Exception as e:
            log.error("cost_upsert_failed", city=cost.city, error=str(e))
