import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title Section: Cardiovascular Disease Clustering
st.title("Cardiovascular Disease Clustering")

# Project Summary
st.header("Project Summary")
st.write("""
This project aims to identify different segments of patients based on various features related to cardiovascular health. By using unsupervised learning techniques like K-means clustering, we grouped patients to gain insights into the factors contributing to cardiovascular disease.
The objective is to better understand patient profiles, allowing healthcare providers to focus on high-risk groups more effectively.
""")
st.markdown("Download Comprehensive Exploratory Data Analysis Report generated using ydata-profiling here: [Click Here](https://github.com/puravpatel3/portfolio/blob/72c47bef2c21cf6e0d6892ece3491a71bc1554d2/files/cardio_eda_report.html)\n\nClick on the 'Download raw file' button in Github to access the report")

# Use Case
st.header("Use Case")
st.write("""
This project is crucial in the healthcare industry for identifying patient groups at high risk for cardiovascular disease. The insights gained can help healthcare professionals create targeted treatment plans, preventive strategies, and effective interventions to mitigate risks.
""")

# Key Technologies Used
st.header("Key Technologies Used")
st.write("""
- **Pandas**: For data manipulation and preparation.
- **Scikit-learn**: To perform K-means clustering.
- **Matplotlib & Seaborn**: For creating visualizations.
- **Streamlit**: For building the interactive web application.
""")

# Project Steps
st.header("Project Steps")
with st.expander("Step 1: Perform Exploratory Data Analysis (EDA)"):
    st.write("Exploratory Data Analysis was performed to understand the distribution and relationships between features.")
    

with st.expander("Step 2: Prepare the Data for Unsupervised Learning"):
    st.write("Data preparation involved filtering outliers and engineering features to make the dataset ready for clustering.")
    st.markdown("**Binning Age and Weight**: K-means binning was used to create bins for age and weight, allowing us to group continuous variables into meaningful segments. This helps in simplifying the clustering process and makes it easier to identify patterns.")
    st.markdown("**Binning Categorical Variables**: Categorical variables such as blood pressure, cholesterol, and glucose were grouped into categories like 'Normal', 'Above Normal', and 'Well Above Normal'. This binning helps capture the different health levels of patients in a structured way, making it easier for clustering algorithms to differentiate between varying risk levels.")
    

with st.expander("Step 3: Correlation Analysis"):
    st.write("A correlation analysis was conducted to understand which features were most related to cardiovascular disease.")
    
    st.markdown("**Key Insights**: Age, systolic blood pressure, and cholesterol levels showed the highest correlation with cardiovascular disease.")

with st.expander("Step 4: Unsupervised Learning - Clustering"):
    st.write("K-means clustering was used to group patients based on their cardiovascular-related features.")
    st.markdown("We identified four distinct clusters, each representing patients with different risk levels.")
    

# Key Takeaways
st.header("Key Takeaways")

st.subheader("Correlation Analysis")
st.write("The following features showed the highest correlation with cardiovascular disease:")
correlation_data = pd.DataFrame({
    'Variable': ['age_years', 'height', 'weight', 'ap_hi', 'ap_lo', 'gender', 'smoke', 'alco', 'active', 'cholesterol', 'gluc'],
    'Correlation': [0.239164, -0.011358, 0.179144, 0.427449, 0.337459, 0.006763, -0.016299, -0.008289, -0.037419, 0.221265, 0.091994],
    'P-value': ['0.000000e+00', '2.921999e-03', '0.000000e+00', '0.000000e+00', '0.000000e+00', '7.641558e-02', '1.951802e-05', '2.988575e-02', '1.054363e-22', '0.000000e+00', '7.233263e-127']
})

# Bold the highest correlated rows
def highlight_high_corr(s):
    if s['Variable'] in ['age_years', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc']:
        return ['font-weight: bold'] * len(s)
    else:
        return [''] * len(s)

styled_correlation_data = correlation_data.style.apply(highlight_high_corr, axis=1)
st.write(styled_correlation_data)

st.subheader("Unsupervised Learning Insights")
st.write("Scatter plots of clusters provide insights into the characteristics of each group.")


st.write("**Cluster Definitions**:")
st.markdown("""
- **Cluster 0**: Primarily younger individuals with lower blood pressure and cholesterol levels. Low cardiovascular disease prevalence.
- **Cluster 1**: Middle-aged individuals with normal cholesterol but elevated blood pressure. Moderate cardiovascular disease prevalence.
- **Cluster 2**: Older individuals with high cholesterol and high blood pressure. High cardiovascular disease prevalence.
- **Cluster 3**: Mixed-age group with varying levels of cholesterol and blood pressure, but generally high cardiovascular disease prevalence.
""")

# Next Steps
st.header("Next Steps")
st.write("""
Based on the clustering results, healthcare providers can:
- **Identify High-Risk Patients**: Use the clustering information to identify patients at high risk for cardiovascular disease.
- **Develop Targeted Interventions**: Create personalized treatment and preventive plans for each cluster.
""")

# Placeholder for more visualizations or detailed analysis
