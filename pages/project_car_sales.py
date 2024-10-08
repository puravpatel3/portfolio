import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title Section: Car Sales Analysis
st.title("Car Sales Analysis")

# Project Summary
st.header("Project Summary")
st.write("""
This project showcases my analytical skills in exploring sales patterns, customer demographics, and dealer performance using a car sales dataset. The goal is to uncover insights into sales distributions, customer income-price relationships, and regional dealer performance, while also identifying top-selling car models. This analysis is valuable for car manufacturers, dealers, and marketing teams to optimize their strategies based on data-driven insights.
""")

# Instructions
st.header("Instructions")
st.write("""
1. Use the **Sales Distribution** section to view sales by dealer region and specific dealers.
2. Check the **Income vs. Price** section to analyze how customer income correlates with car prices.
3. Explore the **Sales by Model & Body Style** to identify top-selling models and their body styles.
4. Use **Sales Over Time** to observe seasonal and yearly sales trends.
5. The **Top 5 Dealers by Revenue** section highlights the top revenue-generating dealerships.
""")

# Use Case
st.header("Use Case")
st.write("""
This analysis helps stakeholders understand customer behavior, sales distribution across regions, and high-performing dealerships. It enables better decision-making for inventory management, pricing strategies, and targeted marketing campaigns.
""")

# Key Technologies Used
st.header("Key Technologies Used")
st.write("""
- **Pandas**: Used for data manipulation and preparation.
- **Matplotlib & Seaborn**: For generating visualizations to track sales trends.
- **Streamlit**: Used to build the interactive web application.
""")

# Load dataset
csv_url = 'https://github.com/puravpatel3/portfolio/blob/7e1c707c1363b45cc59b4ed89a411f88fae04e82/files/car_sales.csv'
df = pd.read_csv(csv_url)

# Convert Date column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Sidebar Filters
st.sidebar.header('Filter Options')

# Filter by Dealer Region
dealer_region_filter = st.sidebar.selectbox('Select Dealer Region', options=['All'] + sorted(df['Dealer_Region'].unique()))

# Filter by Dealer Name
if dealer_region_filter == 'All':
    dealer_filter = st.sidebar.selectbox('Select Dealer', options=['All'] + sorted(df['Dealer_Name'].unique()))
else:
    filtered_dealers = df[df['Dealer_Region'] == dealer_region_filter]['Dealer_Name'].unique()
    dealer_filter = st.sidebar.selectbox('Select Dealer', options=['All'] + sorted(filtered_dealers))

# Filter by Body Style
body_style_filter = st.sidebar.selectbox('Select Body Style', options=['All'] + sorted(df['Body Style'].unique()))

# Filter dataset based on user selection
if dealer_region_filter != 'All':
    df = df[df['Dealer_Region'] == dealer_region_filter]
if dealer_filter != 'All':
    df = df[df['Dealer_Name'] == dealer_filter]
if body_style_filter != 'All':
    df = df[df['Body Style'] == body_style_filter]

# 1. Sales Distribution by Region and Dealer
st.header("Sales Distribution by Region and Dealer")
sales_by_region = df.groupby('Dealer_Region').agg(total_sales=('Car_id', 'size')).reset_index()

# Bar chart for Sales by Region
st.write("### Sales by Region")
fig, ax = plt.subplots()
sns.barplot(x='Dealer_Region', y='total_sales', data=sales_by_region, ax=ax)
ax.set_title('Sales by Region')
ax.set_xlabel('Region')
ax.set_ylabel('Total Sales')
st.pyplot(fig)

# 2. Income vs. Price Correlation
st.header("Income vs. Price Correlation")
fig, ax = plt.subplots()
sns.scatterplot(x='Annual Income', y='Price ($)', hue='Body Style', data=df, ax=ax)
ax.set_title('Annual Income vs. Price ($)')
st.pyplot(fig)

# 3. Sales by Model and Body Style
st.header("Sales by Model & Body Style")
sales_by_model = df.groupby('Model').agg(total_sales=('Car_id', 'size')).reset_index().nlargest(10, 'total_sales')

# Bar chart for Top 10 Car Models by Sales
st.write("### Top 10 Car Models by Sales")
fig, ax = plt.subplots()
sns.barplot(x='Model', y='total_sales', data=sales_by_model, ax=ax)
ax.set_title('Top 10 Car Models by Sales')
st.pyplot(fig)

# 6. Sales Over Time
st.header("Sales Over Time")
df['Year'] = df['Date'].dt.year
sales_by_year = df.groupby('Year').agg(total_sales=('Car_id', 'size')).reset_index()

# Line chart for Sales Over Time
st.write("### Sales Trend Over Time")
fig, ax = plt.subplots()
sns.lineplot(x='Year', y='total_sales', data=sales_by_year, ax=ax)
ax.set_title('Car Sales Over Time')
st.pyplot(fig)

# 7. Top 5 Dealers by Revenue
st.header("Top 5 Dealers by Revenue")
revenue_by_dealer = df.groupby('Dealer_Name').agg(total_revenue=('Price ($)', 'sum')).reset_index().nlargest(5, 'total_revenue')

# Bar chart for Top 5 Dealers by Revenue
st.write("### Top 5 Dealers by Revenue")
fig, ax = plt.subplots()
sns.barplot(x='Dealer_Name', y='total_revenue', data=revenue_by_dealer, ax=ax)
ax.set_title('Top 5 Dealers by Revenue')
st.pyplot(fig)
