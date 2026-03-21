import json
import os
import re
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

    # 1. duration_months
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

    # 2. tuition_fee and currency
    tf = cleaned.get('tuition_fee')
    if isinstance(tf, str):
        tf_lower = tf.lower()
        if "contact" in tf_lower or "not specified" in tf_lower:
            cleaned['tuition_fee'] = None
        else:
            # Look for 3 letter currency pattern BEFORE extracting numbers
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

    # 3. ielts_overall
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

    # Date handling just in case
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

def test_insert_5():
    with open("scraped_data/idp_courses.json", "r") as f:
        data = json.load(f)
        
    test_batch = [clean_course_record(r) for r in data[:5]]
    
    print("Test courses batch cleaned. Attempting to UPSERT 5 records into Supabase...")
    try:
        # We try UPSERT first like scholarships.
        # If the courses table lacks the UNIQUE constraint, it will fail and we can fallback/insert.
        result = supabase.table("courses").upsert(
            test_batch, 
            on_conflict="name,university"
        ).execute()
        
        print(f"Successfully UPSERTED {len(result.data)} courses!")
        print(json.dumps(result.data, indent=2))
        
    except Exception as e:
        error_str = str(e)
        if "constraint" in error_str.lower() or "42P10" in error_str:
            print("UPSERT FAILED due to missing constraint. Attempting regular INSERT...")
            try:
                # Fallback to pure INSERT if no constraint exists
                result = supabase.table("courses").insert(test_batch).execute()
                print(f"Successfully INSERTED {len(result.data)} courses!")
                print(json.dumps(result.data, indent=2))
            except Exception as e2:
                print(f"FAILED to fall back to insert: {e2}")
        else:
            print(f"FAILED to insert: {e}")

if __name__ == "__main__":
    test_insert_5()
