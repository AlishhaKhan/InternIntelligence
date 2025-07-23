import speedtest
from datetime import datetime

def test_speed():
    st = speedtest.Speedtest()
    st.get_best_server()

    download = st.download() / 1_000_000  # Convert to Mbps
    upload = st.upload() / 1_000_000      # Convert to Mbps
    ping = st.results.ping
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return {
        "Timestamp": timestamp,
        "Download (Mbps)": round(download, 2),
        "Upload (Mbps)": round(upload, 2),
        "Ping (ms)": round(ping, 2)
    }
