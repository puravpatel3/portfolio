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
2. Explore the **Sales by Model & Body Style** to identify top-selling models and their body styles.
3. Use **Sales Over Time** to observe seasonal and yearly sales trends.
4. The **Top 5 Dealers by Revenue** section highlights the top revenue-generating dealerships.
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
csv_url = 'https://raw.githubusercontent.com/puravpatel3/portfolio/7e1c707c1363b45cc59b4ed89a411f88fae04e82/files/car_sales.csv'
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

# Filter by Car Model
car_model_filter = st.sidebar.selectbox('Select Car Model', options=['All'] + sorted(df['Model'].unique()))

# Filter dataset based on user selection
if dealer_region_filter != 'All':
    df = df[df['Dealer_Region'] == dealer_region_filter]
if dealer_filter != 'All':
    df = df[df['Dealer_Name'] == dealer_filter]
if body_style_filter != 'All':
    df = df[df['Body Style'] == body_style_filter]
if car_model_filter != 'All':
    df = df[df['Model'] == car_model_filter]

# 1. Sales Distribution by Region and Dealer
st.header("Sales Distribution by Region and Dealer")
sales_by_region = df.groupby('Dealer_Region').agg(total_sales=('Price ($)', 'sum')).reset_index().sort_values(by='total_sales', ascending=False)

# 2. Car Sales Over Time (Aggregated by Quarter-Year)
df['Quarter-Year'] = df['Date'].dt.to_period('Q')
sales_by_quarter = df.groupby('Quarter-Year').agg(total_sales=('Price ($)', 'sum')).reset_index()

# First row: Sales by Region and Car Sales Over Time side by side
col1, col2 = st.columns(2)

with col1:
    st.write("### Sales by Region")
    fig, ax = plt.subplots()
    sns.barplot(x='Dealer_Region', y='total_sales', data=sales_by_region, ax=ax)
    for index, value in enumerate(sales_by_region['total_sales']):
        ax.text(index, value, f'${value/1_000_000:.1f}M', ha='center')
    ax.set_title('Sales by Region')
    ax.set_xlabel('Region')
    ax.set_ylabel('Total Sales ($M)')
    st.pyplot(fig)

with col2:
    st.write("### Car Sales Over Time (by Quarter)")
    fig, ax = plt.subplots()
    sns.barplot(x='Quarter-Year', y='total_sales', data=sales_by_quarter, ax=ax)
    for index, value in enumerate(sales_by_quarter['total_sales']):
        ax.text(index, value, f'${value/1_000_000:.1f}M', ha='center')
    ax.set_title('Car Sales Over Time (by Quarter-Year)')
    ax.set_xlabel('Quarter-Year')
    ax.set_ylabel('Total Sales ($M)')
    plt.xticks(rotation=45)
    st.pyplot(fig)

# 3. Top 5 Dealers by Revenue
revenue_by_dealer = df.groupby('Dealer_Name').agg(total_revenue=('Price ($)', 'sum')).reset_index().nlargest(5, 'total_revenue')

# 4. Top 5 Car Models by Sales
sales_by_model = df.groupby('Model').agg(total_sales=('Price ($)', 'sum')).reset_index().nlargest(5, 'total_sales')

# Second row: Top 5 Dealers by Revenue and Top 5 Car Models by Sales side by side
col3, col4 = st.columns(2)

with col3:
    st.write("### Top 5 Dealers by Revenue")
    fig, ax = plt.subplots()
    sns.barplot(x='Dealer_Name', y='total_revenue', data=revenue_by_dealer, ax=ax)
    for index, value in enumerate(revenue_by_dealer['total_revenue']):
        ax.text(index, value, f'${value/1_000_000:.1f}M', ha='center')
    ax.set_title('Top 5 Dealers by Revenue')
    ax.set_xlabel('Dealer Name')
    ax.set_ylabel('Total Revenue ($M)')
    plt.xticks(rotation=45, ha='right', wrap=True)
    st.pyplot(fig)

with col4:
    st.write("### Top 5 Car Models by Sales")
    fig, ax = plt.subplots()
    sns.barplot(x='Model', y='total_sales', data=sales_by_model, ax=ax)
    for index, value in enumerate(sales_by_model['total_sales']):
        ax.text(index, value, f'${value/1_000_000:.1f}M', ha='center')
    ax.set_title('Top 5 Car Models by Sales')
    ax.set_xlabel('Car Model')
    ax.set_ylabel('Total Sales ($M)')
    plt.xticks(rotation=45, ha='right', wrap=True)
    st.pyplot(fig)
