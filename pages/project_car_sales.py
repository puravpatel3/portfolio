import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title and Summary Section
st.title("Car Sales Analysis")

st.header("Project Summary")
st.write("""
This project analyzes car sales across multiple dealerships, allowing for insights into sales performance, regional breakdowns, and top models sold. You can toggle between the number of cars sold (Count) and total sales revenue (Sales) for each analysis.
""")

st.header("Instructions")
st.write("""
1. Use the toggle to switch between Count of car sales and Sales revenue.
2. Visualize sales by region, top car models, sales over time, and dealer performance.
3. For each chart, hover over bars to see additional details.
""")

# Load dataset from the uploaded file or the appropriate source
csv_url = '/mnt/data/your_dataset.csv'  # Update this path with your dataset location
df = pd.read_csv(csv_url)

# Convert Date column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Sidebar for toggle between Count and Sales
toggle = st.sidebar.radio("Select View:", ['Sales', 'Count'])

# Helper function to abbreviate numbers
def abbreviate_number(val):
    if val >= 1e6:
        return f"${val/1e6:.1f}M"
    elif val >= 1e3:
        return f"${val/1e3:.1f}k"
    else:
        return f"${val:.0f}"

# Process data based on the toggle selection
if toggle == 'Sales':
    df['Value'] = df['Price ($)']
    label = 'Total Sales ($)'
else:
    df['Value'] = 1
    label = 'Total Count of Cars Sold'

# 1. Sales by Region (descending order)
region_sales = df.groupby('Dealer_Region')['Value'].sum().reset_index()
region_sales = region_sales.sort_values(by='Value', ascending=False)

st.subheader(f"Sales by Region ({label})")
plt.figure(figsize=(10, 6))
ax = sns.barplot(x='Dealer_Region', y='Value', data=region_sales, palette='coolwarm')
ax.bar_label(ax.containers[0], labels=[abbreviate_number(x) for x in ax.containers[0].datavalues])
plt.title(f"Sales by Region ({label})")
plt.xticks(rotation=45, ha='right')
plt.ylabel(label)
plt.xlabel("Region")
st.pyplot(plt)

# 2. Top 5 Car Models by Sales
model_sales = df.groupby('Model')['Value'].sum().reset_index()
model_sales = model_sales.sort_values(by='Value', ascending=False).head(5)

st.subheader(f"Top 5 Car Models by {label}")
plt.figure(figsize=(10, 6))
ax = sns.barplot(x='Model', y='Value', data=model_sales, palette='muted')
ax.bar_label(ax.containers[0], labels=[abbreviate_number(x) for x in ax.containers[0].datavalues])
plt.title(f"Top 5 Car Models by {label}")
plt.xticks(rotation=45, ha='right', wrap=True)  # Wrapping long x-axis labels
plt.ylabel(label)
plt.xlabel("Car Model")
st.pyplot(plt)

# 3. Car Sales Over Time (Month-Year)
df['Month-Year'] = df['Date'].dt.to_period('M')
time_sales = df.groupby('Month-Year')['Value'].sum().reset_index()

st.subheader(f"Car Sales Over Time ({label})")
plt.figure(figsize=(10, 6))
ax = sns.barplot(x='Month-Year', y='Value', data=time_sales, palette='coolwarm')
ax.bar_label(ax.containers[0], labels=[abbreviate_number(x) for x in ax.containers[0].datavalues])
plt.title(f"Car Sales Over Time ({label})")
plt.xticks(rotation=45, ha='right')
plt.ylabel(label)
plt.xlabel("Month-Year")
st.pyplot(plt)

# 4. Top 5 Dealers by Revenue
dealer_sales = df.groupby('Dealer_Name')['Value'].sum().reset_index()
dealer_sales = dealer_sales.sort_values(by='Value', ascending=False).head(5)

st.subheader(f"Top 5 Dealers by {label}")
plt.figure(figsize=(10, 6))
ax = sns.barplot(x='Dealer_Name', y='Value', data=dealer_sales, palette='coolwarm')
ax.bar_label(ax.containers[0], labels=[abbreviate_number(x) for x in ax.containers[0].datavalues])
plt.title(f"Top 5 Dealers by {label}")
plt.xticks(rotation=45, ha='right', wrap=True)
plt.ylabel(label)
plt.xlabel("Dealer Name")
st.pyplot(plt)
