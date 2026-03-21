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

def parse_currency_amount(value):
    """Clean currency like $35,000 and return float."""
    if not value or value in ["None", "N/A", "Not specified"]:
        return None
    if isinstance(value, (int, float)):
        return float(value)
    
    # Remove everything except digits, decimal point, and 'to' (if range)
    value_str = str(value)
    # Check if range
    if ' to ' in value_str.lower():
        return value_str # Handle in clean_record
    
    clean_str = re.sub(r'[^\d.]', '', value_str)
    try:
        if clean_str:
            return float(clean_str)
    except ValueError:
        pass
    return None

def clean_record(record):
    """Clean individual record according to rules."""
    cleaned = {}
    
    for k, v in record.items():
        # Handle "None" or "N/A"
        if v == "None" or v == "N/A" or v == "":
            cleaned[k] = None
        else:
            cleaned[k] = v

    # Handle award values (e.g., "$35,000" or "2000 to 5000")
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
                
    # Parse dates if they exist and are strings
    for key in ['deadline', 'last_verified']:
        if key in cleaned and isinstance(cleaned[key], str) and cleaned[key] not in [None, 'None', 'N/A']:
            try:
                parsed_date = date_parser.parse(cleaned[key])
                if key == 'deadline':
                    cleaned[key] = parsed_date.strftime('%Y-%m-%d')
                else:
                    # last_verified is TIMESTAMPTZ
                    cleaned[key] = parsed_date.isoformat()
            except (ValueError, TypeError, OverflowError):
                # If it's a completely unparseable string like "Contact the university"
                cleaned[key] = None

    # Ensure no None dictionary keys
    # Map 'award_value_min' logic correctly if they are combined in one string
    # Actually, the user asked to split if "2000 to 5000". If it's in a single string like award_value_min
    if isinstance(record.get('award_value_min'), str) and 'to' in record.get('award_value_min', '').lower():
        parts = re.split(r'\s+to\s+', record['award_value_min'].lower())
        if len(parts) == 2:
            cleaned['award_value_min'] = parse_currency_amount(parts[0])
            cleaned['award_value_max'] = parse_currency_amount(parts[1])

    # Convert is_active to bool
    if 'is_active' in cleaned:
        cleaned['is_active'] = bool(cleaned['is_active'])

    return cleaned

def test_insert_5():
    with open("scraped_data/idp_scholarships.json", "r") as f:
        data = json.load(f)
        
    test_batch = [clean_record(r) for r in data[:5]]
    
    print("Test batch cleaned. Attempting to UPSERT 5 records into Supabase...")
    try:
        result = supabase.table("scholarships").upsert(
            test_batch, 
            on_conflict="title,university"
        ).execute()
        
        print(f"Successfully inserted {len(result.data)} records!")
        print("Here are the 5 inserted records directly from Supabase:")
        print(json.dumps(result.data, indent=2))
        
    except Exception as e:
        print(f"FAILED to insert: {e}")
        print("Note: If the error is about a constraint, you need to run:")
        print("ALTER TABLE scholarships ADD CONSTRAINT uq_scholarship_title_univ UNIQUE (title, university);")

if __name__ == "__main__":
    test_insert_5()
