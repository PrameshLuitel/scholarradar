-- CRICOS Database Migration - Add Unique Constraints
-- Run this in your Supabase SQL Editor: https://app.supabase.com/project/ewtcagefczcxmudjwogh/sql/new

-- 1. Add unique constraint on cricos_code for courses table
-- This allows proper upserts using cricos_code as the unique identifier
ALTER TABLE courses 
ADD CONSTRAINT uq_courses_cricos_code 
UNIQUE (cricos_code);

-- 2. Add unique constraint on provider_code for universities table
-- This allows proper upserts using provider_code as the unique identifier
ALTER TABLE universities 
ADD CONSTRAINT uq_universities_provider_code 
UNIQUE (provider_code);

-- 3. Create performance indexes for faster filtering
CREATE INDEX IF NOT EXISTS idx_courses_state ON courses(state) WHERE state IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_courses_city ON courses(city) WHERE city IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_courses_level ON courses(level) WHERE level IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_courses_university ON courses(university);
CREATE INDEX IF NOT EXISTS idx_courses_country ON courses(country);

-- Verify the constraints were added
SELECT 
    conname as constraint_name,
    conrelid::regclass as table_name,
    pg_get_constraintdef(oid) as definition
FROM pg_constraint
WHERE conname IN ('uq_courses_cricos_code', 'uq_universities_provider_code');
