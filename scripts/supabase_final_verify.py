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

async def normalize_study_levels():
    print("--- Normalizing ALL Study Levels (Paginated) ---")
    offset = 0
    batch_size = 500
    total_changed = 0
    
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
                    total_changed += 1

            if len(res.data) < batch_size:
                break
            offset += batch_size
            print(f"Processed {offset} records... (Normalization changes this batch: {total_changed})")
        except Exception as e:
            print(f"Error at offset {offset}: {e}")
            break

    print(f"Study level normalization complete. Total changed in this run: {total_changed}")

async def verify():
    print("--- Verification ---")
    broken_urls = supabase.table("scholarships").select("*", count="exact").eq("source", "idp").ilike("apply_url", "%stage-details%").execute().count
    print(f"Broken Apply URLs remaining: {broken_urls}")
    
    total_idp = supabase.table("scholarships").select("*", count="exact").eq("source", "idp").execute().count
    print(f"Total IDP Scholarships: {total_idp}")

async def main():
    await normalize_study_levels()
    await verify()

if __name__ == "__main__":
    asyncio.run(main())
