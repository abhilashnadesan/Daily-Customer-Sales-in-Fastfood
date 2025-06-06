import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

st.title("🍔 Fast Food Sales Dashboard")

# Connect to DB
conn = sqlite3.connect('db/sales_data.db')
df = pd.read_sql_query("SELECT * FROM sales", conn)

# Clean columns
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Example chart: Top 10 items
top_items = df['item'].value_counts().head(10).reset_index()
top_items.columns = ['item', 'count']

fig = px.bar(top_items, x='item', y='count', title='Top 10 Ordered Items', color_discrete_sequence=['teal'])
st.plotly_chart(fig)

# Filter by time
if 'when' in df.columns:
    time_filter = st.selectbox("Select time of day:", sorted(df['when'].unique()))
    filtered_df = df[df['when'] == time_filter]
    st.write(f"Showing orders for: {time_filter}")
    st.dataframe(filtered_df)
