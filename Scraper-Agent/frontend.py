# frontend.py

import streamlit as st
import requests

st.title("🕵️ Web Scraper Agent")

url = st.text_input("Enter a URL to scrape:")

if st.button("Scrape & Summarize"):
    response = requests.get(f"http://localhost:8000/scrape?url={url}")
    if response.status_code == 200:
        st.success("✅ Scraped successfully!")
        st.write(response.json()["summary"])
    else:
        st.error("❌ Something went wrong.")
