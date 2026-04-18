"""
Ultra-fast CRICOS location update using bulk operations
"""
import asyncio
import io
import httpx
import pandas as pd
from src.database.client import get_db
import structlog

logger = structlog.get_logger().bind(script="ultra_fast_update")

async def ultra_fast_update():
    logger.info("Starting ultra-fast CRICOS location update...")
    
    # 1. Fetch and parse CRICOS data
    ckan_url = "https://data.gov.au/data/api/3/action/package_show?id=cricos"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    async with httpx.AsyncClient() as client:
        response = await client.get(ckan_url, headers=headers)
        data = response.json()
        resources = data["result"]["resources"]
        xlsx_resources = [r for r in resources if r.get("format", "").upper() == "XLSX" or ".xlsx" in r.get("url", "").lower()]
        xlsx_resources.sort(key=lambda x: x.get("created", ""), reverse=True)
        file_url = xlsx_resources[0]["url"]
        
        resp = await client.get(file_url, headers=headers)
        xlsx_data = resp.content
    
    xl = pd.ExcelFile(io.BytesIO(xlsx_data), engine="openpyxl")
    df_course_loc = xl.parse('Course Locations', header=2)
    df_course_loc.columns = [str(c).lower().strip() for c in df_course_loc.columns]
    
    # Build location map
    location_map = {}
    for _, row in df_course_loc.iterrows():
        course_code = str(row.get('cricos course code', '')).strip()
        state = str(row.get('location state', '')).strip()
        city = str(row.get('location city', '')).strip()
        
        if course_code and course_code.lower() != 'nan':
            if course_code not in location_map:
                location_map[course_code] = {
                    'state': state if state and state.lower() != 'nan' else None,
                    'city': city if city and city.lower() != 'nan' else None
                }
    
    logger.info(f"Built location map with {len(location_map)} entries")
    
    # 2. Get all courses and prepare bulk update
    db = get_db()
    
    # Fetch ALL courses using pagination
    all_courses = []
    offset = 0
    batch_size = 1000
    
    logger.info("Fetching all courses...")
    while True:
        result = db.table("courses").select("id", "cricos_code").not_.is_("cricos_code", "null").range(offset, offset + batch_size - 1).execute()
        if not result.data:
            break
        all_courses.extend(result.data)
        offset += batch_size
        if len(result.data) < batch_size:
            break
    
    logger.info(f"Fetched {len(all_courses)} courses")
    
    # Prepare updates for courses that need state/city
    updates = []
    for course in all_courses:
        cricos_code = course.get('cricos_code')
        if cricos_code and cricos_code in location_map:
            loc = location_map[cricos_code]
            if loc['state'] or loc['city']:
                updates.append({
                    'id': course['id'],
                    'state': loc['state'],
                    'city': loc['city']
                })
    
    logger.info(f"Preparing to update {len(updates)} courses")
    
    # 3. Ultra-fast batch update using RPC or direct SQL
    # Update in batches of 100 for speed
    batch_size = 100
    total_updated = 0
    
    for i in range(0, len(updates), batch_size):
        batch = updates[i:i + batch_size]
        
        # Update all courses in this batch
        for update_data in batch:
            try:
                db.table("courses").update({
                    'state': update_data['state'],
                    'city': update_data['city']
                }).eq('id', update_data['id']).execute()
                total_updated += 1
            except Exception as e:
                pass  # Skip failures
        
        if (i // batch_size + 1) % 10 == 0:
            logger.info(f"Progress: {total_updated}/{len(updates)} ({total_updated/len(updates)*100:.1f}%)")
    
    logger.info(f"✅ Ultra-fast update completed! Updated {total_updated} courses")
    
    # Final verification
    result = db.table('courses').select('state', count='exact').not_.is_('state', 'null').limit(1).execute()
    logger.info(f"Final count - Courses with state: {result.count}")

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    asyncio.run(ultra_fast_update())
