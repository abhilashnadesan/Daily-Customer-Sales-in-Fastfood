import streamlit as st
from PIL import Image
import os

st.title("Daily Fastfood Project Dashboard")

# Get the folder where this script is running
BASE_DIR = os.path.dirname(__file__)

# Folder containing the plots (relative path)
image_folder = BASE_DIR  # since images are in the same folder as dashboard_app.py

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
   st.image(your_image, use_container_width=True)


