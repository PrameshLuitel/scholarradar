import asyncio
import sys
import os

from src.scheduler.jobs import scrape_all_databases, health_report

async def main():
    print("🚀 Starting GitHub Actions Daily Scraper")
    
    try:
        print("\n📊 Pre-scrape Health Report:")
        await health_report()
        
        print("\n🌐 Running All live scrapers and syncing to Supabase...")
        await scrape_all_databases()
        
        print("\n📊 Post-scrape Health Report:")
        await health_report()
        
        print("\n✅ Scrape workflow completed successfully.")
    except Exception as e:
        print(f"\n❌ Scraper failed with error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Ensure stdout is unbuffered
    sys.stdout.reconfigure(line_buffering=True)
    asyncio.run(main())
