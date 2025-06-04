import pandas as pd
import os

# Bigger sample data for better training
data = {
    'gender': [0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1],
    'hour':   [9, 14, 11, 19, 20, 8, 17, 12, 21, 13, 18, 10, 16, 22, 7],
    'order_type': [
        'Online', 'In-Person', 'Online', 'In-Person', 'Online',
        'Online', 'In-Person', 'In-Person', 'Online', 'In-Person',
        'Online', 'Online', 'In-Person', 'Online', 'In-Person'
    ]
}

df = pd.DataFrame(data)

# Create folders if not exist
os.makedirs('data/processed', exist_ok=True)

# Save the CSV file
df.to_csv('data/processed/sales_cleaned.csv', index=False)

print("Sample sales_cleaned.csv created at data/processed/")

