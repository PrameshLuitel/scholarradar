import json
import os
import re
import time
from collections import Counter
from datetime import datetime
from dateutil import parser as date_parser
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_SERVICE_ROLE_KEY") or os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def parse_currency_amount(value):
    if not value or value in ["None", "N/A", "Not specified"]:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    value_str = str(value)
    if ' to ' in value_str.lower():
        return value_str 
    clean_str = re.sub(r'[^\d.]', '', value_str)
    try:
        if clean_str:
            return float(clean_str)
    except ValueError:
        pass
    return None

def clean_record(record):
    cleaned = {}
    for k, v in record.items():
        if v == "None" or v == "N/A" or v == "":
            cleaned[k] = None
        else:
            cleaned[k] = v

    for key in ['award_value_min', 'award_value_max']:
        if key in cleaned and isinstance(cleaned[key], str):
            val = cleaned[key]
            if ' to ' in val.lower():
                parts = val.lower().split(' to ')
                if key == 'award_value_min':
                    cleaned[key] = parse_currency_amount(parts[0])
                if key == 'award_value_max':
                    cleaned[key] = parse_currency_amount(parts[1])
            else:
                cleaned[key] = parse_currency_amount(val)
                
    for key in ['deadline', 'last_verified']:
        if key in cleaned and isinstance(cleaned[key], str) and cleaned[key] not in [None, 'None', 'N/A']:
            try:
                parsed_date = date_parser.parse(cleaned[key])
                if key == 'deadline':
                    cleaned[key] = parsed_date.strftime('%Y-%m-%d')
                else:
                    cleaned[key] = parsed_date.isoformat()
            except (ValueError, TypeError, OverflowError):
                cleaned[key] = None

    if isinstance(record.get('award_value_min'), str) and 'to' in record.get('award_value_min', '').lower():
        parts = re.split(r'\s+to\s+', record['award_value_min'].lower())
        if len(parts) == 2:
            cleaned['award_value_min'] = parse_currency_amount(parts[0])
            cleaned['award_value_max'] = parse_currency_amount(parts[1])

    if 'is_active' in cleaned:
        cleaned['is_active'] = bool(cleaned['is_active'])

    return cleaned

def upload_file(filename):
    print(f"Loading {filename}...")
    with open(filename, "r") as f:
        data = json.load(f)
        
    total_records = len(data)
    print(f"Loaded {total_records} records from {filename}.")
    
    batch_size = 100
    for i in range(0, total_records, batch_size):
        batch = data[i:i+batch_size]
        cleaned_batch = []
        
        for record in batch:
            try:
                cleaned = clean_record(record)
                cleaned_batch.append(cleaned)
            except Exception as e:
                print(f"Validation failed for record {record.get('title')}: {e}")
                print(f"Raw record: {record}")
                
        # Retry logic for upsert
        max_retries = 3
        for attempt in range(max_retries):
            try:
                supabase.table("scholarships").upsert(
                    cleaned_batch, 
                    on_conflict="title,university"
                ).execute()
                print(f"Progress: Upserted {i + len(cleaned_batch)} / {total_records} records.")
                break
            except Exception as e:
                if attempt == max_retries - 1:
                    print(f"FAILED batch {i} to {i+batch_size}. Error: {e}")
                    # Print exact data to see which field is wrong
                    print("First failed record details:", cleaned_batch[0])
                else:
                    print(f"Retrying batch due to error: {e}")
                    time.sleep(2)

def generate_report():
    print("\n--- FINAL REPORT ---")
    print("Fetching countries to generate COUNT(*) report...")
    
    # We fetch all country values to group by locally since PostgREST doesn't support GROUP BY yet natively
    countries = []
    limit = 1000
    offset = 0
    while True:
        try:
            res = supabase.table("scholarships").select("country").range(offset, offset+limit-1).execute()
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
    print("\nSELECT COUNT(*), country FROM scholarships GROUP BY country ORDER BY count DESC;")
    for country, count in counts.most_common():
        print(f"{count:10} | {country}")

if __name__ == "__main__":
    files = ["scraped_data/govt_scholarships.json", "scraped_data/idp_scholarships.json"]
    for f in files:
        if os.path.exists(f):
            upload_file(f)
        else:
            print(f"File {f} not found!")
            
    generate_report()
