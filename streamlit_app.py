import streamlit as st
import requests
import pandas as pd

API_URL = "http://127.0.0.1:5055/api/sales"
API_KEY = "12345abcde"

st.title("Sales Data Viewer")

# Filter input
item_filter = st.selectbox("Filter by order type", ["All", "Online", "In-Person"])

headers = {"x-api-key": API_KEY}
params = {}

if item_filter != "All":
    params['item'] = item_filter

try:
    response = requests.get(API_URL, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        if data:
            df = pd.DataFrame(data)
            st.write(f"Showing {len(df)} records")
            st.dataframe(df)
        else:
            st.write("No data available for this filter.")
    else:
        st.error(f"API error: {response.status_code} - {response.text}")
except requests.exceptions.ConnectionError:
    st.error("Cannot connect to API. Is your Flask server running?")

# Show summary stats
if st.button("Show Summary"):
    summary_url = API_URL.replace('/sales', '/sales/summary')
    try:
        summary_resp = requests.get(summary_url, headers=headers)
        if summary_resp.status_code == 200:
            summary = summary_resp.json()
            st.write("Sales Summary by Order Type:")
            for k, v in summary.items():
                st.write(f"- {k}: {v}")
        else:
            st.error(f"API error: {summary_resp.status_code}")
    except requests.exceptions.ConnectionError:
        st.error("Cannot connect to API.")

