import streamlit as st

def show_projects():
    st.title("Projects")
    st.write("### Explore some of my key projects.")

    # Displaying projects summary
    st.write("#### 1. Exploratory Data Analysis (EDA)")
    st.write("Summary: In-depth exploration of data from various industries, uncovering trends and actionable insights.")
    if st.button("View EDA Details"):
        import pages.project_eda as project_eda
        project_eda.show_project_eda()

    st.write("#### 2. Sentiment Analysis")
    st.write("Summary: Analyzing sentiment from customer reviews to understand product perception and satisfaction.")
    if st.button("View Sentiment Analysis Details"):
        import pages.project_sentiment as project_sentiment
        project_sentiment.show_project_sentiment()

    st.write("#### 3. Machine Learning")
    st.write("Summary: Built machine learning models to predict on-time deliveries and optimize business processes.")
    if st.button("View ML Details"):
        import pages.project_ml as project_ml
        project_ml.show_project_ml()
