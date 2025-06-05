# Daily Fastfood Sales Analysis

“The project uses fast food sales data to analyze customer behavior by time of day, gender, and item popularity. It helps a fast food chain understand peak sales hours, best-selling items, and preferred order types for each demographic segment.”

 

## Data Pipeline Architecture
![Data Pipeline Diagram](data_pipeline_architecture.png)

**Key Layers:**
1. **Data Source**: CSV files from Kaggle
2. **Processing**: Pandas ETL
3. **Storage**: SQLite (sales_data.db)
4. **Automation**: Cron/Airflow (with email alerts)
5. **Visualization**: Matplotlib/Seaborn
6. **Containerization**: Docker
7. **Deployment**: GitHub Pages/Streamlit
8. **Machine Learning Model:** A simple classification model built with Python (Random Forest).

## Email Alerts Setup

To enable email notifications for ETL pipeline success/failure, configure your environment variables in the `.env` file located in the project root:

EMAIL_SERVER=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=abhilashnadesan66@gmail.com
EMAIL_PASS=xxxxxxxxxx
EMAIL_TO=abhilashnadesan66@gmail.com

**Note:** Use an App Password for `EMAIL_PASS` if using Gmail with 2FA enabled.


## Step-by-Step Guide

###  Step 1: Data Collection

We start by placing your **raw sales CSV file** inside the `/data/raw/` folder.  
This file should include info like order ID, item name, order time, gender, and order type.

Example in Python:
```python
import pandas as pd
df = pd.read_csv("data/raw/sales_data.csv")

 Step 2: Data Cleaning and Preparation
Before we use the data, we clean it:

Remove columns we don’t need
Fix column names (e.g., lowercase, no spaces)
Drop rows with missing data
Add helpful new columns:
hour: time of the order (e.g., 15 for 3 PM)
day_of_week: Monday, Tuesday, etc.
date: just the date (no time)
The cleaned data is saved in /data/processed/.

🗄️ Step 3: Data Storage in Database

We store the clean data in a SQLite database. This makes it easier and faster to work with later.

Example:

import sqlite3
conn = sqlite3.connect("db/sales_data.db")
df.to_sql("fastfood_sales", conn, if_exists="replace", index=False)
conn.close()
The database file is saved in the /db/ folder.

⚙️ Step 4: Workflow Automation

No need to run everything by hand! We automate the whole pipeline using:

A shell script: run_pipeline.sh
A cron job to run daily/hourly (you can set this on your machine)
(Optional) Use Apache Airflow for better scheduling and UI
Email alerts notify you when the job succeeds or fails

📊 Step 5: Data Analysis and Visualization

Now the fun part — we create 4 visuals that show key insights:

🕒 Sales by time of day
👩‍🍳 Order types by gender
🍔 Top 10 best-selling items
📅 Sales trends by day
All charts are saved inside /visuals/ and are also viewable on the dashboard.

🤖 Step 6: Machine Learning (Bonus)

We add a machine learning model to predict how a customer placed the order.

Model: Random Forest Classifier
Features used: Gender, Time of order, etc.
It predicts: Online vs In-Person order
A fake (synthetic) dataset is used for training/testing
You get an accuracy score to see how well it works

🌐 Step 7: Streamlit Dashboard

We’ve built a simple dashboard with Streamlit so you can explore:

The 4 charts
A summary of sales data
The machine learning prediction and accuracy
To run the dashboard:

streamlit run app.py
This will open in your browser.

🐳 Step 8: Docker Containerization (Optional)

Don’t want to install Python and libraries? No problem.

Use Docker to run everything inside a container:

docker build -t fastfood-pipeline .
docker run -it --rm fastfood-pipeline
Works the same on any computer!

📦 Project Structure

Here’s what each folder or file is used for:

Path / File	Description
data/raw/	Put your original sales CSV here
data/processed/	Cleaned data is saved here
db/	Contains the SQLite database
visuals/	Stores the 4 charts made from the data
scripts/	All the Python code: ETL, visuals, email, ML
run_pipeline.sh	Script to run the full process
Dockerfile	Builds a Docker container
app.py	The Streamlit dashboard code
✅ Quick Start Instructions

Put your CSV file in data/raw/
Run everything with:
bash run_pipeline.sh
Check your 4 visuals in visuals/
Start the dashboard:
streamlit run app.py
Set up a cron job or use Docker if you prefer automation
Watch for email alerts when the job runs
📧 Stay in Touch

Made by: Abhilash Nadesan
Email: abhilash.nadesan@euruni.edu

Note: Even though the project could use public APIs, I decided to work with an open CSV dataset instead. This made it easier to build a full ETL pipeline, connect to a database, add machine learning predictions, and set everything up with Docker—all on my local machine. If needed, I could later switch to using an API with authentication using a .env file."

