import os
import pandas as pd
import sqlite3

csv_path = 'data/processed/sales_cleaned.csv'

df_csv = pd.read_csv(csv_path)

os.makedirs('db', exist_ok=True)  # Create folder if needed

conn = sqlite3.connect('db/sales_data.db')

df_csv.to_sql('sales', conn, if_exists='replace', index=False)

print(f"Loaded {len(df_csv)} rows into SQLite database.")

conn.close()
