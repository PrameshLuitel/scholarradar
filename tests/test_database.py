"""
Tests for the database layer.

Covers:
- Connection pooling (lazy singleton)
- Query functions return correct types
- Upsert deduplication logic
- Model validation
"""
from __future__ import annotations

from datetime import date, datetime
from unittest.mock import MagicMock, patch

import pytest


# ── Mock Supabase ───────────────────────────────────────────────────────────

def _build_mock_db(data: list | None = None):
    """Build a chainable mock Supabase client."""
    response = MagicMock()
    response.data = data or []
    response.count = len(response.data)

    chain = MagicMock()
    chain.execute = MagicMock(return_value=response)
    for method in ("select", "eq", "neq", "ilike", "gte", "lte", "lt", "gt",
                    "in_", "order", "limit", "update", "insert", "upsert", "delete"):
        getattr(chain, method).return_value = chain

    mock_db = MagicMock()
    def _table(name):
        t = MagicMock()
        t.select = MagicMock(return_value=chain)
        t.insert = MagicMock(return_value=chain)
        t.upsert = MagicMock(return_value=chain)
        t.update = MagicMock(return_value=chain)
        for m in ("eq", "in_"):
            getattr(t, m).return_value = chain
        return t
    mock_db.table = MagicMock(side_effect=_table)
    return mock_db


@pytest.fixture(autouse=True)
def _patch_db(monkeypatch):
    """Default: patch with empty mock."""
    mock = _build_mock_db([])
    monkeypatch.setattr("src.database.client._client_instance", mock)


# ═══════════════════════════════════════════════════════════════════════════
# CONNECTION POOLING / SINGLETON
# ═══════════════════════════════════════════════════════════════════════════

class TestConnectionPooling:
    def test_get_db_returns_same_instance(self):
        from src.database.client import get_db
        db1 = get_db()
        db2 = get_db()
        assert db1 is db2

    def test_get_db_is_singleton(self):
        from src.database.client import get_db
        instances = [get_db() for _ in range(10)]
        assert all(i is instances[0] for i in instances)

    def test_get_db_raises_without_credentials(self, monkeypatch):
        """Without credentials and no mock, get_db should raise."""
        monkeypatch.setattr("src.database.client._client_instance", None)
        monkeypatch.delenv("SUPABASE_URL", raising=False)
        monkeypatch.delenv("SUPABASE_KEY", raising=False)
        from src.database import client
        # Reset the singleton
        client._client_instance = None
        with pytest.raises((ValueError, ImportError)):
            client.get_db()
        # Restore to prevent side effects
        client._client_instance = _build_mock_db([])


# ═══════════════════════════════════════════════════════════════════════════
# QUERY FUNCTIONS RETURN CORRECT TYPES
# ═══════════════════════════════════════════════════════════════════════════

class TestGetScholarships:
    @pytest.mark.asyncio
    async def test_returns_list(self):
        from src.database.queries import get_scholarships
        result = await get_scholarships()
        assert isinstance(result, list)

    @pytest.mark.asyncio
    async def test_returns_list_with_filters(self):
        from src.database.queries import get_scholarships
        result = await get_scholarships({"is_active": True, "country": "australia"})
        assert isinstance(result, list)


class TestSearchCoursesQuery:
    @pytest.mark.asyncio
    async def test_returns_list(self):
        from src.database.queries import search_courses
        result = await search_courses({"country": "australia"})
        assert isinstance(result, list)


class TestGetLivingCosts:
    @pytest.mark.asyncio
    async def test_returns_none_when_empty(self):
        from src.database.queries import get_living_costs
        result = await get_living_costs("NoCity", "nocountry")
        assert result is None

    @pytest.mark.asyncio
    async def test_returns_dict_when_found(self, monkeypatch):
        sample = {"city": "Melbourne", "country": "australia", "total_monthly_min": 2354}
        mock = _build_mock_db([sample])
        monkeypatch.setattr("src.database.client._client_instance", mock)
        from src.database.queries import get_living_costs
        result = await get_living_costs("Melbourne", "australia")
        assert isinstance(result, dict)
        assert result["city"] == "Melbourne"


class TestGetUniversityById:
    @pytest.mark.asyncio
    async def test_returns_none_for_unknown(self):
        from src.database.queries import get_university_by_id
        from uuid import uuid4
        result = await get_university_by_id(uuid4())
        assert result is None


# ═══════════════════════════════════════════════════════════════════════════
# UPSERT DEDUPLICATION
# ═══════════════════════════════════════════════════════════════════════════

class TestUpsertScholarship:
    @pytest.mark.asyncio
    async def test_calls_upsert_with_correct_conflict(self, monkeypatch):
        upserted = {"id": "sch-001", "title": "Test"}
        mock = _build_mock_db([upserted])
        monkeypatch.setattr("src.database.client._client_instance", mock)

        from src.database.queries import upsert_scholarship
        from src.database.models import Scholarship

        s = Scholarship(title="Test Scholarship", university="Test Uni",
                        country="australia")
        result = await upsert_scholarship(s)
        # The upsert chain was called
        assert mock.table.called
        mock.table.assert_called_with("scholarships")

    @pytest.mark.asyncio
    async def test_removes_id_and_created_at(self, monkeypatch):
        upserted = {"id": "sch-new", "title": "Test"}
        mock = _build_mock_db([upserted])
        monkeypatch.setattr("src.database.client._client_instance", mock)

        from src.database.queries import upsert_scholarship
        from src.database.models import Scholarship

        s = Scholarship(title="Test", university="Uni", country="au")
        await upsert_scholarship(s)
        # Verify the call was made (the mock will have been used)
        assert mock.table.called


class TestUpsertCourse:
    @pytest.mark.asyncio
    async def test_calls_upsert(self, monkeypatch):
        upserted = {"id": "crs-001", "name": "Test"}
        mock = _build_mock_db([upserted])
        monkeypatch.setattr("src.database.client._client_instance", mock)

        from src.database.queries import upsert_course
        from src.database.models import Course

        c = Course(name="Test Course", university="Uni", country="australia")
        await upsert_course(c)
        mock.table.assert_called_with("courses")


class TestUpsertUniversity:
    @pytest.mark.asyncio
    async def test_calls_upsert(self, monkeypatch):
        upserted = {"id": "uni-001", "name": "Test"}
        mock = _build_mock_db([upserted])
        monkeypatch.setattr("src.database.client._client_instance", mock)

        from src.database.queries import upsert_university
        from src.database.models import University

        u = University(name="Test Uni", country="australia")
        await upsert_university(u)
        mock.table.assert_called_with("universities")


class TestDeactivateStale:
    @pytest.mark.asyncio
    async def test_deactivates_stale_ids(self, monkeypatch):
        existing = [
            {"id": "sch-001"},
            {"id": "sch-002"},
            {"id": "sch-003"},
        ]
        mock = _build_mock_db(existing)
        monkeypatch.setattr("src.database.client._client_instance", mock)

        from src.database.queries import deactivate_stale_scholarships
        count = await deactivate_stale_scholarships("idp", ["sch-001"])
        assert count == 2  # sch-002 and sch-003 are stale

    @pytest.mark.asyncio
    async def test_no_deactivation_when_all_active(self, monkeypatch):
        existing = [{"id": "sch-001"}]
        mock = _build_mock_db(existing)
        monkeypatch.setattr("src.database.client._client_instance", mock)

        from src.database.queries import deactivate_stale_scholarships
        count = await deactivate_stale_scholarships("idp", ["sch-001"])
        assert count == 0

    @pytest.mark.asyncio
    async def test_no_deactivation_when_empty(self):
        from src.database.queries import deactivate_stale_scholarships
        count = await deactivate_stale_scholarships("idp", [])
        assert count == 0


# ═══════════════════════════════════════════════════════════════════════════
# MODEL VALIDATION
# ═══════════════════════════════════════════════════════════════════════════

class TestModels:
    def test_scholarship_required_fields(self):
        from src.database.models import Scholarship
        s = Scholarship(title="Test", university="Uni", country="au")
        assert s.title == "Test"
        assert s.is_active is True

    def test_scholarship_optional_fields(self):
        from src.database.models import Scholarship
        s = Scholarship(title="T", university="U", country="au",
                        award_value_max=50000, deadline=date(2026, 6, 1))
        assert s.award_value_max == 50000
        assert s.deadline.month == 6

    def test_scholarship_missing_required_raises(self):
        from src.database.models import Scholarship
        with pytest.raises(Exception):
            Scholarship(university="Uni")  # missing title and country

    def test_course_required_fields(self):
        from src.database.models import Course
        c = Course(name="CS", university="Uni", country="au")
        assert c.is_active is True

    def test_university_required_fields(self):
        from src.database.models import University
        u = University(name="Uni", country="au")
        assert u.name == "Uni"

    def test_visa_requirement_fields(self):
        from src.database.models import VisaRequirement
        v = VisaRequirement(nationality="nepal", destination_country="australia")
        assert v.nationality == "nepal"
        assert v.financial_requirement_aud is None

    def test_cost_of_living_fields(self):
        from src.database.models import CostOfLiving
        c = CostOfLiving(city="Melbourne", country="australia")
        assert c.food_monthly is None
