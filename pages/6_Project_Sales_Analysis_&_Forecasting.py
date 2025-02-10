import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from prophet import Prophet
import matplotlib.dates as mdates

# ------------------- Page Configuration -------------------
st.set_page_config(page_title="Sales Analysis and Forecasting for Automotive Industry", layout="wide")

# ------------------- Project Title -------------------
st.title("Sales Analysis and Forecasting for Automotive Industry")

# ------------------- Project Summary -------------------
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

# ------------------- Use Case -------------------
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
""")

# ------------------- Key Technologies Used -------------------
st.header("Key Technologies Used")
st.write("""
- **Pandas**: Data manipulation and preparation.
- **Matplotlib & Seaborn**: Visualization of sales trends and distributions.
- **Streamlit**: Interactive web application development.
- **Prophet**: Time series forecasting for predicting future revenue trends.
- **NumPy**: Numerical operations.
""")

# ------------------- Project Steps -------------------
st.header("Project Steps")
with st.expander("Step 1: Data Cleaning & Preprocessing"):
    st.markdown("""
    **Actions Taken:**  
    - Loaded the raw car sales data and standardized column names.
    - Converted the Date column to a datetime format.
    - Applied filters (by region, dealer, car model, body style) to allow for focused analysis.
    
    **Why It’s Important:**  
    Proper data cleaning and filtering ensure the analysis is based on accurate and relevant data, which is crucial for reliable forecasting.
    """)
with st.expander("Step 2: Exploratory Data Analysis (EDA)"):
    st.markdown("""
    **Actions Taken:**  
    - Analyzed sales distribution by region and over time.
    - Created visualizations (bar charts, heatmaps) to reveal regional performance and sales trends.
    
    **Why It’s Important:**  
    EDA helps uncover hidden trends and patterns, which inform both the modeling process and strategic decision-making.
    """)
with st.expander("Step 3: Modeling & Forecasting"):
    st.markdown("""
    **Actions Taken:**  
    - Utilized Prophet to develop a forecasting model based on historical sales data.
    - Enhanced the Prophet model by adding monthly, quarterly, and yearly seasonalities to better capture temporal trends.
    - Generated a revenue forecast for the upcoming periods, with a focus on 2024.
    
    **Why It’s Important:**  
    Accurate forecasting allows for proactive planning in inventory management, pricing, and resource allocation, reducing uncertainty and risk.
    """)
with st.expander("Step 4: Deployment & Dashboard"):
    st.markdown("""
    **Actions Taken:**  
    - Built an interactive dashboard using Streamlit to present sales analysis, forecasts, and key metrics.
    - Integrated filtering options to allow stakeholders to explore data by region, dealer, model, and body style.
    
    **Why It’s Important:**  
    An interactive dashboard makes complex data and forecasts accessible to decision-makers, supporting data-driven strategies.
    """)

# ------------------- Dataset Section -------------------
st.header("Dataset")
st.markdown("""
**Data Source**: [Car Sales Data](https://github.com/puravpatel3/portfolio/blob/018984013112e43d9f5447b7ce51bfd4d764f7cc/files/car_sales.csv)

*Click on the 'Download raw file' button in Github to access the data.*
""")
st.subheader("Dataset Preview")
csv_url = 'https://raw.githubusercontent.com/puravpatel3/portfolio/7e1c707c1363b45cc59b4ed89a411f88fae04e82/files/car_sales.csv'
df = pd.read_csv(csv_url)
df['Date'] = pd.to_datetime(df['Date'])
st.write(df.head())

# ------------------- Sidebar Filters -------------------
st.sidebar.header('Filter Options')
region_filter = st.sidebar.selectbox('Select Dealer Region', options=['All'] + sorted(df['Dealer_Region'].unique()))
if region_filter == 'All':
    dealer_filter = st.sidebar.selectbox('Select Dealer', options=['All'] + sorted(df['Dealer_Name'].unique()))
else:
    filtered_dealers = df[df['Dealer_Region'] == region_filter]['Dealer_Name'].unique()
    dealer_filter = st.sidebar.selectbox('Select Dealer', options=['All'] + sorted(filtered_dealers))
car_model_filter = st.sidebar.selectbox('Select Car Model', options=['All'] + sorted(df['Model'].unique()))
body_style_filter = st.sidebar.selectbox('Select Body Style', options=['All'] + sorted(df['Body Style'].unique()))
filtered_df = df.copy()
if region_filter != 'All':
    filtered_df = filtered_df[filtered_df['Dealer_Region'] == region_filter]
if dealer_filter != 'All':
    filtered_df = filtered_df[filtered_df['Dealer_Name'] == dealer_filter]
if body_style_filter != 'All':
    filtered_df = filtered_df[filtered_df['Body Style'] == body_style_filter]
if car_model_filter != 'All':
    filtered_df = filtered_df[filtered_df['Model'] == car_model_filter]

# ------------------- Sales Analysis Visualizations -------------------
st.header("Sales Analysis Visualizations")

# 1. Sales Distribution by Region and Dealer
st.subheader("Sales Distribution by Region and Dealer")
sales_by_region = filtered_df.groupby('Dealer_Region').agg(total_sales=('Price ($)', 'sum')).reset_index().sort_values(by='total_sales', ascending=False)
filtered_df['YearQuarter'] = filtered_df['Date'].dt.year.astype(str) + "Q" + (((filtered_df['Date'].dt.month - 1) // 3 + 1).astype(str))
sales_by_quarter = filtered_df.groupby('YearQuarter').agg(total_sales=('Price ($)', 'sum')).reset_index()

col1, col2 = st.columns(2)
with col1:
    st.write("### Sales by Region")
    fig, ax = plt.subplots(figsize=(5, 3))
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
    fig, ax = plt.subplots(figsize=(5, 3))
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

# 2. Top 5 Dealers by Revenue & Top 5 Car Models by Sales
revenue_by_dealer = filtered_df.groupby('Dealer_Name').agg(total_revenue=('Price ($)', 'sum')).reset_index().nlargest(5, 'total_revenue')
sales_by_model = filtered_df.groupby('Model').agg(total_sales=('Price ($)', 'sum')).reset_index().nlargest(5, 'total_sales')
col3, col4 = st.columns(2)
with col3:
    st.write("### Top 5 Dealers by Revenue")
    fig, ax = plt.subplots(figsize=(5, 3))
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
    fig, ax = plt.subplots(figsize=(5, 3))
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

# ------------------- Advanced Analytics Section -------------------
st.header("Advanced Analytics")

# Sales Breakdown by Region and Car Model (Heatmap)
st.subheader("Sales Breakdown by Region and Car Model")
st.write("""
This heatmap visualizes the sales performance of various car models across different dealer regions. The color gradient represents the total sales volume in millions of dollars, ranging from green for higher sales to red for lower sales.
""")
sales_by_region_model = filtered_df.groupby(['Dealer_Region', 'Model']).agg(total_sales=('Price ($)', 'sum')).reset_index()
top_models = sales_by_region_model.groupby('Model').agg(total_sales=('total_sales', 'sum')).nlargest(10, 'total_sales').index
filtered_sales = sales_by_region_model[sales_by_region_model['Model'].isin(top_models)]
heatmap_data = filtered_sales.pivot_table(index='Dealer_Region', columns='Model', values='total_sales', aggfunc='sum')
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(heatmap_data / 1_000_000, cmap='RdYlGn', annot=True, fmt='.1f', linewidths=.5, ax=ax, cbar_kws={'label': 'Total Sales ($M)'})
ax.set_title('Sales Breakdown by Region and Car Model')
ax.set_xlabel('Car Model')
ax.set_ylabel('Dealer Region')
st.pyplot(fig)

# ------------------- Forecasting Section -------------------
st.header("Revenue Forecasting")

# Aggregating data for forecasting
st.subheader("Revenue Forecasting for Regions")
st.write("""
This time series forecast predicts revenue trends for all regions over the next year based on historical data. By analyzing past sales performance and projecting future revenue, 
this forecast enables business leaders to make proactive decisions on inventory, staffing, and advertising. The forecast includes confidence intervals to indicate uncertainty.
""")
if not filtered_df.empty:
    region_data = filtered_df.groupby('Date').agg(total_sales=('Price ($)', 'sum')).reset_index()
    if len(region_data) > 30:
        region_data = region_data.rename(columns={'Date': 'ds', 'total_sales': 'y'})
        # Initialize Prophet with additional yearly seasonality for improved accuracy
        model = Prophet(changepoint_prior_scale=0.0015, seasonality_prior_scale=10)
        model.add_seasonality(name='monthly', period=30.5, fourier_order=3)
        model.add_seasonality(name='quarterly', period=91.25, fourier_order=5)
        model.add_seasonality(name='yearly', period=365.25, fourier_order=10)
        # For further accuracy, consider adding holiday effects or external regressors if available.
        try:
            model.fit(region_data)
            future = model.make_future_dataframe(periods=730)
            forecast = model.predict(future)
            fig2, ax = plt.subplots()
            model.plot(forecast, ax=ax)
            ax.set_title(f'Revenue Forecast for {region_filter} Region')
            ax.set_xlabel('YearQuarter')
            ax.set_ylabel('Revenue ($)')
            ax.set_xticks(pd.date_range(start='2023-01-01', end='2024-12-31', freq='QS'))
            ax.set_xticklabels([f'{date.year}Q{((date.month - 1) // 3) + 1}' for date in pd.date_range(start='2023-01-01', end='2024-12-31', freq='QS')])
            plt.xticks(rotation=45)
            start_date = pd.to_datetime('2023-01-01')
            end_date = pd.to_datetime('2024-12-31')
            ax.set_xlim([start_date, end_date])
            ax.set_yticklabels([f'${tick / 1_000_000:.1f}M' for tick in ax.get_yticks()])
            st.pyplot(fig2)
        except Exception as e:
            st.error(f"An error occurred while forecasting: {str(e)}")
    else:
        st.warning(f"Not enough data points available to forecast for the selected region. Please select a different region.")
else:
    st.warning("No data available for the selected filters. Please choose different filter options.")

# Revenue Forecast for 2024
st.subheader("Revenue Forecast for 2024")
forecast_2024 = forecast[(forecast['ds'] >= '2024-01-01') & (forecast['ds'] <= '2024-12-31')]
forecast_2024['YearMonth'] = forecast_2024['ds'].dt.to_period('M')
forecast_2024['Month'] = forecast_2024['ds'].dt.strftime('%b')
monthly_forecast = forecast_2024.groupby('YearMonth').agg(revenue_forecast=('yhat', 'sum')).reset_index()
monthly_forecast['Month'] = monthly_forecast['YearMonth'].dt.strftime('%b')
monthly_forecast['Cumulative'] = monthly_forecast['revenue_forecast'].cumsum()
monthly_forecast['Revenue Forecast ($)'] = monthly_forecast['revenue_forecast'].apply(lambda x: f'${int(x):,}')
monthly_forecast['Cumulative Revenue ($)'] = monthly_forecast['Cumulative'].apply(lambda x: f'${int(x):,}')
col5, col6 = st.columns(2)
with col5:
    fig3, ax = plt.subplots()
    ax.plot(monthly_forecast['YearMonth'].dt.to_timestamp(), monthly_forecast['revenue_forecast'], color='blue', label='Predicted Revenue')
    ax.fill_between(monthly_forecast['YearMonth'].dt.to_timestamp(), 
                    forecast_2024.groupby('YearMonth').agg(yhat_lower=('yhat_lower', 'sum')).reset_index()['yhat_lower'], 
                    forecast_2024.groupby('YearMonth').agg(yhat_upper=('yhat_upper', 'sum')).reset_index()['yhat_upper'], 
                    color='skyblue', alpha=0.3, label='Uncertainty Interval')
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

# ------------------- Key Takeaways -------------------
st.header("Key Takeaways")
st.markdown("""
- **Sales Trends:**  
  Analysis shows distinct regional differences and seasonal trends in car sales, indicating areas of strong performance and opportunities for improvement.
  
- **Forecasting Insights:**  
  The predictive model, enhanced with monthly, quarterly, and yearly seasonalities, forecasts revenue trends that can inform strategic decisions. The 2024 revenue forecast provides a granular, month-by-month outlook along with cumulative revenue projections.
  
- **Actionable Intelligence:**  
  These insights support inventory management, pricing strategies, and targeted marketing efforts, enabling dealerships and manufacturers to optimize operations.
""")

# ------------------- Next Steps -------------------
st.header("Next Steps")
st.markdown("""
- **Improve Forecasting Accuracy:**  
  - Tune Prophet parameters further and consider incorporating additional seasonalities or external regressors (e.g., holidays, economic indicators).
  - Use cross-validation with Prophet to assess forecast performance and adjust model settings accordingly.
  
- **Data Enrichment:**  
  - Integrate more granular data (e.g., promotional events, customer demographics) to enhance forecasting and analysis.
  
- **Dashboard Enhancements:**  
  - Add more interactive filtering options and drill-down capabilities to allow for deeper exploration of the data.
  - Explore integrating other forecasting methods for ensemble predictions.
  
- **Operational Integration:**  
  - Use the forecast outputs to drive real-time decision-making in inventory management, pricing strategies, and targeted marketing campaigns.
""")
