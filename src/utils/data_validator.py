from pydantic import BaseModel, HttpUrl, Field
from typing import List, Optional
from datetime import datetime

class Scholarship(BaseModel):
    title: str
    organization: str
    amount: Optional[str] = None
    deadline: Optional[datetime] = None
    url: HttpUrl
    description: str
    country: List[str] = Field(default_factory=list)

class Course(BaseModel):
    name: str
    university: str
    level: str  # e.g., Undergraduate, Postgraduate
    duration: str
    fee: Optional[str] = None
    url: HttpUrl

class University(BaseModel):
    name: str
    location: str
    ranking: Optional[int] = None
    website: HttpUrl
    description: Optional[str] = None

class VisaInfo(BaseModel):
    country: str
    type: str
    requirements: List[str]
    fee: str
    processing_time: str

class CostOfLiving(BaseModel):
    city: str
    country: str
    monthly_estimate: str
    breakdown: dict
