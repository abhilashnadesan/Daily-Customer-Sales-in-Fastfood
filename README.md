# daily-customer-sales-in-fast-food-outlets  Analysis

This project explores and analyzes customer orders from a fast-food outlet. It includes data cleaning, visual insights, a live interactive dashboard, machine learning prediction, and pipeline automation — all wrapped into one deployable solution using Docker and Airflow
 

## Data Pipeline Architecture

![Workflow Diagram](https://github.com/abhilashnadesan/Daily-Customer-Sales-in-Fastfood/blob/main/Sales%20Fast%20food.png?raw=true)



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
```python
cd "/Users/jenniferabhilash/Desktop/EUBS/Third Semester/daily fastfood project"
```

## Section 1: Load the Raw Data

Copy
Edit
import pandas as pd

file_path = "data/raw/sales_data.csv"
df = pd.read_csv(file_path)


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
Key Insights from Sales Dashboard:
## Top Locations
San Francisco has the highest order volume, followed by Indianapolis and Buffalo.
Action Point: Focus marketing efforts on top-performing cities.

## Order Type Preference
Online orders (≈80) significantly outnumber in-person orders (≈60).
Opportunity: Enhance digital ordering experience to drive more sales.

## Gender Distribution
Female customers place more orders (≈60) than male customers (≈40).
Suggestion: Tailor promotions to female demographics.

## Payment Methods
Credit Card is most common, followed by Cash and Debit Card.
Insight: Customers prefer digital payments; consider cashless initiatives.

## Peak Order Hours
Orders spike .
Recommendation: Schedule promotions around mealtime peaks.

## Popular Food Items
Burgers and Pizza are top sellers across locations.
Opportunity: Bundle popular items for combo deals.
All graphs automatically adjust based on selected filters in the app.

## Target Top Cities - Based on th below Visualization

Data: San Francisco, Indianapolis, Buffalo are top order locations.

Benefit: Focus ads/discounts in these cities to attract more customers.

## Push Online Orders

Data: 57% of orders are online (vs. 43% in-person).

Benefit: Improve your app/website — faster ordering = more sales!

## Win Male Customers

Data: 60% Male and 50 % Female of orders are from women.

Benefit: Create promotions (e.g., "Meal Deals") tailored to Men — boost loyalty.

## win Debit Card

Debit  Card users (36.7%) spend 12-18% more on average than cash users — focus on card promotions to increase order value
.

## Staff & Food Planning

 Burgers/pizza sell best.

Benefit:

Schedule extra staff during busy hours.

Stock more burgers/pizza — reduce waste, sell more!


# Here is the sample Plans - Summary

Push ads in top cities
(San Francisco, Indianapolis, Buffalo)

Make online ordering faster
(Most sales come from apps/websites)

Offer discounts for card payments
(Debit/credit users spend more)

Bundle burgers/pizza + add staff at busy hours
(Peak times: mornings, lunch, dinner)



<img width="936" alt="Screenshot 2025-06-10 at 1 17 30 PM" src="https://github.com/user-attachments/assets/a261e1de-ccf7-41ae-b5db-edcdc83b9648" />

<img width="1073" alt="Screenshot 2025-06-10 at 1 17 37 PM" src="https://github.com/user-attachments/assets/3dbd41c2-260e-4e5c-a53d-2cdd0b062808" />


<img width="1057" alt="Screenshot 2025-06-10 at 1 17 33 PM" src="https://github.com/user-attachments/assets/644b9066-d135-48b8-86c5-e099f0cff2be" />

<img width="1001" alt="Screenshot 2025-06-10 at 1 17 26 PM" src="https://github.com/user-attachments/assets/a102099e-25c3-487d-b3a9-4d55cb938cc1" />

<img width="1055" alt="Screenshot 2025-06-10 at 1 17 39 PM" src="https://github.com/user-attachments/assets/998cc1eb-0170-4102-b388-69f7e05ff304" />

<img width="1289" alt="Screenshot 2025-06-10 at 1 35 32 PM" src="https://github.com/user-attachments/assets/dd2349e3-83ae-4cf0-8d95-70e9c0fd081e" />


```python
"This data shows where to advertise (top cities), how to sell (online + card payments), and who to target (women). Use it to:

Run ads in San Francisco/Indianapolis.

Make  app faster.

Launch a ‘Male Burger Night’ promo.

Add Apple Pay.

Schedule extra cooks during dinner rush!"

```

## Section 5: Streamlit Interactive Web App
You can launch the full interactive dashboard with:

bash
Copy
Edit
```bash
python3 mock_api.py
````
```python
streamlit run app.py
```
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

 The app ensures that you always see data and graphs, even if your selected filter combination has no direct matches.

## Section 6: Automation + Email Alerts
The project includes automation and notifications.

 Manual Pipeline Run:
bash
Copy
Edit
```python
bash run_pipeline.sh
```
```python
airflow standalone
```
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

 Cron Job Setup (Every Hour):
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

## Details for Email Alerts

In a fast-food business, it's important to have the latest data to make good decisions, like how much food to prepare or how many staff to schedule. Our ETL pipeline runs every hour to clean and update sales data. But if something goes wrong and no one knows, the business might use old or wrong data. To fix this, we added email alerts. When the pipeline finishes, it sends an email saying "ETL done" or "ETL failed." For example, if the pipeline runs at 2 PM and fails, the manager gets an email right away and can ask the team to fix it. This helps keep everything running smoothly.

## Section 7: Airflow UI and DAG (Pipeline Scheduler)
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

## Section 8: Machine Learning Model
We trained a Random Forest Classifier to predict whether an order will be Online or In-Person based on:

Gender

Hour of the day

 Output Example:
bash
Copy
Edit

To run the model, use the following command:
```bash
python ml_model.py
```
yaml
Copy
Edit
# Order Type Prediction Model

## Model Summary
We built a machine learning model to predict if an order is **Online (0)** or **In-Person (1)**.

## Best Settings
- Number of trees: 100  
- Minimum samples to split a node: 10  
- Minimum samples per leaf: 1  
- No limit on tree depth

## Results
- **Accuracy:** 75% (the model correctly predicted 3 out of 4 orders)  
- Predictions:
  - 1 Online order correctly predicted  
  - 2 In-Person orders correctly predicted  
  - 1 In-Person order was incorrectly predicted as Online

 ## Simple Example

| Order | Actual       | Predicted    | Correct/Wrong |
|-------|--------------|--------------|---------------|
| 1     | In-Person (1)| In-Person (1)| Correct       |
| 2     | Online (0)   | Online (0)   | Correct       |
| 3     | In-Person (1)| Online (0)   | Wrong         |
| 4     | Online (0)   | In-Person(1) | Wrong         |

The model achieved 75% accuracy, which is a good start for this demo.

---


## Section 9: Docker Container
To run the full pipeline with no environment setup:

bash
Copy
Edit
```python
docker build -t fastfood-pipeline -f Dockerfile .
docker run -it --rm fastfood-pipeline
```
Docker ensures consistency across any machine and deployment.


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
 



