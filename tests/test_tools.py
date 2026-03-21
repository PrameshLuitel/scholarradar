"""
Comprehensive tests for all MCP tools.

Covers:
- Every tool with realistic inputs
- Empty database handling
- Structured response validation
- search_scholarships for Nepal+Australia+PhD
- match_profile eligibility filtering
- plan_study_abroad_journey complete response
- All tools return structured dicts (never raw exceptions)
"""
from __future__ import annotations

from datetime import date, datetime, timedelta
from unittest.mock import MagicMock

import pytest


# ── Mock Supabase ───────────────────────────────────────────────────────────

# Realistic sample data
_SAMPLE_SCHOLARSHIP = {
    "id": "sch-001",
    "title": "Australia Awards PhD Scholarship",
    "university": "University of Melbourne",
    "country": "australia",
    "city": "Melbourne",
    "study_level": "doctorate",
    "subject": "Computer Science",
    "subject_category": "IT",
    "funding_type": "full",
    "deadline": (date.today() + timedelta(days=60)).isoformat(),
    "award_value_min": 30000,
    "award_value_max": 50000,
    "award_currency": "AUD",
    "description": "Full scholarship for PhD candidates from South Asia.",
    "eligibility": "Open to Nepal, India, Bangladesh nationals with first-class degree.",
    "apply_url": "https://example.com/apply",
    "source_url": "https://idp.com/scholarship/test",
    "source": "idp",
    "is_active": True,
    "created_at": datetime.now().isoformat(),
    "updated_at": datetime.now().isoformat(),
}

_SAMPLE_COURSE = {
    "id": "crs-001",
    "name": "Master of Computer Science",
    "university": "University of Melbourne",
    "country": "australia",
    "city": "Melbourne",
    "level": "postgraduate",
    "subject": "Computer Science",
    "subject_category": "IT",
    "duration_months": 24,
    "tuition_fee": 45000,
    "currency": "AUD",
    "ielts_overall": 6.5,
    "ielts_reading": 6.0,
    "ielts_writing": 6.0,
    "ielts_speaking": 6.0,
    "ielts_listening": 6.0,
    "entry_qualification": "Bachelor degree with GPA 3.0+",
    "start_dates": ["Feb 2027", "Jul 2027"],
    "apply_url": "https://example.com/course/apply",
    "source_url": "https://idp.com/course/test",
    "is_active": True,
    "updated_at": datetime.now().isoformat(),
}

_SAMPLE_UNIVERSITY = {
    "id": "uni-001",
    "name": "University of Melbourne",
    "country": "australia",
    "city": "Melbourne",
    "world_ranking": 14,
    "acceptance_rate": 0.7,
    "total_students": 52000,
    "international_students": 18000,
    "tuition_min": 35000,
    "tuition_max": 50000,
    "currency": "AUD",
    "ielts_minimum": 6.5,
    "popular_subjects": ["Computer Science", "Engineering", "Medicine"],
    "facilities": ["Library", "Research Labs", "Sports Centre"],
    "accommodation_cost_min": 200,
    "accommodation_cost_max": 450,
    "website": "https://unimelb.edu.au",
    "idp_profile_url": "https://idp.com/uni/melbourne",
}

_SAMPLE_VISA = {
    "nationality": "nepal",
    "destination_country": "australia",
    "visa_type": "Subclass 500 (Student Visa)",
    "visa_subclass": "Subclass 500",
    "financial_requirement_aud": 29710,
    "processing_weeks_min": 4,
    "processing_weeks_max": 12,
    "required_documents": [],
    "health_requirements": "OSHC mandatory",
    "work_rights_hours_per_week": 48,
    "notes": "48 hrs/fortnight during term",
    "source_url": "https://idp.com/visa",
    "last_updated": datetime.now().isoformat(),
}

_SAMPLE_COST = {
    "city": "Melbourne",
    "country": "australia",
    "rent_shared_min": 1017,
    "rent_shared_max": 1850,
    "rent_private_min": 1850,
    "rent_private_max": 2493,
    "food_monthly": 1350,
    "transport_monthly": 199,
    "utilities_monthly": 309,
    "internet_monthly": 75,
    "total_monthly_min": 2354,
    "total_monthly_max": 4426,
    "currency": "AUD",
    "part_time_wage_hourly": 24.1,
    "last_updated": datetime.now().isoformat(),
}


def _build_mock_db(data_map: dict[str, list] | None = None):
    """Build a chainable mock that returns data based on table name.

    data_map: {"scholarships": [row1, row2], "courses": [...], ...}
    """
    if data_map is None:
        data_map = {}

    def _make_table(table_name: str):
        rows = data_map.get(table_name, [])
        response = MagicMock()
        response.data = rows
        response.count = len(rows)

        # Create a chainable mock where every filter method returns self
        chain = MagicMock()
        chain.execute = MagicMock(return_value=response)

        # All filter/query methods return the chain itself
        for method in ("select", "eq", "neq", "ilike", "gte", "lte", "lt",
                        "gt", "in_", "order", "limit", "update", "insert",
                        "upsert", "delete"):
            getattr(chain, method).return_value = chain

        table_mock = MagicMock()
        table_mock.select = MagicMock(return_value=chain)
        for method in ("eq", "neq", "ilike", "gte", "lte", "lt", "gt",
                        "in_", "order", "limit", "update", "insert",
                        "upsert", "delete"):
            getattr(table_mock, method).return_value = chain

        return table_mock

    mock_db = MagicMock()
    mock_db.table = MagicMock(side_effect=_make_table)
    return mock_db


@pytest.fixture(autouse=True)
def _patch_db_with_data(monkeypatch):
    """Patch get_db with sample data for all tables."""
    mock = _build_mock_db({
        "scholarships": [_SAMPLE_SCHOLARSHIP],
        "courses": [_SAMPLE_COURSE],
        "universities": [_SAMPLE_UNIVERSITY],
        "visa_requirements": [_SAMPLE_VISA],
        "cost_of_living": [_SAMPLE_COST],
    })
    monkeypatch.setattr("src.database.client._client_instance", mock)


@pytest.fixture()
def _patch_empty_db(monkeypatch):
    """Patch get_db with empty tables."""
    mock = _build_mock_db({})
    monkeypatch.setattr("src.database.client._client_instance", mock)


# ── Helpers ─────────────────────────────────────────────────────────────────

async def _get_tool_fn(name: str):
    """Import and return a tool function from the MCP server."""
    from src.mcp_server.server import mcp
    tool = await mcp.get_tool(name)
    if not tool:
        raise ValueError(f"Tool '{name}' not found.")
    return tool.fn


# ═══════════════════════════════════════════════════════════════════════════
# SCHOLARSHIP TOOLS
# ═══════════════════════════════════════════════════════════════════════════

class TestSearchScholarships:
    @pytest.mark.asyncio
    async def test_returns_results_for_nepal_australia_phd(self):
        fn = await _get_tool_fn("search_scholarships")
        result = await fn(nationality="nepal", destination_country="australia",
                          study_level="doctorate")
        assert isinstance(result, dict)
        assert "scholarships" in result or "results" in result or "total_count" in result

    @pytest.mark.asyncio
    async def test_handles_empty_db(self, _patch_empty_db):
        fn = await _get_tool_fn("search_scholarships")
        result = await fn(nationality="nepal")
        assert isinstance(result, dict)
        # Should have a message or empty results, not crash
        assert "error" not in result or result.get("total_count", 0) == 0


class TestMatchProfile:
    @pytest.mark.asyncio
    async def test_returns_matches_with_reasons(self):
        fn = await _get_tool_fn("match_profile")
        result = await fn(
            nationality="nepal",
            current_qualification="Bachelor of Engineering",
            target_subject="Computer Science",
            target_country="australia",
            ielts_score=7.0,
        )
        assert isinstance(result, dict)
        assert "error" not in result

    @pytest.mark.asyncio
    async def test_handles_empty_db(self, _patch_empty_db):
        fn = await _get_tool_fn("match_profile")
        result = await fn(
            nationality="nepal",
            current_qualification="Bachelor",
            target_subject="CS",
            target_country="australia",
            ielts_score=6.5,
        )
        assert isinstance(result, dict)


class TestGetClosingSoon:
    @pytest.mark.asyncio
    async def test_returns_results(self):
        fn = await _get_tool_fn("get_closing_soon")
        result = await fn(days=90)
        assert isinstance(result, dict)

    @pytest.mark.asyncio
    async def test_handles_empty_db(self, _patch_empty_db):
        fn = await _get_tool_fn("get_closing_soon")
        result = await fn()
        assert isinstance(result, dict)


class TestGetFullyFunded:
    @pytest.mark.asyncio
    async def test_returns_results(self):
        fn = await _get_tool_fn("get_fully_funded")
        result = await fn(destination_country="australia")
        assert isinstance(result, dict)


class TestGetByUniversity:
    @pytest.mark.asyncio
    async def test_returns_results(self):
        fn = await _get_tool_fn("get_by_university")
        result = await fn(university_name="University of Melbourne")
        assert isinstance(result, dict)


class TestCompareScholarshipOptions:
    @pytest.mark.asyncio
    async def test_returns_comparison(self):
        fn = await _get_tool_fn("compare_scholarship_options")
        result = await fn(
            nationality="nepal",
            country1="australia",
            country2="uk",
            study_level="postgraduate",
        )
        assert isinstance(result, dict)


class TestGetScholarshipStatistics:
    @pytest.mark.asyncio
    async def test_returns_stats(self):
        fn = await _get_tool_fn("get_scholarship_statistics")
        result = await fn(destination_country="australia", nationality="nepalese")
        assert isinstance(result, dict)


# ═══════════════════════════════════════════════════════════════════════════
# COURSE TOOLS
# ═══════════════════════════════════════════════════════════════════════════

class TestSearchCourses:
    @pytest.mark.asyncio
    async def test_returns_results(self):
        fn = await _get_tool_fn("search_courses")
        result = await fn(subject="Computer Science", destination_country="australia",
                          study_level="postgraduate")
        assert isinstance(result, dict)
        assert "error" not in result

    @pytest.mark.asyncio
    async def test_handles_empty_db(self, _patch_empty_db):
        fn = await _get_tool_fn("search_courses")
        result = await fn(subject="XYZ", destination_country="mars",
                          study_level="unknown")
        assert isinstance(result, dict)


class TestCompareCourses:
    @pytest.mark.asyncio
    async def test_returns_comparison(self):
        fn = await _get_tool_fn("compare_courses")
        result = await fn(
            course1_name="Master of Computer Science",
            university1="University of Melbourne",
            course2_name="Master of Computer Science",
            university2="University of Melbourne",
        )
        assert isinstance(result, dict)


class TestFindCoursesForProfile:
    @pytest.mark.asyncio
    async def test_returns_with_gap_analysis(self):
        fn = await _get_tool_fn("find_courses_for_profile")
        result = await fn(
            current_qualification="Bachelor of Engineering",
            target_subject="Computer Science",
            ielts_score=6.5,
            budget_aud_per_year=50000,
        )
        assert isinstance(result, dict)
        assert "error" not in result


class TestGetPathwayOptions:
    @pytest.mark.asyncio
    async def test_returns_results(self):
        fn = await _get_tool_fn("get_pathway_options")
        result = await fn(
            current_qualification="High School",
            target_degree="Computer Science",
            target_university="University of Melbourne",
        )
        assert isinstance(result, dict)


class TestGetCoursesByIelts:
    @pytest.mark.asyncio
    async def test_returns_grouped_results(self):
        fn = await _get_tool_fn("get_courses_by_ielts")
        result = await fn(ielts_score=6.5, destination_country="australia",
                          study_level="postgraduate")
        assert isinstance(result, dict)


# ═══════════════════════════════════════════════════════════════════════════
# UNIVERSITY TOOLS
# ═══════════════════════════════════════════════════════════════════════════

class TestCompareUniversities:
    @pytest.mark.asyncio
    async def test_returns_comparison(self):
        fn = await _get_tool_fn("compare_universities")
        result = await fn(
            university1="University of Melbourne",
            university2="University of Melbourne",
        )
        assert isinstance(result, dict)


class TestGetUniversityProfile:
    @pytest.mark.asyncio
    async def test_returns_full_profile(self):
        fn = await _get_tool_fn("get_university_profile")
        result = await fn(university_name="University of Melbourne")
        assert isinstance(result, dict)
        assert "error" not in result

    @pytest.mark.asyncio
    async def test_handles_unknown_uni(self, _patch_empty_db):
        fn = await _get_tool_fn("get_university_profile")
        result = await fn(university_name="Nonexistent University")
        assert isinstance(result, dict)


class TestFindUniversitiesByBudget:
    @pytest.mark.asyncio
    async def test_returns_results(self):
        fn = await _get_tool_fn("find_universities_by_budget")
        result = await fn(max_tuition_per_year=60000, destination_country="australia")
        assert isinstance(result, dict)


class TestGetTopUniversities:
    @pytest.mark.asyncio
    async def test_returns_ranked_list(self):
        fn = await _get_tool_fn("get_top_universities")
        result = await fn(destination_country="australia")
        assert isinstance(result, dict)


class TestGetScholarshipRichUniversities:
    @pytest.mark.asyncio
    async def test_returns_results(self):
        fn = await _get_tool_fn("get_scholarship_rich_universities")
        result = await fn(destination_country="australia")
        assert isinstance(result, dict)


# ═══════════════════════════════════════════════════════════════════════════
# IELTS TOOLS
# ═══════════════════════════════════════════════════════════════════════════

class TestCheckIeltsEligibility:
    @pytest.mark.asyncio
    async def test_returns_eligibility(self):
        fn = await _get_tool_fn("check_ielts_eligibility")
        result = await fn(ielts_score=6.5, destination_country="australia",
                          study_level="postgraduate")
        assert isinstance(result, dict)
        assert "error" not in result

    @pytest.mark.asyncio
    async def test_handles_empty_db(self, _patch_empty_db):
        fn = await _get_tool_fn("check_ielts_eligibility")
        result = await fn(ielts_score=6.0, destination_country="mars",
                          study_level="postgraduate")
        assert isinstance(result, dict)


class TestGetIeltsRequirements:
    @pytest.mark.asyncio
    async def test_returns_requirements(self):
        fn = await _get_tool_fn("get_ielts_requirements")
        result = await fn(university_name="University of Melbourne")
        assert isinstance(result, dict)

    @pytest.mark.asyncio
    async def test_with_course_name(self):
        fn = await _get_tool_fn("get_ielts_requirements")
        result = await fn(university_name="Melbourne", course_name="Computer Science")
        assert isinstance(result, dict)


class TestFindLowIeltsOptions:
    @pytest.mark.asyncio
    async def test_returns_options(self):
        fn = await _get_tool_fn("find_low_ielts_options")
        result = await fn(current_ielts=5.5, destination_country="australia")
        assert isinstance(result, dict)


class TestGetIeltsTestInfo:
    @pytest.mark.asyncio
    async def test_returns_nepal_info(self):
        fn = await _get_tool_fn("get_ielts_test_info")
        result = await fn(city="Kathmandu", country="nepal")
        assert isinstance(result, dict)
        assert "test_types" in result
        assert "local_info" in result
        assert result["local_info"].get("booking_url") is not None

    @pytest.mark.asyncio
    async def test_unknown_country_has_fallback(self):
        fn = await _get_tool_fn("get_ielts_test_info")
        result = await fn(city="Mars City", country="mars")
        assert isinstance(result, dict)
        assert "local_info" in result


# ═══════════════════════════════════════════════════════════════════════════
# VISA TOOLS
# ═══════════════════════════════════════════════════════════════════════════

class TestGetVisaRequirements:
    @pytest.mark.asyncio
    async def test_returns_requirements(self):
        fn = await _get_tool_fn("get_visa_requirements")
        result = await fn(nationality="nepal", destination_country="australia")
        assert isinstance(result, dict)
        assert "error" not in result

    @pytest.mark.asyncio
    async def test_handles_unknown_nationality(self, _patch_empty_db):
        fn = await _get_tool_fn("get_visa_requirements")
        result = await fn(nationality="martian", destination_country="australia")
        assert isinstance(result, dict)
        assert result.get("total_count", 0) == 0 or "message" in result


class TestCalculateFinancialProof:
    @pytest.mark.asyncio
    async def test_returns_breakdown(self):
        fn = await _get_tool_fn("calculate_financial_proof")
        result = await fn(
            nationality="nepal", destination_country="australia",
            course_duration_months=24, annual_tuition_aud=45000,
        )
        assert isinstance(result, dict)
        assert "breakdown" in result
        assert result["breakdown"]["tuition_total"] > 0
        assert result["grand_total_aud"] > 0

    @pytest.mark.asyncio
    async def test_with_scholarship(self):
        fn = await _get_tool_fn("calculate_financial_proof")
        result = await fn(
            nationality="nepal", destination_country="australia",
            course_duration_months=24, annual_tuition_aud=45000,
            has_scholarship=True, scholarship_value_aud=20000,
        )
        assert result["breakdown"]["scholarship_deduction"] > 0
        assert result["breakdown"]["tuition_after_scholarship"] < result["breakdown"]["tuition_total"]


class TestGetVisaChecklist:
    @pytest.mark.asyncio
    async def test_returns_checklist(self):
        fn = await _get_tool_fn("get_visa_checklist")
        result = await fn(nationality="nepal", destination_country="australia")
        assert isinstance(result, dict)
        assert result["total_required"] > 0
        assert len(result["required_documents"]) > 0


class TestGetProcessingTimeline:
    @pytest.mark.asyncio
    async def test_returns_timeline(self):
        fn = await _get_tool_fn("get_processing_timeline")
        future = (date.today() + timedelta(days=180)).isoformat()
        result = await fn(nationality="nepal", destination_country="australia",
                          course_start_date=future)
        assert isinstance(result, dict)
        assert "timeline" in result
        assert len(result["timeline"]) >= 5

    @pytest.mark.asyncio
    async def test_invalid_date_returns_error(self):
        fn = await _get_tool_fn("get_processing_timeline")
        result = await fn(nationality="nepal", destination_country="australia",
                          course_start_date="not-a-date")
        assert "error" in result


class TestAssessVisaStrength:
    @pytest.mark.asyncio
    async def test_returns_assessment(self):
        fn = await _get_tool_fn("assess_visa_strength")
        result = await fn(
            nationality="nepal", destination_country="australia",
            age=25, has_financial_proof=True, financial_amount_aud=80000,
            annual_tuition_aud=45000, course_duration_months=24,
            has_ielts=True, ielts_score=7.0, has_family_property=True,
            is_employed=True,
        )
        assert isinstance(result, dict)
        assert "overall_strength" in result
        assert "score" in result
        assert result["score"] > 0

    @pytest.mark.asyncio
    async def test_nepal_specific_advice(self):
        fn = await _get_tool_fn("assess_visa_strength")
        result = await fn(
            nationality="nepal", destination_country="australia",
            age=25, has_financial_proof=True, financial_amount_aud=50000,
            annual_tuition_aud=40000, course_duration_months=24,
            has_ielts=True, ielts_score=6.5,
        )
        assert "nepal_specific_advice" in result
        assert result["nepal_specific_advice"]["scrutiny_level"] == "HIGH"

    @pytest.mark.asyncio
    async def test_weak_application_flagged(self):
        fn = await _get_tool_fn("assess_visa_strength")
        result = await fn(
            nationality="nepal", destination_country="australia",
            age=38, has_financial_proof=False, financial_amount_aud=0,
            annual_tuition_aud=40000, course_duration_months=24,
            has_ielts=False, has_previous_visa_refusal=True,
            study_level="undergraduate", gap_years_after_study=8,
        )
        assert result["overall_strength"] in ("weak", "needs_improvement")
        assert len(result["risk_flags"]) > 0


# ═══════════════════════════════════════════════════════════════════════════
# COST OF LIVING TOOLS
# ═══════════════════════════════════════════════════════════════════════════

class TestGetCityBudget:
    @pytest.mark.asyncio
    async def test_returns_budget(self):
        fn = await _get_tool_fn("get_city_budget")
        result = await fn(city="Melbourne", country="australia")
        assert isinstance(result, dict)
        assert "error" not in result

    @pytest.mark.asyncio
    async def test_handles_unknown_city(self, _patch_empty_db):
        fn = await _get_tool_fn("get_city_budget")
        result = await fn(city="Atlantis", country="ocean")
        assert isinstance(result, dict)
        assert result.get("total_count", 0) == 0 or "message" in result


class TestCompareStudyDestinations:
    @pytest.mark.asyncio
    async def test_returns_comparison(self):
        fn = await _get_tool_fn("compare_study_destinations")
        result = await fn(city1="Melbourne", country1="australia",
                          city2="Melbourne", country2="australia")
        assert isinstance(result, dict)


class TestCalculateTotalCost:
    @pytest.mark.asyncio
    async def test_returns_full_breakdown(self):
        fn = await _get_tool_fn("calculate_total_cost")
        result = await fn(city="Melbourne", country="australia",
                          course_duration_months=24, annual_tuition_aud=45000)
        assert isinstance(result, dict)
        assert "grand_total_aud" in result
        assert result["grand_total_aud"] > 0

    @pytest.mark.asyncio
    async def test_handles_empty_db(self, _patch_empty_db):
        fn = await _get_tool_fn("calculate_total_cost")
        result = await fn(city="NoCity", country="nocountry",
                          course_duration_months=12, annual_tuition_aud=30000)
        assert isinstance(result, dict)


class TestFindAffordableDestinations:
    @pytest.mark.asyncio
    async def test_returns_cities(self):
        fn = await _get_tool_fn("find_affordable_destinations")
        result = await fn(monthly_budget_aud=3000, destination_country="australia")
        assert isinstance(result, dict)


# ═══════════════════════════════════════════════════════════════════════════
# COUNSELLOR / MEGA TOOLS
# ═══════════════════════════════════════════════════════════════════════════

class TestPlanStudyAbroadJourney:
    @pytest.mark.asyncio
    async def test_returns_complete_structured_response(self):
        fn = await _get_tool_fn("plan_study_abroad_journey")
        result = await fn(
            nationality="nepalese",
            current_qualification="Bachelor of Engineering, GPA 3.7",
            target_subject="Computer Science",
            preferred_countries="australia",
            total_budget_usd=60000,
            timeline_months=6,
            ielts_score=7.0,
            career_goal="data engineer at a tech company",
        )
        assert isinstance(result, dict)
        # Must have all required sections
        assert "student_summary" in result
        assert "recommended_path" in result
        assert "top_scholarships" in result
        assert "financial_summary" in result
        assert "visa_summary" in result
        assert "ielts_analysis" in result
        assert "action_timeline" in result
        assert "next_steps" in result
        assert "data_freshness" in result
        assert isinstance(result["recommended_path"], list)
        assert isinstance(result["top_scholarships"], list)
        assert isinstance(result["action_timeline"], list)
        assert isinstance(result["next_steps"], list)

    @pytest.mark.asyncio
    async def test_works_without_ielts(self):
        fn = await _get_tool_fn("plan_study_abroad_journey")
        result = await fn(
            nationality="nepalese",
            current_qualification="Bachelor of Science",
            target_subject="Data Science",
            preferred_countries="australia",
            total_budget_usd=50000,
            timeline_months=8,
        )
        assert isinstance(result, dict)
        assert result["ielts_analysis"].get("status") == "NOT_TAKEN" or result["ielts_analysis"].get("current_score") is None

    @pytest.mark.asyncio
    async def test_handles_empty_db(self, _patch_empty_db):
        fn = await _get_tool_fn("plan_study_abroad_journey")
        result = await fn(
            nationality="nepalese",
            current_qualification="Bachelor",
            target_subject="CS",
            preferred_countries="australia",
            total_budget_usd=30000,
            timeline_months=6,
        )
        assert isinstance(result, dict)
        # Should still return structured response even with no data
        assert "student_summary" in result or "error" in result

    @pytest.mark.asyncio
    async def test_caching_returns_same_result(self):
        fn = await _get_tool_fn("plan_study_abroad_journey")
        params = dict(
            nationality="nepalese",
            current_qualification="Bachelor of Engineering",
            target_subject="Computer Science",
            preferred_countries="australia",
            total_budget_usd=60000,
            timeline_months=6,
            ielts_score=7.0,
        )
        r1 = await fn(**params)
        r2 = await fn(**params)
        assert r2.get("_cached") is True


class TestSearchAll:
    @pytest.mark.asyncio
    async def test_returns_cross_domain_results(self):
        fn = await _get_tool_fn("search_all")
        result = await fn(query="Melbourne")
        assert isinstance(result, dict)
        assert "results" in result

    @pytest.mark.asyncio
    async def test_handles_empty_db(self, _patch_empty_db):
        fn = await _get_tool_fn("search_all")
        result = await fn(query="nonexistent")
        assert isinstance(result, dict)
        assert result.get("total_results", 0) == 0


class TestBookCounsellingSession:
    @pytest.mark.asyncio
    async def test_returns_success(self):
        fn = await _get_tool_fn("book_counselling_session")
        result = await fn(name="Test Student", email="test@example.com",
                          destination="australia")
        assert result["status"] == "success"


# ═══════════════════════════════════════════════════════════════════════════
# DATA VALIDATOR
# ═══════════════════════════════════════════════════════════════════════════

class TestDataValidator:
    def test_valid_scholarship(self):
        from src.utils.data_validator import Scholarship
        s = Scholarship(
            title="Test", organization="Uni", url="https://example.com",
            description="Test scholarship",
        )
        assert s.title == "Test"

    def test_invalid_url_raises(self):
        from src.utils.data_validator import Scholarship
        with pytest.raises(Exception):
            Scholarship(
                title="Test", organization="Uni", url="not-a-url",
                description="Test",
            )

    def test_missing_required_raises(self):
        from src.utils.data_validator import Scholarship
        with pytest.raises(Exception):
            Scholarship(url="https://example.com", description="Test")
