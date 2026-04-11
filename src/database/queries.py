from typing import List, Optional, Any, Dict
import asyncio
from .client import get_db
from .models import Scholarship, Course, University, VisaRequirement, CostOfLiving
from src.utils.logger import logger
from uuid import UUID

# generic helper for insertions
async def _insert_item(table_name: str, item_data: Dict[str, Any]):
    try:
        db = get_db()
        # Note: supabase-py's insert is synchronous in the current version (2.x), 
        # but we wrap it in an async function for future compatibility and consistency.
        response = db.table(table_name).insert(item_data).execute()
        return response.data
    except Exception as e:
        logger.error(f"database_insert_failed", table=table_name, error=str(e))
        raise

# Scholarships
async def create_scholarship(scholarship: Scholarship):
    data = scholarship.model_dump(mode='json', exclude_none=True)
    return await _insert_item("scholarships", data)

async def get_scholarships(filters: Dict[str, Any] = None) -> List[Dict[str, Any]]:
    db = get_db()
    query = db.table("scholarships").select("*")
    if filters:
        for key, value in filters.items():
            query = query.eq(key, value)
    response = query.execute()
    return response.data


async def upsert_scholarship(scholarship: Scholarship) -> Dict[str, Any]:
    """
    Upsert a scholarship row.  If (title, university) already exists it updates
    the existing row; otherwise it inserts a new one.

    Requires a unique constraint on (title, university) in your Supabase schema:
        ALTER TABLE scholarships ADD CONSTRAINT uq_scholarships_title_uni
        UNIQUE (title, university);
    """
    db = get_db()
    data = scholarship.model_dump(mode='json', exclude_none=True)
    # Remove id/created_at — let the DB handle those
    data.pop("id", None)
    data.pop("created_at", None)
    try:
        response = (
            db.table("scholarships")
            .upsert(data, on_conflict="title,university")
            .execute()
        )
        return response.data[0] if response.data else {}
    except Exception as e:
        logger.error("scholarship_upsert_failed", error=str(e), title=data.get("title"))
        raise


    async def bulk_upsert_scholarships(scholarships: List[Scholarship]) -> List[str]:
        if not scholarships:
            return []
        db = get_db()
        data = []
        for s in scholarships:
            d = s.model_dump(mode='json', exclude_none=True)
            d.pop("id", None)
            d.pop("created_at", None)
            data.append(d)
        
        all_ids = []
        chunk_size = 500
        for i in range(0, len(data), chunk_size):
            chunk = data[i:i + chunk_size]
            try:
                # Wrap synchronous DB call in to_thread so it doesn't block the async loop
                response = await asyncio.to_thread(
                    db.table("scholarships").upsert(chunk, on_conflict="title,university").execute
                )
                if response.data:
                    all_ids.extend([row["id"] for row in response.data if "id" in row])
            except Exception as e:
                logger.error("scholarships_bulk_upsert_failed", error=str(e), count=len(chunk))
        return all_ids


async def deactivate_stale_scholarships(
    source: str,
    active_ids: List[str],
) -> int:
    """
    Mark scholarships as is_active=false if they belong to `source` but their
    id is NOT in `active_ids`.  Returns the count of deactivated rows.
    """
    db = get_db()
    try:
        # Fetch all currently active IDs for this source
        existing = (
            db.table("scholarships")
            .select("id")
            .eq("source", source)
            .eq("is_active", True)
            .execute()
        )
        stale_ids = [
            row["id"] for row in (existing.data or [])
            if row["id"] not in active_ids
        ]
        if not stale_ids:
            return 0

        db.table("scholarships").update({"is_active": False}).in_("id", stale_ids).execute()
        logger.info("scholarships_deactivated", source=source, count=len(stale_ids))
        return len(stale_ids)
    except Exception as e:
        logger.error("deactivate_stale_failed", source=source, error=str(e))
        raise

# Courses
async def create_course(course: Course):
    data = course.model_dump(mode='json', exclude_none=True)
    return await _insert_item("courses", data)


async def upsert_course(course: Course) -> Dict[str, Any]:
    """
    Upsert a course row.  If (name, university) already exists it updates
    the existing row; otherwise it inserts a new one.

    Requires a unique constraint on (name, university) in your Supabase schema:
        ALTER TABLE courses ADD CONSTRAINT uq_courses_name_uni UNIQUE (name, university);
    """
    db = get_db()
    data = course.model_dump(mode='json', exclude_none=True)
    data.pop("id", None)
    data.pop("created_at", None)
    try:
        response = (
            db.table("courses")
            .upsert(data, on_conflict="name,university")
            .execute()
        )
        return response.data[0] if response.data else {}
    except Exception as e:
        logger.error("course_upsert_failed", error=str(e), name=data.get("name"))
        raise


    async def bulk_upsert_courses(courses: List[Course]) -> List[str]:
        if not courses:
            return []
        db = get_db()
        data = []
        for c in courses:
            d = c.model_dump(mode='json', exclude_none=True)
            d.pop("id", None)
            d.pop("created_at", None)
            data.append(d)
        
        all_ids = []
        chunk_size = 500
        for i in range(0, len(data), chunk_size):
            chunk = data[i:i + chunk_size]
            try:
                response = await asyncio.to_thread(
                    db.table("courses").upsert(chunk, on_conflict="name,university").execute
                )
                if response.data:
                    all_ids.extend([row["id"] for row in response.data if "id" in row])
            except Exception as e:
                logger.error("courses_bulk_upsert_failed", error=str(e), count=len(chunk))
        return all_ids


async def search_courses(query_params: Dict[str, Any]) -> List[Dict[str, Any]]:
    db = get_db()
    query = db.table("courses").select("*")
    for key, value in query_params.items():
        query = query.eq(key, value)
    response = query.execute()
    return response.data

# Universities
async def create_university(uni: University):
    data = uni.model_dump(mode='json', exclude_none=True)
    return await _insert_item("universities", data)


async def upsert_university(uni: University) -> Dict[str, Any]:
    """
    Upsert a university row.  If (name, country) already exists it updates;
    otherwise inserts.

    Requires:
        ALTER TABLE universities ADD CONSTRAINT uq_uni_name_country UNIQUE (name, country);
    """
    db = get_db()
    data = uni.model_dump(mode='json', exclude_none=True)
    data.pop("id", None)
    data.pop("created_at", None)
    try:
        response = (
            db.table("universities")
            .upsert(data, on_conflict="name,country")
            .execute()
        )
        return response.data[0] if response.data else {}
    except Exception as e:
        logger.error("university_upsert_failed", error=str(e), name=data.get("name"))
        raise


    async def bulk_upsert_universities(universities: List[University]) -> List[str]:
        if not universities:
            return []
        db = get_db()
        data = []
        for u in universities:
            d = u.model_dump(mode='json', exclude_none=True)
            d.pop("id", None)
            d.pop("created_at", None)
            data.append(d)
            
        all_ids = []
        chunk_size = 100
        for i in range(0, len(data), chunk_size):
            chunk = data[i:i + chunk_size]
            try:
                response = await asyncio.to_thread(
                    db.table("universities").upsert(chunk, on_conflict="name,country").execute
                )
                if response.data:
                    all_ids.extend([row["id"] for row in response.data if "id" in row])
            except Exception as e:
                logger.error("universities_bulk_upsert_failed", error=str(e), count=len(chunk))
        return all_ids


async def get_university_by_id(uni_id: UUID) -> Optional[Dict[str, Any]]:
    db = get_db()
    response = db.table("universities").select("*").eq("id", str(uni_id)).execute()
    return response.data[0] if response.data else None

# Visa Requirements
async def upsert_visa_requirement(visa: VisaRequirement):
    data = visa.model_dump(mode='json', exclude_none=True)
    db = get_db()
    response = db.table("visa_requirements").upsert(data).execute()
    return response.data

# Cost of Living
async def get_living_costs(city: str, country: str) -> Optional[Dict[str, Any]]:
    db = get_db()
    response = db.table("cost_of_living").select("*").eq("city", city).eq("country", country).execute()
    return response.data[0] if response.data else None
