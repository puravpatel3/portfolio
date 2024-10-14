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
This project focuses on analyzing car sales data to uncover sales distribution patterns, regional trends, and dealership performance. By breaking down car sales by model, region, and time, and employing advanced analytics like heatmaps, high and low-performing areas are identified. A key component of the project is the development of a sales forecasting model, which assists car manufacturers and dealers in anticipating future demand and making informed strategic decisions.
""")

# Instructions
st.header("Instructions")
st.write("""
1. Use the **Sales Distribution** section to view sales by dealer region and top dealers.
2. Explore the **Sales by Car Model** to identify top-selling models.
3. Use **Sales Over Time** to observe seasonal and yearly sales trends.
4. Filter on any Region, Dealer, Car Model or Body Style to take a deeper look.
""")

# Use Case
st.header("Use Case")
st.write("""
This analysis helps stakeholders understand customer behavior, sales distribution across regions, and high-performing dealerships. It enables better decision-making for inventory management, pricing strategies, and targeted marketing campaigns. Additionally, the insights can help identify underperforming regions or models that need more focus and provide a benchmark for dealer performance comparisons. The analysis also supports resource allocation and helps in optimizing marketing efforts based on regional demand patterns.
""")

# Key Technologies Used
st.header("Key Technologies Used")
st.write("""
- **Pandas**: Used for data manipulation and preparation.
- **Matplotlib & Seaborn**: For generating visualizations to track sales trends.
- **Streamlit**: Used to build the interactive web application.
- **Prophet**: Used for time series forecasting to predict future revenue trends.
- **NumPy**: Utilized for numerical operations and array manipulations.
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

# Filter by Car Model
car_model_filter = st.sidebar.selectbox('Select Car Model', options=['All'] + sorted(df['Model'].unique()))

# Filter by Body Style
body_style_filter = st.sidebar.selectbox('Select Body Style', options=['All'] + sorted(df['Body Style'].unique()))

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
filtered_df['YearQuarter'] = filtered_df['Date'].dt.year.astype(str) + "Q" + ((filtered_df['Date'].dt.month - 1) // 3 + 1).astype(str)
sales_by_quarter = filtered_df.groupby('YearQuarter').agg(total_sales=('Price ($)', 'sum')).reset_index()

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
    ax.set_yticks([i * 10_000_000 for i in range(0, int(sales_by_region['total_sales'].max() // 10_000_000) + 2)])
    ax.set_yticklabels([f'${tick/1_000_000:.1f}M' for tick in ax.get_yticks()])
    st.pyplot(fig)

with col2:
    st.write("### Car Sales Over Time (by Quarter)")
    fig, ax = plt.subplots(figsize=(5, 3))  # Adjusting figure size
    sns.barplot(x='YearQuarter', y='total_sales', data=sales_by_quarter, ax=ax)
    for index, value in enumerate(sales_by_quarter['total_sales']):
        ax.text(index, value, f'${value/1_000_000:.1f}M', ha='center', fontsize=10)
    ax.set_title('Car Sales Over Time (by YearQuarter)', fontsize=12)
    ax.set_xlabel('YearQuarter', fontsize=10)
    ax.set_ylabel('Total Sales ($M)', fontsize=10)
    plt.xticks(rotation=45, fontsize=8)
    ax.set_yticks([i * 10_000_000 for i in range(0, int(sales_by_quarter['total_sales'].max() // 10_000_000) + 2)])
    ax.set_yticklabels([f'${tick/1_000_000:.1f}M' for tick in ax.get_yticks()])
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
    ax.set_yticks([i * 5_000_000 for i in range(0, int(revenue_by_dealer['total_revenue'].max() // 5_000_000) + 2)])
    ax.set_yticklabels([f'${tick/1_000_000:.1f}M' for tick in ax.get_yticks()])
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
    ax.set_yticks([i * 5_000_000 for i in range(0, int(sales_by_model['total_sales'].max() // 5_000_000) + 2)])
    ax.set_yticklabels([f'${tick/1_000_000:.1f}M' for tick in ax.get_yticks()])
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

**Chart Explanation:**
- **Black dots**: Represent the actual historical revenue data points.
- **Darker blue line**: Represents the predicted revenue trend for the next year.
- **Lighter blue shaded area**: Represents the uncertainty interval (confidence interval) around the forecast.
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

            # Creating a future dataframe to forecast 730 days ahead (2 years)
            future = model.make_future_dataframe(periods=730)

            # Predicting future sales
            forecast = model.predict(future)

            # Plotting the forecast
            fig2, ax = plt.subplots()
            model.plot(forecast, ax=ax)
            ax.set_title(f'Revenue Forecast for {region_filter} Region')

            # Formatting x-axis and y-axis
            ax.set_xlabel('YearQuarter')
            ax.set_ylabel('Revenue ($)')
            ax.set_xticks(pd.date_range(start='2023-01-01', end='2024-12-31', freq='QS'))
            ax.set_xticklabels([f'{date.year}Q{((date.month - 1) // 3) + 1}' for date in pd.date_range(start='2023-01-01', end='2024-12-31', freq='QS')])
            plt.xticks(rotation=45)

            # Set x-axis limits using datetime objects
            start_date = pd.to_datetime('2023-01-01')
            end_date = pd.to_datetime('2024-12-31')
            ax.set_xlim([start_date, end_date])

            # Update y-axis tick labels to show as dollars in millions
            ax.set_yticklabels([f'${tick / 1_000_000:.1f}M' for tick in ax.get_yticks()])

            st.pyplot(fig2)
        except Exception as e:
            st.error(f"An error occurred while forecasting: {str(e)}")
    else:
        st.warning(f"Not enough data points available to forecast for the selected region. Please select a different region.")
else:
    st.warning("No data available for the selected filters. Please choose different filter options.")

# 3. Revenue Forecast for 2024
st.subheader("Revenue Forecast for 2024")

# Filter forecast data for the year 2024
forecast_2024 = forecast[(forecast['ds'] >= '2024-01-01') & (forecast['ds'] <= '2024-12-31')]

# Creating monthly aggregation for 2024
forecast_2024['YearMonth'] = forecast_2024['ds'].dt.to_period('M')
monthly_forecast = forecast_2024.groupby('YearMonth').agg(revenue_forecast=('yhat', 'sum')).reset_index()
monthly_forecast['Cumulative'] = monthly_forecast['revenue_forecast'].cumsum()

# Plotting the monthly forecast for 2024
col5, col6 = st.columns(2)

with col5:
    fig3, ax = plt.subplots()
    ax.plot(monthly_forecast['YearMonth'].dt.to_timestamp(), monthly_forecast['revenue_forecast'], color='blue', label='Predicted Revenue')
    ax.fill_between(monthly_forecast['YearMonth'].dt.to_timestamp(), forecast_2024.groupby('YearMonth').agg(yhat_lower=('yhat_lower', 'sum')).reset_index()['yhat_lower'], forecast_2024.groupby('YearMonth').agg(yhat_upper=('yhat_upper', 'sum')).reset_index()['yhat_upper'], color='skyblue', alpha=0.3, label='Uncertainty Interval')
    ax.set_title('Revenue Forecast for 2024')
    ax.set_xlabel('Month')
    ax.set_ylabel('Revenue ($M)')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.xticks(rotation=45, fontsize=8)
    ax.set_yticklabels([f'${tick / 1_000_000:.1f}M' for tick in ax.get_yticks()])

    st.pyplot(fig3)

with col6:
    st.write("### Revenue Forecast Table for 2024")
    st.table(monthly_forecast.rename(columns={'YearMonth': 'Year-Month', 'revenue_forecast': 'Revenue Forecast ($)', 'Cumulative': 'Cumulative Revenue ($)'}))
