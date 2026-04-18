"""
Lightning fast CRICOS update using CSV files
"""
import httpx
import pandas as pd
import csv
import io
from src.database.client import get_db

print("Downloading CRICOS Course Locations CSV...")
csv_url = "https://data.gov.au/data/dataset/e5ae7059-bfa8-4fa4-a5c0-c13cf3520193/resource/4cd2de02-8ba3-4eb2-bac2-fe272cae3f5f/download/cricos-course-locations.csv"

response = httpx.get(csv_url)
print("Parsing CSV...")

# Read CSV
df = pd.read_csv(io.StringIO(response.text))
print(f"Loaded {len(df)} course locations")

# Build location map: CRICOS Course Code -> (state, city)
location_map = {}
for _, row in df.iterrows():
    course_code = str(row.get('CRICOS Course Code', '')).strip()
    state = str(row.get('Location State', '')).strip()
    city = str(row.get('Location City', '')).strip()
    
    if course_code and course_code.lower() != 'nan':
        if course_code not in location_map:
            location_map[course_code] = {
                'state': state if state and state.lower() != 'nan' else None,
                'city': city if city and city.lower() != 'nan' else None
            }

print(f"Built location map with {len(location_map)} unique courses")

# Get database connection
db = get_db()

# Fetch all courses
print("Fetching all courses from database...")
all_courses = []
offset = 0
while True:
    result = db.table("courses").select("id", "cricos_code").not_.is_("cricos_code", "null").range(offset, offset + 1000).execute()
    if not result.data:
        break
    all_courses.extend(result.data)
    offset += 1000
    if len(result.data) < 1000:
        break

print(f"Fetched {len(all_courses)} courses")

# Prepare updates
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

print(f"Need to update {len(updates)} courses")

# Fast batch update
print("Updating courses...")
updated = 0
for i, update_data in enumerate(updates):
    try:
        db.table("courses").update({
            'state': update_data['state'],
            'city': update_data['city']
        }).eq('id', update_data['id']).execute()
        updated += 1
        
        if (i + 1) % 500 == 0:
            print(f"  Progress: {updated}/{len(updates)} ({updated/len(updates)*100:.1f}%)")
    except Exception as e:
        pass

print(f"\n✅ COMPLETED! Updated {updated} courses with state and city data")

# Verify
result = db.table('courses').select('state', count='exact').not_.is_('state', 'null').limit(1).execute()
print(f"Final count - Courses with state: {result.count}")
