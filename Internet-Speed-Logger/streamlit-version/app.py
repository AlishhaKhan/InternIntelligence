import streamlit as st
import pandas as pd
import os
import csv
from utils.speed_test import test_speed

# ---- CONFIG & TITLE ----
st.set_page_config(page_title="🚀 Internet Speed Logger", layout="centered")
st.markdown("<h1 style='text-align:center; color:#6C63FF;'>📶 Internet Speed Logger</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Test, track & visualize your internet speed effortlessly!</p>", unsafe_allow_html=True)

CSV_FILE = "logs/speed_data.csv"
os.makedirs("logs", exist_ok=True)

# ---- DATA UTILS ----
def load_data():
    if os.path.exists(CSV_FILE):
        return pd.read_csv(CSV_FILE)
    return pd.DataFrame(columns=["Timestamp", "Download (Mbps)", "Upload (Mbps)", "Ping (ms)"])

def append_to_csv(data):
    file_exists = os.path.exists(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

# ---- MAIN ACTION ----
st.divider()
if st.button("🧪 Run Speed Test Now"):
    st.info("Testing speed... Please wait ⏳")
    results = test_speed()
    append_to_csv(results)
    st.success("✅ Speed logged successfully!")

    st.metric(label="💾 Download Speed", value=f"{results['Download (Mbps)']} Mbps")
    st.metric(label="📤 Upload Speed", value=f"{results['Upload (Mbps)']} Mbps")
    st.metric(label="📡 Ping", value=f"{results['Ping (ms)']} ms")

# ---- HISTORY VIEW ----
st.divider()
st.markdown("## 📈 Speed Test History")
df = load_data()

if not df.empty:
    st.dataframe(df[::-1], use_container_width=True)
else:
    st.warning("No speed data logged yet. Run a test above! 📊")
