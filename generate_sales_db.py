import sqlite3
import pandas as pd
import numpy as np
from faker import Faker
import random
import os

# Initialize Faker for random city names and times
fake = Faker()

# Set seed for reproducibility
random.seed(42)
np.random.seed(42)

# Define data options
genders = ['Men', 'Women', 'Kids']
order_types = ['Online', 'In-Person']
payment_methods = ['Credit Card', 'Debit Card', 'Cash']
locations = ['Austin', 'New York', 'Los Angeles', 'Chicago', 'Houston']
hours = list(range(8, 22))  # business hours from 8 AM to 9 PM

# Number of records to generate
num_records = 1000

data = []
for _ in range(num_records):
    gender = random.choice(genders)
    order_type = random.choice(order_types)
    payment_method = random.choice(payment_methods)
    location = random.choice(locations)
    hour = random.choice(hours)
    # Generate dummy profit: higher profit for online and credit card
    base_profit = np.random.uniform(5, 50)
    profit = base_profit * (1.2 if order_type == 'Online' else 1.0)
    profit *= (1.1 if payment_method == 'Credit Card' else 1.0)
    profit = round(profit, 2)

    data.append({
        'gender': gender,
        'order_type': order_type,
        'payment_method': payment_method,
        'location': location,
        'hour': hour,
        'profit': profit
    })

# Create DataFrame
df = pd.DataFrame(data)

# Create folder if not exists
os.makedirs('db', exist_ok=True)

# Connect to SQLite DB
conn = sqlite3.connect('db/sales_data.db')

# Save to SQL table named 'sales'
df.to_sql('sales', conn, if_exists='replace', index=False)

conn.close()

print("Sample sales_data.db created with 1000 records.")
