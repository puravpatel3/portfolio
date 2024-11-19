import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title Section: Cardiovascular Disease Clustering
st.title("Cardiovascular Disease Patient Clustering")

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
This project holds significant importance in the healthcare industry, specifically for identifying and understanding patient groups at high risk for cardiovascular disease. 
By leveraging the insights gained from clustering analysis, healthcare professionals can develop targeted treatment plans, implement preventive measures, 
and design effective interventions to mitigate risks and improve patient outcomes. This approach not only enhances patient care but also optimizes resource 
allocation and operational efficiency within healthcare systems.

The applications of unsupervised learning techniques, such as clustering, extend beyond healthcare and can address a diverse range of business challenges, including:

- **Customer Segmentation**: Clustering customers based on purchasing behavior, preferences, or demographics to enable more personalized marketing strategies, 
optimize product offerings, and improve customer retention.

- **Operational Insights**: Identifying patterns in operational data, such as supply chain inefficiencies, bottlenecks, or service delays, to focus on problem areas, 
enhance process efficiency, and reduce costs.

- **Risk Management**: Segmenting financial or operational risks to create targeted mitigation strategies, enabling organizations to respond proactively to potential challenges.

- **Product Development**: Grouping feedback and usage patterns to better understand customer needs and drive the design of more impactful products or services.

By uncovering underlying patterns in data, clustering empowers both businesses and healthcare providers to make data-driven, strategic decisions, unlocking opportunities 
for innovation, efficiency, and improved outcomes.
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
    st.write("Exploratory Data Analysis (EDA) is essential to understanding the dataset's characteristics, including identifying trends, distributions, and outliers. It is the first step in any data science project to ensure data quality, highlight anomalies, and provide insights into which features are relevant. This builds a foundation for further analysis by addressing data quality issues early and understanding data patterns.")
    

with st.expander("Step 2: Prepare the Data for Unsupervised Learning"):
    st.write("Data preparation involved filtering outliers and engineering features to make the dataset ready for clustering. Proper data preparation ensures that the clustering results are meaningful and accurate.")
    st.markdown("**Binning Age and Weight**: K-means binning was used to create bins for age and weight, allowing for grouping continuous variables into meaningful segments. This simplifies the clustering process and makes it easier to identify patterns in patient demographics.")
    st.markdown("**Binning Categorical Variables**: Categorical variables such as blood pressure, cholesterol, and glucose were grouped into categories like 'Normal', 'Above Normal', and 'Well Above Normal'. This binning captures the different health levels of patients in a structured way, making it easier for clustering algorithms to differentiate between varying risk levels.")
    
with st.expander("Step 3: Correlation Analysis"):
    st.write(
        "Correlation analysis plays a critical role in identifying the features most strongly associated with cardiovascular disease. "
        "Using Pearson's correlation coefficient, we analyzed the strength and direction of relationships between various variables "
        "and the presence of cardiovascular disease. This step is crucial for uncovering potential contributing factors to the onset "
        "of cardiovascular conditions, providing a foundation for prioritizing features for further analysis, predictive modeling, or targeted interventions."
    )
    st.markdown(
        "**Key Insights**: "
        "The analysis revealed that systolic and diastolic blood pressure exhibited the highest correlation with cardiovascular disease, "
        "underscoring their importance as primary predictive factors. These were followed by cholesterol levels, patient age, body weight, "
        "and glucose levels, which also demonstrated significant correlations with the target variable. These findings highlight the most impactful features, "
        "which will serve as the basis for the clustering algorithm. By leveraging these variables, we aim to segment patients into distinct groups, "
        "enabling a more refined understanding of cardiovascular risk profiles and facilitating data-driven strategies for prevention and treatment."
    )

with st.expander("Step 4: Unsupervised Learning - Clustering"):
    st.write(
        "Unsupervised learning techniques, such as K-means clustering, are employed to uncover natural groupings within the dataset without predefined labels. "
        "In this project, the K-means algorithm was utilized to segment patients into four distinct clusters. The algorithm operates by iteratively assigning data points to clusters, "
        "aiming to minimize the sum of squared distances between data points and their respective cluster centroids. This process ensures that each cluster is as homogeneous as possible, "
        "while maintaining clear distinctions from other clusters."
    )
    st.write(
        "Clustering patients serves as a powerful tool for gaining deeper insights into varying patient profiles, enabling the identification of groups with higher cardiovascular disease risk. "
        "This segmentation facilitates targeted healthcare strategies, including risk-specific interventions, personalized treatment plans, and resource allocation to improve overall patient outcomes."
    )
    st.markdown(
        "**Key Insights**: "
        "The analysis resulted in the identification of four distinct clusters, each representing unique risk levels and health characteristics. "
        "These clusters provide actionable insights for healthcare providers to develop data-driven approaches to patient care and disease prevention."
    )


# Key Takeaways
st.header("Key Takeaways")

st.subheader("Correlation Analysis")
st.write("The following features showed the highest correlation with cardiovascular disease:")
correlation_data = pd.DataFrame({
    'Variable': ['age_years', 'height', 'weight', 'ap_hi', 'ap_lo', 'gender', 'smoke', 'alco', 'active', 'cholesterol', 'gluc'],
    'Correlation': [0.239164, -0.011358, 0.179144, 0.427449, 0.337459, 0.006763, -0.016299, -0.008289, -0.037419, 0.221265, 0.091994],
    'P-value': ['0.000000e+00', '2.921999e-03', '0.000000e+00', '0.000000e+00', '0.000000e+00', '7.641558e-02', '1.951802e-05', '2.988575e-02', '1.054363e-22', '0.000000e+00', '7.233263e-127'],
    'Explanation': [
        'age_years has a moderate positive correlation with cardiovascular disease, which is statistically significant.',
        'height has a very weak negative correlation, and the p-value indicates it is statistically significant.',
        'weight has a moderate positive correlation with cardiovascular disease, which is statistically significant.',
        'ap_hi (systolic blood pressure) has a strong positive correlation with cardiovascular disease, indicating its importance.',
        'ap_lo (diastolic blood pressure) has a moderate positive correlation, also significant for cardiovascular health.',
        'gender shows a very weak correlation, which is not statistically significant at conventional levels.',
        'smoke has a very weak negative correlation, but it is statistically significant.',
        'alco shows a very weak negative correlation, which is statistically significant.',
        'active has a weak negative correlation, suggesting physically active individuals are at slightly lower risk.',
        'cholesterol has a moderate positive correlation with cardiovascular disease, indicating it is a significant factor.',
        'gluc has a weak positive correlation, suggesting that elevated glucose levels are linked to cardiovascular disease.'
    ]
})

# Bold the highest correlated rows
def highlight_high_corr(s):
    if s['Variable'] in ['age_years', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc']:
        return ['font-weight: bold'] * len(s)
    else:
        return [''] * len(s)

styled_correlation_data = correlation_data.style.apply(highlight_high_corr, axis=1)
st.write(styled_correlation_data)

# Displaying full dataframe without scroll and with expanded column widths
#st.dataframe(correlation_data, width=1500, height=600)

st.subheader("Unsupervised Learning Insights")
st.write("Scatter plots of clusters provide insights into the characteristics of each group.")


st.write("**Overall Cluster Definitions**:")
st.markdown("""
- **Cluster 0**: Primarily younger individuals with lower blood pressure and cholesterol levels. Low cardiovascular disease prevalence.
- **Cluster 1**: Middle-aged individuals with normal cholesterol but elevated blood pressure. Moderate cardiovascular disease prevalence.
- **Cluster 2**: Older individuals with high cholesterol and high blood pressure. High cardiovascular disease prevalence.
- **Cluster 3**: Mixed-age group with varying levels of cholesterol and blood pressure, but generally high cardiovascular disease prevalence.
""")

# Patients Scatterplot by Cardiovascular Disease
col1, col2 = st.columns(2)

with col1:
    st.image('https://raw.githubusercontent.com/puravpatel3/portfolio/72c47bef2c21cf6e0d6892ece3491a71bc1554d2/files/cluster_patients_no_cardio_disease.png', caption='Cluster of Patients by Age & Weight without Cardiovascular Disease', use_column_width=True)

with col2:
    st.image('https://raw.githubusercontent.com/puravpatel3/portfolio/72c47bef2c21cf6e0d6892ece3491a71bc1554d2/files/cluster_patients_cardio_disease.png', caption='Cluster of Patients by Age & Weight with Cardiovascular Disease', use_column_width=True)

with st.expander("Cluster 0 Definition"):
    st.markdown("""
    - **Cardio Distribution**: Approximately 62% of Cluster 0 has cardiovascular disease (cardio = 1), making it a cluster with a relatively higher presence of cardiovascular disease.
    - **Age**: Majority of individuals fall in the age ranges of 50-64 years, with a slight skew toward older individuals (55.02 to 64.97 years).
    - **Weight**: Individuals are spread across different weight categories, with the largest representation in the 65-76 kg range. There is also a significant number in the 76-88 kg range, especially among those with cardiovascular disease.
    - **Systolic Blood Pressure**: Most individuals fall under the "Normal" systolic blood pressure category (90-120 mmHg), while there are also a considerable number in the "High" range, particularly those with cardiovascular disease.
    - **Diastolic Blood Pressure**: The majority of individuals in this cluster have "Normal" diastolic blood pressure (60-80 mmHg). There are also a significant number with "High" diastolic blood pressure.
    - **Cholesterol**: Most people have normal cholesterol levels, with a significant proportion also falling into the above-normal or well-above-normal categories.
    - **Glucose**: Glucose levels are mixed, with a substantial number in the "well above normal" category (cardio = 1).

    **Cluster 0 Summary**: Cluster 0 is characterized by individuals mostly in their late 50s to early 60s, with a significant proportion having cardiovascular disease. Blood pressure tends to be in the normal range, but a considerable number have high systolic and diastolic pressure. Cholesterol and glucose levels vary, with a noticeable number having elevated values.
    """)

with st.expander("Cluster 1 Definition"):
    st.markdown("""
    - **Cardio Distribution**: Cluster 1 has the lowest percentage of individuals with cardiovascular disease, with only about 24% (cardio = 1).
    - **Age**: Most individuals in this cluster are between the ages of 39-50 years, making this the youngest cluster.
    - **Weight**: The majority fall into the 50-76 kg range, making it the cluster with generally lower weight compared to others.
    - **Systolic Blood Pressure**: The majority fall under the "Normal" category, with very few individuals classified in other categories.
    - **Diastolic Blood Pressure**: Most individuals have "Normal" diastolic blood pressure, with few in the "High" or "Very High" categories.
    - **Cholesterol**: Most people have normal cholesterol levels.
    - **Glucose**: Almost all individuals in this cluster have normal glucose levels.

    **Cluster 1 Summary**: Cluster 1 is the healthiest cluster, consisting mainly of younger individuals (39-50 years), with normal systolic and diastolic blood pressure, cholesterol, and glucose levels. This cluster also has the lowest prevalence of cardiovascular disease.
    """)

with st.expander("Cluster 2 Definition"):
    st.markdown("""
    - **Cardio Distribution**: Cluster 2 has the highest percentage of individuals with cardiovascular disease, with approximately 82% of individuals being cardio = 1.
    - **Age**: Most individuals in this cluster are in the age ranges of 55-65 years.
    - **Weight**: There is a mix of weights, with a significant representation across all weight ranges, particularly in the 65-88 kg category.
    - **Systolic Blood Pressure**: This cluster has a significant presence of individuals with "High" and "Very High" systolic blood pressure, especially among those with cardiovascular disease.
    - **Diastolic Blood Pressure**: There is a notable prevalence of individuals with "High" diastolic blood pressure.
    - **Cholesterol**: Elevated cholesterol levels are common, with many individuals in the "well above normal" category.
    - **Glucose**: Many individuals have elevated glucose levels, particularly among those with cardiovascular disease.

    **Cluster 2 Summary**: Cluster 2 primarily represents individuals with cardiovascular disease. It includes older individuals (55-65 years) with predominantly high systolic and diastolic blood pressure, and many have elevated cholesterol and glucose levels.
    """)

with st.expander("Cluster 3 Definition"):
    st.markdown("""
    - **Cardio Distribution**: Approximately 45% of individuals in Cluster 3 have cardiovascular disease, indicating a somewhat balanced mix of health statuses.
    - **Age**: The majority of individuals are in the 50-64 age range, with a slight skew toward older ages (55.02 to 64.97 years).
    - **Weight**: There is a mix of weights, with significant representation in the 65-76 kg and 76-88 kg categories.
    - **Systolic Blood Pressure**: Most individuals fall under the "Normal" category, but there is also a considerable number in the "High" category, particularly for those with cardiovascular disease.
    - **Diastolic Blood Pressure**: The majority have "Normal" diastolic blood pressure, but there is also a significant number with "High" diastolic blood pressure.
    - **Cholesterol**: Most individuals have normal cholesterol, but elevated cholesterol is also present, particularly among those with cardiovascular disease.
    - **Glucose**: There is a notable presence of elevated glucose levels among individuals with cardiovascular disease.

    **Cluster 3 Summary**: Cluster 3 is a mixed group, primarily consisting of individuals aged 50-64 years, with both cardiovascular and non-cardiovascular disease cases. Blood pressure tends to be in the normal range, but there are elevated values in those with cardiovascular disease, and cholesterol and glucose levels also show variation.
    """)

# Adding Pictures Side by Side After Cluster 3 Definition
col3, col4 = st.columns(2)

with col3:
    st.image('https://raw.githubusercontent.com/puravpatel3/portfolio/72c47bef2c21cf6e0d6892ece3491a71bc1554d2/files/scatter_age_weight_cardio.png', caption='Scatter Plot by Age & Weight with Cardiovascular Disease', use_column_width=True)

with col4:
    st.image('https://raw.githubusercontent.com/puravpatel3/portfolio/72c47bef2c21cf6e0d6892ece3491a71bc1554d2/files/scatter_blood_pressure_cardio.png', caption='Scatter Plot by Blood Pressure with Cardiovascular Disease', use_column_width=True)

# Adding Insights Below the Images
col5, col6 = st.columns(2)

with col5:
    st.write("**Age vs. Weight Relationship by Cardiovascular Disease (Scatter Plot 1):**")
    st.markdown("""
    The scatter plot illustrates the relationship between patient age (x-axis) and weight (y-axis), also color-coded by cardiovascular disease presence. Key insights include:

    **Distribution Across Ages**:
    - Patients with cardiovascular disease (red points) appear consistently distributed across the age range but show increased density in higher weight categories.
    - This suggests that while age alone may not be the strongest differentiator, higher weight combined with age increases cardiovascular disease risk.

    **Weight as a Risk Factor**:
    - Blue points (no disease) are more evenly distributed across lower and moderate weight ranges, with fewer appearing in the higher weight bands.
    - This reinforces weight as a significant factor for cardiovascular disease, especially when considered alongside other risk features like blood pressure.

    **No Clear Age Threshold**:
    - Unlike blood pressure, no definitive threshold for age seems to differentiate patients with and without cardiovascular disease. Instead, age acts as a complementary factor when combined with others, like weight or blood pressure.

    **Implications**:
    - Weight should be prioritized as an influential feature in clustering and prediction models. While age contributes, its interaction with other variables likely provides more value than age alone.
    """)

with col6:
    st.write("**Blood Pressure Relationship by Cardiovascular Disease (Scatter Plot 2):**")
    st.markdown("""
    The scatter plot shows the relationship between systolic (x-axis) and diastolic (y-axis) blood pressure, color-coded by cardiovascular disease presence (blue = no disease, red = disease). Key observations include:

    **Higher Blood Pressure Correlation**:
    - Red points (patients with cardiovascular disease) are concentrated in areas with higher systolic and diastolic blood pressure values.
    - This suggests a strong association between elevated blood pressure levels and the likelihood of cardiovascular disease.

    **Clear Thresholds**:
    - Many blue points (no disease) cluster in the lower ranges of both systolic and diastolic blood pressure, indicating that normal or low blood pressure is more common among patients without cardiovascular disease.
    - A noticeable separation begins at systolic values of around 140 and diastolic values of 90, aligning with clinical hypertension thresholds.

    **Implications**:
    - Blood pressure serves as a critical feature for identifying high-risk patients. The clustering pattern justifies its inclusion as a primary variable in further analyses, such as clustering algorithms or predictive models.
    """)

# Placeholder for more visualizations or detailed analysis

# Next Steps
st.header("Next Steps")
st.write("""
Based on the clustering results, healthcare providers can:
- **Identify High-Risk Patients**: Use the clustering information to identify patients at high risk for cardiovascular disease.
- **Develop Targeted Interventions**: Create personalized treatment and preventive plans for each cluster.
""")
