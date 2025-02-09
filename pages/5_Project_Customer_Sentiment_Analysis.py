import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# ---- Set Page Configuration ----
st.set_page_config(
    page_title="Customer Sentiment Analysis",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---- Project Title ----
st.title("Customer Sentiment Analysis on Amazon Product Reviews")

# ---- Project Summary ----
st.header("Project Summary")
st.write("""
This project analyzes Amazon product reviews using sentiment analysis and Aspect-Based Sentiment Analysis (ABSA) to extract insights from customer feedback. 
By applying natural language processing (NLP), we classify reviews as positive, neutral, or negative, determine sentiment trends over time, and identify specific aspects 
customers discuss.

Our goal is to uncover actionable insights that businesses can use to improve product offerings, marketing strategies, and customer satisfaction.

- **Dataset**: [Amazon Reviews Dataset](https://github.com/puravpatel3/portfolio/blob/9120460482515ef843eee964f7278e5b81b889ee/files/final_amazon_sentiment_dataset.csv)
- **Timeframe Analyzed**: 10/26/2010 – 10/26/2012
- **Key Insights**: Identify which products receive the best/worst sentiment and what specific aspects drive customer satisfaction or complaints.
""")

# ---- Use Case ----
st.header("Use Case")
st.write("""
**Why analyze customer sentiment?**
- **Product Improvement**: Identify trends in feedback to refine product features.
- **Marketing Strategy**: Optimize ad campaigns by understanding what customers love or dislike.
- **Customer Experience**: Address pain points in product quality or user experience.
- **Competitive Analysis**: Compare sentiment trends against competitor products.
- **Brand Reputation**: Monitor customer perceptions and respond proactively.
""")

# ---- Key Technologies Used ----
st.header("Key Technologies Used")
st.write("""
- **Python**: Data processing & sentiment analysis.
- **pandas**: Data manipulation.
- **matplotlib & seaborn**: Data visualization.
- **Streamlit**: Interactive dashboard.
- **VADER Sentiment Analysis**: Classifies overall sentiment.
- **spaCy NLP**: Extracts relevant product aspects.
- **Transformers (BERT)**: Aspect-Based Sentiment Analysis (ABSA).
""")

# ---- Project Steps ----
st.header("Project Steps")

with st.expander("Step 1: Data Cleaning & Preparation"):
    st.write("""
    - Filtered dataset to only include reviews from the latest 2 years (10/26/2010 - 10/26/2012).
    - Reduced file size by keeping only the top 50 most-reviewed products.
    - Converted timestamps to human-readable review dates.
    - Removed missing values and irrelevant columns.
    """)

with st.expander("Step 2: Sentiment Analysis (VADER)"):
    st.write("""
    - Used VADER (Valence Aware Dictionary and sEntiment Reasoner) to classify reviews as Positive, Neutral, or Negative.
    - Extracted compound sentiment scores to quantify sentiment intensity.
    - Applied text preprocessing (lowercasing, punctuation removal) to improve accuracy.
    """)

with st.expander("Step 3: Aspect-Based Sentiment Analysis (ABSA)"):
    st.write("""
    - Extracted key aspects from review text using spaCy NLP.
    - Applied BERT-based ABSA to determine sentiment for each aspect.
    - Filtered out stop words and irrelevant terms to keep only meaningful aspects.
    """)

with st.expander("Step 4: Visualization & Insights"):
    st.write("""
    - Created Sentiment Distribution (positive, neutral, negative %).
    - Developed Word Cloud to visualize frequently mentioned aspects.
    - Added Sentiment Over Time visualization (Quarterly trend).
    - Enabled interactive filters for dynamic analysis.
    """)

# ---- Data Visualizations ----
st.header("Data Visualizations")

# Load Data
data_url = "https://github.com/puravpatel3/portfolio/raw/9120460482515ef843eee964f7278e5b81b889ee/files/final_amazon_sentiment_dataset.csv"
df = pd.read_csv(data_url)

# Convert review_date to datetime format
df["review_date"] = pd.to_datetime(df["review_date"])

# Filters
st.sidebar.header("Filters")
selected_product = st.sidebar.selectbox("Select Product ID", options=["All"] + list(df["ProductId"].unique()))
selected_sentiment = st.sidebar.multiselect("Select Sentiment", ["Positive", "Neutral", "Negative"], default=["Positive", "Neutral", "Negative"])
selected_date_range = st.sidebar.date_input("Select Date Range", [df["review_date"].min(), df["review_date"].max()])

# Apply filters
if selected_product != "All":
    df = df[df["ProductId"] == selected_product]
df = df[df["overall_sentiment"].isin(selected_sentiment)]
df = df[(df["review_date"] >= selected_date_range[0]) & (df["review_date"] <= selected_date_range[1])]

# Sentiment Distribution & Sentiment Over Time (side by side)
col1, col2 = st.columns(2)

with col1:
    st.subheader("Sentiment Distribution")
    sentiment_counts = df["overall_sentiment"].value_counts()
    fig, ax = plt.subplots()
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette={"Positive": "green", "Neutral": "gray", "Negative": "red"}, ax=ax)
    ax.set_xlabel("Sentiment")
    ax.set_ylabel("Number of Reviews")
    st.pyplot(fig)

with col2:
    st.subheader("Sentiment Over Time (Quarterly)")
    df["quarter"] = df["review_date"].dt.to_period("Q")
    sentiment_trend = df.groupby(["quarter", "overall_sentiment"]).size().unstack(fill_value=0)

    fig, ax = plt.subplots(figsize=(8, 5))
    sentiment_trend.plot(kind="line", marker="o", ax=ax)
    ax.set_xlabel("Quarter")
    ax.set_ylabel("Number of Reviews")
    ax.legend(title="Sentiment")
    st.pyplot(fig)

# ProductID Pareto Chart & Wordcloud (side by side)
col3, col4 = st.columns(2)

with col3:
    st.subheader("Top 10 Most Reviewed Products")
    product_counts = df["ProductId"].value_counts().nlargest(10)
    fig, ax = plt.subplots()
    sns.barplot(x=product_counts.index, y=product_counts.values, ax=ax)
    ax.set_xlabel("Product ID")
    ax.set_ylabel("Number of Reviews")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig)

with col4:
    st.subheader("Frequent Aspects in Reviews")
    aspect_text = " ".join(df["refined_aspects"].dropna().astype(str))
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(aspect_text)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

# ---- Key Takeaways ----
st.header("Key Takeaways")

st.write("""
- **Positive Sentiment Dominates**
  - Most reviews are positive, meaning customers generally like the products.
  - This is useful for marketing teams to highlight strong product features.

- **Negative Reviews Offer Improvement Areas**
  - Negative reviews highlight pain points such as packaging issues, product quality, or misleading descriptions.
  - Companies can use this data to improve customer experience.

- **Sentiment Fluctuates Over Time**
  - Seasonal trends affect product sentiment (e.g., holiday season spikes).
  - Businesses can time promotions and improvements based on sentiment trends.

- **Aspect-Based Insights Provide Granularity**
  - Instead of a general positive/negative rating, ABSA identifies which product features drive sentiment.
  - Example: Coffee drinkers love "bold flavor" but dislike "weak aroma."
""")

# ---- Next Steps ----
st.header("Next Steps")
st.write("""
- Expand analysis to more product categories.
- Integrate real-time sentiment monitoring from live customer reviews.
- Improve aspect sentiment classification using advanced BERT models.
""")
