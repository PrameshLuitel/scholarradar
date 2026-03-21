"""
Unit tests for ScholarRadar scrapers.

- BaseScraper tests (retry, error handling, rate limiting, robots, verify_url)
- IDPScholarshipScraper tests (real HTML fixture parsing, award/deadline/funding
  parsers, detail page extraction, full build+validate)

All network calls mocked.  HTML fixtures match the REAL idp.com structure.
"""

import time
import pytest
import httpx

from pathlib import Path
from unittest.mock import AsyncMock, patch, MagicMock

from src.scrapers.base_scraper import BaseScraper, DomainRateLimiter
from src.scrapers.idp_scholarships import (
    IDPScholarshipScraper,
    _parse_award_value,
    _parse_deadline,
    _parse_funding_type,
)

FIXTURES = Path(__file__).parent / "fixtures"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _mock_response(status_code: int = 200, text: str = "<html></html>"):
    resp = MagicMock(spec=httpx.Response)
    resp.status_code = status_code
    resp.text = text
    resp.raise_for_status = MagicMock()
    if status_code >= 400:
        resp.raise_for_status.side_effect = httpx.HTTPStatusError(
            message=f"{status_code}", request=MagicMock(), response=resp
        )
    return resp


class _TestScraper(BaseScraper):
    async def scrape(self):
        return await self.fetch(self.base_url)


# ===================================================================
# BaseScraper — Retry Logic
# ===================================================================
class TestRetryLogic:
    @pytest.mark.asyncio
    async def test_retries_on_503_then_succeeds(self):
        scraper = _TestScraper("https://example.com", rate_limit_interval=0.0)
        client = AsyncMock(spec=httpx.AsyncClient)
        client.is_closed = False
        resp_503 = _mock_response(503)
        resp_503.raise_for_status = MagicMock()
        resp_200 = _mock_response(200, "<html>OK</html>")
        client.get = AsyncMock(side_effect=[resp_503, resp_200])
        scraper._client = client

        with patch.object(scraper._robots, "is_allowed", return_value=True):
            result = await scraper.fetch("https://example.com/page")
        assert result == "<html>OK</html>"
        assert client.get.call_count == 2

    @pytest.mark.asyncio
    async def test_retries_on_429_then_succeeds(self):
        scraper = _TestScraper("https://example.com", rate_limit_interval=0.0)
        client = AsyncMock(spec=httpx.AsyncClient)
        client.is_closed = False
        resp_429 = _mock_response(429)
        resp_429.raise_for_status = MagicMock()
        resp_200 = _mock_response(200, "<html>Finally</html>")
        client.get = AsyncMock(side_effect=[resp_429, resp_429, resp_200])
        scraper._client = client

        with patch.object(scraper._robots, "is_allowed", return_value=True):
            result = await scraper.fetch("https://example.com/page")
        assert result == "<html>Finally</html>"
        assert client.get.call_count == 3

    @pytest.mark.asyncio
    async def test_max_retries_returns_none(self):
        scraper = _TestScraper("https://example.com", rate_limit_interval=0.0)
        client = AsyncMock(spec=httpx.AsyncClient)
        client.is_closed = False
        resp_503 = _mock_response(503)
        resp_503.raise_for_status = MagicMock()
        client.get = AsyncMock(return_value=resp_503)
        scraper._client = client

        with patch.object(scraper._robots, "is_allowed", return_value=True):
            result = await scraper.fetch("https://example.com/page")
        assert result is None
        assert client.get.call_count == 3


# ===================================================================
# BaseScraper — Error Handling
# ===================================================================
class TestErrorHandling:
    @pytest.mark.asyncio
    async def test_403_returns_none_no_retry(self):
        scraper = _TestScraper("https://example.com", rate_limit_interval=0.0)
        client = AsyncMock(spec=httpx.AsyncClient)
        client.is_closed = False
        resp_403 = _mock_response(403)
        resp_403.raise_for_status = MagicMock()
        client.get = AsyncMock(return_value=resp_403)
        scraper._client = client

        with patch.object(scraper._robots, "is_allowed", return_value=True):
            result = await scraper.fetch("https://example.com/forbidden")
        assert result is None
        assert client.get.call_count == 1

    @pytest.mark.asyncio
    async def test_timeout_returns_none(self):
        scraper = _TestScraper("https://example.com", rate_limit_interval=0.0)
        client = AsyncMock(spec=httpx.AsyncClient)
        client.is_closed = False
        client.get = AsyncMock(side_effect=httpx.TimeoutException("timed out"))
        scraper._client = client

        with patch.object(scraper._robots, "is_allowed", return_value=True):
            result = await scraper.fetch("https://example.com/slow")
        assert result is None

    @pytest.mark.asyncio
    async def test_connection_error_returns_none(self):
        scraper = _TestScraper("https://example.com", rate_limit_interval=0.0)
        client = AsyncMock(spec=httpx.AsyncClient)
        client.is_closed = False
        client.get = AsyncMock(side_effect=httpx.ConnectError("refused"))
        scraper._client = client

        with patch.object(scraper._robots, "is_allowed", return_value=True):
            result = await scraper.fetch("https://example.com/down")
        assert result is None


# ===================================================================
# BaseScraper — Rate Limiting
# ===================================================================
class TestRateLimiting:
    @pytest.mark.asyncio
    async def test_enforces_delay_same_domain(self):
        limiter = DomainRateLimiter(interval=0.3)
        start = time.monotonic()
        await limiter.wait("https://example.com/a")
        await limiter.wait("https://example.com/b")
        assert time.monotonic() - start >= 0.25

    @pytest.mark.asyncio
    async def test_no_delay_different_domains(self):
        limiter = DomainRateLimiter(interval=1.0)
        start = time.monotonic()
        await limiter.wait("https://a.com/x")
        await limiter.wait("https://b.com/y")
        assert time.monotonic() - start < 0.5


# ===================================================================
# BaseScraper — Robots.txt
# ===================================================================
class TestRobotsTxt:
    @pytest.mark.asyncio
    async def test_disallowed_returns_none(self):
        scraper = _TestScraper("https://example.com", rate_limit_interval=0.0)
        client = AsyncMock(spec=httpx.AsyncClient)
        client.is_closed = False
        scraper._client = client

        with patch.object(scraper._robots, "is_allowed", return_value=False):
            result = await scraper.fetch("https://example.com/private")
        assert result is None
        client.get.assert_not_called()


# ===================================================================
# BaseScraper — verify_url
# ===================================================================
class TestVerifyUrl:
    @pytest.mark.asyncio
    async def test_alive(self):
        scraper = _TestScraper("https://example.com", rate_limit_interval=0.0)
        client = AsyncMock(spec=httpx.AsyncClient)
        client.is_closed = False
        client.head = AsyncMock(return_value=_mock_response(200))
        scraper._client = client
        assert await scraper.verify_url("https://example.com/s") is True

    @pytest.mark.asyncio
    async def test_dead(self):
        scraper = _TestScraper("https://example.com", rate_limit_interval=0.0)
        client = AsyncMock(spec=httpx.AsyncClient)
        client.is_closed = False
        client.head = AsyncMock(return_value=_mock_response(404))
        scraper._client = client
        assert await scraper.verify_url("https://example.com/gone") is False

    @pytest.mark.asyncio
    async def test_error_returns_false(self):
        scraper = _TestScraper("https://example.com", rate_limit_interval=0.0)
        client = AsyncMock(spec=httpx.AsyncClient)
        client.is_closed = False
        client.head = AsyncMock(side_effect=httpx.ConnectError("down"))
        scraper._client = client
        assert await scraper.verify_url("https://example.com/x") is False


# ===================================================================
# IDP — Award Value Parser (real IDP strings)
# ===================================================================
class TestAwardValueParser:
    def test_eur_single(self):
        r = _parse_award_value("Value of award: 2000 EUR")
        assert r["award_currency"] == "EUR"
        assert r["award_value_min"] == 2000.0
        assert r["award_value_max"] == 2000.0

    def test_eur_range(self):
        r = _parse_award_value("Value of award: 2000 to 5000 EUR")
        assert r["award_currency"] == "EUR"
        assert r["award_value_min"] == 2000.0
        assert r["award_value_max"] == 5000.0

    def test_aud_up_to(self):
        r = _parse_award_value("Value of award: Up to AUD 40,000")
        assert r["award_currency"] == "AUD"
        assert r["award_value_min"] is None
        assert r["award_value_max"] == 40000.0

    def test_gbp_symbol(self):
        r = _parse_award_value("Value of award: £15,000")
        assert r["award_currency"] == "GBP"
        assert r["award_value_min"] == 15000.0

    def test_empty(self):
        r = _parse_award_value("")
        assert r["award_currency"] is None

    def test_none(self):
        r = _parse_award_value(None)
        assert r["award_currency"] is None


# ===================================================================
# IDP — Deadline Parser (real IDP strings)
# ===================================================================
class TestDeadlineParser:
    def test_real_idp_format(self):
        d = _parse_deadline("Deadline:01 Apr 2026")
        assert d is not None
        assert d.year == 2026
        assert d.month == 4
        assert d.day == 1

    def test_with_space(self):
        d = _parse_deadline("Deadline: 15 Jul 2026")
        assert d is not None
        assert d.month == 7

    def test_iso(self):
        d = _parse_deadline("2026-07-15")
        assert d is not None

    def test_invalid(self):
        assert _parse_deadline("not a date") is None

    def test_empty(self):
        assert _parse_deadline("") is None

    def test_none(self):
        assert _parse_deadline(None) is None


# ===================================================================
# IDP — Funding Type Parser (real IDP strings)
# ===================================================================
class TestFundingTypeParser:
    def test_fee_waiver(self):
        assert _parse_funding_type("Funding type: Fee waiver/discount") == "fee_waiver"

    def test_full(self):
        assert _parse_funding_type("Funding type: Full tuition") == "full"

    def test_none(self):
        assert _parse_funding_type(None) is None

    def test_empty(self):
        assert _parse_funding_type("") is None


# ===================================================================
# IDP — Listing Page Parser (real HTML fixture)
# ===================================================================
class TestIDPListingParser:
    @pytest.fixture
    def listing_html(self) -> str:
        return (FIXTURES / "idp_listing.html").read_text()

    def test_parses_all_cards(self, listing_html):
        cards = IDPScholarshipScraper._parse_listing(listing_html)
        assert len(cards) == 3

    def test_first_card_title(self, listing_html):
        cards = IDPScholarshipScraper._parse_listing(listing_html)
        assert cards[0]["title"] == "MSc Merit Based Scholarships for non-UCD Students / Graduates"

    def test_first_card_university(self, listing_html):
        cards = IDPScholarshipScraper._parse_listing(listing_html)
        assert cards[0]["university"] == "University College Dublin"

    def test_first_card_detail_url(self, listing_html):
        cards = IDPScholarshipScraper._parse_listing(listing_html)
        assert "/scholarship/" in cards[0]["detail_url"]
        assert "148208" in cards[0]["detail_url"]

    def test_first_card_country(self, listing_html):
        cards = IDPScholarshipScraper._parse_listing(listing_html)
        assert cards[0]["country_text"] == "Ireland"

    def test_first_card_level(self, listing_html):
        cards = IDPScholarshipScraper._parse_listing(listing_html)
        assert cards[0]["level_text"] == "Postgraduate"

    def test_first_card_funding(self, listing_html):
        cards = IDPScholarshipScraper._parse_listing(listing_html)
        assert "Fee waiver" in cards[0]["funding_text"]

    def test_first_card_award(self, listing_html):
        cards = IDPScholarshipScraper._parse_listing(listing_html)
        assert "2000 EUR" in cards[0]["award_text"]

    def test_second_card_deadline(self, listing_html):
        cards = IDPScholarshipScraper._parse_listing(listing_html)
        assert cards[1]["deadline_text"] is not None
        assert "01 Apr 2026" in cards[1]["deadline_text"]

    def test_second_card_award_range(self, listing_html):
        cards = IDPScholarshipScraper._parse_listing(listing_html)
        assert "2000 to 5000 EUR" in cards[1]["award_text"]

    def test_minimal_card_no_deadline(self, listing_html):
        cards = IDPScholarshipScraper._parse_listing(listing_html)
        assert cards[2]["title"] == "Monash Future Leaders Scholarship"
        assert cards[2]["deadline_text"] is None
        assert cards[2]["award_text"] is None


# ===================================================================
# IDP — Detail Page Parser (real HTML fixture)
# ===================================================================
class TestIDPDetailParser:
    @pytest.fixture
    def detail_html(self) -> str:
        return (FIXTURES / "idp_detail.html").read_text()

    @pytest.mark.asyncio
    async def test_extracts_overview(self, detail_html):
        scraper = IDPScholarshipScraper(save_to_db=False, rate_limit_interval=0.0)
        card = {"detail_url": "https://www.idp.com/scholarship/test/148208/"}

        with patch.object(scraper, "fetch", return_value=detail_html):
            detail = await scraper._fetch_detail(card)

        assert detail["description"] is not None
        assert "University College Dublin" in detail["description"]
        assert "2000 EUR" in detail["description"]

    @pytest.mark.asyncio
    async def test_extracts_eligibility(self, detail_html):
        scraper = IDPScholarshipScraper(save_to_db=False, rate_limit_interval=0.0)
        card = {"detail_url": "https://www.idp.com/scholarship/test/148208/"}

        with patch.object(scraper, "fetch", return_value=detail_html):
            detail = await scraper._fetch_detail(card)

        assert detail["eligibility"] is not None
        assert "Academic excellence" in detail["eligibility"]

    @pytest.mark.asyncio
    async def test_extracts_application_process(self, detail_html):
        scraper = IDPScholarshipScraper(save_to_db=False, rate_limit_interval=0.0)
        card = {"detail_url": "https://www.idp.com/scholarship/test/148208/"}

        with patch.object(scraper, "fetch", return_value=detail_html):
            detail = await scraper._fetch_detail(card)

        assert detail["application_process"] is not None
        assert "programme application" in detail["application_process"]

    @pytest.mark.asyncio
    async def test_extracts_apply_url(self, detail_html):
        scraper = IDPScholarshipScraper(save_to_db=False, rate_limit_interval=0.0)
        card = {"detail_url": "https://www.idp.com/scholarship/test/148208/"}

        with patch.object(scraper, "fetch", return_value=detail_html):
            detail = await scraper._fetch_detail(card)

        assert detail["apply_url"] is not None
        assert "apply" in detail["apply_url"].lower()


# ===================================================================
# IDP — Full Build + Pydantic Validation
# ===================================================================
class TestIDPBuildScholarship:
    def test_builds_valid_scholarship_from_real_data(self):
        scraper = IDPScholarshipScraper(save_to_db=False)
        card = {
            "title": "MSc Merit Based Scholarships for non-UCD Students / Graduates",
            "university": "University College Dublin",
            "detail_url": "https://www.idp.com/scholarship/ucd/msc-merit/148208/",
            "country_text": "Ireland",
            "level_text": "Postgraduate",
            "funding_text": "Funding type: Fee waiver/discount",
            "deadline_text": "Deadline:01 Apr 2026",
            "award_text": "Value of award: 2000 EUR",
        }
        detail = {
            "description": "A number of €2,000 scholarships toward tuition fees.",
            "eligibility": "Academic excellence. All international.",
            "application_process": "Submit programme application before deadline.",
            "apply_url": "https://scholarships.ucd.ie/apply",
        }
        result = scraper._build_scholarship(card, detail, "ireland", "postgraduate")

        assert result is not None
        assert result.title == card["title"]
        assert result.university == card["university"]
        assert result.country == "ireland"
        assert result.study_level == "postgraduate"
        assert result.funding_type == "fee_waiver"
        assert result.award_value_min == 2000.0
        assert result.award_value_max == 2000.0
        assert result.award_currency == "EUR"
        assert result.source == "idp"
        assert result.is_active is True
        assert result.deadline is not None
        assert result.deadline.month == 4

    def test_builds_with_range_award(self):
        scraper = IDPScholarshipScraper(save_to_db=False)
        card = {
            "title": "Global Excellence",
            "university": "Trinity College Dublin",
            "detail_url": "https://www.idp.com/scholarship/test/129919/",
            "country_text": "Ireland",
            "level_text": "Undergraduate",
            "funding_text": "Funding type: Fee waiver/discount",
            "deadline_text": None,
            "award_text": "Value of award: 2000 to 5000 EUR",
        }
        detail = {"description": "Test", "eligibility": None, "application_process": None, "apply_url": None}
        result = scraper._build_scholarship(card, detail, "ireland", "undergraduate")

        assert result is not None
        assert result.award_value_min == 2000.0
        assert result.award_value_max == 5000.0

    def test_returns_none_on_missing_title(self):
        scraper = IDPScholarshipScraper(save_to_db=False)
        card = {
            "title": None,
            "university": "X",
            "detail_url": None,
            "country_text": None,
            "level_text": None,
            "funding_text": None,
            "deadline_text": None,
            "award_text": None,
        }
        result = scraper._build_scholarship(card, {}, "uk", "undergraduate")
        assert result is None


# ===================================================================
# IDP — URL Builder
# ===================================================================
class TestIDPUrlBuilder:
    def test_page_1(self):
        scraper = IDPScholarshipScraper(save_to_db=False, locale="nepal")
        url = scraper._build_url("australia", "postgraduate", 1)
        assert "nepal/find-a-scholarship" in url
        assert "country=australia" in url
        assert "level=postgraduate" in url
        assert "page=" not in url  # page=1 is omitted

    def test_page_2(self):
        scraper = IDPScholarshipScraper(save_to_db=False, locale="nepal")
        url = scraper._build_url("uk", "doctorate", 2)
        assert "page=2" in url
