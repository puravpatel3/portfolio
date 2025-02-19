import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from prophet import Prophet
from prophet.plot import plot_plotly

# ------------------- Page Configuration -------------------
st.set_page_config(
    page_title="Retail Supply Chain Sales Analysis & Forecasting", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

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
This project leverages advanced data analytics, feature engineering, and forecasting techniques to address complex retail supply chain challenges.  
The dashboard highlights revenue drivers, operational efficiencies, and future trends, empowering proactive decision-making.
""")

# ------------------- Project Summary -------------------
st.header("Project Summary")
st.markdown("""
**Objective:**  
Analyze a comprehensive retail sales dataset—combining historical sales, shipping data, and product details—to derive actionable insights for inventory planning, logistics optimization, and profitability improvement. The integrated forecasting model anticipates future demand to help manage supply chain disruptions.

**Business Impact:**  
- **Operational Efficiency:** Identify bottlenecks and shipping delays to reduce costs.  
- **Inventory Management:** Forecast future sales to optimize stock levels and minimize waste.  
- **Revenue Optimization:** Pinpoint high-performing products and regions for strategic investments.
""")

# ------------------- Use Case -------------------
st.header("Use Case")
st.markdown("""
- **Demand Planning:** Use forecasting insights to adjust inventory levels and minimize stockouts.
- **Performance Benchmarking:** Analyze product categories and shipping modes to enhance service levels.
- **Strategic Decisions:** Leverage filterable historical and forecast data to guide supply chain investments.
""")

# ------------------- Key Technologies Used -------------------
st.header("Key Technologies Used")
st.markdown("""
- **Python 3.12:** Modern scripting environment  
- **Pandas & NumPy:** Data manipulation and numerical computations  
- **Plotly Express:** Interactive data visualizations with tooltips  
- **Streamlit:** Rapid development of executive-grade dashboards  
- **Prophet:** Time-series forecasting with confidence intervals and extra regressors
""")

# ------------------- Project Steps -------------------
st.header("Project Steps")
with st.expander("Step 1: Data Cleaning & Preprocessing"):
    st.markdown("""
    **Actions Taken:**  
    - Loaded the raw retail sales dataset from GitHub.
    - Converted date fields into standardized datetime objects and removed rows with missing critical values.
    - Retained all original fields for granular filtering and detailed analysis.

    **Why It’s Important:**  
    Ensures the reliability of downstream analytics and provides a robust basis for visualization and forecasting.
    """)
with st.expander("Step 2: Feature Engineering & Aggregation"):
    st.markdown("""
    **Actions Taken:**  
    - Engineered new features such as *Shipping Delay* (days between order and ship dates) and *Profit Margin*.
    - Extracted temporal components (Order Year, Month, Day) for time-series analysis.
    
    **Why It’s Important:**  
    Transforms raw data into meaningful metrics that reveal hidden patterns and support accurate forecasting.
    """)
with st.expander("Step 3: Exploratory Data Analysis (EDA) & Visualization"):
    st.markdown("""
    **Actions Taken:**  
    - Performed an in-depth EDA using interactive Plotly charts.
    - Visualized trends over time, compared product performance, and identified high-profit items.
    
    **Why It’s Important:**  
    Uncovers insights that drive strategic decision-making and validates the effectiveness of feature engineering.
    """)
with st.expander("Step 4: Forecasting & Advanced Analytics"):
    st.markdown("""
    **Actions Taken:**  
    - Integrated historical data with forecasted sales (via Prophet) to create a unified view.
    - Developed interactive visualizations to compare historical trends with forecasted performance.
    
    **Why It’s Important:**  
    Provides a forward-looking view of sales, allowing executives to anticipate demand shifts and adjust operational strategies.
    """)

# ------------------- Sidebar Filters -------------------
st.sidebar.header("Advanced Filters")

def get_filter_option(label, options):
    options = ["All"] + sorted(options)
    selection = st.sidebar.selectbox(label, options, index=0)
    return None if selection == "All" else selection

# Using select boxes with an "All" option to reduce clutter
selected_data_type = get_filter_option("Data Type", df["Data Type"].dropna().unique())
selected_category = get_filter_option("Product Category", df["Category"].dropna().unique())
selected_ship_mode = get_filter_option("Ship Mode", df["Ship Mode"].dropna().unique())
selected_segment = get_filter_option("Segment", df["Segment"].dropna().unique())
selected_sub_category = get_filter_option("Product Sub-Category", df["Sub-Category"].dropna().unique())

# Apply filters: if a filter returns None, include all values
filtered_df = df.copy()
if selected_data_type is not None:
    filtered_df = filtered_df[filtered_df["Data Type"] == selected_data_type]
if selected_category is not None:
    filtered_df = filtered_df[filtered_df["Category"] == selected_category]
if selected_ship_mode is not None:
    filtered_df = filtered_df[filtered_df["Ship Mode"] == selected_ship_mode]
if selected_segment is not None:
    filtered_df = filtered_df[filtered_df["Segment"] == selected_segment]
if selected_sub_category is not None:
    filtered_df = filtered_df[filtered_df["Sub-Category"] == selected_sub_category]

# ------------------- Dataset Preview & Field Descriptions -------------------
st.header("Dataset Preview")
st.markdown("Below is a preview of the filtered dataset:")
st.dataframe(filtered_df.head(10), height=250)

st.subheader("Field Descriptions")
st.markdown("""
- **Order ID:** Unique identifier for each order.
- **Order Date & Ship Date:** Dates when the order was placed and shipped.
- **Ship Mode:** Shipping method (e.g., Standard, Second Class).
- **Customer ID, Name, Segment:** Customer identifiers and market segments.
- **Product ID, Category, Sub-Category, Product Name:** Details of the product sold.
- **Sales, Quantity, Discount, Profit:** Key performance indicators.
- **Shipping Delay:** Computed days between order and ship dates.
- **Profit Margin:** Ratio of profit to sales.
- **Data Type:** Indicates if the row is historical or forecasted.
""")

# ------------------- Visualizations -------------------
st.header("Visualizations")

# Side-by-side visualizations
col1, col2 = st.columns(2)

with col1:
    st.subheader("Sales Trend Over Time")
    # Aggregate sales by Order Date (historical only)
    df_trend = filtered_df[filtered_df["Data Type"] == "Historical"].groupby("Order Date")["Sales"].sum().reset_index().sort_values("Order Date")
    fig_trend = px.line(df_trend, x="Order Date", y="Sales", markers=True, 
                        title="Daily Sales Trend", 
                        labels={"Sales": "Total Sales", "Order Date": "Date"},
                        hover_data={"Sales": ":$,.0f"})
    st.plotly_chart(fig_trend, use_container_width=True)
    
with col2:
    st.subheader("Top 10 Products by Sales")
    # Aggregate sales and profit by Product Name (historical only)
    df_products = filtered_df[filtered_df["Data Type"] == "Historical"].groupby("Product Name").agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    ).reset_index()
    df_products = df_products.sort_values("Sales", ascending=False).head(10)
    fig_products = px.bar(df_products, x="Product Name", y="Sales", 
                          title="Top 10 Products by Sales", 
                          labels={"Sales": "Total Sales", "Product Name": "Product"},
                          hover_data={"Sales": ":$,.0f", "Profit": ":$,.0f"})
    st.plotly_chart(fig_products, use_container_width=True)

st.markdown("---")

# Additional combined visualizations in a two-column layout
col3, col4 = st.columns(2)
with col3:
    st.subheader("Sales vs. Profit Scatter")
    # Scatter plot using historical data with Sales & Profit in tooltips
    fig_scatter = px.scatter(filtered_df[filtered_df["Data Type"]=="Historical"],
                             x="Sales", y="Profit",
                             color="Category",
                             hover_data={"Product Name": True, "Segment": True, "Sales": ":$,.0f", "Profit": ":$,.0f"},
                             title="Sales vs. Profit by Product Category",
                             labels={"Sales": "Sales", "Profit": "Profit"})
    st.plotly_chart(fig_scatter, use_container_width=True)
with col4:
    st.subheader("Sales by Ship Mode")
    df_ship = filtered_df[filtered_df["Data Type"]=="Historical"].groupby("Ship Mode")["Sales"].sum().reset_index()
    fig_ship = px.pie(df_ship, names="Ship Mode", values="Sales", 
                      title="Sales Distribution by Ship Mode",
                      hover_data={"Sales": ":$,.0f"})
    fig_ship.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_ship, use_container_width=True)

st.markdown("---")

# ------------------- US Heat Map & Top 10 States Table -------------------
st.header("US Performance by State")

col3, col4 = st.columns(2)
with col3:
    st.subheader("US Heat Map by Profit")
    # Aggregate Sales and Profit by State (historical only)
    state_profit = filtered_df[filtered_df["Data Type"]=="Historical"].groupby("State").agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    ).reset_index()

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

    fig_heat = px.choropleth(
        state_profit,
        locations="state_code",
        locationmode="USA-states",
        color="Profit",
        color_continuous_scale="Blues",
        scope="usa",
        labels={"Profit": "Total Profit"},
        hover_data={"Profit": ":$,.0f", "Sales": ":$,.0f"},
        title="Total Profit by State"
    )
    st.plotly_chart(fig_heat, use_container_width=True)

with col4:
    st.subheader("Top 10 States by Profit")
    state_summary = filtered_df[filtered_df["Data Type"]=="Historical"].groupby("State").agg(
        Sum_of_Sales=("Sales", "sum"),
        Sum_of_Profit=("Profit", "sum")
    ).reset_index().sort_values("Sum_of_Profit", ascending=False).head(10)
    state_summary = state_summary.style.format({"Sum_of_Sales": "${:,.0f}", "Sum_of_Profit": "${:,.0f}"})
    st.dataframe(state_summary)

st.markdown("---")

# ------------------- Forecasting / Advanced Analytics -------------------
st.header("Revenue Forecasting")
st.subheader("Revenue Forecasting for Regions")
st.markdown("""
This interactive time series forecast predicts revenue trends for a selected region over the next year based on historical data.  
By analyzing past sales performance and projecting future revenue (with confidence intervals), this forecast enables proactive decisions on inventory, staffing, and advertising.
""")
region_options = sorted(filtered_df["Region"].dropna().unique().tolist())
selected_region_forecast = st.selectbox("Select a Region for Forecasting", options=region_options)

# Filter historical data for the selected region
region_df = filtered_df[(filtered_df["Region"] == selected_region_forecast) & (filtered_df["Data Type"] == "Historical")]

# Always include the discount value as a regressor
region_data = region_df.groupby("Order Date").agg(
    total_sales=("Sales", "sum"),
    avg_discount=("Discount", "mean")
).reset_index()
region_data = region_data.rename(columns={"Order Date": "ds", "total_sales": "y", "avg_discount": "discount"})

if not region_data.empty and len(region_data) > 30:
    model = Prophet(changepoint_prior_scale=0.0015, seasonality_prior_scale=10)
    model.add_seasonality(name="monthly", period=30.5, fourier_order=3)
    model.add_seasonality(name="quarterly", period=91.25, fourier_order=5)
    model.add_seasonality(name="yearly", period=365.25, fourier_order=10)
    model.add_regressor("discount")
    try:
        model.fit(region_data)
        future = model.make_future_dataframe(periods=365)
        # For future dates, fill discount with the average discount from historical data
        future["discount"] = region_data["discount"].mean()
        forecast = model.predict(future)
        fig_forecast = plot_plotly(model, forecast)
        fig_forecast.update_layout(
            title=f"Revenue Forecast for {selected_region_forecast} Region",
            xaxis_title="Date", 
            yaxis_title="Revenue ($)",
            yaxis_tickformat="$,",
            hovermode="x unified"
        )
        st.plotly_chart(fig_forecast, use_container_width=True)
    except Exception as e:
        st.error(f"An error occurred while forecasting: {str(e)}")
else:
    st.warning("Not enough data points available to forecast for the selected region. Please select a different region.")

# ------------------- Key Takeaways -------------------
st.header("Key Takeaways")
st.markdown("""
- **Data-Driven Insights:** Advanced filtering and interactive visualizations uncover critical trends in sales, product performance, and operational efficiency.
- **Forecasting Value:** Integrating historical and forecast data provides a forward-looking perspective to support proactive supply chain management.
- **Actionable Intelligence:** Detailed metrics like shipping delays and profit margins identify clear areas for operational optimization.
""")

# ------------------- Next Steps -------------------
st.header("Next Steps")
st.markdown("""
- **Enhance Forecasting Models:** Evaluate advanced time-series models (e.g., further Prophet enhancements, LSTM) for improved accuracy.
- **Expand Filter Options:** Consider additional filters (e.g., Retail Sales People, Order Date Range) for deeper segmentation.
- **Integrate Real-Time Data:** Connect the dashboard to live data feeds for continuous operational insights.
- **Dashboard Refinement:** Further streamline visualizations and interactivity to support executive-level decision making.
""")
