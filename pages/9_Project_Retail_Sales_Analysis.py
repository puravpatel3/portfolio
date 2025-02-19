import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration
st.set_page_config(
    page_title="Retail Supply Chain Sales Analysis & Forecasting",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------------------------------------
# Helper Function: Load Data
# --------------------------------------------------------------------------------
@st.cache_data
def load_data(url):
    # The URL below is the "raw" version of your GitHub file.
    df = pd.read_csv(url, parse_dates=['Order Date'])
    return df

# --------------------------------------------------------------------------------
# Data URL (raw GitHub URL)
# --------------------------------------------------------------------------------
data_url = "https://raw.githubusercontent.com/puravpatel3/portfolio/55f52c9a729c11496dbcc4a0ff3db811ca2aedb6/files/retail_sales_data_final.csv"
df = load_data(data_url)

# --------------------------------------------------------------------------------
# Page Title and Introduction
# --------------------------------------------------------------------------------
st.title("Retail Supply Chain Sales Analysis & Forecasting")
st.markdown("""
Welcome to the Retail Supply Chain Sales Analysis & Forecasting project.  
This project leverages advanced data analytics and forecasting techniques to address key challenges in the retail supply chain—from understanding revenue drivers and operational inefficiencies to predicting future sales trends.  
""")

# --------------------------------------------------------------------------------
# Project Summary
# --------------------------------------------------------------------------------
st.header("Project Summary")
st.markdown("""
This project analyzes a comprehensive retail sales dataset to provide insights into sales performance, product profitability, and operational efficiency.  
Key objectives include:
- **Forecasting Sales:** Using time-series analysis (ARIMA) to predict future sales.
- **Operational Insights:** Evaluating metrics such as shipping delays and profit margins.
- **Strategic Recommendations:** Identifying key revenue drivers and areas for supply chain improvements.
""")

# --------------------------------------------------------------------------------
# Use Case
# --------------------------------------------------------------------------------
st.header("Use Case")
st.markdown("""
**Practical Applications:**
- **Inventory & Demand Planning:** Accurate forecasting aids in optimizing inventory levels.
- **Process Optimization:** Insights into shipping delays and profitability help identify operational gaps.
- **Strategic Focus:** Identifying top-selling and high-margin product categories enables targeted improvements.
""")

# --------------------------------------------------------------------------------
# Key Technologies Used
# --------------------------------------------------------------------------------
st.header("Key Technologies Used")
st.markdown("""
- **Python 3.12** for scripting and analysis
- **Pandas & NumPy** for data manipulation
- **Matplotlib & Seaborn** for data visualization
- **Statsmodels (ARIMA)** for time-series forecasting
- **Streamlit** for building interactive dashboards
""")

# --------------------------------------------------------------------------------
# Project Steps (using Expanders)
# --------------------------------------------------------------------------------
st.header("Project Steps")
with st.expander("Step 1: Data Cleaning & Preparation"):
    st.markdown("""
    - Loaded raw data from a CSV file hosted on GitHub.
    - Converted date columns and handled missing values.
    - Retained all original columns for rich filtering in the dashboard.
    """)
with st.expander("Step 2: Feature Engineering & Aggregation"):
    st.markdown("""
    - Created engineered features such as *Shipping Delay* and *Profit Margin*.
    - Extracted date components (Year, Month, Day) to support temporal analysis.
    """)
with st.expander("Step 3: Exploratory Data Analysis & Visualization"):
    st.markdown("""
    - Analyzed sales performance by product category.
    - Visualized the relationship between Sales and Profit to identify high-value items.
    """)
with st.expander("Step 4: Forecasting & Advanced Analytics"):
    st.markdown("""
    - Developed an ARIMA model to forecast sales for the next 30 days.
    - Merged historical and forecast data for a unified view.
    """)

# --------------------------------------------------------------------------------
# Sidebar Filters
# --------------------------------------------------------------------------------
st.sidebar.header("Filters")
data_type_options = st.sidebar.multiselect("Select Data Type", options=df["Data Type"].unique(), default=df["Data Type"].unique())
category_options = st.sidebar.multiselect("Select Product Category", options=sorted(df["Category"].dropna().unique()), default=sorted(df["Category"].dropna().unique()))
# Additional filters can be added similarly...
filtered_df = df[(df["Data Type"].isin(data_type_options)) & (df["Category"].isin(category_options))]

# --------------------------------------------------------------------------------
# Dataset Preview
# --------------------------------------------------------------------------------
st.header("Dataset Preview")
st.markdown("Below is a preview of the dataset (filtered as per your selections):")
st.dataframe(filtered_df.head(10))

# --------------------------------------------------------------------------------
# Visualizations
# --------------------------------------------------------------------------------
st.header("Visualizations")

# Create two side-by-side columns for visualizations
col1, col2 = st.columns(2)

with col1:
    st.subheader("Total Sales by Product Category")
    # Using only historical data for aggregation
    df_hist = df[df["Data Type"] == "Historical"]
    sales_by_category = df_hist.groupby("Category")["Sales"].sum().sort_values(ascending=False).reset_index()
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(x="Category", y="Sales", data=sales_by_category, palette="viridis", ax=ax)
    ax.set_title("Total Sales by Product Category")
    ax.set_xlabel("Product Category")
    ax.set_ylabel("Total Sales")
    plt.xticks(rotation=45)
    st.pyplot(fig)
    
with col2:
    st.subheader("Sales vs. Profit Scatter Plot")
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    sns.scatterplot(data=df_hist, x="Sales", y="Profit", hue="Category", alpha=0.7, ax=ax2)
    ax2.set_title("Sales vs. Profit")
    ax2.set_xlabel("Sales")
    ax2.set_ylabel("Profit")
    st.pyplot(fig2)

# --------------------------------------------------------------------------------
# Forecasting / Advanced Analytics
# --------------------------------------------------------------------------------
st.header("Forecasting / Advanced Analytics")
st.markdown("""
The chart below displays historical sales alongside forecasted sales for the next 30 days.  
Forecasted entries are labeled as **Forecast** in the *Data Type* column.
""")

# Create a line plot for forecasting
fig3, ax3 = plt.subplots(figsize=(12, 6))
# Separate historical and forecast data and sort by Order Date
df_hist_line = df[df["Data Type"] == "Historical"].sort_values("Order Date")
df_forecast_line = df[df["Data Type"] == "Forecast"].sort_values("Order Date")

ax3.plot(df_hist_line["Order Date"], df_hist_line["Sales"], label="Historical Sales", color="blue")
ax3.plot(df_forecast_line["Order Date"], df_forecast_line["Sales"], label="Forecasted Sales", linestyle="--", color="red")
ax3.set_title("Sales Forecasting")
ax3.set_xlabel("Order Date")
ax3.set_ylabel("Sales")
ax3.legend()
st.pyplot(fig3)

# --------------------------------------------------------------------------------
# Key Takeaways
# --------------------------------------------------------------------------------
st.header("Key Takeaways")
st.markdown("""
- **Revenue Drivers:** The analysis clearly identifies the product categories that are the primary revenue drivers.
- **Forecasting Insights:** The ARIMA-based forecast provides a forward-looking view that can aid in proactive inventory and supply chain planning.
- **Operational Efficiency:** Metrics like shipping delays and profit margins highlight opportunities to optimize operations and enhance customer satisfaction.
""")

# --------------------------------------------------------------------------------
# Next Steps
# --------------------------------------------------------------------------------
st.header("Next Steps")
st.markdown("""
- **Model Enhancement:** Explore advanced forecasting techniques (e.g., Prophet, LSTM) to further improve prediction accuracy.
- **Deeper Analysis:** Incorporate additional dimensions such as customer segmentation and geographic performance for richer insights.
- **Dashboard Interactivity:** Expand interactive filtering and drill-down capabilities to allow more granular analysis.
- **Operational Metrics:** Integrate KPIs like delivery times and order fulfillment accuracy to better align with supply chain optimization goals.
""")

st.markdown("### Thank you for exploring this Retail Supply Chain Sales Analysis & Forecasting project!")
