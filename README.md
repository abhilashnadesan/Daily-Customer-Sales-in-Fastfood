# Daily Fastfood Sales Analysis

A data pipeline to analyze daily fast-food customer sales, generate insights, and visualize trends using Python, SQLite, and Jupyter.

## How to Run
1. Clone the repo  
2. Install dependencies: `pip install -r requirements.txt`  
3. Start Jupyter: `jupyter notebook`  
4. Open `notebooks/etl_analysis.ipynb`  

## Visualizations
- Total sales by outlet  
- Sales by day and hour  
- Top 10 ordered items  
- Order type distribution by gender  

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

## Email Alerts Setup

To enable email notifications for ETL pipeline success/failure, configure your environment variables in the `.env` file located in the project root:

EMAIL_SERVER=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=abhilashnadesan66@gmail.com
EMAIL_PASS=uhffsuavjrzycgpa
EMAIL_TO=abhilashnadesan66@gmail.com,another@example.com

**Note:** Use an App Password for `EMAIL_PASS` if using Gmail with 2FA enabled.

### Testing Email Notifications

You can test sending an email alert by running the following command in your project directory:

```bash
python3 email_notifier.py "Test Alert" "This is a test email from the fastfood ETL pipeline."


Core Objective
A data pipeline that transforms raw fast-food sales data into actionable insights, revealing:

Peak sales periods (Best/worst times for staffing)

Top-selling items (Menu optimization)

Customer behavior (Gender-based preferences, order patterns)

Technical Stack
Languages: Python (77.4%), JavaScript (19.9%)

Data Tools:

ETL: Pandas (cleaning), SQLite (storage)

Automation: Cron/Airflow (scheduled jobs + email alerts)

Visualization: Matplotlib/Seaborn (static charts), Plotly (interactive dashboards)

Infrastructure:

Containerization: Docker (consistent environments)

Deployment: Streamlit (web apps), GitHub Pages (documentation)

Key Features
Automated Pipeline:

Scheduled data pulls → Cleaning → Database updates → Email alerts for failures.

Dynamic Visuals:

Hourly sales heatmaps, item popularity trends, demographic breakdowns.

Scalable Design:

Dockerized for easy replication; Jupyter notebooks for iterative analysis.

Business Impact
Reduce Waste: Predict ingredient needs using sales patterns.

Boost Revenue: Highlight underperforming items for promotions.

Staff Optimization: Align shifts with peak order volumes.

Example Insight:
"The 7–9 AM coffee surge (32% of morning sales) suggests adding breakfast combos to increase average order value."




