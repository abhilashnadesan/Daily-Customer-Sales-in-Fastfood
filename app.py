import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Sales Data Viewer", layout="wide")
st.title("Sales Data Viewer")

# Load data
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

# Apply filters
filtered_df = df.copy()
if selected_gender != "All":
    filtered_df = filtered_df[filtered_df['gender'] == selected_gender]
if selected_order_type != "All":
    filtered_df = filtered_df[filtered_df['order_type'] == selected_order_type]
if selected_location != "All":
    filtered_df = filtered_df[filtered_df['location'] == selected_location]
if selected_payment != "All":
    filtered_df = filtered_df[filtered_df['payment_method'] == selected_payment]
if selected_food != "All":
    filtered_df = filtered_df[filtered_df['food_item'] == selected_food]

st.write(f"### Showing {len(filtered_df)} records for filters:")
st.write(f"- Gender: {selected_gender}")
st.write(f"- Order Type: {selected_order_type}")
st.write(f"- Location: {selected_location}")
st.write(f"- Payment Method: {selected_payment}")
st.write(f"- Food Item: {selected_food}")

st.dataframe(filtered_df.head(50), height=700)

# --- Analytics graphs ---
st.subheader("Analytics & Visualizations")

if filtered_df.empty:
    st.warning("No data available for selected filters.")
else:
    # 1. Orders by Gender
    st.markdown("**Orders by Gender**")
    gender_counts = filtered_df['gender'].value_counts()
    fig1, ax1 = plt.subplots()
    gender_counts.plot(kind='bar', color='mediumslateblue', ax=ax1)
    ax1.set_ylabel("Number of Orders")
    ax1.set_xlabel("Gender")
    ax1.set_xticklabels(gender_counts.index, rotation=0)
    st.pyplot(fig1)

    # 2. Orders by Location
    st.markdown("**Orders by Location**")
    location_counts = filtered_df['location'].value_counts().nlargest(10)  # top 10
    fig2, ax2 = plt.subplots(figsize=(8,4))
    location_counts.plot(kind='barh', color='teal', ax=ax2)
    ax2.set_xlabel("Number of Orders")
    ax2.set_ylabel("Location")
    ax2.invert_yaxis()
    st.pyplot(fig2)

    # 3. Orders by Payment Method
    st.markdown("**Orders by Payment Method**")
    payment_counts = filtered_df['payment_method'].value_counts()
    fig3, ax3 = plt.subplots()
    payment_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"), ax=ax3)
    ax3.set_ylabel('')
    st.pyplot(fig3)

    # 4. Orders by Order Type
    st.markdown("**Orders by Order Type**")
    order_type_counts = filtered_df['order_type'].value_counts()
    fig4, ax4 = plt.subplots()
    order_type_counts.plot(kind='bar', color='coral', ax=ax4)
    ax4.set_ylabel("Number of Orders")
    ax4.set_xlabel("Order Type")
    st.pyplot(fig4)

    # 5. Orders by Hour (bar plot)
    st.markdown("**Orders by Hour**")
    hour_counts = filtered_df['hour'].value_counts().sort_index()
    fig5, ax5 = plt.subplots(figsize=(10,3))
    sns.barplot(x=hour_counts.index, y=hour_counts.values, palette="viridis", ax=ax5)
    ax5.set_xlabel("Hour of Day")
    ax5.set_ylabel("Number of Orders")
    st.pyplot(fig5)
