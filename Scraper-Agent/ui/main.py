import os
import sys
import streamlit as st

# ✅ Dynamically add base dir (Scraper-Agent) to sys.path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# ✅ Now import safely
from myapp.agent import summarize_text

st.set_page_config(page_title="Scraper Agent", layout="centered")

st.title("🕵️‍♀️ Scraper Agent - Text Summarizer")
st.markdown("Enter any long content and get a 2-line summary using **Gemini**.")

text_input = st.text_area("📥 Paste your content here", height=300)

if st.button("🔍 Summarize"):
    if text_input.strip() == "":
        st.warning("Please enter some content to summarize.")
    else:
        with st.spinner("Generating summary..."):
            result = summarize_text(text_input)
            # If using Gemini 1.5, result is probably a `Generation` object; check `.content`
            result = getattr(result, 'content', result)  # fallback if it's already string
        st.success("✅ Summary Generated")
        st.write(result)
        
        print("Current sys.path:", sys.path)

