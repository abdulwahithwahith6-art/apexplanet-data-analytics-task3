import pandas as pd

# Load dataset
data = pd.read_csv("data/raw/supermarket_sales.csv")

print("Missing Values:")
print(data.isnull().sum())

# Remove duplicate rows
data = data.drop_duplicates()

# Save cleaned dataset
data.to_csv("data/raw/cleaned_supermarket_sales.csv", index=False)

print("\nData cleaned successfully!")
print("Cleaned dataset saved as cleaned_supermarket_sales.csv")