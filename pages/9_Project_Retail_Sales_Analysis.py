import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# For forecasting with Prophet
from prophet import Prophet
from prophet.plot import plot_plotly

# ------------------- Page Configuration -------------------
st.set_page_config(page_title="Retail Supply Chain Sales Analysis & Forecasting", layout="wide", initial_sidebar_state="expanded")

# ------------------- Helper Functions -------------------
@st.cache_data
def load_data(url):
    df = pd.read_csv(url, parse_dates=['Order Date', 'Ship Date'])
    return df

# ------------------- Data Loading -------------------
data_url = "https://raw.githubusercontent.com/puravpatel3/portfolio/55f52c9a729c11496dbcc4a0ff3db811ca2aedb6/files/retail_sales_data_final.csv"
df = load_data(data_url)

# ------------------- Page Title & Intro -------------------
st.title("Retail Supply Chain Sales Analysis & Forecasting")
st.markdown("""
Welcome to the Retail Supply Chain Sales Analysis & Forecasting project.  
This project leverages advanced data analytics, feature engineering, and forecasting techniques to solve complex retail supply chain challenges.  
The analysis highlights revenue drivers, operational efficiencies, and future trends to empower proactive decision-making.
""")

# ------------------- Project Summary -------------------
st.header("Project Summary")
st.markdown("""
**Objective:**  
This project analyzes a comprehensive retail sales dataset—incorporating historical sales, shipping data, and product-level details—to derive actionable insights that improve inventory planning, streamline logistics, and boost overall profitability. The integrated forecasting model anticipates future demand, enabling a proactive approach to managing supply chain disruptions.

**Business Impact:**  
- **Enhanced Operational Efficiency:** Identify bottlenecks and shipping delays to reduce costs.  
- **Strategic Inventory Management:** Forecast future sales to optimize stock levels and reduce waste.  
- **Revenue Optimization:** Understand product performance and profitability for better market positioning.
""")

# ------------------- Use Case -------------------
st.header("Use Case")
st.markdown("""
- **Demand Planning:** Leverage forecasting insights to fine-tune inventory levels and minimize stockouts.
- **Performance Benchmarking:** Analyze product categories, shipping modes, and regional trends to improve service levels.
- **Strategic Decision Making:** Utilize granular, filterable views of historical and forecast data to guide investments in supply chain improvements.
""")

# ------------------- Key Technologies Used -------------------
st.header("Key Technologies Used")
st.markdown("""
- **Python 3.12:** Modern scripting environment  
- **Pandas & NumPy:** Data manipulation and numerical computations  
- **Plotly Express:** Dynamic, interactive data visualizations with tooltips  
- **Streamlit:** Rapid development of interactive, executive-grade dashboards  
- **Prophet:** Time-series forecasting with confidence intervals
""")

# ------------------- Project Steps -------------------
st.header("Project Steps")
with st.expander("Step 1: Data Cleaning & Preprocessing"):
    st.markdown("""
    **Actions Taken:**  
    - Loaded the raw retail sales dataset from GitHub.
    - Converted date fields into standardized datetime objects and removed rows with missing critical values.
    - Retained all original fields to support granular filtering and detailed analysis.

    **Why It’s Important:**  
    Proper cleaning and standardization ensure the reliability of downstream analytics and provide a robust basis for both visualization and forecasting.
    """)
with st.expander("Step 2: Feature Engineering & Aggregation"):
    st.markdown("""
    **Actions Taken:**  
    - Engineered new features such as *Shipping Delay* (the days between order and ship dates) and *Profit Margin*.
    - Extracted temporal components (Order Year, Month, Day) to enable time-series analysis.
    
    **Why It’s Important:**  
    Feature engineering transforms raw data into meaningful metrics that reveal hidden patterns and support more accurate forecasting.
    """)
with st.expander("Step 3: Exploratory Data Analysis (EDA) & Visualization"):
    st.markdown("""
    **Actions Taken:**  
    - Conducted an in-depth EDA using interactive Plotly charts.
    - Visualized trends over time, compared product-level performance, and identified high-profit items.
    
    **Why It’s Important:**  
    EDA uncovers insights that drive strategic decision-making and validates the effectiveness of the feature engineering process.
    """)
with st.expander("Step 4: Forecasting & Advanced Analytics"):
    st.markdown("""
    **Actions Taken:**  
    - Integrated historical data with forecasted sales (using a Prophet model) to create a unified view.
    - Developed interactive visualizations to compare historical trends with forecasted performance.
    
    **Why It’s Important:**  
    Forecasting provides a forward-looking view of sales, allowing executives to anticipate demand shifts and adjust operational strategies accordingly.
    """)

# ------------------- Sidebar Filters -------------------
st.sidebar.header("Advanced Filters")

# Filter for Data Type (Historical vs Forecast)
data_type_options = sorted(df["Data Type"].dropna().unique().tolist())
selected_data_type = st.sidebar.multiselect("Data Type", options=data_type_options, default=data_type_options)

# Filter for Product Category
product_categories = sorted(df["Category"].dropna().unique().tolist())
selected_category = st.sidebar.multiselect("Product Category", options=product_categories, default=product_categories)

# Filter for Ship Mode
ship_modes = sorted(df["Ship Mode"].dropna().unique().tolist())
selected_ship_mode = st.sidebar.multiselect("Ship Mode", options=ship_modes, default=ship_modes)

# Filter for Segment
segments = sorted(df["Segment"].dropna().unique().tolist())
selected_segment = st.sidebar.multiselect("Segment", options=segments, default=segments)

# Filter for Product Sub-Category
sub_categories = sorted(df["Sub-Category"].dropna().unique().tolist())
selected_sub_category = st.sidebar.multiselect("Product Sub-Category", options=sub_categories, default=sub_categories)

# Apply filters
filtered_df = df[
    (df["Data Type"].isin(selected_data_type)) &
    (df["Category"].isin(selected_category)) &
    (df["Ship Mode"].isin(selected_ship_mode)) &
    (df["Segment"].isin(selected_segment)) &
    (df["Sub-Category"].isin(selected_sub_category))
]

# ------------------- Dataset Preview & Field Descriptions -------------------
st.header("Dataset Preview")
st.markdown("Below is a preview of the filtered dataset:")
st.dataframe(filtered_df.head(10), height=250)

st.subheader("Field Descriptions")
st.markdown("""
- **Order ID:** Unique identifier for each order.
- **Order Date & Ship Date:** Dates when the order was placed and shipped.
- **Ship Mode:** Shipping method (e.g., Standard, Second Class).
- **Customer ID, Name, Segment:** Customer identifiers and their market segments.
- **Product ID, Category, Sub-Category, Product Name:** Details of the product sold.
- **Sales, Quantity, Discount, Profit:** Key performance indicators.
- **Shipping Delay:** Computed days between order and ship dates.
- **Profit Margin:** Ratio of profit to sales.
- **Data Type:** Indicates if the row is from historical data or forecasted.
""")

# ------------------- Visualizations -------------------
st.header("Visualizations")

# Side-by-side visualizations
col1, col2 = st.columns(2)

with col1:
    st.subheader("Sales Trend Over Time")
    # Aggregate sales by Order Date (historical only)
    df_trend = filtered_df[filtered_df["Data Type"] == "Historical"].groupby("Order Date")["Sales"].sum().reset_index()
    fig_trend = px.line(df_trend, x="Order Date", y="Sales", markers=True, 
                        title="Daily Sales Trend", 
                        labels={"Sales": "Total Sales", "Order Date": "Date"},
                        hover_data={"Sales": ":,.2f"})
    st.plotly_chart(fig_trend, use_container_width=True)
    
with col2:
    st.subheader("Top 10 Products by Sales")
    # Aggregate sales by Product Name (historical only)
    df_products = filtered_df[filtered_df["Data Type"] == "Historical"].groupby("Product Name")["Sales"].sum().reset_index()
    df_products = df_products.sort_values("Sales", ascending=False).head(10)
    fig_products = px.bar(df_products, x="Product Name", y="Sales", 
                          title="Top 10 Products by Sales", 
                          labels={"Sales": "Total Sales", "Product Name": "Product"},
                          hover_data={"Sales": ":,.2f"})
    st.plotly_chart(fig_products, use_container_width=True)

st.markdown("---")

# Additional combined visualizations in a two-column layout
col3, col4 = st.columns(2)
with col3:
    st.subheader("Sales vs. Profit Scatter")
    # Scatter plot using historical data
    fig_scatter = px.scatter(filtered_df[filtered_df["Data Type"]=="Historical"],
                             x="Sales", y="Profit",
                             color="Category",
                             hover_data=["Product Name", "Segment"],
                             title="Sales vs. Profit by Product Category",
                             labels={"Sales": "Sales", "Profit": "Profit"})
    st.plotly_chart(fig_scatter, use_container_width=True)
with col4:
    st.subheader("Sales by Ship Mode")
    df_ship = filtered_df[filtered_df["Data Type"]=="Historical"].groupby("Ship Mode")["Sales"].sum().reset_index()
    fig_ship = px.pie(df_ship, names="Ship Mode", values="Sales", 
                      title="Sales Distribution by Ship Mode",
                      hover_data={"Sales": ":,.2f"})
    fig_ship.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_ship, use_container_width=True)

st.markdown("---")

# ------------------- US Heat Map by Profit -------------------
st.header("US Heat Map by Profit")
st.markdown("The map below aggregates profit by state and displays a heat map of the US. Higher profit states are shown in darker colors.")

# Aggregate Profit by State using historical data only
state_profit = filtered_df[filtered_df["Data Type"]=="Historical"].groupby("State")["Profit"].sum().reset_index()

# Mapping from full state names to USPS abbreviations
us_state_abbrev = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
    'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'District of Columbia': 'DC',
    'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL',
    'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
    'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN',
    'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV',
    'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY',
    'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK',
    'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
    'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT',
    'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI',
    'Wyoming': 'WY'
}
state_profit['state_code'] = state_profit['State'].map(us_state_abbrev)

fig_heat = px.choropleth(state_profit,
                         locations="state_code",
                         locationmode="USA-states",
                         color="Profit",
                         color_continuous_scale="Blues",
                         scope="usa",
                         labels={"Profit": "Total Profit"},
                         title="Total Profit by State")
st.plotly_chart(fig_heat, use_container_width=True)

# ------------------- Forecasting / Advanced Analytics -------------------
st.header("Revenue Forecasting")
st.subheader("Revenue Forecasting for Regions")
st.markdown("""
This interactive time series forecast predicts revenue trends for a selected region over the next year based on historical data.  
By analyzing past sales performance and projecting future revenue (with confidence intervals), this forecast enables proactive decisions on inventory, staffing, and advertising.
""")

# Select a region for forecasting using a dropdown
region_options = sorted(filtered_df["Region"].dropna().unique().tolist())
selected_region_forecast = st.selectbox("Select a Region for Forecasting", options=region_options)

# Filter data for the selected region (historical only)
region_df = filtered_df[(filtered_df["Region"] == selected_region_forecast) & (filtered_df["Data Type"] == "Historical")]

# Group by Order Date and sum Sales
region_data = region_df.groupby("Order Date").agg(total_sales=("Sales", "sum")).reset_index()

if not region_data.empty and len(region_data) > 30:
    # Prepare data for Prophet
    region_data = region_data.rename(columns={"Order Date": "ds", "total_sales": "y"})
    model = Prophet(changepoint_prior_scale=0.0015, seasonality_prior_scale=10)
    model.add_seasonality(name="monthly", period=30.5, fourier_order=3)
    model.add_seasonality(name="quarterly", period=91.25, fourier_order=5)
    model.add_seasonality(name="yearly", period=365.25, fourier_order=10)
    try:
        model.fit(region_data)
        future = model.make_future_dataframe(periods=365)
        forecast = model.predict(future)
        fig_forecast = plot_plotly(model, forecast)
        fig_forecast.update_layout(title=f"Revenue Forecast for {selected_region_forecast} Region",
                                     xaxis_title="Date", yaxis_title="Revenue ($)",
                                     hovermode="x unified")
        st.plotly_chart(fig_forecast, use_container_width=True)
    except Exception as e:
        st.error(f"An error occurred while forecasting: {str(e)}")
else:
    st.warning("Not enough data points available to forecast for the selected region. Please select a different region.")

# ------------------- Key Takeaways -------------------
st.header("Key Takeaways")
st.markdown("""
- **Data-Driven Insights:** Detailed filtering and interactive visualizations uncover critical trends in sales, product performance, and operational efficiency.
- **Forecasting Value:** Integrating historical and forecast data provides a forward-looking perspective to support proactive supply chain management.
- **Actionable Intelligence:** By examining metrics like shipping delays and profit margins, the project identifies clear areas for operational optimization.
""")

# ------------------- Next Steps -------------------
st.header("Next Steps")
st.markdown("""
- **Enhance Forecasting Models:** Evaluate advanced time-series models (e.g., Prophet enhancements, LSTM) for improved accuracy.
- **Expand Filter Options:** Integrate additional filters (e.g., Retail Sales People, Order Date Range) for deeper segmentation.
- **Integrate Real-Time Data:** Connect the dashboard to live data feeds for continuous operational insights.
- **Dashboard Refinement:** Further streamline visualizations and interactivity to support executive-level decision making.
""")

st.markdown("### Thank you for exploring this Retail Supply Chain Sales Analysis & Forecasting project!")
