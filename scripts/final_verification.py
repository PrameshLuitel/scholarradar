import os
from dotenv import load_dotenv
from supabase import create_client, Client
import json

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_SERVICE_ROLE_KEY") or os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def run_verification():
    tables = [
        "scholarships",
        "courses",
        "universities",
        "visa_requirements",
        "cost_of_living"
    ]
    
    print("--- TABLE COUNTS ---")
    print(f"{'table_name':<20} | {'total'}")
    print("-" * 30)
    
    total_count = 0
    for table in tables:
        # Fetching count only
        res = supabase.table(table).select("*", count="exact").limit(1).execute()
        count = res.count
        total_count += count
        print(f"{table:<20} | {count}")
        
    print(f"\nTOTAL ALL TABLES COMBINED: {total_count}")
    
    print("\n--- SCHOLARSHIPS: AUSTRALIA & DOCTORATE ---")
    try:
        # Use ilike to handle case-insensitivity on australia vs Australia
        res2 = supabase.table("scholarships").select("*").ilike("country", "%ustralia%").ilike("study_level", "doctorate").limit(5).execute()
        
        if not res2.data:
            print("No records found with exact match 'Australia' and 'doctorate'.")
        else:
            print(json.dumps(res2.data, indent=2))
    except Exception as e:
        print(f"Error fetching scholarships: {e}")

if __name__ == "__main__":
    run_verification()
