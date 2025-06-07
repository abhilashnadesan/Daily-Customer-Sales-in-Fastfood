# daily-customer-sales-in-fast-food-outlets  Analysis

This project explores and analyzes customer orders from a fast-food outlet. It includes data cleaning, visual insights, a live interactive dashboard, machine learning prediction, and pipeline automation — all wrapped into one deployable solution using Docker and Airflow
 

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


# Step-by-Step Guide
Daily Customer Sales in Fast Food Outlets
This project explores and analyzes customer orders from a fast-food outlet. It includes data cleaning, visual insights, a live interactive dashboard, machine learning prediction, and pipeline automation — all wrapped into one deployable solution using Docker and Airflow.

 Dataset Source
 Kaggle Dataset: Daily Customer Sales in Fast Food
 
 ## Project Directory
bash
Copy
Edit
cd "/Users/jenniferabhilash/Desktop/EUBS/Third Semester/daily fastfood project"
## Section 1: Load the Raw Data
```python
Copy
Edit
import pandas as pd

file_path = "data/raw/sales_data.csv"
df = pd.read_csv(file_path)
```

print("Shape of data:", df.shape)
print(df.head())
This loads the original customer sales dataset.

## Section 2: Data Cleaning and Feature Engineering
To prepare the dataset for analysis and visualizations, we cleaned and transformed it:

Cleaning Performed:
Removed unnecessary columns like unnamed:_5, unnamed:_6

Dropped rows with missing/null values

Standardized all column names to lowercase and replaced spaces with underscores

Renamed ordereditem → item

 New Features Added:
hour: Converted time-of-day strings (Morning, Afternoon…) to numerical hours (9, 14, 18, 21)

day_of_week: Added using a fixed date to extract weekday names

sale: A value of 1 for each row to help count orders

gender: Transformed numeric codes to readable labels (0 → Female, 1 → Male)

All of this cleaned data is saved to:

bash
Copy
Edit
sales_cleaned.csv
## Section 3: Store Cleaned Data into SQLite
python
Copy
Edit
import sqlite3

conn = sqlite3.connect("db/sales_data.db")
df.to_sql("fastfood_sales", conn, if_exists="replace", index=False)
conn.close()
 This allows us to reuse the cleaned dataset for fast queries and consistent app behavior.

## Section 4: Visual Analysis with Plotly (in Streamlit)
Instead of static plots, we now use interactive Plotly charts in our dashboard (app.py):

 Key Insights:
Orders by gender, time of day, and location

Top food items

Payment method preferences

In-person vs online ordering

Order patterns by hour of day

All graphs automatically adjust based on selected filters in the app.

## Section 5: Streamlit Interactive Web App
You can launch the full interactive dashboard with:

bash
Copy
Edit
streamlit run app.py
 Key Features:
Sidebar filters for:

Gender

Order Type

Location

Payment Method

Food Item

Plots update based on filters

If a combination returns no data, the app intelligently removes one filter at a time until it finds data

View the filtered table and related graphs directly

💡 The app ensures that you always see data and graphs, even if your selected filter combination has no direct matches.

## Section 6: Automation + Email Alerts
The project includes automation and notifications.

 Manual Pipeline Run:
bash
Copy
Edit
bash run_pipeline.sh
This script runs:

ETL processing

Email notification after completion

 Email Notification:
bash
Copy
Edit
python3 email_notifier.py "Pipeline Completed" "ETL job done at $(date)"
You’ll receive an email like:

 Subject: Pipeline Completed
 Message: ETL job done at 3:00 PM

⏱ Cron Job Setup (Every Hour):
bash
Copy
Edit
crontab -e
Add this line:

bash
Copy
Edit
0 * * * * /path/to/run_pipeline.sh >> /path/to/logs/pipeline.log 2>&1
This runs the pipeline every hour automatically and sends an alert based on success or failure.

## Section 7: Machine Learning Model
We trained a Random Forest Classifier to predict whether an order will be Online or In-Person based on:

Gender

Hour of the day

🧪 Output Example:
bash
Copy
Edit
python ml_model.py
yaml
Copy
Edit
Best hyperparameters: {'max_depth': None, 'min_samples_leaf': 1, 'min_samples_split': 10, 'n_estimators': 100}
Model Accuracy: 0.75

Confusion Matrix:
[[1 0]
 [1 2]]

Classification Report:
              precision    recall  f1-score   support
      Online       0.50      1.00      0.67         1
   In-Person       1.00      0.67      0.80         3

Predictions: [1 0 1 0]
Actual:      [1 1 1 0]
🤖 Simple Explanation:
If a man orders at 6 PM, the model might predict: “In-Person”

If a woman orders at 10 AM, it might predict: “Online”

This can help managers prepare inventory and staff ahead of time based on customer behavior.

## Section 8: Docker Container
To run the full pipeline with no environment setup:

bash
Copy
Edit
docker build -t fastfood-pipeline -f Dockerfile .
docker run -it --rm fastfood-pipeline
Docker ensures consistency across any machine and deployment.

## Section 9: Airflow UI and DAG (Pipeline Scheduler)
Launch Airflow to manage and monitor the pipeline:

bash
Copy
Edit
airflow webserver --port 8080
Open your browser: http://localhost:8080

Default Login:

Username: admin

Password: admin

Then run:

bash
Copy
Edit
airflow scheduler
The fastfood_sales DAG will appear. Toggle it ON to start scheduled runs.

## Section 10: Deployment to GitHub
All code is pushed to GitHub

Includes: data files, Streamlit dashboard, visuals, ETL scripts, ML model, and documentation

 GitHub Repo

  ## Summary: What We Learned & Business Insight
This project helps fast food businesses:

Understand what sells the most and when

See how gender, location, and payment method affect orders

Predict order type to prepare staffing and inventory

Use email alerts and Airflow to track pipeline status

Deploy across any system using Docker

Always deliver filtered, clean data in the dashboard, even with complex user filters

It turns raw sales data into something useful for decision-making — helping the business boost profitability, streamline operations, and better understand customer behavior.
 



