import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title Section: Sentiment Analysis
st.title("Customer Sentiment Analysis for Pharmaceutical Products")

# Project Summary
st.header("Project Summary")
st.write("""
This project demonstrates the ability to extract actionable insights from customer feedback through sentiment analysis, showcasing both technical expertise and strategic thinking. Using Python and libraries such as `sklearn`, `textblob`, and `pandas`, the analysis involved preprocessing and cleaning text data, quantifying sentiment scores, and identifying trends in customer satisfaction.  

Key highlights of this project include:  
- **Sentiment Scoring and Trends**: Quantified sentiment to uncover how customers perceive different pharmaceutical products, providing a clear picture of satisfaction and dissatisfaction trends.  
- **Insights into Key Factors**: Extracted common themes from the reviews, such as mentions of drug effectiveness, side effects, and user experiences, helping to pinpoint drivers of sentiment.  
- **Business Impact**: Provided data-driven insights to help pharmaceutical companies optimize resource allocation, whether for improving underperforming products through R&D, promoting successful drugs via marketing, or enhancing customer support strategies.  

The project highlights the practical applications of sentiment analysis in identifying patterns and trends that influence business decisions. By bridging technical implementation with strategic insights, it demonstrates how data science can empower organizations to enhance customer satisfaction, improve operational efficiency, and make more informed decisions.  

Additionally, the skills and techniques demonstrated in this project—such as working with unstructured text data, applying natural language processing (NLP), and creating actionable insights—are highly transferable across industries, making sentiment analysis a versatile and impactful tool for any organization seeking to better understand its customers.
""")

# Data Source
st.markdown("""
**Data Source**: [Drug Review Dataset on Kaggle](https://www.kaggle.com/datasets/mohamedabdelwahabali/drugreview?select=drug_review_train.csv)

**Download Comprehensive Exploratory Data Analysis Report generated using ydata-profiling here**: [Click Here](https://github.com/puravpatel3/portfolio/blob/4e61793ecc3404ce11f9bcd576de021d9f19c674/files/drugreview_eda_report.html)

*Click on the 'Download raw file' button in Github to access the data or report*
""")

# Instructions
st.header("Instructions")
st.write("""
1. Start by viewing the **Top 10 Conditions & Drugs by Count** to understand the most reviewed conditions and drugs.
2. View the **Top 10 Drugs by Highest/Lowest Sentiment** using the default data provided.
3. Filter the data by a specific **condition** using the dropdown in the sidebar. Once a condition is selected, the app will show:
   - The average sentiment for the **Top 5 Drugs** for that condition.
   - Sentiment trends over time for these top drugs.
4. Select a specific **drug** from the dropdown to view detailed customer reviews. Two tables will be displayed:
   - Top 10 Reviews by Highest Sentiment
   - Top 10 Reviews by Lowest Sentiment
""")

# Use Case
st.header("Use Case")
st.write("""
Customer feedback is a critical resource for any company seeking to improve its products and services. In the pharmaceutical industry, sentiment analysis offers unique value by providing an objective view of how customers perceive drugs and their effectiveness. Through this project, I demonstrated how sentiment analysis can drive data-informed decisions across key business functions:  

1. **Refine R&D Efforts**:  
   Sentiment analysis can identify drugs with low customer satisfaction or recurring complaints in reviews, enabling pharmaceutical companies to focus their research and development resources on improving those products. For instance, reviews highlighting side effects or limited effectiveness can guide the refinement of formulations.  

2. **Optimize Marketing Strategy**:  
   Positive sentiment trends can be used to identify high-performing drugs and inform marketing campaigns. Companies can allocate advertising budgets to promote these products more effectively, enhancing their market presence and profitability.  

3. **Enhance Product Development**:  
   By extracting common themes and pain points from reviews, companies can identify areas for product improvement. For example, if reviews frequently mention confusing dosage instructions, this feedback can inform updates to packaging or educational materials.  

4. **Broader Applications Beyond Pharmaceuticals**:  
   The versatility of sentiment analysis extends far beyond pharmaceuticals. Any industry reliant on customer feedback—such as retail, technology, or hospitality—can leverage similar techniques to improve products, refine services, and better understand customer needs. For example:  
   - **E-commerce**: Analyze product reviews to identify popular products or common complaints.  
   - **Hospitality**: Evaluate guest reviews to improve services and drive customer loyalty.  
   - **Technology**: Understand user feedback on software to prioritize features or address bugs.  

Sentiment analysis serves as a vital tool for modern businesses, enabling them to make strategic, data-driven decisions that enhance customer satisfaction and operational efficiency.
""")


# Key Technologies
st.header("Key Technologies Used")
st.write("""
- **TextBlob**: Used for calculating sentiment polarity from customer reviews.
- **scikit-learn (sklearn)**: Applied for vectorizing review text and calculating correlation metrics.
- **NumPy**: Utilized for numerical operations.
- **Pandas**: Essential for data manipulation and preparation.
- **Matplotlib & Seaborn**: For generating visualizations to track sentiment trends.
- **Streamlit**: Used to build the interactive web application that showcases sentiment analysis results.
""")

# Load your dataset from GitHub
csv_url = 'https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/drug_review_output_clean.csv'
df = pd.read_csv(csv_url)

# Data preparation
df['year'] = pd.to_datetime(df['date']).dt.year

# Sidebar Filters
st.sidebar.header('Filter Options')

# Dropdown for conditions (default 'All')
condition_filter = st.sidebar.selectbox('Select Condition', options=['All'] + sorted(df['condition'].unique()))

# Filter drug names based on the selected condition
if condition_filter == 'All':
    drug_filter = st.sidebar.selectbox('Select Drug', options=['All'] + sorted(df['drugName'].unique()))
else:
    filtered_drugs = df[df['condition'] == condition_filter]['drugName'].unique()
    drug_filter = st.sidebar.selectbox('Select Drug', options=['All'] + sorted(filtered_drugs))

# Minimum Review Count filter (default set to 100)
min_review_count = st.sidebar.text_input('Minimum Review Count', '100')  # Default is 100

# Convert min_review_count to integer for filtering
try:
    min_review_count = int(min_review_count)
except ValueError:
    st.error('Please enter a valid number for minimum review count.')
    min_review_count = 100  # Set to 100 if invalid input

# Filter dataset based on user selection
if condition_filter != 'All':
    df = df[df['condition'] == condition_filter]
if drug_filter != 'All':
    df = df[df['drugName'] == drug_filter]

# Calculate average sentiment and apply the minimum review count filter
sentiment_table = df.groupby(['condition', 'drugName']).agg(
    avg_sentiment=('sentiment', 'mean'),
    review_count=('review', 'size')
).reset_index()

sentiment_table = sentiment_table[sentiment_table['review_count'] >= min_review_count]

# New Section: Top 10 Conditions & Drugs by Count
st.write('### Top 10 Conditions & Drugs by Count')

# Top 10 Conditions by Review Count
top_10_conditions = df.groupby('condition').agg(
    avg_sentiment=('sentiment', 'mean'),
    review_count=('review', 'size')
).reset_index().nlargest(10, 'review_count')

# Top 10 Drugs by Review Count
top_10_drugs = df.groupby('drugName').agg(
    avg_sentiment=('sentiment', 'mean'),
    review_count=('review', 'size')
).reset_index().nlargest(10, 'review_count')

col1, col2 = st.columns(2)

with col1:
    st.write('#### Top 10 Conditions by Review Count')
    st.dataframe(top_10_conditions)

with col2:
    st.write('#### Top 10 Drugs by Review Count')
    st.dataframe(top_10_drugs)

# ================================================================================================
## Top 10 Drugs by Highest/Lowest Sentiment
st.write('### Top 10 Drugs by Highest/Lowest Sentiment')

# Top 10 Highest Sentiment
top_10_highest_sentiment = sentiment_table.nlargest(10, 'avg_sentiment')

# Top 10 Lowest Sentiment
top_10_lowest_sentiment = sentiment_table.nsmallest(10, 'avg_sentiment')

col1, col2 = st.columns(2)

with col1:
    st.write('#### Top 10 Drugs by Highest Sentiment')
    st.dataframe(top_10_highest_sentiment)

with col2:
    st.write('#### Top 10 Drugs by Lowest Sentiment')
    st.dataframe(top_10_lowest_sentiment)

# ================================================================================================
## Average sentiment by year (Line Chart)
if condition_filter != 'All':  # Only plot if a condition is selected
    st.write('### Average Sentiment by Year (Top 5 Drugs)')

    # Calculate the top 5 drugs based on the count of reviews
    top_5_drugs = df['drugName'].value_counts().nlargest(5).index

    # Filter data for the top 5 drugs
    df_top_5 = df[df['drugName'].isin(top_5_drugs)]

    # Group the data by year and drug name for sentiment calculation
    sentiment_by_year = df_top_5.groupby(['year', 'drugName'])['sentiment'].mean().reset_index()

    # Create the line plot with the top 5 drugs, and move the legend to the right
    plt.figure(figsize=(10, 6))
    line_plot = sns.lineplot(x='year', y='sentiment', hue='drugName', data=sentiment_by_year, palette='bright')

    plt.title('Average Sentiment by Year (Top 5 Drugs)')
    plt.xlabel('Year')
    plt.ylabel('Average Sentiment')

    # Move legend to the right of the chart
    plt.legend(title='Drug Name', loc='center left', bbox_to_anchor=(1, 0.5))

    # Display the chart
    st.pyplot(plt)

    # Display Top Sentiment and Bottom Sentiment Reviews if a specific drug is selected
    if drug_filter != 'All':
        # Top 10 Reviews by Highest Sentiment (filtering for reviews with a rating of 7 or higher)
        st.write('### Top Sentiment Reviews')
        top_sentiment_reviews = df[(df['rating'] >= 7)].nlargest(10, 'sentiment')[['condition', 'drugName', 'review', 'date', 'rating', 'sentiment']]
        st.dataframe(top_sentiment_reviews)

        # Bottom 10 Reviews by Lowest Sentiment (filtering for reviews with a rating of 5 or lower)
        st.write('### Bottom Sentiment Reviews')
        bottom_sentiment_reviews = df[(df['rating'] <= 5)].nsmallest(10, 'sentiment')[['condition', 'drugName', 'review', 'date', 'rating', 'sentiment']]
        st.dataframe(bottom_sentiment_reviews)

else:
    st.info('Please select a condition to display the sentiment trend over time.')
