import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("data/raw/cleaned_supermarket_sales.csv")

# Total sales by branch
sales = df.groupby("Branch")["Total"].sum().reset_index()

# Create interactive bar chart
fig = px.bar(
    sales,
    x="Branch",
    y="Total",
    title="Interactive Total Sales by Branch",
    color="Branch",
    text="Total"
)

fig.show()