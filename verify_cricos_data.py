"""
Verify CRICOS data in the database
"""
import asyncio
from src.database.client import get_db

async def verify_cricos_data():
    db = get_db()
    
    print("="*80)
    print("CRICOS DATA VERIFICATION")
    print("="*80)
    
    # Check total courses with cricos_code
    courses_result = db.table("courses").select("*", count="exact").not_.is_("cricos_code", "null").limit(1).execute()
    print(f"\n✓ Total courses with CRICOS code: {courses_result.count}")
    
    # Check total universities with provider_code
    unis_result = db.table("universities").select("*", count="exact").not_.is_("provider_code", "null").limit(1).execute()
    print(f"✓ Total universities with provider code: {unis_result.data}")
    
    # Sample course data
    if courses_result.data:
        print("\n" + "="*80)
        print("SAMPLE COURSE DATA (First Record):")
        print("="*80)
        sample_course = db.table("courses").select("*").not_.is_("cricos_code", "null").limit(1).execute()
        if sample_course.data:
            course = sample_course.data[0]
            print(f"  Name: {course.get('name')}")
            print(f"  University: {course.get('university')}")
            print(f"  CRICOS Code: {course.get('cricos_code')}")
            print(f"  Provider Code: {course.get('provider_code')}")
            print(f"  Level: {course.get('level')}")
            print(f"  State: {course.get('state')}")
            print(f"  City: {course.get('city')}")
            print(f"  Tuition Fee: {course.get('tuition_fee')} {course.get('currency')}")
            print(f"  Duration: {course.get('duration_months')} months")
            print(f"  Subject: {course.get('subject')}")
            print(f"  Subject Category: {course.get('subject_category')}")
    
    # Sample university data
    print("\n" + "="*80)
    print("SAMPLE UNIVERSITY DATA (First Record):")
    print("="*80)
    sample_uni = db.table("universities").select("*").not_.is_("provider_code", "null").limit(1).execute()
    if sample_uni.data:
        uni = sample_uni.data[0]
        print(f"  Name: {uni.get('name')}")
        print(f"  Provider Code: {uni.get('provider_code')}")
        print(f"  State: {uni.get('state')}")
        print(f"  City: {uni.get('city')}")
        print(f"  Website: {uni.get('website')}")
        print(f"  Institution Type: {uni.get('institution_type')}")
        print(f"  Phone: {uni.get('phone_number')}")
        print(f"  Email: {uni.get('email_address')}")
        print(f"  Total Students: {uni.get('total_students')}")
    
    # Check state distribution
    print("\n" + "="*80)
    print("COURSES BY STATE:")
    print("="*80)
    states_result = db.table("courses").select("state", count="exact").not_.is_("cricos_code", "null").execute()
    if states_result.data:
        state_counts = {}
        for course in states_result.data:
            state = course.get('state') or 'NULL'
            state_counts[state] = state_counts.get(state, 0) + 1
        
        for state, count in sorted(state_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f"  {state}: {count} courses")
    
    print("\n" + "="*80)
    print("VERIFICATION COMPLETE")
    print("="*80)

if __name__ == "__main__":
    asyncio.run(verify_cricos_data())
