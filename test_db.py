from dotenv import load_dotenv
load_dotenv()
from src.database.client import get_db

db = get_db()
print("Total courses:", db.table("courses").select("*", count="exact").limit(0).execute().count)

c = db.table("courses").select("name,cricos_code,source").limit(5).execute()
print("Sample courses:", c.data)

cricos = db.table("courses").select("name,cricos_code,source").eq("source", "CRICOS").limit(5).execute()
print("CRICOS source courses:", len(cricos.data), cricos.data)

cricos2 = db.table("courses").select("name,cricos_code,source").ilike("cricos_code", "%_%").limit(5).execute()
print("ilike cricos_code courses:", len(cricos2.data), cricos2.data)

try:
    cricos3 = db.table("courses").select("name,cricos_code,source").neq("cricos_code", "null").limit(5).execute()
    print("neq null:", len(cricos3.data))
except Exception as e:
    print("neq null error:", e)

