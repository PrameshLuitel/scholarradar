-- Add contact information columns to universities table for CRICOS data
ALTER TABLE universities ADD COLUMN IF NOT EXISTS phone_number TEXT;
ALTER TABLE universities ADD COLUMN IF NOT EXISTS email_address TEXT;
ALTER TABLE universities ADD COLUMN IF NOT EXISTS postal_address TEXT;
ALTER TABLE universities ADD COLUMN IF NOT EXISTS institution_type TEXT;

-- Add indexes for better query performance
CREATE INDEX IF NOT EXISTS idx_universities_phone ON universities(phone_number) WHERE phone_number IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_universities_email ON universities(email_address) WHERE email_address IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_universities_institution_type ON universities(institution_type) WHERE institution_type IS NOT NULL;
