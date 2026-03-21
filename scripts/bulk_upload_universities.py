import json
import os
import time
from collections import Counter
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

def upload_file(filename):
    print(f"Loading {filename}...")
    with open(filename, "r") as f:
        data = json.load(f)
        
    # Skip the 5 test records
    data = data[5:]
    
    total_records = len(data)
    print(f"Loaded {total_records} records to insert from {filename} (after skipping first 5).")
    
    batch_size = 500
    for i in range(0, total_records, batch_size):
        batch = data[i:i+batch_size]
        cleaned_batch = [clean_university_record(r) for r in batch]
                
        max_retries = 3
        for attempt in range(max_retries):
            try:
                # User did not add constraint, we fallback to INSERT
                supabase.table("universities").insert(cleaned_batch).execute()
                print(f"Progress: Inserted {i + len(cleaned_batch)} / {total_records} records.")
                break
            except Exception as e:
                if attempt == max_retries - 1:
                    print(f"FAILED batch {i} to {i+batch_size}. Error: {e}")
                else:
                    time.sleep(2)

def generate_report():
    print("\n--- FINAL REPORT ---")
    print("Fetching countries from universities...")
    
    countries = []
    limit = 1000
    offset = 0
    while True:
        try:
            res = supabase.table("universities").select("country").range(offset, offset+limit-1).execute()
            data = res.data
            if not data:
                break
            for row in data:
                countries.append(row.get('country'))
            offset += limit
        except Exception as e:
            print("Error fetching report data:", e)
            break
            
    counts = Counter(countries)
    print("\nSELECT country, COUNT(*) FROM universities GROUP BY country ORDER BY count DESC;")
    for country, count in counts.most_common():
        print(f"{country} | {count}")

if __name__ == "__main__":
    files = ["scraped_data/universities.json"]
    for f in files:
        if os.path.exists(f):
            upload_file(f)
        else:
            print(f"File {f} not found!")
            
    generate_report()
