import sqlite3

conn = sqlite3.connect('db/sales_data.db')
cursor = conn.cursor()

# Insert example sales data
cursor.execute('''
INSERT INTO sales (item, quantity, price, order_time)
VALUES (?, ?, ?, ?)
''', ("Burger", 2, 5.99, "Lunch"))

cursor.execute('''
INSERT INTO sales (item, quantity, price, order_time)
VALUES (?, ?, ?, ?)
''', ("Fries", 1, 2.49, "Dinner"))

conn.commit()
conn.close()

print("Sample data inserted successfully!")
