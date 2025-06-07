import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Sales Data Viewer", layout="wide")
st.title("Sales Data Viewer")

@st.cache_data
def load_data():
    df = pd.read_csv('sales_cleaned.csv')
    df['gender'] = df['gender'].map({0: 'Female', 1: 'Male'})
    df['hour'] = df['hour'].astype(int)
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")

genders = ["All"] + sorted(df['gender'].dropna().unique().tolist())
selected_gender = st.sidebar.selectbox("Select Gender", genders)

order_types = ["All"] + sorted(df['order_type'].dropna().unique().tolist())
selected_order_type = st.sidebar.selectbox("Select Order Type", order_types)

locations = ["All"] + sorted(df['location'].dropna().unique().tolist())
selected_location = st.sidebar.selectbox("Select Location", locations)

payment_methods = ["All"] + sorted(df['payment_method'].dropna().unique().tolist())
selected_payment = st.sidebar.selectbox("Select Payment Method", payment_methods)

food_items = ["All"] + sorted(df['food_item'].dropna().unique().tolist())
selected_food = st.sidebar.selectbox("Select Food Item", food_items)

# List of filters in order
filters = [
    ('gender', selected_gender),
    ('order_type', selected_order_type),
    ('location', selected_location),
    ('payment_method', selected_payment),
    ('food_item', selected_food)
]

def filter_df(dataframe, filters_list):
    temp_df = dataframe.copy()
    for col, val in filters_list:
        if val != "All":
            temp_df = temp_df[temp_df[col] == val]
    return temp_df

# Try applying all filters, if empty relax filters one by one from the end
filtered_df = filter_df(df, filters)
applied_filters = filters.copy()

while filtered_df.empty and applied_filters:
    applied_filters.pop()  # remove last filter
    filtered_df = filter_df(df, applied_filters)

if not filtered_df.empty:
    st.success(f"Showing {len(filtered_df)} records with filters applied:")
    for col, val in applied_filters:
        if val != "All":
            st.write(f"- {col}: {val}")
    if len(applied_filters) < len(filters):
        st.info("Some filters were removed to show data because the selected combination had no records.")
else:
    st.error("No data available, even after removing all filters.")

st.dataframe(filtered_df.head(50), height=700)

st.subheader("Analytics & Visualizations")

if not filtered_df.empty:
    # Orders by Gender
    gender_counts = filtered_df['gender'].value_counts().reset_index()
    gender_counts.columns = ['gender', 'count']
    fig1 = px.bar(gender_counts, x='gender', y='count', color='gender',
                  title="Orders by Gender",
                  color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig1, use_container_width=True)

    # Orders by Location
    location_counts = filtered_df['location'].value_counts().nlargest(10).reset_index()
    location_counts.columns = ['location', 'count']
    fig2 = px.bar(location_counts, x='count', y='location', orientation='h',
                  title="Top 10 Orders by Location",
                  color_discrete_sequence=px.colors.qualitative.Vivid)
    fig2.update_layout(yaxis={'autorange':'reversed'})
    st.plotly_chart(fig2, use_container_width=True)

    # Orders by Payment Method
    payment_counts = filtered_df['payment_method'].value_counts().reset_index()
    payment_counts.columns = ['payment_method', 'count']
    fig3 = px.pie(payment_counts, names='payment_method', values='count',
                  title="Orders by Payment Method",
                  color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig3, use_container_width=True)

    # Orders by Order Type
    order_type_counts = filtered_df['order_type'].value_counts().reset_index()
    order_type_counts.columns = ['order_type', 'count']
    fig4 = px.bar(order_type_counts, x='order_type', y='count',
                  title="Orders by Order Type",
                  color_discrete_sequence=px.colors.qualitative.Safe)
    st.plotly_chart(fig4, use_container_width=True)

    # Orders by Hour
    hour_counts = filtered_df['hour'].value_counts().reset_index()
    hour_counts.columns = ['hour', 'count']
    hour_counts = hour_counts.sort_values(by='hour')
    fig5 = px.bar(hour_counts, x='hour', y='count',
                  title="Orders by Hour",
                  color_discrete_sequence=px.colors.sequential.Viridis)
    st.plotly_chart(fig5, use_container_width=True)
else:
    st.warning("No data to show graphs.")
