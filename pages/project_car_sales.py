import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title Section: Car Sales Analysis
st.title("Car Sales Analysis Dashboard")

# Load dataset
csv_url = 'https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/car_sales.csv'
df = pd.read_csv(csv_url)

# Convert 'User ID' to string to avoid serialization issues
df['User ID'] = df['User ID'].astype(str)

# Convert 'Date' column to datetime and format as 'MM-YY' for easier visualization
df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%m-%y')

# Sidebar Filter for Sales/Count toggle
toggle_option = st.sidebar.radio(
    "Toggle between Sales and Count",
    ('Sales', 'Count'),
    index=0  # Default to Sales
)

# Toggle logic
if toggle_option == 'Sales':
    metric = 'Price ($)'
    agg_func = 'sum'
    value_label = 'Sales ($)'
    number_format = "${:,.0f}k"  # Format in thousands
else:
    metric = 'Car_id'
    agg_func = 'count'
    value_label = 'Count'
    number_format = "{:,.0f}k"  # Format in thousands

# Function to format the value as thousands for better readability
def format_thousands(val):
    return f"{val/1000:.0f}k"

# 1. Sales by Region
st.subheader("Sales by Region")
region_sales = df.groupby('Dealer_Region').agg({metric: agg_func}).reset_index()
region_sales = region_sales.sort_values(by=metric, ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x='Dealer_Region', y=metric, data=region_sales)
plt.title(f"{value_label} by Region")
plt.ylabel(value_label)
plt.xlabel("Region")

# Add text on top of bars
for i, row in region_sales.iterrows():
    plt.text(i, row[metric], format_thousands(row[metric]), ha='center')

st.pyplot(plt)

# 2. Top 5 Car Models by Sales
st.subheader("Top 5 Car Models by Sales")
top_models = df.groupby('Model').agg({metric: agg_func}).reset_index().nlargest(5, metric)

plt.figure(figsize=(10, 6))
sns.barplot(x='Model', y=metric, data=top_models)
plt.title(f"Top 5 Car Models by {value_label}")
plt.ylabel(value_label)
plt.xlabel("Car Model")

# Add text on top of bars
for i, row in top_models.iterrows():
    plt.text(i, row[metric], format_thousands(row[metric]), ha='center')

plt.xticks(rotation=45, ha='right')  # Ensure text is readable
st.pyplot(plt)

# 3. Sales Over Time (Month-Year)
st.subheader(f"{value_label} Over Time")
sales_time = df.groupby('Date').agg({metric: agg_func}).reset_index()

plt.figure(figsize=(12, 6))
sns.barplot(x='Date', y=metric, data=sales_time)
plt.title(f"{value_label} Over Time (by Month-Year)")
plt.ylabel(value_label)
plt.xlabel("Month-Year")

# Add text on top of bars
for i, row in sales_time.iterrows():
    plt.text(i, row[metric], format_thousands(row[metric]), ha='center')

plt.xticks(rotation=45, ha='right')  # Ensure Month-Year is readable
st.pyplot(plt)

# 4. Top 5 Dealers by Revenue (or Count based on toggle)
st.subheader(f"Top 5 Dealers by {value_label}")
top_dealers = df.groupby('Dealer_Name').agg({metric: agg_func}).reset_index().nlargest(5, metric)

plt.figure(figsize=(10, 6))
sns.barplot(x='Dealer_Name', y=metric, data=top_dealers)
plt.title(f"Top 5 Dealers by {value_label}")
plt.ylabel(value_label)
plt.xlabel("Dealer Name")

# Add text on top of bars in $M format
for i, row in top_dealers.iterrows():
    plt.text(i, row[metric], format_thousands(row[metric]), ha='center')

plt.xticks(rotation=45, ha='right')  # Ensure text is readable
st.pyplot(plt)
