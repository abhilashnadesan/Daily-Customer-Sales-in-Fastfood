import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_URL = "http://127.0.0.1:5055/api/sales"
API_KEY = "12345abcde"

st.title("Sales Data Viewer")

# Filter input
item_filter = st.selectbox("Filter by order type", ["All", "Online", "In-Person"])

headers = {"x-api-key": API_KEY}
params = {}

if item_filter != "All":
    params['item'] = item_filter

df = pd.DataFrame()  # Initialize empty

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

# If data available, show updated graph
if not df.empty:
    st.subheader("Sales by Order Type")

    # Clean columns for safe use
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Check if 'order_type' or equivalent exists (change to actual column name)
    if 'order_type' in df.columns:
        sales_count = df['order_type'].value_counts().reset_index()
        sales_count.columns = ['order_type', 'count']

        fig = px.bar(
            sales_count,
            x='order_type',
            y='count',
            title="Number of Sales by Order Type",
            color='order_type',
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(fig)
    else:
        st.write("Column 'order_type' not found in data for graph.")

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
