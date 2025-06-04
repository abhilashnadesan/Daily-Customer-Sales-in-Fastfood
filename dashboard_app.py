# dashboard_app.py

import streamlit as st
from PIL import Image
import os

st.title("Daily Fastfood Project Dashboard")

# Folder containing the plots
image_folder = "/Users/jenniferabhilash/Desktop/EUBS/Third Semester/daily fastfood project/plots"

# List of image files
image_files = [
    "top_10_items.png",
    "items_by_time_of_day.png",
    "order_type_by_gender.png",
    "sales_by_time_of_day.png"
]

# Display each image
for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    st.subheader(image_file.replace("_", " ").replace(".png", "").title())
    img = Image.open(image_path)
    st.image(img, use_column_width=True)
