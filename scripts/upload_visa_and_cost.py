import json
import os
import re
from dateutil import parser as date_parser
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_SERVICE_ROLE_KEY") or os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def clean_record(record):
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
            
    # Make sure text arrays are actual lists
    if 'required_documents' in cleaned and cleaned['required_documents'] is None:
        cleaned['required_documents'] = []
        
    for k in cleaned.keys():
        if 'last_updated' in k or 'last_verified' in k:
            if cleaned[k]:
                try:
                    cleaned[k] = date_parser.parse(cleaned[k]).isoformat()
                except:
                    cleaned[k] = None
                    
    return cleaned

def upload_visa():
    print("Loading Visa Requirements...")
    with open("scraped_data/visa_requirements.json", "r") as f:
        data = json.load(f)
        
    cleaned_data = [clean_record(r) for r in data]
    print(f"Loaded {len(cleaned_data)} visa records. Inserting...")
    
    # We use INSERT. If they already insert once, another run might duplicate.
    try:
        supabase.table("visa_requirements").insert(cleaned_data).execute()
        print("Success inserting visa requirements.")
    except Exception as e:
        if "duplicate key" in str(e).lower():
            print("Visa requirements likely already exist (duplicate).")
        else:
            print(f"Insert failed: {e}")

def upload_cost():
    print("Loading Cost of Living...")
    with open("scraped_data/cost_of_living.json", "r") as f:
        data = json.load(f)
        
    cleaned_data = [clean_record(r) for r in data]
    print(f"Loaded {len(cleaned_data)} cost records. Inserting...")
    
    try:
        supabase.table("cost_of_living").insert(cleaned_data).execute()
        print("Success inserting cost of living.")
    except Exception as e:
        print(f"Insert failed: {e}")

def verify_data():
    print("\n--- VERIFICATION ---")
    
    # Visa Nepal query
    print("Query: SELECT * FROM visa_requirements WHERE nationality = 'nepal';")
    res_visa = supabase.table("visa_requirements").select("*").eq("nationality", "nepal").execute()
    data_visa = res_visa.data
    if data_visa:
        print(f"SUCCESS: Found {len(data_visa)} records for Nepal in Visa requirements.")
        print("First record snippet:", {k: data_visa[0].get(k) for k in ['nationality', 'destination_country', 'financial_requirement_aud']})
    else:
        print("CRITICAL ERROR: No records found for Nepal in visa_requirements.")

    # Cost Australia query
    print("\nQuery: SELECT * FROM cost_of_living WHERE country = 'australia';")
    res_cost = supabase.table("cost_of_living").select("*").eq("country", "australia").execute()
    data_cost = res_cost.data
    if data_cost:
        print(f"SUCCESS: Found {len(data_cost)} records for Australia in Cost of Living.")
        print("First record snippet:", {k: data_cost[0].get(k) for k in ['city', 'country', 'currency', 'rent_shared_min']})
    else:
        print("CRITICAL ERROR: No records found for Australia in cost_of_living.")

if __name__ == "__main__":
    upload_visa()
    upload_cost()
    verify_data()
