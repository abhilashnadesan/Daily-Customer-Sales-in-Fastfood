import sqlite3

# Connect to the SQLite database file (make sure the path is correct)
conn = sqlite3.connect('db/sales_data.db')

# Create a cursor object
cursor = conn.cursor()

# Get the column information from the 'sales' table
cursor.execute("PRAGMA table_info(sales);")

# Fetch all column info
columns = cursor.fetchall()

# Extract and print column names
print("Columns in sales table:", [col[1] for col in columns])

# Close the connection
conn.close()
