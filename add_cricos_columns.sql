-- Add CRICOS-specific columns to courses table
ALTER TABLE courses ADD COLUMN IF NOT EXISTS cricos_code TEXT;
ALTER TABLE courses ADD COLUMN IF NOT EXISTS provider_code TEXT;
ALTER TABLE courses ADD COLUMN IF NOT EXISTS state TEXT;

-- Add CRICOS-specific columns to universities table
ALTER TABLE universities ADD COLUMN IF NOT EXISTS provider_code TEXT;
ALTER TABLE universities ADD COLUMN IF NOT EXISTS state TEXT;

-- Add indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_courses_cricos_code ON courses(cricos_code);
CREATE INDEX IF NOT EXISTS idx_courses_state ON courses(state);
CREATE INDEX IF NOT EXISTS idx_courses_provider_code ON courses(provider_code);
