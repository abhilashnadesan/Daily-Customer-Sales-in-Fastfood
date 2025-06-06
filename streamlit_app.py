import streamlit as st
import requests
import pandas as pd
import plotly.express as px

API_URL = "http://127.0.0.1:5000/api/sales"
API_KEY = "12345abcde"

st.title("Sales Data Viewer")

order_types = ["All", "Online", "In-Person"]
selected_order_type = st.selectbox("Filter by order type", order_types)

headers = {"x-api-key": API_KEY}
params = {}

if selected_order_type != "All":
    params['order_type'] = selected_order_type

try:
    with st.spinner("Loading data..."):
        response = requests.get(API_URL, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

    if data and "data" in data and data["data"]:
        df = pd.DataFrame(data["data"])

        st.write(f"Showing {len(df)} records")
        st.dataframe(df)

        # Normalize column names for convenience
        df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

        if 'order_type' in df.columns:
            sales_count = df['order_type'].value_counts().reset_index()
            sales_count.columns = ['order_type', 'count']

            fig = px.bar(
                sales_count,
                x='order_type',
                y='count',
                title="Number of Sales by Order Type",
                color='order_type',
                color_discrete_sequence=px.colors.qualitative.Pastel,
                labels={"order_type": "Order Type", "count": "Number of Sales"}
            )
            st.plotly_chart(fig)
        else:
            st.warning("Column 'order_type' not found for plotting.")
    else:
        st.info("No sales data available for the selected filter.")

except requests.exceptions.RequestException as e:
    st.error(f"API request error: {e}")

if st.button("Show Summary"):
    summary_url = API_URL.replace('/sales', '/sales/summary')
    try:
        with st.spinner("Loading summary..."):
            summary_resp = requests.get(summary_url, headers=headers)
            summary_resp.raise_for_status()
            summary_data = summary_resp.json()

        summary = summary_data.get("summary", {})
        total_orders = summary_data.get("total_orders", 0)

        if summary:
            st.write("### Sales Summary by Order Type:")
            for order_type, count in summary.items():
                st.write(f"- {order_type}: {count}")
            st.write(f"**Total Orders:** {total_orders}")
        else:
            st.info("No summary data available.")
    except requests.exceptions.RequestException as e:
        st.error(f"API request error: {e}")
