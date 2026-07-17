import sqlite3
import pandas as pd

# Connect to SQLite database (creates supermarket.db)
conn = sqlite3.connect("supermarket.db")

# Read cleaned CSV
df = pd.read_csv("data/raw/cleaned_supermarket_sales.csv")

# Save data into SQLite table
df.to_sql("sales", conn, if_exists="replace", index=False)

print("✅ Database created successfully!")
print("✅ Table 'sales' created successfully!")

conn.close()