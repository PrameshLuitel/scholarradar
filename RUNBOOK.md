# ScholarRadar — Scraper Runbook

## Prerequisites

```bash
cd /Users/prameshluitel/Documents/ScholarRadar

# Create virtualenv
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Environment Setup

```bash
cp .env.example .env
# Edit .env with your actual Supabase credentials:
#   SUPABASE_URL=https://xxxxx.supabase.co
#   SUPABASE_KEY=eyJhb...
```

## Database Setup

Run the schema SQL in your **Supabase SQL Editor** (Dashboard → SQL Editor → New query):

1. Paste contents of `src/database/schema.sql`
2. Execute — this creates all tables, indexes, the unique constraint, and auto-update trigger

## Running Scrapers

### IDP Scholarships (6 countries × 6 levels, ~6,288 scholarships)

```bash
python -c "
import asyncio
from src.scrapers.idp_scholarships import IDPScholarshipScraper

async def main():
    scraper = IDPScholarshipScraper(save_to_db=True)
    results = await scraper.scrape()
    print(f'Total scholarships scraped: {len(results)}')

asyncio.run(main())
"
```

> **⚠️ This will take a long time** — 524 pages × 12 cards × detail page per card,
> with 2-second rate limiting between requests. Budget ~6-12 hours for a full run.

### Government Scholarships (StudyAustralia.gov.au aggregator)

```bash
python -c "
import asyncio
from src.scrapers.govt_scholarships import StudyAustraliaScholarshipScraper

async def main():
    scraper = StudyAustraliaScholarshipScraper(save_to_db=True)
    results = await scraper.scrape()
    print(f'Government scholarships scraped: {len(results)}')

asyncio.run(main())
"
```

### Dry Run (no database writes)

```bash
python -c "
import asyncio
from src.scrapers.idp_scholarships import IDPScholarshipScraper

async def main():
    scraper = IDPScholarshipScraper(save_to_db=False)
    results = await scraper.scrape()
    for s in results[:5]:
        print(f'{s.title} | {s.university} | {s.country} | {s.award_value_min}-{s.award_value_max} {s.award_currency}')
    print(f'Total: {len(results)}')

asyncio.run(main())
"
```

### Quick Test — Scrape 1 page only

```bash
python -c "
import asyncio
from src.scrapers.idp_scholarships import IDPScholarshipScraper

async def main():
    scraper = IDPScholarshipScraper(save_to_db=False)
    cards = []
    url = scraper._build_url('australia', 'postgraduate', 1)
    html = await scraper.fetch(url)
    if html:
        cards = scraper._parse_listing(html)
        print(f'Cards found: {len(cards)}')
        for c in cards:
            print(f'  {c[\"title\"]} | {c[\"university\"]} | {c[\"award_text\"]}')
    await scraper.close()

asyncio.run(main())
"
```

## Running Tests

```bash
# All tests
python -m pytest tests/test_scrapers.py -v

# Specific test class
python -m pytest tests/test_scrapers.py::TestIDPListingParser -v

# With coverage
python -m pytest tests/ -v --tb=short
```

## Troubleshooting

| Symptom | Fix |
|---|---|
| `SUPABASE_URL not set` | Check `.env` file exists and has valid credentials |
| `403 Forbidden` on IDP | IDP may be blocking; increase `rate_limit_interval` |
| `429 Too Many Requests` | Increase `rate_limit_interval` (default 2.0 seconds) |
| `0 cards found per page` | IDP changed their HTML — inspect page and update CSS selectors in `_parse_listing()` |
| SSL errors | `pip install certifi` and ensure up-to-date certificates |
| `ModuleNotFoundError` | Ensure you're running from project root with `PYTHONPATH=.` |

## Key Architecture Notes

- **IDP locale**: The scraper uses `/nepal/` as the URL locale prefix (returns English content for all destinations). Change `LOCALE` in `idp_scholarships.py` if needed.
- **Pagination stop**: Scraper stops when a page returns fewer than 12 cards (the standard page size).
- **Upsert**: Uses `(title, university)` as the unique key — same scholarship won't create duplicates.
- **Stale records**: After a full scrape, any IDP scholarships in the DB that weren't found are marked `is_active=false`.
- **Government sites**: DFAT and education.gov.au block server-side scraping. We use StudyAustralia.gov.au as the aggregator instead.
