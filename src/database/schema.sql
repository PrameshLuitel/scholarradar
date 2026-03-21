-- Enable UUID extension
create extension if not exists "uuid-ossp";

-- Scholarships Table
create table if not exists scholarships (
    id uuid primary key default uuid_generate_v4(),
    title text not null,
    university text not null,
    country text not null,
    city text,
    study_level text,
    subject text,
    subject_category text,
    funding_type text,
    deadline date,
    award_value_min numeric,
    award_value_max numeric,
    award_currency text,
    description text,
    eligibility text,
    apply_url text,
    source text,
    source_url text,
    is_active boolean default true,
    last_verified timestamptz,
    created_at timestamptz default now(),
    updated_at timestamptz default now()
);

create index if not exists idx_scholarships_country on scholarships(country);
create index if not exists idx_scholarships_study_level on scholarships(study_level);
create index if not exists idx_scholarships_subject on scholarships(subject);
create index if not exists idx_scholarships_subject_category on scholarships(subject_category);
create index if not exists idx_scholarships_deadline on scholarships(deadline);
create index if not exists idx_scholarships_is_active on scholarships(is_active);

-- Unique constraint for upsert (prevents duplicate title+university combos)
alter table scholarships
    add constraint uq_scholarships_title_uni unique (title, university);

-- Auto-update updated_at on row modification
create or replace function update_updated_at()
returns trigger as $$
begin
    new.updated_at = now();
    return new;
end;
$$ language plpgsql;

create trigger trg_scholarships_updated_at
    before update on scholarships
    for each row execute function update_updated_at();

-- Courses Table
create table if not exists courses (
    id uuid primary key default uuid_generate_v4(),
    name text not null,
    university text not null,
    country text not null,
    city text,
    level text,
    subject text,
    subject_category text,
    duration_months integer,
    tuition_fee numeric,
    currency text,
    ielts_overall numeric,
    ielts_reading numeric,
    ielts_writing numeric,
    ielts_speaking numeric,
    ielts_listening numeric,
    gpa_requirement text,
    entry_qualification text,
    start_dates jsonb,
    apply_url text,
    source_url text,
    is_active boolean default true,
    last_verified timestamptz,
    created_at timestamptz default now(),
    updated_at timestamptz default now()
);

create index if not exists idx_courses_country on courses(country);
create index if not exists idx_courses_level on courses(level);
create index if not exists idx_courses_subject on courses(subject);

-- Universities Table
create table if not exists universities (
    id uuid primary key default uuid_generate_v4(),
    name text not null,
    country text not null,
    city text,
    world_ranking integer,
    subject_rankings jsonb,
    acceptance_rate numeric,
    total_students integer,
    international_students integer,
    tuition_min numeric,
    tuition_max numeric,
    currency text,
    ielts_minimum numeric,
    popular_subjects jsonb,
    facilities jsonb,
    accommodation_cost_min numeric,
    accommodation_cost_max numeric,
    website text,
    idp_profile_url text,
    created_at timestamptz default now(),
    updated_at timestamptz default now()
);

-- Visa Requirements Table
create table if not exists visa_requirements (
    id uuid primary key default uuid_generate_v4(),
    nationality text not null,
    destination_country text not null,
    visa_type text,
    visa_subclass text,
    financial_requirement_aud numeric,
    processing_weeks_min integer,
    processing_weeks_max integer,
    required_documents jsonb,
    health_requirements text,
    work_rights_hours_per_week integer,
    notes text,
    source_url text,
    last_updated timestamptz default now()
);

-- Cost of Living Table
create table if not exists cost_of_living (
    id uuid primary key default uuid_generate_v4(),
    city text not null,
    country text not null,
    rent_shared_min numeric,
    rent_shared_max numeric,
    rent_private_min numeric,
    rent_private_max numeric,
    food_monthly numeric,
    transport_monthly numeric,
    utilities_monthly numeric,
    internet_monthly numeric,
    total_monthly_min numeric,
    total_monthly_max numeric,
    currency text,
    part_time_wage_hourly numeric,
    last_updated timestamptz default now()
);
