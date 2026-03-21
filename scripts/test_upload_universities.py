import json
import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_SERVICE_ROLE_KEY") or os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def clean_university_record(record):
    cleaned = {}
    for k, v in record.items():
        if v == "None" or v == "N/A" or v == "":
            cleaned[k] = None
        elif isinstance(v, list) and len(v) == 0:
            cleaned[k] = []
        elif isinstance(v, dict) and len(v) == 0:
            cleaned[k] = {}
        else:
            cleaned[k] = v
            
    return cleaned

def test_insert_5():
    with open("scraped_data/universities.json", "r") as f:
        data = json.load(f)
        
    test_batch = [clean_university_record(r) for r in data[:5]]
    
    print("Test universities batch cleaned. Attempting to UPSERT 5 records into Supabase...")
    try:
        result = supabase.table("universities").upsert(
            test_batch, 
            on_conflict="name,country"
        ).execute()
        
        print(f"Successfully UPSERTED {len(result.data)} universities!")
        print(json.dumps(result.data, indent=2))
        
    except Exception as e:
        error_str = str(e)
        if "constraint" in error_str.lower() or "42P10" in error_str:
            print("UPSERT FAILED due to missing constraint. Attempting regular INSERT...")
            try:
                result = supabase.table("universities").insert(test_batch).execute()
                print(f"Successfully INSERTED {len(result.data)} universities!")
                print(json.dumps(result.data, indent=2))
            except Exception as e2:
                print(f"FAILED to fall back to insert: {e2}")
        else:
            print(f"FAILED to insert: {e}")

if __name__ == "__main__":
    test_insert_5()
