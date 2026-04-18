-- SUPABASE MIGRATION: Add CRICOS columns
-- Run this in your Supabase SQL Editor: https://app.supabase.com/project/ewtcagefczcxmudjwogh/sql/new

-- Add CRICOS-specific columns to courses table
ALTER TABLE courses ADD COLUMN IF NOT EXISTS cricos_code TEXT;
ALTER TABLE courses ADD COLUMN IF NOT EXISTS provider_code TEXT;
ALTER TABLE courses ADD COLUMN IF NOT EXISTS state TEXT;

-- Add CRICOS-specific columns to universities table  
ALTER TABLE universities ADD COLUMN IF NOT EXISTS provider_code TEXT;
ALTER TABLE universities ADD COLUMN IF NOT EXISTS state TEXT;

-- Add indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_courses_cricos_code ON courses(cricos_code) WHERE cricos_code IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_courses_state ON courses(state) WHERE state IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_courses_provider_code ON courses(provider_code) WHERE provider_code IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_universities_provider_code ON universities(provider_code) WHERE provider_code IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_universities_state ON universities(state) WHERE state IS NOT NULL;

-- Verify the columns were added
SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'courses' 
AND column_name IN ('cricos_code', 'provider_code', 'state')
ORDER BY column_name;

SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'universities' 
AND column_name IN ('provider_code', 'state')
ORDER BY column_name;
