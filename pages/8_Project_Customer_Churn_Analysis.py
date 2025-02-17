import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# ------------------- Page Configuration -------------------
st.set_page_config(page_title="Telco Customer Churn Analysis", layout="wide")

# ------------------- Project Title -------------------
st.title("Telco Customer Churn Analysis")

# ------------------- Project Summary -------------------
st.header("Project Summary")
st.markdown("""
**Objective:**  
The goal of this project is to analyze customer churn in the telecommunications industry and develop a robust predictive model to identify at-risk customers. I evaluated several models using 5-fold cross-validation and selected Logistic Regression, which achieved a prediction rate (accuracy) of approximately 80%. This model enables the business to anticipate churn, facilitating targeted retention strategies and proactive customer engagement.

**Dataset:**  
An enriched Telco Customer Churn dataset is utilized, containing both original customer data and machine learning predictions. The dataset is hosted on GitHub for seamless integration and deployment.

**Business Impact:**  
Reducing churn is vital for revenue maximization. By accurately identifying customers at risk of leaving, the company can launch targeted interventions, reduce revenue loss, and improve overall customer satisfaction and loyalty. This predictive model serves as a strategic tool to drive data-informed retention efforts.
""")

# ------------------- Use Case -------------------
st.header("Use Case")
st.markdown("""
- **Customer Retention:** Identify and engage customers likely to churn through targeted retention programs.
- **Revenue Maximization:** Prevent revenue loss by addressing churn proactively with personalized offers.
- **Operational Efficiency:** Enhance customer service and marketing strategies by leveraging data-driven insights.
""")

# ------------------- Key Technologies Used -------------------
st.header("Key Technologies Used")
st.markdown("""
- **Pandas:** Data manipulation and analysis  
- **NumPy:** Numerical computations  
- **Scikit-learn:** Machine learning and model evaluation  
- **Plotly Express:** Interactive and dynamic data visualization  
- **Streamlit:** Interactive web app development  
- **GitHub:** Version control and cloud deployment
""")

# ------------------- Project Steps -------------------
st.header("Project Steps")
with st.expander("Step 1: Data Cleaning & Preprocessing"):
    st.markdown("""
    **Actions Taken:**  
    - I cleaned the raw dataset by removing missing values and extraneous characters (e.g., in the TotalCharges field).  
    - I standardized column names and formatted numeric fields.
    - I engineered new features such as `tenure_group` (to segment customers by their duration with the company) and `AvgCharges` (average monthly charge derived from TotalCharges/tenure).

    **Why It’s Important:**  
    Proper data cleaning and feature engineering ensure that the dataset is reliable and insightful, forming a solid foundation for accurate predictive modeling.
    """)
with st.expander("Step 2: Exploratory Data Analysis (EDA)"):
    st.markdown("""
    **Actions Taken:**  
    - I performed statistical summaries, correlation analyses, and visualizations to understand data distributions and relationships.  
    - I identified key trends and potential issues in the data, such as the impact of tenure and monthly charges on churn.

    **Why It’s Important:**  
    Exploratory data analysis uncovers hidden patterns and informs subsequent feature selection and model development, ensuring that the predictive model targets the most influential factors.
    """)
with st.expander("Step 3: Modeling"):
    st.markdown("""
    **Actions Taken:**  
    - I evaluated multiple machine learning models (Logistic Regression, Decision Tree, and Random Forest) using 5-fold cross-validation.
    - I selected Logistic Regression as the best model based on its performance (approximately 80% accuracy).
    - I integrated the model’s predictions back into the dataset.

    **Why It’s Important:**  
    The modeling step provides a data-driven method to predict customer churn, which is critical for identifying at-risk customers and deploying effective retention strategies.
    """)
with st.expander("Step 4: Deployment & Dashboard"):
    st.markdown("""
    **Actions Taken:**  
    - I developed an interactive Streamlit dashboard that dynamically visualizes key metrics and model predictions.
    - I enabled filtering (e.g., by tenure group) to allow stakeholders to explore the data in depth.

    **Why It’s Important:**  
    An interactive dashboard facilitates clear communication of insights and supports executive-level decision-making by providing real-time, actionable information.
    """)

# ------------------- Dataset Section -------------------
st.header("Dataset")
st.markdown("The final dataset, which includes the model predictions, is hosted on GitHub. Access it via the link below:")
dataset_url = "https://raw.githubusercontent.com/puravpatel3/portfolio/3d0ea6e6edb91da1cc432498f5bb064717a165b9/files/telco_customer_churn_with_predictions_final.csv"
st.markdown(f"[Telco Customer Churn Dataset]({dataset_url})")

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

df = load_data(dataset_url)

st.write("### Dataset Preview")
st.dataframe(df.head(), height=250)

st.markdown("""
**Field Descriptions for Model Input Features:**

- **tenure:** Number of months the customer has been with the company.
- **MonthlyCharges:** The monthly fee charged to the customer.
- **TotalCharges:** The total amount charged to the customer over their tenure.
- **AvgCharges:** The average monthly charge (calculated as TotalCharges divided by tenure).
- **SeniorCitizen:** Binary indicator (0 or 1) showing if the customer is a senior citizen.
- **Partner:** Indicates if the customer has a partner.
- **Dependents:** Indicates if the customer has dependents.
- **MultipleLines:** Specifies whether the customer has multiple phone lines.
- **InternetService:** Type of internet service provided (e.g., DSL, Fiber optic).
- **StreamingTV:** Indicates if the customer subscribes to streaming TV services.
- **StreamingMovies:** Indicates if the customer subscribes to streaming movie services.
- **Contract:** Type of contract (e.g., Month-to-month, One year, Two year).
""")

# ------------------- Data Visualizations -------------------
st.header("Data Visualizations")

# Define the desired order and labels for tenure groups
tenure_order = ["0-12 Months", "12-24 Months", "24-48 Months", "48-60 Months", "60+ Months"]

if 'tenure_group' not in df.columns or df['tenure_group'].dtype.name != 'category':
    df['tenure_group'] = pd.cut(
        df['tenure'],
        bins=[0, 12, 24, 48, 60, df['tenure'].max()],
        labels=tenure_order
    )
else:
    df['tenure_group'] = df['tenure_group'].cat.rename_categories(tenure_order)

# Interactive Filter: Select Tenure Group
selected_tenure = st.selectbox("Select Tenure Group for Analysis", tenure_order)
filtered_df = df[df['tenure_group'] == selected_tenure]

# Define a consistent, bolder yet still pastel-like palette for churn:
churn_palette = {"Yes": "#ff9999", "No": "#99ccff"}

# Place the Churn Distribution and Charges Comparison charts side by side
col1, col2 = st.columns(2)

with col1:
    st.subheader("Churn Distribution")
    # Compute counts by churn status
    churn_counts = filtered_df["Churn"].value_counts().reset_index()
    churn_counts.columns = ["Churn", "Count"]
    fig1 = px.bar(churn_counts, x="Churn", y="Count", 
                  color="Churn", 
                  color_discrete_map=churn_palette,
                  hover_data={"Count": ":,d"},
                  title="Churn Count in Selected Tenure Group")
    fig1.update_layout(xaxis_title="Churn", yaxis_title="Number of Customers", hovermode="x unified")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Charges Comparison by Predicted Churn")
    # Convert Predicted_Churn to string labels for consistency
    filtered_df['Predicted_Churn_str'] = filtered_df['Predicted_Churn'].replace({0: "No", 1: "Yes"})
    fig2 = px.scatter(filtered_df, x="MonthlyCharges", y="TotalCharges", 
                      color="Predicted_Churn_str", 
                      color_discrete_map=churn_palette,
                      title="Monthly Charges vs. Total Charges",
                      hover_data={"MonthlyCharges": ":$,.2f", "TotalCharges": ":$,.2f"})
    fig2.update_layout(xaxis_title="Monthly Charges ($)", yaxis_title="Total Charges ($)", hovermode="closest")
    st.plotly_chart(fig2, use_container_width=True)

# Visualization 3: Overall Churn Distribution by Tenure Group (Grouped Bars)
st.subheader("Overall Churn Distribution by Tenure Group")
overall_counts = df.groupby(["tenure_group", "Churn"]).size().reset_index(name="Count")
fig3 = px.bar(overall_counts, x="tenure_group", y="Count", color="Churn",
              color_discrete_map=churn_palette,
              title="Churn Count by Tenure Group",
              hover_data={"Count": ":,d"},
              barmode="group")
fig3.update_layout(xaxis_title="Tenure Group", yaxis_title="Number of Customers", hovermode="x unified")
st.plotly_chart(fig3, use_container_width=True)

# ------------------- Key Takeaways -------------------
st.header("Key Takeaways")
st.markdown("""
- **Insightful Trends:**  
  Analysis reveals that customer churn is significantly influenced by tenure, monthly charges, and contract types.
- **Model Performance:**  
  The best-performing model (Logistic Regression) achieved approximately 80% accuracy, serving as a strong baseline for predicting churn.
- **Actionable Strategies:**  
  By identifying at-risk customers, targeted retention campaigns can be implemented and resource allocation optimized to improve customer loyalty and revenue.
""")

# ------------------- Next Steps -------------------
st.header("Next Steps")
st.markdown("""
- **Model Enhancement:**  
  - Perform further feature engineering (e.g., interaction terms, polynomial features).  
  - Utilize hyperparameter tuning and experiment with advanced models (e.g., Gradient Boosting, XGBoost).
- **Operational Deployment:**  
  - Integrate the dashboard with real-time data feeds.  
  - Optimize decision thresholds to improve the recall rate for churn prediction.
- **Data Enrichment:**  
  - Incorporate additional customer data (demographics, usage patterns) to enhance predictive accuracy.
""")
