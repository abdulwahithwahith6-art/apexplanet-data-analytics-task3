# ApexPlanet Data Analytics Project

## Project Overview

This project performs data cleaning, exploratory data analysis, SQL analysis,
visualization, dashboard creation, and automation using a supermarket sales
dataset.

The project was completed as part of the ApexPlanet Data Analytics Internship.

## Dataset

The dataset contains supermarket sales transaction information.

### Dataset Details

- Records: 10
- Columns: 13
- Missing values: 0
- Duplicate rows: 0

### Main Columns

- Invoice_ID
- Date
- Branch
- City
- Customer_Type
- Gender
- Product_Line
- Unit_Price
- Quantity
- Tax_5%
- Total
- Payment
- Rating

## Tasks Completed

### Task 1 - Data Preparation and Exploratory Data Analysis

The raw supermarket sales dataset was cleaned and analyzed.

Activities included:

- Loading the CSV dataset
- Checking data types
- Checking missing values
- Removing duplicate records
- Generating descriptive statistics
- Exploring sales and customer information

### Task 2 - SQL Analysis

SQL queries were used to analyze the supermarket sales database.

The SQL analysis includes:

- Sales analysis
- Customer analysis
- Product analysis
- Aggregation queries
- Grouping and filtering
- Database-based analysis

### Task 3 - Power BI Dashboard

A Power BI dashboard was created using the cleaned supermarket sales data.

The dashboard includes KPI cards such as:

- Total Sales
- Total Orders
- Average Rating

The Power BI project file is:

`Task3_PowerBI_Dashboard.pbix`

### Task 4 - Tableau Dashboard

An interactive Tableau dashboard was created to visualize supermarket sales.

The dashboard includes:

- Total Sales
- Total Orders
- Average Rating
- Sales by City
- Branch-level sales analysis

The Tableau project file is:

`Task4_Tableau_Dashboard.twbx`

### Task 5 - Automation Pipeline

An automated Python pipeline was created to simplify the complete analysis workflow.

The pipeline:

1. Loads the raw dataset
2. Checks missing values
3. Checks duplicate records
4. Removes duplicate records
5. Converts the Date column
6. Saves the processed dataset
7. Generates summary statistics
8. Calculates sales by branch
9. Calculates sales by city
10. Saves analysis results as CSV files

The automation script is:

`scripts/automation_pipeline.py`

## Automation Results

The automated pipeline produced the following results:

- Total Records: 10
- Total Columns: 13
- Total Sales: 10,500
- Average Sales: 1,050
- Average Quantity: 3
- Average Rating: 8.7
- Minimum Sales: 525
- Maximum Sales: 1,680
- Missing Values: 0
- Duplicate Rows Removed: 0

### Sales by Branch

| Branch | Sales |
|---|---:|
| A | 3832.5 |
| C | 3727.5 |
| B | 2940.0 |

### Sales by City

| City | Sales |
|---|---:|
| Coimbatore | 3832.5 |
| Bangalore | 3727.5 |
| Chennai | 2940.0 |

## Project Structure

```text
apexplanet-data-analytics/
│
├── data/
│   ├── raw/
│   │   ├── supermarket_sales.csv
│   │   └── cleaned_supermarket_sales.csv
│   │
│   └── processed/
│       └── cleaned_supermarket_sales.csv
│
├── reports/
│   ├── summary_statistics.csv
│   ├── sales_by_branch.csv
│   └── sales_by_city.csv
│
├── scripts/
│   ├── data_cleaning.py
│   ├── eda.py
│   ├── visualization.py
│   ├── task2_sql.ipynb
│   └── automation_pipeline.py
│
├── Task3_PowerBI_Dashboard.pbix
├── Task4_Tableau_Dashboard.twbx
├── requirements.txt
└── README.md