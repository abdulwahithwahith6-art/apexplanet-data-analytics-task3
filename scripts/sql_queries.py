import sqlite3

conn = sqlite3.connect("supermarket.db")
cursor = conn.cursor()

cursor.execute("""
SELECT Branch, COUNT(*)
FROM sales
GROUP BY Branch
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()