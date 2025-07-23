import aiohttp
from bs4 import BeautifulSoup

async def fetch_html(session, url):
    async with session.get(url) as response:
        return await response.text()

async def scrape_page(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch_html(session, url)
        soup = BeautifulSoup(html, "html.parser")

        # Example: grab all <h1> titles
        titles = [h1.get_text(strip=True) for h1 in soup.find_all("h1")]
        return titles
