import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from prophet import Prophet
import matplotlib.dates as mdates

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
region_filter = st.sidebar.selectbox('Select Dealer Region', options=['All'] + sorted(df['Dealer_Region'].unique()))

# Filter by Dealer Name
if region_filter == 'All':
    dealer_filter = st.sidebar.selectbox('Select Dealer', options=['All'] + sorted(df['Dealer_Name'].unique()))
else:
    filtered_dealers = df[df['Dealer_Region'] == region_filter]['Dealer_Name'].unique()
    dealer_filter = st.sidebar.selectbox('Select Dealer', options=['All'] + sorted(filtered_dealers))

# Filter by Body Style
body_style_filter = st.sidebar.selectbox('Select Body Style', options=['All'] + sorted(df['Body Style'].unique()))

# Filter by Car Model
car_model_filter = st.sidebar.selectbox('Select Car Model', options=['All'] + sorted(df['Model'].unique()))

# Filter dataset based on user selection
filtered_df = df.copy()
if region_filter != 'All':
    filtered_df = filtered_df[filtered_df['Dealer_Region'] == region_filter]
if dealer_filter != 'All':
    filtered_df = filtered_df[filtered_df['Dealer_Name'] == dealer_filter]
if body_style_filter != 'All':
    filtered_df = filtered_df[filtered_df['Body Style'] == body_style_filter]
if car_model_filter != 'All':
    filtered_df = filtered_df[filtered_df['Model'] == car_model_filter]

# 1. Sales Distribution by Region and Dealer
st.header("Sales Distribution by Region and Dealer")
sales_by_region = filtered_df.groupby('Dealer_Region').agg(total_sales=('Price ($)', 'sum')).reset_index().sort_values(by='total_sales', ascending=False)

# 2. Car Sales Over Time (Aggregated by Quarter-Year)
filtered_df['Quarter-Year'] = filtered_df['Date'].dt.to_period('Q')
sales_by_quarter = filtered_df.groupby('Quarter-Year').agg(total_sales=('Price ($)', 'sum')).reset_index()

# First row: Sales by Region and Car Sales Over Time side by side
col1, col2 = st.columns(2)

with col1:
    st.write("### Sales by Region")
    fig, ax = plt.subplots(figsize=(5, 3))  # Adjusting figure size
    sns.barplot(x='Dealer_Region', y='total_sales', data=sales_by_region, ax=ax)
    for index, value in enumerate(sales_by_region['total_sales']):
        ax.text(index, value, f'${value/1_000_000:.1f}M', ha='center', fontsize=10)
    ax.set_title('Sales by Region', fontsize=12)
    ax.set_xlabel('Region', fontsize=10)
    ax.set_ylabel('Total Sales ($M)', fontsize=10)
    ax.tick_params(axis='x', labelsize=8, rotation=30)
    st.pyplot(fig)

with col2:
    st.write("### Car Sales Over Time (by Quarter)")
    fig, ax = plt.subplots(figsize=(5, 3))  # Adjusting figure size
    sns.barplot(x='Quarter-Year', y='total_sales', data=sales_by_quarter, ax=ax)
    for index, value in enumerate(sales_by_quarter['total_sales']):
        ax.text(index, value, f'${value/1_000_000:.1f}M', ha='center', fontsize=10)
    ax.set_title('Car Sales Over Time (by Quarter-Year)', fontsize=12)
    ax.set_xlabel('Quarter-Year', fontsize=10)
    ax.set_ylabel('Total Sales ($M)', fontsize=10)
    plt.xticks(rotation=45, fontsize=8)
    st.pyplot(fig)

# 3. Top 5 Dealers by Revenue
revenue_by_dealer = filtered_df.groupby('Dealer_Name').agg(total_revenue=('Price ($)', 'sum')).reset_index().nlargest(5, 'total_revenue')

# 4. Top 5 Car Models by Sales
sales_by_model = filtered_df.groupby('Model').agg(total_sales=('Price ($)', 'sum')).reset_index().nlargest(5, 'total_sales')

# Second row: Top 5 Dealers by Revenue and Top 5 Car Models by Sales side by side
col3, col4 = st.columns(2)

with col3:
    st.write("### Top 5 Dealers by Revenue")
    fig, ax = plt.subplots(figsize=(5, 3))  # Adjusting figure size
    sns.barplot(x='Dealer_Name', y='total_revenue', data=revenue_by_dealer, ax=ax)
    for index, value in enumerate(revenue_by_dealer['total_revenue']):
        ax.text(index, value, f'${value/1_000_000:.1f}M', ha='center', fontsize=10)
    ax.set_title('Top 5 Dealers by Revenue', fontsize=12)
    ax.set_xlabel('Dealer Name', fontsize=10)
    ax.set_ylabel('Total Revenue ($M)', fontsize=10)
    ax.set_yticklabels([f'${int(tick * 10)}M' for tick in ax.get_yticks()])  # Update y-axis labels
    plt.xticks(rotation=45, ha='right', wrap=True, fontsize=8)
    st.pyplot(fig)

with col4:
    st.write("### Top 5 Car Models by Sales")
    fig, ax = plt.subplots(figsize=(5, 3))  # Adjusting figure size
    sns.barplot(x='Model', y='total_sales', data=sales_by_model, ax=ax)
    for index, value in enumerate(sales_by_model['total_sales']):
        ax.text(index, value, f'${value/1_000_000:.1f}M', ha='center', fontsize=10)
    ax.set_title('Top 5 Car Models by Sales', fontsize=12)
    ax.set_xlabel('Car Model', fontsize=10)
    ax.set_ylabel('Total Sales ($M)', fontsize=10)
    ax.set_yticklabels([f'${int(tick * 10)}M' for tick in ax.get_yticks()])  # Update y-axis labels
    plt.xticks(rotation=45, ha='right', wrap=True, fontsize=8)
    st.pyplot(fig)

# Clean the column names by stripping whitespace
filtered_df.columns = filtered_df.columns.str.strip()

# Advanced Analytics Section
st.header("Advanced Analytics")

# 1. Sales Breakdown by Region and Car Model
st.subheader("Sales Breakdown by Region and Car Model")
st.write("""
This heatmap visualizes the sales breakdown by region and car model. The colors represent the volume of sales, with green indicating higher sales and red indicating lower sales. This is helpful for identifying high-performing regions and car models.

**Key Takeaways:**
Focus on the top-performing car models in high-sales regions to optimize inventory management and marketing strategies. By understanding which regions and models drive the highest sales, stakeholders can make more informed decisions about resource allocation, promotional focus, and dealership support.
""")

# Aggregating sales by region and car model
sales_by_region_model = filtered_df.groupby(['Dealer_Region', 'Model']).agg(total_sales=('Price ($)', 'sum')).reset_index()

# Get the top 10 car models by total sales
top_models = sales_by_region_model.groupby('Model').agg(total_sales=('total_sales', 'sum')).nlargest(10, 'total_sales').index

# Filter the dataset for the top 10 models
filtered_sales = sales_by_region_model[sales_by_region_model['Model'].isin(top_models)]

# Pivot the data to create a heatmap-compatible format
heatmap_data = filtered_sales.pivot_table(index='Dealer_Region', columns='Model', values='total_sales', aggfunc='sum')

# Creating the heatmap visualization with green for high sales and red for low sales
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(heatmap_data / 1_000_000, cmap='RdYlGn', annot=True, fmt='.1f', linewidths=.5, ax=ax, cbar_kws={'label': 'Total Sales ($M)'})
ax.set_title('Sales Breakdown by Region and Car Model')
ax.set_xlabel('Car Model')
ax.set_ylabel('Dealer Region')

# Display the heatmap
st.pyplot(fig)

# 2. Revenue Forecasting for Regions
st.subheader("Revenue Forecasting for Regions")
st.write("""
This time series forecast predicts the revenue for a specific region for the next year based on historical data. It allows business leaders to anticipate future trends in sales performance and adjust strategies accordingly.

**Key Takeaways:**
Use the forecasted data to plan for inventory, marketing, and regional strategy adjustments. Forecasting can help decision-makers understand future demand and align resources accordingly.
""")

# Ensure we have data to work with
if not filtered_df.empty:
    # Aggregating data to prepare for forecasting
    region_data = filtered_df.groupby('Date').agg(total_sales=('Price ($)', 'sum')).reset_index()

    # Check if we have enough data for a meaningful forecast
    if len(region_data) > 30:  # Ensure we have at least 30 data points for a reasonable forecast
        # Renaming columns for Prophet
        region_data = region_data.rename(columns={'Date': 'ds', 'total_sales': 'y'})

        # Initializing and fitting the Prophet model
        model = Prophet()
        try:
            model.fit(region_data)

            # Creating a future dataframe to forecast 365 days ahead
            future = model.make_future_dataframe(periods=365)

            # Predicting future sales
            forecast = model.predict(future)

            # Plotting the forecast
            fig2, ax = plt.subplots()
            model.plot(forecast, ax=ax)
            ax.set_title(f'Revenue Forecast for {region_filter} Region')

            # Formatting x-axis and y-axis
            ax.set_xlabel('Quarter')
            ax.set_ylabel('Revenue ($)')
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%YQ'))
            plt.xticks(rotation=45)

            # Set x-axis limits using datetime objects
            start_date = pd.to_datetime('2023-01-01')
            end_date = pd.to_datetime('2024-12-31')
            ax.set_xlim([start_date, end_date])

            st.pyplot(fig2)
        except Exception as e:
            st.error(f"An error occurred while forecasting: {str(e)}")
    else:
        st.warning(f"Not enough data points available to forecast for the selected region. Please select a different region.")
else:
    st.warning("No data available for the selected filters. Please choose different filter options.")
