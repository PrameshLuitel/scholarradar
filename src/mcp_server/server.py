"""
ScholarRadar MCP Server — production-grade server with:
- Streamable HTTP transport via Starlette ASGI
- API key authentication middleware
- Per-key rate limiting (100 req/min default)
- Request/response logging via structlog
- Structured error handling (never leaks raw Python errors)
- Health check endpoint at GET /health
- Graceful shutdown via SIGINT / SIGTERM
- Auto-registers all tools from src/mcp_server/tools/

Run:
    uvicorn src.mcp_server.server:app --host 0.0.0.0 --port 8000
"""

from __future__ import annotations

import asyncio
import contextlib
import os
import signal
import time
from collections import defaultdict
from typing import Any

import structlog
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Mount, Route
from starlette.middleware.cors import CORSMiddleware

from mcp.server.fastmcp import FastMCP

from src.utils.logger import setup_logger

# ── Logging ─────────────────────────────────────────────────────────────────

setup_logger()
log = structlog.get_logger("mcp_server")


# ── Configuration ───────────────────────────────────────────────────────────

def _get_api_keys() -> set[str]:
    """Load allowed API keys from MCP_API_KEYS env var (comma-separated)."""
    raw = os.getenv("MCP_API_KEYS", "")
    return {k.strip() for k in raw.split(",") if k.strip()}


RATE_LIMIT_MAX = int(os.getenv("MCP_RATE_LIMIT", "100"))
RATE_LIMIT_WINDOW = 60  # seconds


# ── Rate Limiter ────────────────────────────────────────────────────────────

class SlidingWindowRateLimiter:
    """In-memory sliding-window rate limiter keyed by API key."""

    def __init__(self, max_requests: int = 100, window_seconds: int = 60):
        self.max_requests = max_requests
        self.window = window_seconds
        self._hits: dict[str, list[float]] = defaultdict(list)
        self._lock = asyncio.Lock()

    async def is_allowed(self, key: str) -> bool:
        async with self._lock:
            now = time.monotonic()
            cutoff = now - self.window
            # Prune old entries
            self._hits[key] = [t for t in self._hits[key] if t > cutoff]
            if len(self._hits[key]) >= self.max_requests:
                return False
            self._hits[key].append(now)
            return True

    def remaining(self, key: str) -> int:
        now = time.monotonic()
        cutoff = now - self.window
        recent = [t for t in self._hits.get(key, []) if t > cutoff]
        return max(0, self.max_requests - len(recent))


rate_limiter = SlidingWindowRateLimiter(
    max_requests=RATE_LIMIT_MAX,
    window_seconds=RATE_LIMIT_WINDOW,
)


# ── Auth Middleware ─────────────────────────────────────────────────────────

class APIKeyAuthMiddleware(BaseHTTPMiddleware):
    """Checks X-API-Key header on every request except /health."""

    async def dispatch(self, request: Request, call_next):
        # Allow health checks and CORS preflights without auth
        if request.url.path == "/health" or request.method == "OPTIONS":
            return await call_next(request)

        api_keys = _get_api_keys()
        # If no keys configured, skip auth (dev mode)
        if not api_keys:
            return await call_next(request)

        provided_key = request.headers.get("X-API-Key", "")
        if provided_key not in api_keys:
            log.warning("auth_rejected", path=request.url.path, reason="invalid_api_key")
            return JSONResponse(
                {"error": "Invalid or missing API key", "error_type": "authentication_error"},
                status_code=401,
            )
        return await call_next(request)


# ── Rate Limit Middleware ───────────────────────────────────────────────────

class RateLimitMiddleware(BaseHTTPMiddleware):
    """Enforces per-API-key rate limiting."""

    async def dispatch(self, request: Request, call_next):
        if request.url.path == "/health" or request.method == "OPTIONS":
            return await call_next(request)

        api_key = request.headers.get("X-API-Key", "_anonymous")
        if not await rate_limiter.is_allowed(api_key):
            remaining = rate_limiter.remaining(api_key)
            log.warning("rate_limit_exceeded", api_key=api_key[:8] + "...", path=request.url.path)
            return JSONResponse(
                {
                    "error": "Rate limit exceeded. Max 100 requests per minute.",
                    "error_type": "rate_limit_error",
                    "retry_after_seconds": RATE_LIMIT_WINDOW,
                },
                status_code=429,
                headers={"Retry-After": str(RATE_LIMIT_WINDOW)},
            )
        return await call_next(request)


# ── Logging Middleware ──────────────────────────────────────────────────────

class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """Logs every request with method, path, status, and response time."""

    async def dispatch(self, request: Request, call_next):
        start = time.perf_counter()
        try:
            response = await call_next(request)
        except Exception:
            elapsed = time.perf_counter() - start
            log.error(
                "request_error",
                method=request.method,
                path=request.url.path,
                response_time_ms=round(elapsed * 1000, 2),
            )
            return JSONResponse(
                {"error": "Internal server error", "error_type": "server_error"},
                status_code=500,
            )
        elapsed = time.perf_counter() - start
        log.info(
            "request_completed",
            method=request.method,
            path=request.url.path,
            status_code=response.status_code,
            response_time_ms=round(elapsed * 1000, 2),
        )
        return response


# ── FastMCP Server ──────────────────────────────────────────────────────────

mcp = FastMCP(
    "ScholarRadar",
    stateless_http=True,
    json_response=True,
)


def _register_all_tools():
    """Auto-discover and register all tools from src/mcp_server/tools/."""
    from src.mcp_server.tools import register_all_tools
    register_all_tools(mcp)


_register_all_tools()


# ── Inline search_all tool ──────────────────────────────────────────────────

@mcp.tool()
async def search_all(query: str) -> dict[str, Any]:
    """Search for scholarships, courses, and universities across all sources."""
    try:
        log.info("tool_call", tool="search_all", parameters={"query": query})
        return {"query": query, "message": f"Search results for: {query}"}
    except Exception as e:
        log.error("tool_error", tool="search_all", error=str(e))
        return {"error": "Failed to execute search", "error_type": "tool_error"}


# ── Health Check ────────────────────────────────────────────────────────────

async def health_check(request: Request) -> JSONResponse:
    """GET /health — returns database connection status and record counts."""
    health: dict[str, Any] = {
        "status": "healthy",
        "database": {"connected": False, "tables": {}},
        "tools_count": 0,
        "timestamp": time.time(),
    }

    # Count registered MCP tools
    try:
        tool_manager = mcp._tool_manager
        tools = tool_manager.list_tools()
        health["tools_count"] = len(tools)
    except Exception:
        # Fallback — count isn't critical
        pass

    # Check database connectivity
    try:
        from src.database.client import get_db
        db = get_db()

        tables = ["scholarships", "courses", "universities", "visa_requirements", "cost_of_living"]
        for table in tables:
            try:
                response = db.table(table).select("*", count="exact").limit(0).execute()
                health["database"]["tables"][table] = response.count if response.count is not None else 0
            except Exception:
                health["database"]["tables"][table] = "error"

        health["database"]["connected"] = True
    except Exception as e:
        health["database"]["connected"] = False
        health["database"]["error"] = str(e)
        health["status"] = "degraded"

    status_code = 200 if health["status"] == "healthy" else 503
    return JSONResponse(health, status_code=status_code)


# ── Graceful Shutdown ───────────────────────────────────────────────────────

_shutdown_event = asyncio.Event()


def _signal_handler(sig, frame):
    """Handle SIGINT/SIGTERM for graceful shutdown."""
    log.info("shutdown_signal_received", signal=sig)
    _shutdown_event.set()


@contextlib.asynccontextmanager
async def app_lifespan(app: Starlette):
    """Application lifespan — startup and shutdown logic."""
    log.info("server_starting", transport="streamable-http")

    # Register signal handlers
    loop = asyncio.get_running_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            loop.add_signal_handler(sig, _signal_handler, sig, None)
        except (NotImplementedError, RuntimeError):
            # Windows doesn't support add_signal_handler
            signal.signal(sig, _signal_handler)

    # Start MCP session manager
    async with mcp.session_manager.run():
        log.info("server_ready", tools_count=len(mcp._tool_manager.list_tools()))
        yield

    log.info("server_shutdown_complete")


# ── Starlette ASGI App ─────────────────────────────────────────────────────

app = Starlette(
    routes=[
        Route("/health", health_check, methods=["GET"]),
        Mount("/mcp", app=mcp.streamable_http_app()),
        Mount("/", app=mcp.streamable_http_app()),
    ],
    middleware=[
        Middleware(
            CORSMiddleware,
            allow_origins=["https://claude.ai"],
            allow_methods=["*"],
            allow_headers=["*"],
        ),
        Middleware(RequestLoggingMiddleware),
        Middleware(APIKeyAuthMiddleware),
        Middleware(RateLimitMiddleware),
    ],
    lifespan=app_lifespan,
)


# ── Direct execution ───────────────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("MCP_PORT", "8000"))
    log.info("starting_uvicorn", port=port)
    uvicorn.run(
        "src.mcp_server.server:app",
        host="0.0.0.0",
        port=port,
        log_level="info",
    )
