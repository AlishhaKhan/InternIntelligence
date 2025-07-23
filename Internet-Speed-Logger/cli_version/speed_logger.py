import speedtest
import csv
import os
from datetime import datetime

def test_speed():
    st = speedtest.Speedtest()
    download = st.download() / 1_000_000  # Convert to Mbps
    upload = st.upload() / 1_000_000      # Convert to Mbps
    ping = st.results.ping
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return [timestamp, round(download, 2), round(upload, 2), round(ping, 2)]

def log_speed():
    data = test_speed()
    file_path = "logs/speed_data.csv"

    # ✅ Check if file exists — if not, write headers first
    if not os.path.exists(file_path):
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Timestamp", "Download (Mbps)", "Upload (Mbps)", "Ping (ms)"])

    try:
        with open(file_path, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(data)
        print(f"[{data[0]}] ✅ Speed logged successfully.")
    except Exception as e:
        print(f"❌ Error writing to CSV: {e}")

if __name__ == "__main__":
    print("📡 Running Internet Speed Logger...")
    log_speed()
