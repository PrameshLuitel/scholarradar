"""
PhD-Seeker Integration Scraper — integrates Aghababaei/PhD-Seeker data into ScholarRadar.

PhD-Seeker scrapes fully funded PhD positions from:
- scholarshipdb.net
- findaphd.com (EU and non-EU)

This scraper runs PhD-Seeker and converts the output to ScholarRadar database format.
"""

import sys
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional

import pandas as pd
import structlog

log = structlog.get_logger().bind(scraper="PhDSeekerScraper")

# Add PhD-Seeker to path
phd_seeker_path = Path(__file__).parent.parent.parent / "temp_phd_seeker"
sys.path.insert(0, str(phd_seeker_path))

try:
    from phdseeker.main import PhDSeeker
except ImportError as e:
    print(f"Failed to import PhD-Seeker: {e}")
    PhDSeeker = None

from src.scrapers.base_scraper import BaseScraper
from src.database.models import Scholarship

# Lazy DB imports
_upsert_scholarship = None


def _get_upsert_fn():
    global _upsert_scholarship
    if _upsert_scholarship is None:
        from src.database.queries import upsert_scholarship
        _upsert_scholarship = upsert_scholarship
    return _upsert_scholarship


class PhDSeekerScraper:
    """Scraper that integrates PhD-Seeker data into ScholarRadar."""

    def __init__(self):
        self.save_to_db = True
        self.keywords = "Computer Science, Engineering, Science, Technology, Mathematics, Physics, Chemistry, Biology"

    def run_phd_seeker(self, keywords: str, max_pages: int = 5) -> Optional[pd.DataFrame]:
        """Run PhD-Seeker and return the DataFrame of positions."""
        if PhDSeeker is None:
            log.error("PhD-Seeker not available")
            return None

        try:
            # Create PhD-Seeker instance
            ps = PhDSeeker(keywords, maxpage=max_pages)

            # Get positions DataFrame
            df = ps.positions

            if df is None or df.empty:
                log.warning("No positions found by PhD-Seeker")
                return None

            return df

        except Exception as e:
            log.error(f"Error running PhD-Seeker: {e}")
            return None

    def convert_to_scholarships(self, df) -> List[Dict[str, Any]]:
        """Convert PhD-Seeker DataFrame to ScholarRadar scholarship format."""
        scholarships = []

        for _, row in df.iterrows():
            try:
                # Parse the data
                title = str(row.get('Title', '')).strip()
                country = str(row.get('Country', '')).strip()
                date_str = str(row.get('Date', '')).strip()
                link = str(row.get('Link', '')).strip()

                if not title or not country or not link:
                    continue

                # Convert to ScholarRadar format
                scholarship = {
                    "title": title,
                    "university": "Various Universities",  # PhD-Seeker doesn't specify university
                    "country": country,
                    "city": None,
                    "study_level": "doctorate",
                    "subject": None,  # Could be extracted from title
                    "subject_category": None,
                    "funding_type": "full",  # PhD-Seeker focuses on fully funded positions
                    "deadline": None,  # PhD-Seeker doesn't provide deadlines
                    "award_value_min": None,
                    "award_value_max": None,
                    "award_currency": None,
                    "description": f"PhD Position: {title}",
                    "eligibility": "Fully funded PhD position",
                    "apply_url": link,
                    "source": "phd_seeker",
                    "source_url": link,
                    "is_active": True,
                    "last_verified": datetime.now(),
                }

                scholarships.append(scholarship)

            except Exception as e:
                log.error(f"Error processing row: {e}")
                continue

        return scholarships

    def scrape(self) -> List[Dict[str, Any]]:
        """Main scraping method."""
        log.info("Starting PhD-Seeker integration scrape")

        # Run PhD-Seeker
        df = self.run_phd_seeker(self.keywords, max_pages=3)
        if df is None or df.empty:
            log.warning("No data retrieved from PhD-Seeker")
            return []

        log.info(f"Retrieved {len(df)} positions from PhD-Seeker")

        # Convert to ScholarRadar format
        scholarships = self.convert_to_scholarships(df)

        log.info(f"Converted {len(scholarships)} positions to ScholarRadar format")

        return scholarships

    def save_to_database(self, scholarships: List[Dict[str, Any]]) -> int:
        """Save scholarships to database."""
        upsert_fn = _get_upsert_fn()
        saved_count = 0

        for scholarship_data in scholarships:
            try:
                scholarship = Scholarship(**scholarship_data)
                upsert_fn(scholarship)
                saved_count += 1
            except Exception as e:
                log.error(f"Error saving scholarship: {e}")
                continue

        log.info(f"Saved {saved_count} scholarships to database")
        return saved_count


def run_scraper():
    """Run the PhD-Seeker scraper."""
    scraper = PhDSeekerScraper()
    scholarships = scraper.scrape()
    if scholarships:
        saved_count = scraper.save_to_database(scholarships)
        print(f"Successfully scraped and saved {saved_count} PhD positions from PhD-Seeker")
    else:
        print("No scholarships scraped from PhD-Seeker")


if __name__ == "__main__":
    run_scraper()