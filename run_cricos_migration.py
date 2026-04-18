"""Add unique constraints for CRICOS data upserts"""
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

project_ref = SUPABASE_URL.split('//')[1].split('.')[0]
DB_HOST = f"db.{project_ref}.supabase.co"
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = SUPABASE_SERVICE_KEY
DB_PORT = 5432

print(f"Connecting to Supabase database: {DB_HOST}")

try:
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )
    conn.autocommit = True
    cursor = conn.cursor()
    
    print("Connected successfully!")
    print("\nAdding unique constraints for CRICOS data...\n")
    
    # 1. Add unique constraint on cricos_code for courses
    print("1. Adding unique constraint on courses.cricos_code...")
    try:
        cursor.execute("""
            ALTER TABLE courses 
            ADD CONSTRAINT uq_courses_cricos_code 
            UNIQUE (cricos_code);
        """)
        print("   SUCCESS: Unique constraint added to cricos_code")
    except Exception as e:
        print(f"   ERROR: {e}")
    
    # 2. Add unique constraint on provider_code for universities
    print("\n2. Adding unique constraint on universities.provider_code...")
    try:
        cursor.execute("""
            ALTER TABLE universities 
            ADD CONSTRAINT uq_universities_provider_code 
            UNIQUE (provider_code);
        """)
        print("   SUCCESS: Unique constraint added to provider_code")
    except Exception as e:
        print(f"   ERROR: {e}")
    
    # 3. Create indexes for better performance
    print("\n3. Creating performance indexes...")
    try:
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_courses_state ON courses(state) WHERE state IS NOT NULL;
            CREATE INDEX IF NOT EXISTS idx_courses_city ON courses(city) WHERE city IS NOT NULL;
            CREATE INDEX IF NOT EXISTS idx_courses_level ON courses(level) WHERE level IS NOT NULL;
            CREATE INDEX IF NOT EXISTS idx_courses_university ON courses(university);
        """)
        print("   SUCCESS: Indexes created")
    except Exception as e:
        print(f"   ERROR: {e}")
    
    print("\nMigration completed!")
    
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"Failed to connect or execute: {e}")
    import traceback
    traceback.print_exc()
