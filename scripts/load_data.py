import pandas as pd

# Load the dataset
df = pd.read_csv("data/raw/supermarket_sales.csv")

# Display the first 5 rows
print("First 5 Rows of the Dataset:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Display the shape of the dataset
print("\nDataset Shape:")
print(df.shape)
