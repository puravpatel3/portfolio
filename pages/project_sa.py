import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset from GitHub
csv_url = 'https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/drug_review_output.csv'
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

# Top 10 Highest Sentiment
top_10_highest_sentiment = sentiment_table.nlargest(10, 'avg_sentiment')

# Top 10 Lowest Sentiment
top_10_lowest_sentiment = sentiment_table.nsmallest(10, 'avg_sentiment')

# Display the Top 10 Highest and Lowest Sentiment drugs side by side
st.write('### Top 10 Drugs by Highest/Lowest Sentiment')

col1, col2 = st.columns(2)

with col1:
    st.write('#### Top 10 Drugs by Highest Sentiment')
    st.dataframe(top_10_highest_sentiment)

with col2:
    st.write('#### Top 10 Drugs by Lowest Sentiment')
    st.dataframe(top_10_lowest_sentiment)

# Average sentiment by year (Line Chart)
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
        # Top 10 Reviews by Highest Sentiment
        st.write('### Top Sentiment Reviews')
        top_sentiment_reviews = df.nlargest(10, 'sentiment')[['condition', 'drugName', 'clean_review', 'date', 'rating', 'sentiment']]
        top_sentiment_reviews = top_sentiment_reviews.rename(columns={'clean_review': 'review'})  # Rename 'clean_review' to 'review'
        st.dataframe(top_sentiment_reviews)

        # Bottom 10 Reviews by Lowest Sentiment
        st.write('### Bottom Sentiment Reviews')
        bottom_sentiment_reviews = df.nsmallest(10, 'sentiment')[['condition', 'drugName', 'clean_review', 'date', 'rating', 'sentiment']]
        bottom_sentiment_reviews = bottom_sentiment_reviews.rename(columns={'clean_review': 'review'})  # Rename 'clean_review' to 'review'
        st.dataframe(bottom_sentiment_reviews)

else:
    st.info('Please select a condition to display the sentiment trend over time.')
