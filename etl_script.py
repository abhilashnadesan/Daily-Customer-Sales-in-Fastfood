import pandas as pd

chunk_size = 1000
results = []

for chunk in pd.read_csv('data/raw/sales_data.csv', chunksize=chunk_size):
    # Just keep chunk as-is for now
    results.append(chunk)

data = pd.concat(results)

print(data.head())  # Show first few rows to confirm it worked

