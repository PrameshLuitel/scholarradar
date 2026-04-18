import asyncio
from src.database.client import get_db

def test():
    db = get_db()
    res = db.table("courses").select("id, name, cricos_code, source").limit(5).execute()
    print("ALL:", res.data)
    
    res2 = db.table("courses").select("id, name, cricos_code, source").not_.is_null("cricos_code").limit(5).execute()
    # wait, not_.is_null might be wrong syntax
    print("NOT NULL:", res2.data)

test()
