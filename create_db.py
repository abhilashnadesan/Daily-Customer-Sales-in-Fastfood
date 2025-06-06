import sqlite3

conn = sqlite3.connect('db/sales_data.db')
cursor = conn.cursor()

# Create sales table with renamed column 'order_time'
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    item TEXT,
    quantity INTEGER,
    price REAL,
    order_time TEXT
)
''')

conn.commit()
conn.close()
