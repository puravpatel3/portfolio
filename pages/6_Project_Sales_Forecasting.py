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
This project delves into car sales data to provide a comprehensive analysis of sales distribution patterns, regional trends, and dealership performance. 
The analysis breaks down sales by car model, region, and time, uncovering actionable insights into market dynamics. Advanced analytics techniques, 
such as heatmaps and trend analysis, are used to identify high- and low-performing areas, offering valuable benchmarks for performance evaluation.

A critical component of the project is the development of a predictive sales forecasting model. By leveraging historical sales data and advanced forecasting algorithms, 
the model enables car manufacturers and dealerships to anticipate future demand with greater accuracy. These insights empower stakeholders to make data-driven decisions 
that enhance inventory management, optimize pricing strategies, and streamline resource allocation.

The project underscores the importance of leveraging data analytics to transform raw sales data into meaningful insights, fostering strategic growth, 
and improving operational efficiency in the automotive industry.
""")

# Data Source
st.markdown("""
**Data Source**: [Car Sales Data](https://github.com/puravpatel3/portfolio/blob/018984013112e43d9f5447b7ce51bfd4d764f7cc/files/car_sales.csv)

**Download Comprehensive Exploratory Data Analysis Report generated using ydata-profiling here**: [Click Here](https://github.com/puravpatel3/portfolio/blob/018984013112e43d9f5447b7ce51bfd4d764f7cc/files/car_sales_eda_report.html)

*Click on the 'Download raw file' button in Github to access the data or report*
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
The car sales analysis and forecasting project provides stakeholders with essential insights to drive strategic decision-making and optimize operations in the automotive industry. Key use cases include:

1. **Enhanced Inventory Management**:  
   Insights into regional sales trends and demand patterns help manufacturers and dealerships ensure optimal inventory levels, minimizing overstocking or stockouts.

2. **Optimized Pricing Strategies**:  
   Regional sales performance and customer behavior data inform dynamic pricing strategies, ensuring competitiveness while maximizing profitability.

3. **Targeted Marketing Campaigns**:  
   By identifying high-performing regions and popular car models, marketing efforts can be focused on areas with the highest potential for returns, improving campaign efficiency and effectiveness.

4. **Performance Benchmarking**:  
   The analysis provides benchmarks for comparing dealership performance, enabling the identification of underperforming locations or regions that require additional focus and resources.

5. **Resource Allocation**:  
   The insights support smarter allocation of resources, such as advertising budgets or inventory placement, based on regional demand patterns and forecasted trends.

6. **Future Demand Forecasting**:  
   The sales forecasting model assists manufacturers and dealerships in anticipating future trends, reducing uncertainty and supporting long-term planning efforts.

This project highlights the value of advanced analytics and predictive modeling in understanding market dynamics and improving business outcomes in the automotive sector. 
The methodologies and insights are adaptable to other industries, showcasing the versatility of data analytics in solving complex business challenges.
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

# Clean the column names
filtered_df.columns = filtered_df.columns.str.strip()

# Advanced Analytics Section
st.header("Advanced Analytics")

# Sales Breakdown by Region and Car Model
st.subheader("Sales Breakdown by Region and Car Model")
st.write("""
This heatmap visualizes the sales performance of various car models across different dealer regions. The color gradient represents the total sales volume in millions of dollars, 
ranging from green for higher sales to red for lower sales. By analyzing this visualization, key trends and patterns in sales distribution can be identified, aiding in strategic decision-making.

**Key Insights:**  
1. **Top-Performing Regions and Models**:  
   Regions such as Austin and Janesville show consistently higher sales for models like the LS400 and Ram Pickup, suggesting strong demand and successful dealership operations in these areas.  
   
2. **Underperforming Models and Regions**:  
   Models like Montero Sport and Prizm have significantly lower sales across most regions, indicating potential issues with market appeal or availability.  

3. **Strategic Applications**:  
   - Focus marketing efforts and promotional campaigns on high-performing regions and models to maximize returns.  
   - Allocate inventory to regions with consistent demand for specific models to reduce overstocking in underperforming areas.  
   - Investigate underperforming regions and models to identify potential factors such as pricing, competition, or local preferences that could be addressed to improve sales.  

This heatmap highlights critical opportunities for optimizing resource allocation, refining inventory management, and tailoring marketing strategies to regional and model-specific trends. Stakeholders can use these insights to enhance dealership support and drive higher overall performance.
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

# Revenue Forecasting for Regions
st.subheader("Revenue Forecasting for Regions")
st.write("""
This time series forecast predicts revenue trends for all regions over the next year based on historical data. By analyzing past sales performance and projecting future revenue, 
this forecast enables business leaders to make proactive and informed decisions. The ability to anticipate revenue fluctuations across quarters ensures more strategic resource allocation 
and improved operational efficiency.

**Key Insights:**  
1. **Future Demand Prediction**:  
   The forecast provides a clear picture of expected revenue trends, helping businesses plan inventory levels, marketing strategies, and regional initiatives in advance.  

2. **Strategic Adjustments**:  
   Insights from the forecast enable adjustments to production schedules, staffing, and advertising budgets to align with anticipated demand.  

3. **Risk Management**:  
   The confidence intervals highlight potential volatility in revenue, allowing decision-makers to prepare for best- and worst-case scenarios.

**Chart Explanation:**  
- **Black Dots**: Represent actual historical revenue data points, providing a baseline for the forecast.  
- **Darker Blue Line**: Represents the predicted revenue trend for the next year, showing the expected trajectory based on historical patterns.  
- **Lighter Blue Shaded Area**: Represents the uncertainty or confidence interval around the forecast, illustrating the range of potential revenue outcomes.

This predictive model highlights the importance of data-driven forecasting for businesses, offering a competitive advantage by enabling proactive strategy formulation and efficient resource management.
""")

# Ensure we have data to work with
if not filtered_df.empty:
    # Aggregating data to prepare for forecasting
    region_data = filtered_df.groupby('Date').agg(total_sales=('Price ($)', 'sum')).reset_index()

    # Check if we have enough data for a meaningful forecast
    if len(region_data) > 30:  # Ensure we have at least 30 data points for a reasonable forecast
        # Renaming columns for Prophet
        region_data = region_data.rename(columns={'Date': 'ds', 'total_sales': 'y'})

        # Initializing and fitting the Prophet model with adjusted parameters
        model = Prophet(changepoint_prior_scale=0.0015, seasonality_prior_scale=10)
        model.add_seasonality(name='monthly', period=30.5, fourier_order=3)
        model.add_seasonality(name='quarterly', period=91.25, fourier_order=5)
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
forecast_2024['Month'] = forecast_2024['ds'].dt.strftime('%b')
monthly_forecast = forecast_2024.groupby('YearMonth').agg(revenue_forecast=('yhat', 'sum')).reset_index()
monthly_forecast['Month'] = monthly_forecast['YearMonth'].dt.strftime('%b')
monthly_forecast['Cumulative'] = monthly_forecast['revenue_forecast'].cumsum()

# Format the Revenue Forecast and Cumulative columns
monthly_forecast['Revenue Forecast ($)'] = monthly_forecast['revenue_forecast'].apply(lambda x: f'${int(x):,}')
monthly_forecast['Cumulative Revenue ($)'] = monthly_forecast['Cumulative'].apply(lambda x: f'${int(x):,}')

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
    st.table(monthly_forecast[['YearMonth', 'Month', 'Revenue Forecast ($)', 'Cumulative Revenue ($)']])
