from datetime import date, datetime
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, HttpUrl, Field
from uuid import UUID

class BaseDBModel(BaseModel):
    id: Optional[UUID] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class Scholarship(BaseDBModel):
    title: str
    university: str
    country: str
    city: Optional[str] = None
    study_level: Optional[str] = None  # undergraduate/postgraduate/doctorate/foundation/vocational
    subject: Optional[str] = None
    subject_category: Optional[str] = None
    funding_type: Optional[str] = None  # full/partial/fee_waiver/stipend/accommodation
    deadline: Optional[date] = None
    award_value_min: Optional[float] = None
    award_value_max: Optional[float] = None
    award_currency: Optional[str] = None
    description: Optional[str] = None
    eligibility: Optional[str] = None
    apply_url: Optional[str] = None
    source: Optional[str] = None  # idp/australia_awards/rtp/state_govt/university_direct
    source_url: Optional[str] = None
    is_active: bool = True
    last_verified: Optional[datetime] = None

class Course(BaseDBModel):
    name: str
    university: str
    country: str
    city: Optional[str] = None
    level: Optional[str] = None
    subject: Optional[str] = None
    subject_category: Optional[str] = None
    duration_months: Optional[int] = None
    tuition_fee: Optional[float] = None
    currency: Optional[str] = None
    ielts_overall: Optional[float] = None
    ielts_reading: Optional[float] = None
    ielts_writing: Optional[float] = None
    ielts_speaking: Optional[float] = None
    ielts_listening: Optional[float] = None
    gpa_requirement: Optional[str] = None
    entry_qualification: Optional[str] = None
    start_dates: Optional[List[str]] = Field(default_factory=list)
    idp_required: Optional[bool] = None
    cricos_code: Optional[str] = None
    provider_code: Optional[str] = None
    state: Optional[str] = None
    is_active: bool = True
    last_verified: Optional[datetime] = None

class University(BaseDBModel):
    name: str
    country: str
    city: Optional[str] = None
    world_ranking: Optional[int] = None
    subject_rankings: Optional[Dict[str, int]] = Field(default_factory=dict)
    acceptance_rate: Optional[float] = None
    total_students: Optional[int] = None
    international_students: Optional[int] = None
    tuition_min: Optional[float] = None
    tuition_max: Optional[float] = None
    currency: Optional[str] = None
    ielts_minimum: Optional[float] = None
    popular_subjects: Optional[List[str]] = Field(default_factory=list)
    facilities: Optional[List[str]] = Field(default_factory=list)
    accommodation_cost_min: Optional[float] = None
    accommodation_cost_max: Optional[float] = None
    website: Optional[str] = None
    idp_profile_url: Optional[str] = None
    provider_code: Optional[str] = None
    state: Optional[str] = None
    phone_number: Optional[str] = None
    email_address: Optional[str] = None
    postal_address: Optional[str] = None
    institution_type: Optional[str] = None

class VisaRequirement(BaseModel):
    id: Optional[UUID] = None
    nationality: str
    destination_country: str
    visa_type: Optional[str] = None
    visa_subclass: Optional[str] = None
    financial_requirement_aud: Optional[float] = None
    processing_weeks_min: Optional[int] = None
    processing_weeks_max: Optional[int] = None
    required_documents: Optional[List[str]] = Field(default_factory=list)
    health_requirements: Optional[str] = None
    work_rights_hours_per_week: Optional[int] = None
    notes: Optional[str] = None
    source_url: Optional[str] = None
    last_updated: Optional[datetime] = None

class CostOfLiving(BaseModel):
    id: Optional[UUID] = None
    city: str
    country: str
    rent_shared_min: Optional[float] = None
    rent_shared_max: Optional[float] = None
    rent_private_min: Optional[float] = None
    rent_private_max: Optional[float] = None
    food_monthly: Optional[float] = None
    transport_monthly: Optional[float] = None
    utilities_monthly: Optional[float] = None
    internet_monthly: Optional[float] = None
    total_monthly_min: Optional[float] = None
    total_monthly_max: Optional[float] = None
    currency: Optional[str] = None
    part_time_wage_hourly: Optional[float] = None
    last_updated: Optional[datetime] = None
