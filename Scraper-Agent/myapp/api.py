from fastapi import FastAPI
from myapp.scraper import scrape_page
from myapp.agent import summarize_text
import asyncio

app = FastAPI()

@app.get("/scrape")
async def scrape(url: str):
    titles = await scrape_page(url)
    combined_text = "\n".join(titles)
    summary = summarize_text(combined_text)
    return {
        "titles": titles,
        "summary": summary
    }
