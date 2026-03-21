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

def clean_course_record(record):
    cleaned = {}
    for k, v in record.items():
        if v == "None" or v == "N/A" or v == "":
            cleaned[k] = None
        else:
            cleaned[k] = v

    dur = cleaned.get('duration_months')
    if isinstance(dur, str):
        dur_lower = dur.lower()
        if 'year' in dur_lower:
            match = re.search(r'([\d.]+)', dur_lower)
            if match:
                cleaned['duration_months'] = int(float(match.group(1)) * 12)
            else:
                cleaned['duration_months'] = None
        elif 'month' in dur_lower:
            match = re.search(r'([\d.]+)', dur_lower)
            if match:
                cleaned['duration_months'] = int(float(match.group(1)))
            else:
                cleaned['duration_months'] = None
        else:
            try:
                cleaned['duration_months'] = int(dur)
            except ValueError:
                cleaned['duration_months'] = None
    elif isinstance(dur, float):
        cleaned['duration_months'] = int(dur)

    tf = cleaned.get('tuition_fee')
    if isinstance(tf, str):
        tf_lower = tf.lower()
        if "contact" in tf_lower or "not specified" in tf_lower:
            cleaned['tuition_fee'] = None
        else:
            curr_match = re.search(r'([A-Z]{3})', tf)
            if curr_match and not cleaned.get('currency'):
                cleaned['currency'] = curr_match.group(1)
            elif '£' in tf and not cleaned.get('currency'):
                cleaned['currency'] = 'GBP'
            elif '€' in tf and not cleaned.get('currency'):
                cleaned['currency'] = 'EUR'
            elif '$' in tf and not cleaned.get('currency'):
                 cleaned['currency'] = 'USD'
            
            clean_str = re.sub(r'[^\d.]', '', tf)
            try:
                if clean_str:
                    cleaned['tuition_fee'] = float(clean_str)
                else:
                    cleaned['tuition_fee'] = None
            except ValueError:
                cleaned['tuition_fee'] = None

    ielts = cleaned.get('ielts_overall')
    if isinstance(ielts, str):
        ielts_lower = ielts.lower()
        if "not required" in ielts_lower or "none" in ielts_lower:
            cleaned['ielts_overall'] = 0.0
        else:
            match = re.search(r'([\d.]+)', ielts_lower)
            if match:
                try:
                    cleaned['ielts_overall'] = float(match.group(1))
                except ValueError:
                    cleaned['ielts_overall'] = None
            else:
                cleaned['ielts_overall'] = None

    for key_date in ['last_verified']:
        if key_date in cleaned and isinstance(cleaned[key_date], str) and cleaned[key_date] not in [None, 'None', 'N/A']:
            try:
                parsed_date = date_parser.parse(cleaned[key_date])
                cleaned[key_date] = parsed_date.isoformat()
            except (ValueError, TypeError, OverflowError):
                cleaned[key_date] = None
                
    if 'start_dates' in cleaned and isinstance(cleaned['start_dates'], list):
        parsed_dates = []
        for d in cleaned['start_dates']:
            try:
                parsed_dates.append(date_parser.parse(d).strftime('%Y-%m-%d'))
            except:
                pass
        cleaned['start_dates'] = parsed_dates

    if 'is_active' in cleaned:
        cleaned['is_active'] = bool(cleaned['is_active'])

    return cleaned

def upload_file(filename):
    print(f"Loading {filename}...")
    with open(filename, "r") as f:
        data = json.load(f)
        
    # Skip the first 5 records which we already INSERTED via test_upload_courses.py!
    data = data[5:]
    
    total_records = len(data)
    print(f"Loaded {total_records} records to insert from {filename} (after skipping first 5).")
    
    batch_size = 500
    for i in range(0, total_records, batch_size):
        batch = data[i:i+batch_size]
        cleaned_batch = []
        for record in batch:
            try:
                cleaned = clean_course_record(record)
                cleaned_batch.append(cleaned)
            except Exception as e:
                pass
                
        max_retries = 3
        for attempt in range(max_retries):
            try:
                # User did not apply constraint, so we must just INSERT
                supabase.table("courses").insert(cleaned_batch).execute()
                print(f"Progress: Inserted {i + len(cleaned_batch)} / {total_records} records.")
                break
            except Exception as e:
                # Large payloads sometimes cause HTTP timeout, so sleep and retry
                if attempt == max_retries - 1:
                    print(f"FAILED batch {i} to {i+batch_size}. Error: {e}")
                else:
                    time.sleep(2)

def generate_report():
    print("\n--- FINAL REPORT ---")
    print("Fetching subject_category from courses...")
    
    categories = []
    limit = 1000
    offset = 0
    while True:
        try:
            res = supabase.table("courses").select("subject_category").range(offset, offset+limit-1).execute()
            data = res.data
            if not data:
                break
            for row in data:
                categories.append(row.get('subject_category'))
            offset += limit
        except Exception as e:
            print("Error fetching report data:", e)
            break
            
    counts = Counter(categories)
    print("\nSELECT subject_category, COUNT(*) FROM courses GROUP BY subject_category ORDER BY count DESC LIMIT 10;")
    for cat, count in counts.most_common(10):
        print(f"{cat} | {count}")

if __name__ == "__main__":
    files = ["scraped_data/idp_courses.json"]
    for f in files:
        if os.path.exists(f):
            upload_file(f)
        else:
            print(f"File {f} not found!")
            
    generate_report()
