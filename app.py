{\rtf1\ansi\ansicpg1252\cocoartf2820
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw12240\paperh20160\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
import pandas as pd\
import sqlite3\
import plotly.express as px\
\
st.title("\uc0\u55356 \u57172  Fast Food Sales Dashboard")\
\
# Connect to DB\
conn = sqlite3.connect('db/sales_data.db')\
df = pd.read_sql_query("SELECT * FROM sales", conn)\
\
# Clean columns\
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]\
\
# Example chart: Top 10 items\
top_items = df['item'].value_counts().head(10).reset_index()\
top_items.columns = ['item', 'count']\
\
fig = px.bar(top_items, x='item', y='count', title='Top 10 Ordered Items', color_discrete_sequence=['teal'])\
st.plotly_chart(fig)\
\
# Filter by time\
if 'when' in df.columns:\
    time_filter = st.selectbox("Select time of day:", sorted(df['when'].unique()))\
    filtered_df = df[df['when'] == time_filter]\
    st.write(f"Showing orders for: \{time_filter\}")\
    st.dataframe(filtered_df)\
}