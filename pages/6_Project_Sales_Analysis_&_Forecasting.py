import streamlit as st
import pandas as pd
import plotly.express as px
from prophet import Prophet
from prophet.plot import plot_plotly  # Importing the Plotly plotting function for Prophet
import plotly.io as pio
import matplotlib.dates as mdates

# ------------------- Page Configuration -------------------
st.set_page_config(page_title="Sales Analysis and Forecasting for Automotive Industry", layout="wide")

# ------------------- Project Title -------------------
st.title("Sales Analysis and Forecasting for Automotive Industry")

# ------------------- Project Summary -------------------
st.header("Project Summary")
st.write("""
This project delves into car sales data to provide a comprehensive analysis of sales distribution patterns, regional trends, and dealership performance. 
The analysis breaks down sales by car model, region, and time, uncovering actionable insights into market dynamics. Advanced analytics techniques—such as heatmaps and trend analysis—are used to identify high- and low-performing areas, offering valuable benchmarks for performance evaluation.

A critical component of the project is the development of a predictive sales forecasting model. By leveraging historical sales data and advanced forecasting algorithms, 
the model enables car manufacturers and dealerships to anticipate future demand with greater accuracy. These insights empower stakeholders to make data-driven decisions 
that enhance inventory management, optimize pricing strategies, and streamline resource allocation.

This project underscores the importance of transforming raw sales data into meaningful insights to foster strategic growth and improve operational efficiency.
""")

# ------------------- Use Case -------------------
st.header("Use Case")
st.write("""
The car sales analysis and forecasting project provides essential insights to drive strategic decision-making and optimize operations in the automotive industry. Key use cases include:

1. **Enhanced Inventory Management**:  
   Insights into regional sales trends and demand patterns help ensure optimal inventory levels, minimizing overstocking or stockouts.

2. **Optimized Pricing Strategies**:  
   Regional sales performance and customer behavior data inform dynamic pricing strategies that maximize profitability.

3. **Targeted Marketing Campaigns**:  
   Identifying high-performing regions and popular car models allows marketing efforts to be focused on areas with the highest potential returns.

4. **Performance Benchmarking**:  
   Benchmarks for dealership performance enable the identification of underperforming locations that may require additional focus.

5. **Resource Allocation**:  
   The insights support smarter allocation of resources—such as advertising budgets or inventory placement—based on regional demand patterns.

6. **Future Demand Forecasting**:  
   The sales forecasting model assists in anticipating future trends, reducing uncertainty and supporting long-term planning efforts.
""")

# ------------------- Key Technologies Used -------------------
st.header("Key Technologies Used")
st.write("""
- **Pandas**: Data manipulation and preparation.
- **Plotly Express**: Interactive visualizations with dynamic tooltips.
- **Streamlit**: Development of an interactive web application.
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
    EDA uncovers hidden trends and patterns, informing both the modeling process and strategic decision-making.
    """)
with st.expander("Step 3: Modeling & Forecasting"):
    st.markdown("""
    **Actions Taken:**  
    - Utilized Prophet to develop a forecasting model based on historical sales data.
    - Enhanced the Prophet model by adding monthly, quarterly, and yearly seasonalities to better capture temporal trends.
    - Generated a revenue forecast for the upcoming periods, with a focus on 2024.
    
    **Why It’s Important:**  
    Accurate forecasting enables proactive planning in inventory management, pricing, and resource allocation, reducing uncertainty and risk.
    """)
with st.expander("Step 4: Deployment & Dashboard"):
    st.markdown("""
    **Actions Taken:**  
    - Developed an interactive Streamlit dashboard that dynamically visualizes sales analysis, forecasts, and key metrics.
    - Integrated filtering options to allow stakeholders to explore data by region, dealer, model, and body style.
    
    **Why It’s Important:**  
    An interactive dashboard makes complex data and forecasts accessible to decision-makers, supporting data-driven strategies.
    """)

# ------------------- Dataset Section -------------------
st.header("Dataset")
st.markdown("""
**Data Source**: [Car Sales Data](https://github.com/puravpatel3/portfolio/blob/018984013112e43d9f5447b7ce51bfd4d764f7cc/files/car_sales.csv)

*Click on the 'Download raw file' button in GitHub to access the data.*
""")
st.subheader("Dataset Preview")
csv_url = 'https://raw.githubusercontent.com/puravpatel3/portfolio/7e1c707c1363b45cc59b4ed89a411f88fae04e82/files/car_sales.csv'
df = pd.read_csv(csv_url)
df['Date'] = pd.to_datetime(df['Date'])
st.dataframe(df.head(), height=250)

# ------------------- Sidebar Filters -------------------
st.sidebar.header("Filter Options")
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

# Define a custom color palette for charts without grouping
custom_palette = ["#99ccff"]

# Group 1: Sales Distribution by Region & Car Sales Over Time (by Quarter) side by side
col1, col2 = st.columns(2)

with col1:
    st.subheader("Sales Distribution by Region (Stacked by Body Style)")
    # Group by both Dealer Region and Body Style
    sales_by_region_body = filtered_df.groupby(['Dealer_Region', 'Body Style']).agg(total_sales=('Price ($)', 'sum')).reset_index()
    fig1 = px.bar(sales_by_region_body, 
              x='Dealer_Region', 
              y='total_sales', 
              color='Body Style',
              hover_data={'total_sales':':$,.2f'},
              labels={'Dealer_Region':'Region', 'total_sales':'Total Sales ($)'},
              title="Sales by Region (Stacked by Body Style)")
    fig1.update_layout(barmode='stack', xaxis_title="Region", yaxis_title="Total Sales ($)", hovermode="x unified")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Car Sales Over Time (by Quarter)")
    filtered_df['YearQuarter'] = filtered_df['Date'].dt.year.astype(str) + "Q" + (((filtered_df['Date'].dt.month - 1) // 3 + 1).astype(str))
    sales_by_quarter = filtered_df.groupby('YearQuarter').agg(total_sales=('Price ($)', 'sum')).reset_index()
    fig2 = px.bar(sales_by_quarter, x='YearQuarter', y='total_sales',
                  hover_data={'total_sales':':$,.2f'},
                  labels={'YearQuarter':'Year-Quarter', 'total_sales':'Total Sales ($)'},
                  title="Car Sales Over Time (by YearQuarter)")
    fig2.update_traces(marker_color="#99ccff")
    fig2.update_layout(xaxis_title="YearQuarter", yaxis_title="Total Sales ($)", hovermode="x unified")
    st.plotly_chart(fig2, use_container_width=True)

# Group 2: Top 5 Dealers by Revenue & Top 5 Car Models by Sales side by side
col3, col4 = st.columns(2)

with col3:
    st.subheader("Top 5 Dealers by Revenue (Stacked by Body Style)")
    revenue_by_dealer_body = filtered_df.groupby(['Dealer_Name', 'Body Style']).agg(total_revenue=('Price ($)', 'sum')).reset_index()
    total_revenue_by_dealer = filtered_df.groupby('Dealer_Name').agg(total_revenue=('Price ($)', 'sum')).reset_index()
    top_5_dealers = total_revenue_by_dealer.nlargest(5, 'total_revenue')['Dealer_Name']
    revenue_by_dealer_body = revenue_by_dealer_body[revenue_by_dealer_body['Dealer_Name'].isin(top_5_dealers)]
    fig3 = px.bar(revenue_by_dealer_body, x='Dealer_Name', y='total_revenue',
                  color='Body Style',
                  labels={'Dealer_Name':'Dealer Name', 'total_revenue':'Total Revenue ($)'},
                  title="Top 5 Dealers by Revenue (Stacked by Body Style)",
                  hover_data={'total_revenue':':$,.2f'},
                  barmode='stack')
    fig3.update_layout(xaxis_title="Dealer Name", yaxis_title="Total Revenue ($)", hovermode="x unified")
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    st.subheader("Top 5 Car Models by Sales")
    sales_by_model = filtered_df.groupby('Model').agg(total_sales=('Price ($)', 'sum')).reset_index().nlargest(5, 'total_sales')
    fig4 = px.bar(sales_by_model, x='Model', y='total_sales',
                  hover_data={'total_sales':':$,.2f'},
                  labels={'Model':'Car Model', 'total_sales':'Total Sales ($)'},
                  title="Top 5 Car Models by Sales")
    fig4.update_traces(marker_color="#99ccff")
    fig4.update_layout(xaxis_title="Car Model", yaxis_title="Total Sales ($)", hovermode="x unified")
    st.plotly_chart(fig4, use_container_width=True)

# ------------------- Advanced Analytics Section -------------------
st.header("Advanced Analytics")
st.subheader("Sales Breakdown by Region and Car Model")
st.write("""
This heatmap visualizes the sales performance of various car models across different dealer regions. The color gradient represents total sales volume in millions of dollars.
""")
sales_by_region_model = filtered_df.groupby(['Dealer_Region', 'Model']).agg(total_sales=('Price ($)', 'sum')).reset_index()
top_models = sales_by_region_model.groupby('Model').agg(total_sales=('total_sales', 'sum')).nlargest(10, 'total_sales').index
filtered_sales = sales_by_region_model[sales_by_region_model['Model'].isin(top_models)]
heatmap_data = filtered_sales.pivot_table(index='Dealer_Region', columns='Model', values='total_sales', aggfunc='sum')
heatmap_data_m = heatmap_data / 1_000_000  # Convert to millions for display
fig5 = px.imshow(heatmap_data_m,
                 text_auto=".1f",
                 aspect="auto",
                 color_continuous_scale="RdYlGn",
                 labels={"color": "Total Sales ($M)"},
                 title="Sales Breakdown by Region and Car Model")
st.plotly_chart(fig5, use_container_width=True)

# ------------------- Forecasting Section -------------------
st.header("Revenue Forecasting")
st.subheader("Revenue Forecasting for Regions")
st.write("""
This time series forecast predicts revenue trends for all regions over the next year based on historical data. By analyzing past sales performance and projecting future revenue, 
this forecast enables proactive decisions on inventory, staffing, and advertising. The forecast includes confidence intervals to indicate uncertainty.
""")
if not filtered_df.empty:
    region_data = filtered_df.groupby('Date').agg(total_sales=('Price ($)', 'sum')).reset_index()
    if len(region_data) > 30:
        region_data = region_data.rename(columns={'Date': 'ds', 'total_sales': 'y'})
        model = Prophet(changepoint_prior_scale=0.0015, seasonality_prior_scale=10)
        model.add_seasonality(name='monthly', period=30.5, fourier_order=3)
        model.add_seasonality(name='quarterly', period=91.25, fourier_order=5)
        model.add_seasonality(name='yearly', period=365.25, fourier_order=10)
        try:
            model.fit(region_data)
            future = model.make_future_dataframe(periods=730)
            forecast = model.predict(future)
            fig6 = plot_plotly(model, forecast)
            fig6.update_layout(title=f"Revenue Forecast for {region_filter} Region",
                               xaxis_title="YearQuarter", yaxis_title="Revenue ($)",
                               hovermode="x unified")
            st.plotly_chart(fig6, use_container_width=True)
        except Exception as e:
            st.error(f"An error occurred while forecasting: {str(e)}")
    else:
        st.warning("Not enough data points available to forecast for the selected region. Please select a different region.")
else:
    st.warning("No data available for the selected filters. Please choose different filter options.")

st.subheader("Revenue Forecast for 2024")
forecast_2024 = forecast[(forecast['ds'] >= '2024-01-01') & (forecast['ds'] <= '2024-12-31')]
forecast_2024['YearMonth'] = forecast_2024['ds'].dt.to_period('M')
forecast_2024['Month'] = forecast_2024['ds'].dt.strftime('%b')
monthly_forecast = forecast_2024.groupby('YearMonth').agg(revenue_forecast=('yhat', 'sum')).reset_index()
monthly_forecast['Month'] = monthly_forecast['YearMonth'].dt.strftime('%b')
monthly_forecast['Cumulative'] = monthly_forecast['revenue_forecast'].cumsum()
monthly_forecast['Revenue Forecast ($)'] = monthly_forecast['revenue_forecast'].apply(lambda x: f'${int(x):,}')
monthly_forecast['Cumulative Revenue ($)'] = monthly_forecast['Cumulative'].apply(lambda x: f'${int(x):,}')
fig7 = px.line(monthly_forecast, x=monthly_forecast['YearMonth'].dt.to_timestamp(), y='revenue_forecast',
               markers=True, title="Revenue Forecast for 2024",
               labels={'x': 'Month', 'revenue_forecast': 'Revenue ($)'}, color_discrete_sequence=["blue"])
fig7.add_traces(px.area(monthly_forecast, x=monthly_forecast['YearMonth'].dt.to_timestamp(), y='revenue_forecast',
                        color_discrete_sequence=["skyblue"]).data)
fig7.update_layout(xaxis_title="Month", yaxis_title="Revenue ($)", hovermode="x unified")
st.plotly_chart(fig7, use_container_width=True)
st.write("### Revenue Forecast Table for 2024")
st.table(monthly_forecast[['YearMonth', 'Month', 'Revenue Forecast ($)', 'Cumulative Revenue ($)']])

# ------------------- Key Takeaways -------------------
st.header("Key Takeaways")
st.markdown("""
- **Sales Trends:**  
  Analysis shows distinct regional differences and seasonal trends in car sales, indicating areas of strong performance and opportunities for improvement.
  
- **Forecasting Insights:**  
  The predictive model—enhanced with monthly, quarterly, and yearly seasonalities—forecasts revenue trends that can inform strategic decisions. The 2024 revenue forecast provides a granular, month-by-month outlook along with cumulative revenue projections.
  
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
