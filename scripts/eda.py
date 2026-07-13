import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
data = pd.read_csv("data/raw/supermarket_sales.csv")

# Display dataset information
print("========== FIRST 5 ROWS ==========")
print(data.head())

print("\n========== DATASET SHAPE ==========")
print(data.shape)

print("\n========== COLUMN NAMES ==========")
print(data.columns)

print("\n========== DATA TYPES ==========")
print(data.dtypes)

print("\n========== MISSING VALUES ==========")
print(data.isnull().sum())

print("\n========== STATISTICAL SUMMARY ==========")
print(data.describe())
# Bar Chart - Quantity sold by Product Line

sales = data.groupby("Product_Line")["Quantity"].sum()

plt.figure(figsize=(10,5))
sales.plot(kind="bar")

plt.title("Quantity Sold by Product Line")
plt.xlabel("Product Line")
plt.ylabel("Quantity Sold")

plt.show()

# Histogram of Total Sales

plt.figure(figsize=(8,5))

plt.hist(data["Total"], bins=5)

plt.title("Distribution of Total Sales")
plt.xlabel("Total Sales")
plt.ylabel("Number of Bills")

plt.show()

# Pie Chart - Payment Method Distribution

payment = data["Payment"].value_counts()

plt.figure(figsize=(6,6))

plt.pie(payment, labels=payment.index, autopct="%1.1f%%", startangle=90)

plt.title("Payment Method Distribution")

plt.show()

# Box Plot - Total Sales

plt.figure(figsize=(8,5))

plt.boxplot(data["Total"])

plt.title("Box Plot of Total Sales")
plt.ylabel("Total Sales")

plt.show()

# Heatmap - Correlation between numerical columns

plt.figure(figsize=(8,6))

correlation = data.select_dtypes(include="number").corr()

sns.heatmap(correlation, annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap")

plt.show()