"""
Enhanced CRICOS Scraper - Combines ALL sheets with proper joins
Links: Courses + Course Locations + Institutions + Locations
"""
import asyncio
import os
import io
import datetime
from typing import List, Dict, Any

import httpx
import pandas as pd
import structlog
from pydantic import BaseModel

from src.database.models import University, Course
from src.database.queries import bulk_upsert_universities, bulk_upsert_courses

logger = structlog.get_logger().bind(scraper="CRICOSEnhancedScraper")

class CricosEnhancedScraper:
    def __init__(self):
        self.ckan_package_url = "https://data.gov.au/data/api/3/action/package_show?id=cricos"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

    async def _fetch_latest_xlsx_url(self) -> str:
        """Fetch latest CRICOS Excel file URL from data.gov.au"""
        async with httpx.AsyncClient() as client:
            response = await client.get(self.ckan_package_url, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            
            if not data.get("success"):
                raise ValueError("Failed to fetch data package from data.gov.au")
                
            resources = data["result"]["resources"]
            xlsx_resources = [r for r in resources if r.get("format", "").upper() == "XLSX" or ".xlsx" in r.get("url", "").lower()]
            xlsx_resources.sort(key=lambda x: x.get("created", ""), reverse=True)
            
            if not xlsx_resources:
                raise ValueError("No XLSX file found in the dataset")
                
            return xlsx_resources[0]["url"]

    def _process_institutions(self, df: pd.DataFrame) -> List[University]:
        """Process institutions and return list of University objects (deduplicated)"""
        universities_dict = {}
        df.columns = [str(c).lower().strip() for c in df.columns]
        
        # Log all column names for debugging
        logger.info("Institution columns", columns=df.columns.tolist())
        
        for _, row in df.iterrows():
            provider_code = str(row.get('cricos provider code', '')).strip()
            if not provider_code or provider_code.lower() == 'nan':
                continue
                
            institution_name = str(row.get('institution name', '')).strip()
            if not institution_name or institution_name.lower() == 'nan':
                continue
            
            # Skip duplicates - keep first occurrence
            if provider_code in universities_dict:
                continue
            
            # Get primary state from postal address
            state = str(row.get('postal address state', '')).strip()
            if not state or state.lower() == 'nan':
                state = None
            
            # Get city from postal address
            city = str(row.get('postal address city', '')).strip()
            if not city or city.lower() == 'nan':
                city = None
            
            # Get website
            website = str(row.get('website', '')).strip()
            if not website or website.lower() == 'nan':
                website = None
            
            # Get institution type
            institution_type = str(row.get('institution type', '')).strip()
            if not institution_type or institution_type.lower() == 'nan':
                institution_type = None
            
            # Get capacity
            capacity = None
            capacity_val = row.get('institution capacity')
            if pd.notna(capacity_val):
                try:
                    capacity = int(capacity_val)
                except (ValueError, TypeError):
                    pass
            
            # Get phone number - try multiple column name variations
            phone_number = None
            for col_name in ['phone number', 'telephone', 'phone', 'contact number']:
                if col_name in df.columns:
                    phone_val = str(row.get(col_name, '')).strip()
                    if phone_val and phone_val.lower() != 'nan':
                        phone_number = phone_val
                        break
            
            # Get email - try multiple column name variations
            email_address = None
            for col_name in ['email address', 'email', 'contact email']:
                if col_name in df.columns:
                    email_val = str(row.get(col_name, '')).strip()
                    if email_val and email_val.lower() != 'nan':
                        email_address = email_val
                        break
            
            # Build postal address from components
            postal_parts = []
            for col_name in ['postal address line 1', 'postal address line 2', 
                           'postal address line 3', 'postal address line 4',
                           'postal address city', 'postal address state', 'postal address postcode']:
                if col_name in df.columns:
                    val = str(row.get(col_name, '')).strip()
                    if val and val.lower() != 'nan':
                        postal_parts.append(val)
            postal_address = ', '.join(postal_parts) if postal_parts else None
            
            uni_data = {
                "name": institution_name,
                "country": "Australia",
                "world_ranking": None,
                "total_students": capacity,
                "website": website,
                "city": city,
                "state": state,
                "provider_code": provider_code,
                "phone_number": phone_number,
                "email_address": email_address,
                "postal_address": postal_address,
                "institution_type": institution_type,
            }
            universities_dict[provider_code] = University(**uni_data)
            
        universities = list(universities_dict.values())
        logger.info(f"Processed {len(universities)} unique institutions")
        return universities

    def _process_course_locations(self, df: pd.DataFrame) -> Dict[str, Dict[str, str]]:
        """Process course locations - returns dict: {course_code: {state, city}}"""
        course_location_map = {}
        df.columns = [str(c).lower().strip() for c in df.columns]
        
        for _, row in df.iterrows():
            course_code = str(row.get('cricos course code', '')).strip()
            state = str(row.get('location state', '')).strip()
            city = str(row.get('location city', '')).strip()
            
            if not course_code or course_code.lower() == 'nan':
                continue
            
            # Take the first location found for this course
            if course_code not in course_location_map:
                course_location_map[course_code] = {
                    'state': state if state and state.lower() != 'nan' else None,
                    'city': city if city and city.lower() != 'nan' else None
                }
        
        logger.info(f"Processed {len(course_location_map)} course locations")
        return course_location_map

    def _process_courses(self, df: pd.DataFrame, course_location_map: Dict) -> List[Course]:
        """Process courses and join with location data"""
        courses_dict = {}  # Use dict to deduplicate by cricos_code
        df.columns = [str(c).lower().strip() for c in df.columns]
        
        for _, row in df.iterrows():
            course_name = str(row.get('course name', '')).strip()
            institution_name = str(row.get('institution name', '')).strip()
            course_code = str(row.get('cricos course code', '')).strip()
            provider_code = str(row.get('cricos provider code', '')).strip()
            
            if not course_name or course_name.lower() == 'nan':
                continue
            if not institution_name or institution_name.lower() == 'nan':
                continue
            if not course_code or course_code.lower() == 'nan':
                continue
            
            # Skip duplicates - keep first occurrence
            if course_code in courses_dict:
                continue
            
            # Get location data from course_location_map
            location_data = course_location_map.get(course_code, {})
            state = location_data.get('state')
            city = location_data.get('city')
            
            # Parse duration (weeks to months)
            duration_weeks = None
            duration_months = None
            duration_val = row.get('duration (weeks)')
            if pd.notna(duration_val):
                try:
                    duration_weeks = int(float(duration_val))
                    duration_months = int(duration_weeks / 4.345)
                except (ValueError, TypeError):
                    pass
            
            # Parse tuition fee
            tuition_fee = None
            fee_val = row.get('tuition fee')
            if pd.notna(fee_val):
                try:
                    tuition_fee = float(str(fee_val).replace('$', '').replace(',', '').strip())
                except (ValueError, TypeError):
                    pass
            
            # Get course level
            course_level = str(row.get('course level', '')) if pd.notna(row.get('course level')) else None
            if course_level and course_level.lower() == 'nan':
                course_level = None
            
            # Get field of education (subject category)
            subject_category = str(row.get('field of education 1 broad field', '')) if pd.notna(row.get('field of education 1 broad field')) else None
            if subject_category and subject_category.lower() == 'nan':
                subject_category = None
            
            subject = str(row.get('field of education 1 narrow field', '')) if pd.notna(row.get('field of education 1 narrow field')) else None
            if subject and subject.lower() == 'nan':
                subject = None
            
            course_obj = Course(
                name=course_name,
                university=institution_name,
                country="Australia",
                city=city,
                level=course_level,
                subject=subject,
                subject_category=subject_category,
                duration_months=duration_months,
                tuition_fee=tuition_fee,
                currency="AUD",
                cricos_code=course_code,
                provider_code=provider_code if provider_code else None,
                state=state,
                is_active=True,
            )
            courses_dict[course_code] = course_obj
            
            # Log first few courses to verify state is being set
            if len(courses_dict) <= 3:
                logger.info(f"Course {len(courses_dict)}: {course_name[:50]}, cricos_code={course_code}, state={state}, city={city}")
        
        courses = list(courses_dict.values())
        logger.info(f"Processed {len(courses)} unique courses")
        return courses

    async def scrape_and_ingest(self):
        try:
            logger.info("Starting enhanced CRICOS scrape from data.gov.au...")
            file_url = await self._fetch_latest_xlsx_url()
            logger.info("Downloading CRICOS dataset.", url=file_url)
            
            async with httpx.AsyncClient(timeout=httpx.Timeout(120.0)) as client:
                resp = await client.get(file_url, headers=self.headers)
                resp.raise_for_status()
                xlsx_data = resp.content
                
            logger.info("Parsing Excel file...")
            xl = pd.ExcelFile(io.BytesIO(xlsx_data), engine="openpyxl")
            
            sheet_names = xl.sheet_names
            logger.info("Found sheets in workbook.", sheets=sheet_names)
            
            # Process ALL sheets
            universities = []
            course_location_map = {}
            courses = []
            
            # 1. Process Institutions
            if 'Institutions' in sheet_names:
                logger.info("Processing Institutions sheet...")
                df_inst = xl.parse('Institutions', header=2)
                universities = self._process_institutions(df_inst)
            
            # 2. Process Course Locations (LINKING TABLE) - MUST do this before courses
            if 'Course Locations' in sheet_names:
                logger.info("Processing Course Locations sheet...")
                df_course_loc = xl.parse('Course Locations', header=2)
                course_location_map = self._process_course_locations(df_course_loc)
                logger.info(f"Course location map has {len(course_location_map)} entries")
            
            # 3. Process Courses and JOIN with locations
            if 'Courses' in sheet_names:
                logger.info("Processing Courses sheet and joining with locations...")
                df_courses = xl.parse('Courses', header=2)
                courses = self._process_courses(df_courses, course_location_map)
            
            # 4. Also process Locations for additional data
            if 'Locations' in sheet_names:
                logger.info("Processing Locations sheet...")
                df_locations = xl.parse('Locations', header=2)
                # This is optional - we already have state from course locations
            
            logger.info(f"Extracted {len(universities)} universities and {len(courses)} courses.")
            
            # Log sample course to verify state is populated
            if courses:
                sample = courses[0]
                logger.info(f"Sample course: name={sample.name}, state={sample.state}, city={sample.city}, cricos_code={sample.cricos_code}")
            
            # Upsert to database
            if universities:
                logger.info("Upserting Universities to DB...")
                await bulk_upsert_universities(universities)
                logger.info("Universities updated.")
                
            if courses:
                logger.info("Upserting Courses to DB...")
                await bulk_upsert_courses(courses)
                logger.info("Courses updated.")
                
            logger.info("Enhanced CRICOS Scrape Completed Successfully!")
            logger.info(f"Total: {len(universities)} universities, {len(courses)} courses with location data")

        except Exception as e:
            logger.error("Enhanced CRICOS Scrape critical failure", error=str(e))
            raise

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    scraper = CricosEnhancedScraper()
    asyncio.run(scraper.scrape_and_ingest())
