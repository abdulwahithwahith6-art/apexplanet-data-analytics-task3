import pandas as pd
from pathlib import Path

# ============================================================
# TASK 5 - AUTOMATED DATA ANALYTICS PIPELINE
# ============================================================

# Project folders
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_FILE = BASE_DIR / "data" / "raw" / "supermarket_sales.csv"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
REPORTS_DIR = BASE_DIR / "reports"

# Create required folders automatically
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

print("=" * 60)
print("TASK 5 - AUTOMATED DATA ANALYTICS PIPELINE")
print("=" * 60)

# ------------------------------------------------------------
# 1. LOAD DATA
# ------------------------------------------------------------
print("\n[1/6] Loading dataset...")

data = pd.read_csv(RAW_FILE)

print(f"Dataset loaded successfully.")
print(f"Rows    : {data.shape[0]}")
print(f"Columns : {data.shape[1]}")

# ------------------------------------------------------------
# 2. DATA CLEANING
# ------------------------------------------------------------
print("\n[2/6] Cleaning data...")

missing_before = data.isnull().sum().sum()
duplicates_before = data.duplicated().sum()

print(f"Missing values before cleaning : {missing_before}")
print(f"Duplicate rows before cleaning: {duplicates_before}")

# Remove duplicates
data = data.drop_duplicates()

# Convert Date column if available
if "Date" in data.columns:
    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")

missing_after = data.isnull().sum().sum()

print(f"Missing values after cleaning  : {missing_after}")
print(f"Rows after cleaning            : {len(data)}")

# Save processed dataset
cleaned_file = PROCESSED_DIR / "cleaned_supermarket_sales.csv"
data.to_csv(cleaned_file, index=False)

print(f"Cleaned dataset saved to:")
print(cleaned_file)

# ------------------------------------------------------------
# 3. SUMMARY STATISTICS
# ------------------------------------------------------------
print("\n[3/6] Generating summary statistics...")

summary = pd.DataFrame({
    "Metric": [
        "Total Records",
        "Total Columns",
        "Total Sales",
        "Average Sales",
        "Average Quantity",
        "Average Rating",
        "Minimum Sales",
        "Maximum Sales",
        "Missing Values",
        "Duplicate Rows Removed"
    ],
    "Value": [
        len(data),
        len(data.columns),
        data["Total"].sum(),
        data["Total"].mean(),
        data["Quantity"].mean(),
        data["Rating"].mean(),
        data["Total"].min(),
        data["Total"].max(),
        missing_after,
        duplicates_before
    ]
})

summary_file = REPORTS_DIR / "summary_statistics.csv"
summary.to_csv(summary_file, index=False)

print(summary.to_string(index=False))

# ------------------------------------------------------------
# 4. SALES BY BRANCH
# ------------------------------------------------------------
print("\n[4/6] Calculating sales by branch...")

branch_sales = (
    data.groupby("Branch", as_index=False)["Total"]
    .sum()
    .sort_values("Total", ascending=False)
)

branch_file = REPORTS_DIR / "sales_by_branch.csv"
branch_sales.to_csv(branch_file, index=False)

print(branch_sales.to_string(index=False))

# ------------------------------------------------------------
# 5. SALES BY CITY
# ------------------------------------------------------------
print("\n[5/6] Calculating sales by city...")

city_sales = (
    data.groupby("City", as_index=False)["Total"]
    .sum()
    .sort_values("Total", ascending=False)
)

city_file = REPORTS_DIR / "sales_by_city.csv"
city_sales.to_csv(city_file, index=False)

print(city_sales.to_string(index=False))

# ------------------------------------------------------------
# 6. FINAL STATUS
# ------------------------------------------------------------
print("\n[6/6] Pipeline completed successfully!")

print("\nGenerated files:")
print(f"1. {cleaned_file}")
print(f"2. {summary_file}")
print(f"3. {branch_file}")
print(f"4. {city_file}")

print("\n" + "=" * 60)
print("AUTOMATION PIPELINE COMPLETED")
print("=" * 60)