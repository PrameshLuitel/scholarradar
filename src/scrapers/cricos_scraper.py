import asyncio
import os
import io
import datetime
from typing import List

import httpx
import pandas as pd
import structlog
from pydantic import BaseModel

from src.database.models import University, Course
from src.database.queries import bulk_upsert_universities, bulk_upsert_courses

logger = structlog.get_logger().bind(scraper="CRICOSMonthlyScraper")

class CricosScraper:
    def __init__(self):
        self.ckan_package_url = "https://data.gov.au/data/api/3/action/package_show?id=cricos"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}

    async def _fetch_latest_xlsx_url(self) -> str:
        """Hits the CKAN API to find the latest xlsx distribution."""
        async with httpx.AsyncClient() as client:
            response = await client.get(self.ckan_package_url, headers=self.headers)
            response.raise_for_status()
            data = response.json()
            
            if not data.get("success"):
                raise ValueError("Failed to fetch data package from data.gov.au")
                
            resources = data["result"]["resources"]
            
            # Filter to only xlsx files
            xlsx_resources = [r for r in resources if r.get("format", "").upper() == "XLSX" or ".xlsx" in r.get("url", "").lower()]
            
            # Sort by created descending
            xlsx_resources.sort(key=lambda x: x.get("created", ""), reverse=True)
            
            if not xlsx_resources:
                raise ValueError("No XLSX file found in the dataset")
                
            return xlsx_resources[0]["url"]

    def _process_institutions(self, df: pd.DataFrame) -> List[University]:
        universities = []
        # Usually it's Provider Code, Institution Name, Capacity
        # Lowercase all column names for easier lookup
        df.columns = [str(c).lower().strip() for c in df.columns]
        
        provider_name_col = next((c for c in df.columns if 'institution name' in c or 'provider name' in c), None)
        capacity_col = next((c for c in df.columns if 'capacity' in c), None)
        website_col = next((c for c in df.columns if 'website' in c), None)
        city_col = next((c for c in df.columns if 'city' in c or 'locality' in c or 'suburb' in c), None)
        type_col = next((c for c in df.columns if 'type' in c), None)

        if not provider_name_col:
            logger.error("Could not find provider name column in Institutions sheet", cols=df.columns.tolist())
            return []

        for _, row in df.iterrows():
            name = str(row[provider_name_col]).strip()
            if not name or name.lower() == 'nan':
                continue
                
            uni_kwargs = {
                "name": name,
                "country": "Australia",
                "world_ranking": None,
                "total_students": int(row[capacity_col]) if capacity_col and pd.notna(row[capacity_col]) else None,
                "website": str(row[website_col]) if website_col and pd.notna(row[website_col]) else None,
                "city": str(row[city_col]) if city_col and pd.notna(row[city_col]) else None,
            }
            universities.append(University(**uni_kwargs))
            
        # Deduplicate by name and country to prevent DB ON CONFLICT errors
        unique_unis = list({(u.name, u.country): u for u in universities}.values())
        return unique_unis

    def _process_courses(self, df: pd.DataFrame) -> List[Course]:
        courses = []
        df.columns = [str(c).lower().strip() for c in df.columns]
        
        course_name_col = next((c for c in df.columns if 'course name' in c), None)
        provider_name_col = next((c for c in df.columns if 'institution name' in c or 'provider name' in c), None)
        duration_col = next((c for c in df.columns if 'duration' in c and 'week' in c), None)
        tuition_fee_col = next((c for c in df.columns if 'tuition fee' in c), None)
        level_col = next((c for c in df.columns if 'course level' in c or 'aqf level' in c), None)

        if not course_name_col or not provider_name_col:
            logger.error("Could not find necessary columns in Courses sheet", cols=df.columns.tolist())
            return []

        for _, row in df.iterrows():
            course_name = str(row[course_name_col]).strip()
            uni_name = str(row[provider_name_col]).strip()
            
            if not course_name or course_name.lower() == 'nan' or not uni_name or uni_name.lower() == 'nan':
                continue
                
            # Parse Duration (convert weeks to months roughly)
            duration_months = None
            if duration_col and pd.notna(row[duration_col]):
                try:
                    weeks = float(row[duration_col])
                    duration_months = int(weeks / 4.345)
                except ValueError:
                    pass

            # Parse Tuition Fee
            tuition_fee = None
            if tuition_fee_col and pd.notna(row[tuition_fee_col]):
                try:
                    # Remove $ and commas
                    val = str(row[tuition_fee_col]).replace('$', '').replace(',', '').strip()
                    tuition_fee = float(val)
                except ValueError:
                    pass

            course_kwargs = {
                "name": course_name,
                "university": uni_name,
                "country": "Australia",
                "level": str(row[level_col]) if level_col and pd.notna(row[level_col]) else None,
                "duration_months": duration_months,
                "tuition_fee": tuition_fee,
                "currency": "AUD",  # CRICOS deals strictly in AUD
            }
            courses.append(Course(**course_kwargs))
            
        # Deduplicate by course name and university
        unique_courses = list({(c.name, c.university): c for c in courses}.values())
        return unique_courses


    async def scrape_and_ingest(self):
        try:
            logger.info("Finding latest CRICOS dataset from data.gov.au...")
            file_url = await self._fetch_latest_xlsx_url()
            logger.info("Downloading dataset.", url=file_url)
            
            async with httpx.AsyncClient(timeout=httpx.Timeout(120.0)) as client:
                resp = await client.get(file_url, headers=self.headers)
                resp.raise_for_status()
                xlsx_data = resp.content
                
            logger.info("Parsing Excel file...")
            try:
                xl = pd.ExcelFile(io.BytesIO(xlsx_data), engine="openpyxl")
            except Exception as e:
                logger.error("Failed to parse file as Excel. Attempting CSV fallback...", error=str(e))
                # It might be returning a CSV masquerading with an xlsx extension? Or corrupted format.
                raise
                
            sheet_names = xl.sheet_names
            logger.info("Found sheets in workbook.", sheets=sheet_names)
            
            institutions, courses = [], []
            
            # Map sheets based on keywords
            inst_sheet = next((s for s in sheet_names if 'provider' in s.lower() or 'institution' in s.lower()), None)
            course_sheet = next((s for s in sheet_names if 'course' in s.lower() and 'location' not in s.lower()), None)
            
            if inst_sheet:
                logger.info(f"Processing Institutions sheet: {inst_sheet}")
                df_inst = xl.parse(inst_sheet, header=2)
                institutions = self._process_institutions(df_inst)
                
            if course_sheet:
                logger.info(f"Processing Courses sheet: {course_sheet}")
                df_course = xl.parse(course_sheet, header=2)
                courses = self._process_courses(df_course)
                
            logger.info(f"Extracted {len(institutions)} universities and {len(courses)} courses.")
            
            if institutions:
                logger.info("Upserting Universities to DB...")
                await bulk_upsert_universities(institutions)
                logger.info("Universities updated.")
                
            if courses:
                logger.info("Upserting Courses to DB...")
                await bulk_upsert_courses(courses)
                logger.info("Courses updated.")
                
            logger.info("CRICOS Monthly Scrape Completed.")

        except Exception as e:
            logger.error("CRICOS Scrape critical failure", error=str(e))
            raise

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    scraper = CricosScraper()
    asyncio.run(scraper.scrape_and_ingest())
