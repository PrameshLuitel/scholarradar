"""
Production-grade async base scraper with retry logic, rate limiting,
user-agent rotation, robots.txt compliance, and structured logging.
"""

import asyncio
import time
import random
import ssl
from abc import ABC, abstractmethod
from typing import Optional, Dict
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser

import httpx
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
    before_sleep_log,
)
import structlog

from src.utils.logger import logger

# ---------------------------------------------------------------------------
# User-Agent pool — realistic desktop browsers
# ---------------------------------------------------------------------------
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
]

# Errors we want tenacity to retry on
RETRYABLE_STATUS_CODES = {429, 503}


class _RetryableHTTPError(Exception):
    """Raised internally to trigger tenacity retries on specific status codes."""

    def __init__(self, status_code: int, url: str):
        self.status_code = status_code
        self.url = url
        super().__init__(f"HTTP {status_code} for {url}")


# ---------------------------------------------------------------------------
# Per-domain rate limiter
# ---------------------------------------------------------------------------
class DomainRateLimiter:
    """Ensures at most 1 request per `interval` seconds for each domain."""

    def __init__(self, interval: float = 2.0):
        self.interval = interval
        self._last_request: Dict[str, float] = {}
        self._locks: Dict[str, asyncio.Lock] = {}

    def _lock_for(self, domain: str) -> asyncio.Lock:
        if domain not in self._locks:
            self._locks[domain] = asyncio.Lock()
        return self._locks[domain]

    async def wait(self, url: str) -> None:
        domain = urlparse(url).netloc
        lock = self._lock_for(domain)
        async with lock:
            last = self._last_request.get(domain, 0.0)
            elapsed = time.monotonic() - last
            if elapsed < self.interval:
                await asyncio.sleep(self.interval - elapsed)
            self._last_request[domain] = time.monotonic()


# ---------------------------------------------------------------------------
# Robots.txt checker
# ---------------------------------------------------------------------------
class RobotsChecker:
    """Caches and checks robots.txt per domain."""

    def __init__(self):
        self._cache: Dict[str, RobotFileParser] = {}

    async def is_allowed(self, url: str, user_agent: str = "*") -> bool:
        parsed = urlparse(url)
        domain = f"{parsed.scheme}://{parsed.netloc}"

        if domain not in self._cache:
            rp = RobotFileParser()
            robots_url = f"{domain}/robots.txt"
            try:
                async with httpx.AsyncClient(timeout=10.0) as client:
                    resp = await client.get(robots_url)
                    if resp.status_code == 200:
                        rp.parse(resp.text.splitlines())
                    else:
                        # If robots.txt is missing / inaccessible, allow everything
                        rp.parse([])
            except Exception:
                rp.parse([])
            self._cache[domain] = rp

        return self._cache[domain].can_fetch(user_agent, url)


# ---------------------------------------------------------------------------
# Base Scraper
# ---------------------------------------------------------------------------
class BaseScraper(ABC):
    """
    Production async scraper base class.

    Features
    --------
    * httpx async client with session reuse
    * Exponential-backoff retry (max 3 attempts) via tenacity
    * Per-domain rate limiting (1 req / 2 s)
    * Rotating realistic User-Agent headers
    * robots.txt compliance
    * Graceful handling of 429, 403, 503, timeouts, SSL errors
    * Structured logging of every request
    * verify_url() helper to check link liveness
    """

    def __init__(
        self,
        base_url: str,
        rate_limit_interval: float = 2.0,
        timeout: float = 30.0,
    ):
        self.base_url = base_url
        self.timeout = timeout
        self._rate_limiter = DomainRateLimiter(interval=rate_limit_interval)
        self._robots = RobotsChecker()
        self._client: Optional[httpx.AsyncClient] = None
        self._log = structlog.get_logger().bind(scraper=self.__class__.__name__)

    # -- lifecycle -----------------------------------------------------------

    async def _get_client(self) -> httpx.AsyncClient:
        """Lazy-create and reuse a single httpx.AsyncClient (session reuse)."""
        if self._client is None or self._client.is_closed:
            self._client = httpx.AsyncClient(
                timeout=httpx.Timeout(self.timeout),
                follow_redirects=True,
                limits=httpx.Limits(
                    max_connections=40,
                    max_keepalive_connections=20,
                ),
            )
        return self._client

    async def close(self) -> None:
        if self._client and not self._client.is_closed:
            await self._client.aclose()

    # -- user-agent ----------------------------------------------------------

    @staticmethod
    def _random_ua() -> str:
        return random.choice(USER_AGENTS)

    # -- core fetch ----------------------------------------------------------

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        retry=retry_if_exception_type(_RetryableHTTPError),
        reraise=True,
    )
    async def _fetch_with_retry(self, url: str) -> Optional[str]:
        """
        Internal method that httpx-fetches a URL.

        Raises ``_RetryableHTTPError`` on 429/503 so tenacity retries.
        Returns ``None`` for non-retryable failures (403, other errors).
        """
        client = await self._get_client()
        headers = {"User-Agent": self._random_ua()}
        start = time.monotonic()

        try:
            response = await client.get(url, headers=headers)
            elapsed_ms = round((time.monotonic() - start) * 1000, 1)

            await self._log.ainfo(
                "http_request",
                url=url,
                status_code=response.status_code,
                response_time_ms=elapsed_ms,
            )

            if response.status_code in RETRYABLE_STATUS_CODES:
                raise _RetryableHTTPError(response.status_code, url)

            if response.status_code == 403:
                await self._log.awarning("http_forbidden", url=url)
                return None

            response.raise_for_status()
            return response.text

        except _RetryableHTTPError:
            raise  # let tenacity handle
        except httpx.TimeoutException:
            elapsed_ms = round((time.monotonic() - start) * 1000, 1)
            await self._log.aerror("http_timeout", url=url, response_time_ms=elapsed_ms)
            return None
        except ssl.SSLError as exc:
            await self._log.aerror("ssl_error", url=url, error=str(exc))
            return None
        except httpx.ConnectError as exc:
            await self._log.aerror("connection_error", url=url, error=str(exc))
            return None
        except httpx.HTTPStatusError as exc:
            await self._log.aerror(
                "http_error", url=url, status_code=exc.response.status_code
            )
            return None
        except Exception as exc:
            await self._log.aerror("unexpected_error", url=url, error=str(exc))
            return None

    async def fetch(self, url: str) -> Optional[str]:
        """
        Public fetch entry-point.

        1. Checks robots.txt
        2. Applies per-domain rate limiting
        3. Fetches with retry
        4. Returns HTML string or None on failure
        """
        # robots.txt check
        if not await self._robots.is_allowed(url):
            await self._log.awarning("robots_txt_disallowed", url=url)
            return None

        # per-domain rate limit
        await self._rate_limiter.wait(url)

        # fetch with retries (tenacity)
        try:
            return await self._fetch_with_retry(url)
        except _RetryableHTTPError:
            await self._log.aerror("max_retries_exceeded", url=url)
            return None

    # -- link verification ---------------------------------------------------

    async def verify_url(self, url: str) -> bool:
        """
        HEAD-request a URL to check liveness.
        Returns True if the URL responds with a 2xx or 3xx status.
        """
        client = await self._get_client()
        headers = {"User-Agent": self._random_ua()}
        try:
            response = await client.head(url, headers=headers, follow_redirects=True)
            is_alive = response.status_code < 400
            await self._log.ainfo(
                "verify_url",
                url=url,
                status_code=response.status_code,
                is_alive=is_alive,
            )
            return is_alive
        except Exception as exc:
            await self._log.aerror("verify_url_failed", url=url, error=str(exc))
            return False

    # -- abstract ------------------------------------------------------------

    @abstractmethod
    async def scrape(self):
        """Subclasses must implement the scraping logic."""
        ...
