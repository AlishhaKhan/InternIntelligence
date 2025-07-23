import asyncio
from app.scraper import scrape_page
from app.agent import summarize_text
from app.api import app

async def run_scraper_agent(url):
    titles = await scrape_page(url)
    combined_text = "\n".join(titles)
    summary = summarize_text(combined_text)
    print("SUMMARY:\n", summary)

if __name__ == "__main__":
    url = "https://example.com"
    asyncio.run(run_scraper_agent(url))
