-- ==========================================
-- 1. SCHOLARSHIPS TABLE
-- ==========================================
CREATE TABLE scholarships (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    
    title TEXT NOT NULL,
    university TEXT NOT NULL,
    country TEXT NOT NULL,
    city TEXT,
    study_level TEXT,
    subject TEXT,
    subject_category TEXT,
    funding_type TEXT,
    deadline DATE,
    award_value_min DECIMAL,
    award_value_max DECIMAL,
    award_currency TEXT,
    description TEXT,
    eligibility TEXT,
    apply_url TEXT,
    source TEXT,
    source_url TEXT,
    is_active BOOLEAN NOT NULL DEFAULT true,
    last_verified TIMESTAMPTZ
);

-- Indexes for Scholarships
CREATE INDEX idx_scholarships_country ON scholarships(country);
CREATE INDEX idx_scholarships_university ON scholarships(university);
CREATE INDEX idx_scholarships_study_level ON scholarships(study_level);
CREATE INDEX idx_scholarships_is_active ON scholarships(is_active);

-- RLS Policies for Scholarships
ALTER TABLE scholarships ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Allow public read access on scholarships" 
    ON scholarships FOR SELECT USING (true);
CREATE POLICY "Allow service role full access on scholarships" 
    ON scholarships FOR ALL TO service_role USING (true) WITH CHECK (true);


-- ==========================================
-- 2. COURSES TABLE
-- ==========================================
CREATE TABLE courses (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    
    name TEXT NOT NULL,
    university TEXT NOT NULL,
    country TEXT NOT NULL,
    city TEXT,
    level TEXT,
    subject TEXT,
    subject_category TEXT,
    duration_months INTEGER,
    tuition_fee DECIMAL,
    currency TEXT,
    ielts_overall DECIMAL,
    ielts_reading DECIMAL,
    ielts_writing DECIMAL,
    ielts_speaking DECIMAL,
    ielts_listening DECIMAL,
    gpa_requirement TEXT,
    entry_qualification TEXT,
    start_dates TEXT[] DEFAULT '{}',
    apply_url TEXT,
    source_url TEXT,
    is_active BOOLEAN NOT NULL DEFAULT true,
    last_verified TIMESTAMPTZ
);

-- Indexes for Courses
CREATE INDEX idx_courses_country ON courses(country);
CREATE INDEX idx_courses_university ON courses(university);
CREATE INDEX idx_courses_subject_category ON courses(subject_category);
CREATE INDEX idx_courses_is_active ON courses(is_active);

-- RLS Policies for Courses
ALTER TABLE courses ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Allow public read access on courses" 
    ON courses FOR SELECT USING (true);
CREATE POLICY "Allow service role full access on courses" 
    ON courses FOR ALL TO service_role USING (true) WITH CHECK (true);


-- ==========================================
-- 3. UNIVERSITIES TABLE
-- ==========================================
CREATE TABLE universities (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    
    name TEXT NOT NULL,
    country TEXT NOT NULL,
    city TEXT,
    world_ranking INTEGER,
    subject_rankings JSONB DEFAULT '{}'::jsonb,
    acceptance_rate DECIMAL,
    total_students INTEGER,
    international_students INTEGER,
    tuition_min DECIMAL,
    tuition_max DECIMAL,
    currency TEXT,
    ielts_minimum DECIMAL,
    popular_subjects TEXT[] DEFAULT '{}',
    facilities TEXT[] DEFAULT '{}',
    accommodation_cost_min DECIMAL,
    accommodation_cost_max DECIMAL,
    website TEXT,
    idp_profile_url TEXT
);

-- Indexes for Universities
CREATE INDEX idx_universities_country ON universities(country);
CREATE INDEX idx_universities_name ON universities(name);
CREATE INDEX idx_universities_world_ranking ON universities(world_ranking);

-- RLS Policies for Universities
ALTER TABLE universities ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Allow public read access on universities" 
    ON universities FOR SELECT USING (true);
CREATE POLICY "Allow service role full access on universities" 
    ON universities FOR ALL TO service_role USING (true) WITH CHECK (true);


-- ==========================================
-- 4. VISA REQUIREMENTS TABLE
-- ==========================================
CREATE TABLE visa_requirements (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    
    nationality TEXT NOT NULL,
    destination_country TEXT NOT NULL,
    visa_type TEXT,
    visa_subclass TEXT,
    financial_requirement_aud DECIMAL,
    processing_weeks_min INTEGER,
    processing_weeks_max INTEGER,
    required_documents TEXT[] DEFAULT '{}',
    health_requirements TEXT,
    work_rights_hours_per_week INTEGER,
    notes TEXT,
    source_url TEXT,
    last_updated TIMESTAMPTZ
);

-- Indexes for Visa Requirements
CREATE INDEX idx_visa_reqs_dest_country ON visa_requirements(destination_country);
CREATE INDEX idx_visa_reqs_nationality ON visa_requirements(nationality);

-- RLS Policies for Visa Requirements
ALTER TABLE visa_requirements ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Allow public read access on visa_requirements" 
    ON visa_requirements FOR SELECT USING (true);
CREATE POLICY "Allow service role full access on visa_requirements" 
    ON visa_requirements FOR ALL TO service_role USING (true) WITH CHECK (true);


-- ==========================================
-- 5. COST OF LIVING TABLE
-- ==========================================
CREATE TABLE cost_of_living (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    
    city TEXT NOT NULL,
    country TEXT NOT NULL,
    rent_shared_min DECIMAL,
    rent_shared_max DECIMAL,
    rent_private_min DECIMAL,
    rent_private_max DECIMAL,
    food_monthly DECIMAL,
    transport_monthly DECIMAL,
    utilities_monthly DECIMAL,
    internet_monthly DECIMAL,
    total_monthly_min DECIMAL,
    total_monthly_max DECIMAL,
    currency TEXT,
    part_time_wage_hourly DECIMAL,
    last_updated TIMESTAMPTZ
);

-- Indexes for Cost of Living
CREATE INDEX idx_cost_of_living_country ON cost_of_living(country);
CREATE INDEX idx_cost_of_living_city ON cost_of_living(city);

-- RLS Policies for Cost of Living
ALTER TABLE cost_of_living ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Allow public read access on cost_of_living" 
    ON cost_of_living FOR SELECT USING (true);
CREATE POLICY "Allow service role full access on cost_of_living" 
    ON cost_of_living FOR ALL TO service_role USING (true) WITH CHECK (true);
