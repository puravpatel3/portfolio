import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------- Page Configuration -------------------
st.set_page_config(page_title="Telco Customer Churn Analysis Portfolio", layout="wide")

# ------------------- Project Title -------------------
st.title("Telco Customer Churn Analysis Portfolio Project")

# ------------------- Project Summary -------------------
st.header("Project Summary")
st.markdown("""
**Objective:**  
Analyze customer churn in the telecommunications industry to identify at-risk customers and deploy targeted retention strategies, thereby maximizing revenue.

**Dataset:**  
Telco Customer Churn dataset augmented with machine learning predictions.  
*Note: The final dataset is hosted on GitHub for seamless deployment.*

**Business Impact:**  
By understanding key drivers of churn, businesses can proactively address customer attrition, optimize marketing spend, and enhance overall customer retention.
""")

# ------------------- Use Case -------------------
st.header("Use Case")
st.markdown("""
- **Customer Retention:** Identify customers at risk of churning and engage them with targeted retention efforts.
- **Revenue Maximization:** Focus on high-value customers to reduce revenue loss through proactive interventions.
- **Operational Efficiency:** Use data-driven insights to refine customer service and marketing strategies.
""")

# ------------------- Key Technologies Used -------------------
st.header("Key Technologies Used")
st.markdown("""
- **Programming Language:** Python 3.12  
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Streamlit  
- **Tools:** GitHub for version control and deployment on Streamlit Cloud
""")

# ------------------- Project Steps -------------------
st.header("Project Steps")
with st.expander("Click to view Project Steps"):
    st.markdown("""
    1. **Data Cleaning & Preprocessing:**  
       - Clean and transform raw data (handle missing values, remove extraneous characters, etc.)  
       - Engineer new features (e.g., tenure groups, average charges).
    2. **Exploratory Data Analysis (EDA):**  
       - Visualize data distributions, correlations, and trends.
    3. **Modeling:**  
       - Develop and evaluate machine learning models to predict customer churn.
    4. **Deployment:**  
       - Build an interactive dashboard to present findings and enable dynamic data exploration.
    """)

# ------------------- Dataset Reference -------------------
st.header("Dataset")
st.markdown("The final dataset with model predictions is hosted on GitHub. You can access it via the link below:")
dataset_url = "https://raw.githubusercontent.com/puravpatel3/portfolio/3d0ea6e6edb91da1cc432498f5bb064717a165b9/files/telco_customer_churn_with_predictions_final.csv"
st.markdown(f"[Telco Customer Churn Dataset]({dataset_url})")

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

df = load_data(dataset_url)

st.write("### Dataset Preview")
st.write(df.head())

# ------------------- Data Visualizations -------------------
st.header("Data Visualizations")

# Create a 'tenure_group' if it does not exist
if 'tenure_group' not in df.columns:
    df['tenure_group'] = pd.cut(df['tenure'], bins=[0, 12, 24, 48, 60, df['tenure'].max()],
                                labels=['0-12', '12-24', '24-48', '48-60', '60+'])

# Interactive Filter: Select Tenure Group
selected_tenure = st.selectbox("Select Tenure Group for Analysis", sorted(df['tenure_group'].unique()))
filtered_df = df[df['tenure_group'] == selected_tenure]

# Side-by-Side Visualizations
col1, col2 = st.columns(2)

with col1:
    st.subheader("Churn Distribution")
    fig1, ax1 = plt.subplots()
    sns.countplot(x="Churn", data=filtered_df, palette="viridis", ax=ax1)
    ax1.set_title("Churn Count in Selected Tenure Group")
    st.pyplot(fig1)

with col2:
    st.subheader("Monthly Charges vs. Total Charges")
    fig2, ax2 = plt.subplots()
    sns.scatterplot(x="MonthlyCharges", y="TotalCharges", hue="Predicted_Churn", data=filtered_df, 
                    palette="coolwarm", ax=ax2)
    ax2.set_title("Charges Comparison by Predicted Churn")
    st.pyplot(fig2)

# Additional Visualization: Overall Churn Distribution by Tenure Group
st.subheader("Overall Churn Distribution by Tenure Group")
fig3, ax3 = plt.subplots(figsize=(10,6))
sns.countplot(x="tenure_group", hue="Churn", data=df, palette="Set2", ax=ax3)
ax3.set_title("Churn Count by Tenure Group")
st.pyplot(fig3)

# ------------------- Key Takeaways -------------------
st.header("Key Takeaways")
st.markdown("""
- **Insightful Trends:**  
  The analysis identifies that customer churn is significantly influenced by factors such as customer tenure, monthly charges, and service contract types.
- **Model Performance:**  
  The predictive model, while solid in overall accuracy, requires further refinement to better capture at-risk churn cases.
- **Actionable Business Strategies:**  
  Businesses can leverage these insights to deploy targeted retention strategies and optimize resource allocation to minimize churn.
""")

# ------------------- Next Steps -------------------
st.header("Next Steps")
st.markdown("""
- **Model Enhancement:**  
  - Further feature engineering (e.g., interaction terms, polynomial features)  
  - Hyperparameter tuning and testing advanced models (e.g., Gradient Boosting, XGBoost)
- **Operational Deployment:**  
  - Integrate the dashboard into real-time monitoring systems  
  - Optimize the decision threshold to improve recall for churn prediction
- **Data Enrichment:**  
  - Incorporate additional customer data (e.g., demographics, usage patterns) to improve predictive accuracy.
""")
