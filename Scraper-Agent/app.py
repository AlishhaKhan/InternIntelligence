import asyncio
from myapp.scraper import scrape_page
from myapp.agent import summarize_text
from myapp.api import app

async def run_scraper_agent(url):
    titles = await scrape_page(url)
    combined_text = "\n".join(titles)
    summary = summarize_text(combined_text)
    print("SUMMARY:\n", summary)

if __name__ == "__main__":
    url = "https://realpython.com/tutorials/web-dev/"  # 👈 Replace with any valid URL
    asyncio.run(run_scraper_agent(url))
