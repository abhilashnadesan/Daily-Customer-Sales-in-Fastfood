#!/bin/bash

# Activate conda base environment
source /opt/anaconda3/bin/activate base

# Navigate to your project directory
cd "/Users/jenniferabhilash/Desktop/EUBS/Third Semester/daily fastfood project"

# Run ETL and analysis using conda's Python
python etl_analysis.py

# Send email alert using conda's Python
python email_notifier.py "Pipeline completed" "ETL finished at $(date)"
