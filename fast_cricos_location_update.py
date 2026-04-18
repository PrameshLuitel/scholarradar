"""
Fast batch update script to populate state and city for all CRICOS courses
Downloads fresh data from data.gov.au and updates in bulk
"""
import asyncio
import io
import httpx
import pandas as pd
from src.database.client import get_db
import structlog

logger = structlog.get_logger().bind(script="fast_cricos_update")

async def fast_update_cricos_locations():
    """Download CRICOS data and batch update state/city for all courses"""
    
    logger.info("Starting fast CRICOS location update...")
    
    # 1. Fetch latest CRICOS Excel file
    ckan_url = "https://data.gov.au/data/api/3/action/package_show?id=cricos"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    async with httpx.AsyncClient() as client:
        response = await client.get(ckan_url, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        resources = data["result"]["resources"]
        xlsx_resources = [r for r in resources if r.get("format", "").upper() == "XLSX" or ".xlsx" in r.get("url", "").lower()]
        xlsx_resources.sort(key=lambda x: x.get("created", ""), reverse=True)
        
        if not xlsx_resources:
            raise ValueError("No XLSX file found")
        
        file_url = xlsx_resources[0]["url"]
        logger.info("Downloading CRICOS dataset", url=file_url)
        
        resp = await client.get(file_url, headers=headers)
        resp.raise_for_status()
        xlsx_data = resp.content
    
    logger.info("Parsing Excel file...")
    xl = pd.ExcelFile(io.BytesIO(xlsx_data), engine="openpyxl")
    
    # 2. Process Course Locations sheet
    if 'Course Locations' not in xl.sheet_names:
        logger.error("Course Locations sheet not found!")
        return
    
    logger.info("Processing Course Locations sheet...")
    df_course_loc = xl.parse('Course Locations', header=2)
    df_course_loc.columns = [str(c).lower().strip() for c in df_course_loc.columns]
    
    # Build map: cricos_course_code -> {state, city}
    location_map = {}
    for _, row in df_course_loc.iterrows():
        course_code = str(row.get('cricos course code', '')).strip()
        state = str(row.get('location state', '')).strip()
        city = str(row.get('location city', '')).strip()
        
        if not course_code or course_code.lower() == 'nan':
            continue
        
        # Take first location found for each course
        if course_code not in location_map:
            location_map[course_code] = {
                'state': state if state and state.lower() != 'nan' else None,
                'city': city if city and city.lower() != 'nan' else None
            }
    
    logger.info(f"Built location map with {len(location_map)} entries")
    
    # 3. Batch update database
    db = get_db()
    
    # Get all courses with cricos_code
    logger.info("Fetching all courses with CRICOS codes...")
    courses_result = db.table("courses").select("id", "cricos_code").not_.is_("cricos_code", "null").execute()
    
    if not courses_result.data:
        logger.error("No courses found!")
        return
    
    logger.info(f"Found {len(courses_result.data)} courses to update")
    
    # Prepare updates
    updates_needed = []
    for course in courses_result.data:
        cricos_code = course.get('cricos_code')
        if cricos_code and cricos_code in location_map:
            loc = location_map[cricos_code]
            if loc['state'] or loc['city']:
                updates_needed.append({
                    'id': course['id'],
                    'state': loc['state'],
                    'city': loc['city']
                })
    
    logger.info(f"Need to update {len(updates_needed)} courses")
    
    # Batch update in chunks of 1000
    chunk_size = 1000
    total_updated = 0
    
    for i in range(0, len(updates_needed), chunk_size):
        chunk = updates_needed[i:i + chunk_size]
        
        # Update each course in the chunk
        for update_data in chunk:
            try:
                db.table("courses").update({
                    'state': update_data['state'],
                    'city': update_data['city']
                }).eq('id', update_data['id']).execute()
                total_updated += 1
            except Exception as e:
                logger.error("Failed to update course", id=update_data['id'], error=str(e))
        
        logger.info(f"Progress: {total_updated}/{len(updates_needed)} courses updated")
    
    logger.info(f"Fast CRICOS location update completed! Updated {total_updated} courses")

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    asyncio.run(fast_update_cricos_locations())
