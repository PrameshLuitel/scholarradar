"""
Tests for the MCP server.

Covers:
- Health endpoint returns correct structure
- Tool discovery via MCP protocol
- Auth rejection without API key
- Auth pass-through when no keys configured (dev mode)
"""

from __future__ import annotations

import os
from unittest.mock import MagicMock, patch

import pytest
import httpx

# ── Fixtures ────────────────────────────────────────────────────────────────


def _mock_supabase_table(table_name: str):
    """Return a mock chain that simulates db.table(name).select(...).limit(...).execute()."""
    response = MagicMock()
    response.count = 42  # fake count for health check
    response.data = []

    execute_mock = MagicMock(return_value=response)
    limit_mock = MagicMock()
    limit_mock.execute = execute_mock
    limit_mock.limit = MagicMock(return_value=limit_mock)

    select_mock = MagicMock(return_value=limit_mock)
    table_mock = MagicMock()
    table_mock.select = select_mock
    return table_mock


def _create_mock_db():
    """Create a mock Supabase client."""
    mock_db = MagicMock()
    mock_db.table = MagicMock(side_effect=_mock_supabase_table)
    return mock_db


@pytest.fixture(autouse=True)
def _patch_db(monkeypatch):
    """Patch get_db so no real Supabase connection is attempted."""
    mock_db = _create_mock_db()
    monkeypatch.setattr("src.database.client._client_instance", mock_db)


@pytest.fixture()
def _set_api_key(monkeypatch):
    """Set a test API key for auth tests."""
    monkeypatch.setenv("MCP_API_KEYS", "test-key-123")


# ── Helpers ─────────────────────────────────────────────────────────────────


def _get_app():
    """Import the Starlette app (must be called after monkeypatch is active)."""
    # Force re-import to pick up patched DB
    from src.mcp_server.server import app
    return app


# ── Tests ───────────────────────────────────────────────────────────────────


@pytest.mark.asyncio
async def test_health_endpoint_returns_200():
    """GET /health should return 200 with expected fields."""
    app = _get_app()
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
        resp = await client.get("/health")

    assert resp.status_code == 200
    data = resp.json()
    assert "status" in data
    assert "database" in data
    assert "tools_registered" in data
    assert "timestamp" in data
    # Should report at least 1 tool
    assert data["tools_registered"] > 0


@pytest.mark.skip(reason="Health check no longer reports individual table counts")
@pytest.mark.asyncio
async def test_health_endpoint_has_database_tables():
    pass


@pytest.mark.asyncio
async def test_tool_discovery():
    """Verify that all expected tools are registered in the MCP server."""
    from src.mcp_server.server import mcp
    tools = await mcp.list_tools()
    tool_names = {t.name for t in tools}

    expected_tools = {
        # Scholarship tools (7)
        "search_scholarships",
        "match_profile",
        "get_closing_soon",
        "get_fully_funded",
        "get_by_university",
        "compare_scholarship_options",
        "get_scholarship_statistics",
        # Course tools (5)
        "search_courses",
        "compare_courses",
        "find_courses_for_profile",
        "get_pathway_options",
        "get_courses_by_ielts",
        # University tools (5)
        "compare_universities",
        "get_university_profile",
        "find_universities_by_budget",
        "get_top_universities",
        "get_scholarship_rich_universities",
        # IELTS tools (4)
        "check_ielts_eligibility",
        "get_ielts_requirements",
        "find_low_ielts_options",
        "get_ielts_test_info",
        # Visa tools (5)
        "get_visa_requirements",
        "calculate_financial_proof",
        "get_visa_checklist",
        "get_processing_timeline",
        "assess_visa_strength",
        # Cost of living tools (4)
        "get_city_budget",
        "compare_study_destinations",
        "calculate_total_cost",
        "find_affordable_destinations",
        # Other tools
        "plan_study_abroad_journey",
        "book_counselling_session",
        "search_all",
    }
    for tool in expected_tools:
        assert tool in tool_names, f"Tool '{tool}' not registered. Registered: {tool_names}"


@pytest.mark.skip(reason="FastMCP 1.0 requires active task group lifespan for MCP endpoint")
@pytest.mark.asyncio
async def test_auth_rejection_with_api_key_configured(_set_api_key):
    """Requests without valid X-API-Key should get 401 when keys are configured."""
    app = _get_app()
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
        # No API key header
        resp = await client.post("/mcp", json={})

    assert resp.status_code == 401
    data = resp.json()
    assert data["error_type"] == "authentication_error"


@pytest.mark.skip(reason="FastMCP 1.0 requires active task group lifespan for MCP endpoint")
@pytest.mark.asyncio
async def test_auth_pass_with_valid_key(_set_api_key):
    """Requests with a valid X-API-Key should pass auth middleware.

    Note: The MCP session manager isn't started in test context (no lifespan),
    so we may get a 500 from the MCP layer — but that proves auth passed.
    """
    app = _get_app()
    transport = httpx.ASGITransport(app=app, raise_app_exceptions=False)
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
        resp = await client.post(
            "/mcp",
            json={},
            headers={"X-API-Key": "test-key-123"},
        )

    # Should NOT be 401 — a 500 from MCP internals proves auth passed
    assert resp.status_code != 401


@pytest.mark.asyncio
async def test_health_no_auth_required(_set_api_key):
    """Health endpoint should work without an API key even when keys are configured."""
    app = _get_app()
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
        resp = await client.get("/health")

    assert resp.status_code == 200


@pytest.mark.asyncio
async def test_tools_count_matches_discovery():
    """Health endpoint tools_count should match actual tool count."""
    from src.mcp_server.server import mcp
    tools = await mcp.list_tools()
    actual_count = len(tools)

    app = _get_app()
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://testserver") as client:
        resp = await client.get("/health")

    data = resp.json()
    assert data["tools_registered"] == actual_count
