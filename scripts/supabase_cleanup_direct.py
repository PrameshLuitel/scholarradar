import asyncio
import os
import re
from typing import List, Dict, Any
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY") or os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    print("Error: SUPABASE_URL and SUPABASE_KEY must be set in .env")
    exit(1)

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# ---------------------------------------------------------------------------
# Functions
# ---------------------------------------------------------------------------

async def fix_countries():
    print("--- Fixing Countries (Bulk) ---")
    mapping = {
        "uk": ["Newcastle University", "Northumbria", "Norwich", "Hult", "Coventry", "Middlesex", "Ulster", "Anglia", "Brunel", "Surrey", "Sussex", "Warwick", "Leicester", "Hull", "Plymouth", "Keele", "Dundee", "Aberdeen", "Heriot", "Stirling", "Swansea", "Bangor", "Kent", "Strathclyde", "Edinburgh", "Manchester", "London", "Cardiff", "Birmingham", "Sheffield", "Bristol", "Nottingham", "Exeter", "Southampton", "Liverpool", "Leeds", "Bath", "Oxford", "Cambridge", "Imperial", "UCL", "Loughborough", "Durham", "Reading", "York", "Lancaster", "St Andrews", "Glasgow", "Royal Holloway", "King's College", "Queen Mary", "SOAS"],
        "usa": ["Arkansas", "New Mexico", "Tulsa", "San Francisco State", "Indiana", "Massachusetts", "Wright State", "Colorado", "Florida", "Michigan", "Ohio", "Texas", "Arizona", "Oregon", "Washington State", "Iowa", "Montana", "Wichita", "Toledo", "Pace", "Suffolk", "Sacred Heart", "Hawaii", "Rhode Island", "Delaware", "Wyoming", "Maine", "Memphis", "Akron", "Tennessee", "Kentucky", "Marquette", "DePaul", "Northeastern", "Baylor", "Portland", "Saginaw", "Fairleigh", "Stevens", "Hult"],
        "canada": ["Manitoba", "Toronto", "British Columbia", "McGill", "Alberta", "Calgary", "Waterloo", "Dalhousie", "Trent", "Langara", "Seneca", "Humber", "George Brown", "Laurentian", "Carleton", "Ottawa", "Saskatchewan", "Regina", "Winnipeg", "Cape Breton", "Lakehead", "Nipissing", "Algoma", "Kwantlen", "Thompson Rivers", "Fraser", "Douglas", "Bow Valley", "NorQuest", "Red River", "Sheridan", "Fleming", "Georgian", "Cambrian", "Centennial", "Conestoga", "Lambton", "Sault", "MacEwan", "Capilano", "Okanagan", "Concordia University of Edmonton", "Mount Allison", "Lethbridge", "OCAD", "St. Francis Xavier", "Wilfrid Laurier", "Brock", "Acadia", "Bishop", "Royal Roads"],
        "new_zealand": ["Massey", "Auckland", "Waikato", "Victoria University of Wellington", "Canterbury", "Otago", "Lincoln University", "AUT", "Unitec", "Ara Institute", "Otago Polytechnic"],
        "ireland": ["Dublin", "Cork", "Galway", "Limerick", "UCD", "Trinity College", "DCU", "Griffith College", "National College of Ireland"],
    }

    for country, unis in mapping.items():
        total_found = 0
        for uni in unis:
            try:
                res = supabase.table("scholarships").update({"country": country}).eq("country", "australia").eq("source", "idp").ilike("university", f"%{uni}%").execute()
                if res.data:
                    total_found += len(res.data)
            except Exception as e:
                print(f"Error updating {uni}: {e}")
        print(f"Updated {total_found} matched records to {country}")

async def fix_apply_urls():
    print("--- Fixing Apply URLs (Paginated) ---")
    total_fixed = 0
    while True:
        try:
            # Fetch batch of broken records
            res = (supabase.table("scholarships")
                   .select("id, source_url")
                   .eq("source", "idp")
                   .or_("apply_url.ilike.%stage-details%,apply_url.ilike.%how-do-i-apply%")
                   .like("source_url", "%http%")
                   .limit(200) # Small batches for reliability
                   .execute())
            
            if not res.data:
                break

            print(f"Fixing batch of {len(res.data)} URLs... (Total fixed: {total_fixed})")
            
            for row in res.data:
                supabase.table("scholarships").update({"apply_url": row["source_url"]}).eq("id", row["id"]).execute()
                total_fixed += 1
            
        except Exception as e:
            print(f"Error in batch: {e}")
            break
    
    print(f"Apply URL fixes complete. Total fixed: {total_fixed}")

async def normalize_study_levels():
    print("--- Normalizing Study Levels (Paginated) ---")
    # Fetch records that definitely need normalization (containing multiple levels or patterns)
    # We'll fetch all and process, but using pagination.
    offset = 0
    batch_size = 500
    total_normalized = 0
    
    while True:
        try:
            res = supabase.table("scholarships").select("id, study_level").range(offset, offset + batch_size - 1).execute()
            if not res.data:
                break

            for row in res.data:
                level = row.get("study_level") or ""
                orig_level = level
                
                normalized = None
                if re.search(r"doctorate|doctoral|phd|research", level, re.I):
                    normalized = "doctorate"
                elif re.search(r"postgraduate|post-graduate|masters|graduate taught", level, re.I):
                    normalized = "postgraduate"
                elif re.search(r"undergraduate|bachelor", level, re.I):
                    normalized = "undergraduate"
                elif re.search(r"foundation|pathway|pre-degree", level, re.I):
                    normalized = "foundation"
                    
                if normalized and normalized != orig_level:
                    supabase.table("scholarships").update({"study_level": normalized}).eq("id", row["id"]).execute()
                    total_normalized += 1

            if len(res.data) < batch_size:
                break
            offset += batch_size
            print(f"Processed {offset} records... (Normalized: {total_normalized})")
        except Exception as e:
            print(f"Error at offset {offset}: {e}")
            break

    print(f"Study level normalization complete. Total changed: {total_normalized}")

async def main():
    try:
        await fix_countries()
        await fix_apply_urls()
        # await normalize_study_levels() # Skipping this time if we already did 1000, or run it again to be safe
        print("\nAll repairs complete.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
