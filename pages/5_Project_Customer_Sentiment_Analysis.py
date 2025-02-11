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

# ---- 1️⃣ Project Title ----
st.title("Customer Sentiment Analysis on Amazon Product Reviews")

# ---- 2️⃣ Project Summary ----
st.header("Project Summary")
st.write("""
This project analyzes **Amazon product reviews** using **sentiment analysis** and **Aspect-Based Sentiment Analysis (ABSA)** to extract insights from customer feedback.
By applying **natural language processing (NLP)**, I classify reviews as **positive, neutral, or negative**, determine sentiment trends over time, and identify specific aspects discussed by customers.

The goal is to uncover actionable insights that businesses can use to improve **product offerings, marketing strategies, and customer satisfaction**.

- **Dataset**: [Amazon Reviews Dataset](https://github.com/puravpatel3/portfolio/blob/9120460482515ef843eee964f7278e5b81b889ee/files/final_amazon_sentiment_dataset.csv)
- **Timeframe Analyzed**: **10/26/2010 – 10/26/2012**
- **Key Insights**: Identify which products receive the best/worst sentiment and determine which specific aspects drive customer satisfaction or complaints.
""")

# ---- 3️⃣ Use Case ----
st.header("Use Case")
st.write("""
**Why analyze customer sentiment?**
- **Product Improvement**: Identify trends in feedback to refine product features.
- **Marketing Strategy**: Optimize ad campaigns by understanding what customers love or dislike.
- **Customer Experience**: Address pain points in product quality or user experience.
- **Competitive Analysis**: Compare sentiment trends against competitor products.
- **Brand Reputation**: Monitor customer perceptions and respond proactively.
""")

# ---- 4️⃣ Key Technologies Used ----
st.header("Key Technologies Used")
st.write("""
- **Python**: Data processing and sentiment analysis.
- **pandas**: Data manipulation.
- **matplotlib & seaborn**: Data visualization.
- **Streamlit**: Interactive dashboard development.
- **VADER Sentiment Analysis**: Classifies overall sentiment.
- **spaCy NLP**: Extracts relevant product aspects.
- **Transformers (BERT)**: Performs Aspect-Based Sentiment Analysis (ABSA).
""")

# ---- 5️⃣ Project Steps ----
st.header("Project Steps")

with st.expander("Step 1: Data Cleaning & Preparation"):
    st.write("""
    - **Filtered the dataset** to include reviews from the latest 2 years (10/26/2010 - 10/26/2012).
    - **Reduced file size** by retaining only the top 50 most-reviewed products.
    - **Converted timestamps** to human-readable review dates.
    - **Removed missing values** and irrelevant columns.
    """)

with st.expander("Step 2: Sentiment Analysis (VADER)"):
    st.write("""
    - Applied **VADER (Valence Aware Dictionary and sEntiment Reasoner)** to classify reviews as **Positive, Neutral, or Negative**.
    - Extracted **compound sentiment scores** to quantify sentiment intensity.
    - Performed **text preprocessing** (lowercasing, punctuation removal) to enhance accuracy.
    """)

with st.expander("Step 3: Aspect-Based Sentiment Analysis (ABSA)"):
    st.write("""
    - Extracted key **aspects** from review text using **spaCy NLP**.
    - Utilized a **BERT-based ABSA** approach to determine sentiment for each aspect.
    - Filtered out **stop words and irrelevant terms** to retain only meaningful aspects.
    """)

with st.expander("Step 4: Visualization & Insights"):
    st.write("""
    - Created a **Sentiment Distribution** visualization showing the proportions of positive, neutral, and negative reviews.
    - Developed a **Word Cloud** to display frequently mentioned aspects in the reviews.
    - Plotted **Sentiment Over Time** (quarterly trend) to observe how sentiment evolves.
    - Enabled **interactive filters** for dynamic analysis of the review data.
    """)

# ---- Sidebar Filters ----
st.sidebar.header("Filter Data")

# Load Data
data_url = "https://github.com/puravpatel3/portfolio/raw/9120460482515ef843eee964f7278e5b81b889ee/files/final_amazon_sentiment_dataset.csv"
df = pd.read_csv(data_url)
df["review_date"] = pd.to_datetime(df["review_date"])

# Date Filter
min_date = df["review_date"].min()
max_date = df["review_date"].max()
date_range = st.sidebar.date_input("Select Date Range", [min_date, max_date], min_value=min_date, max_value=max_date)

# Product ID Filter
product_options = df["ProductId"].unique()
selected_product = st.sidebar.selectbox("🛍Select Product ID", ["All"] + list(product_options))

# Sentiment Filter
sentiment_options = ["All", "Positive", "Neutral", "Negative"]
selected_sentiment = st.sidebar.selectbox("Select Sentiment", sentiment_options)

# ---- Apply Filters ----
filtered_df = df[
    (df["review_date"] >= pd.to_datetime(date_range[0])) &
    (df["review_date"] <= pd.to_datetime(date_range[1]))
]

if selected_product != "All":
    filtered_df = filtered_df[filtered_df["ProductId"] == selected_product]

if selected_sentiment != "All":
    filtered_df = filtered_df[filtered_df["overall_sentiment"] == selected_sentiment]

# ---- 6️⃣ Data Visualizations ----
st.header("Data Visualizations")

# Layout for Sentiment Charts
col1, col2 = st.columns(2)

# Sentiment Distribution
with col1:
    st.subheader("Sentiment Distribution")
    sentiment_counts = filtered_df["overall_sentiment"].value_counts()
    fig, ax = plt.subplots(figsize=(5, 4))
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, 
                palette={"Positive": "green", "Neutral": "gray", "Negative": "red"}, ax=ax)
    ax.set_xlabel("Sentiment")
    ax.set_ylabel("Number of Reviews")
    st.pyplot(fig)

# Sentiment Over Time
with col2:
    st.subheader("Sentiment Over Time (Quarterly)")
    filtered_df["quarter"] = filtered_df["review_date"].dt.to_period("Q")
    sentiment_trend = filtered_df.groupby(["quarter", "overall_sentiment"]).size().unstack(fill_value=0)

    fig, ax = plt.subplots(figsize=(7, 4))
    sentiment_trend.plot(kind="line", marker="o", ax=ax, color={"Positive": "green", "Neutral": "gray", "Negative": "red"})
    ax.set_xlabel("Quarter")
    ax.set_ylabel("Number of Reviews")
    ax.legend(title="Sentiment")
    st.pyplot(fig)

# Product Pareto Chart & Word Cloud
col3, col4 = st.columns(2)

with col3:
    st.subheader("Top 10 Reviewed Products")
    product_counts = filtered_df["ProductId"].value_counts().head(10).reset_index()
    product_counts.columns = ["ProductId", "Review Count"]
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(y=product_counts["ProductId"], x=product_counts["Review Count"], ax=ax)
    ax.set_ylabel("Product ID")
    ax.set_xlabel("Number of Reviews")
    st.pyplot(fig)

with col4:
    st.subheader("Frequent Aspects in Reviews")
    aspect_text = " ".join(filtered_df["refined_aspects"].dropna().astype(str))
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(aspect_text)
    st.image(wordcloud.to_array(), use_container_width=True)

# ---- Key Takeaways ----
st.header("Key Takeaways")
st.write("""
- **Positive Sentiment Dominates**
  - Most reviews are **positive**, indicating that customers generally appreciate the products.
  - This insight is useful for marketing teams to emphasize strong product features.

- **Negative Reviews Highlight Areas for Improvement**
  - Negative reviews pinpoint **pain points** such as packaging issues, product quality, or misleading descriptions.
  - Companies can use this data to enhance the customer experience.

- **Sentiment Trends Over Time**
  - Quarterly sentiment trends reveal seasonal patterns that can inform promotional timing and product updates.

- **Aspect-Based Insights**
  - Aspect-based sentiment analysis provides granular insights by identifying specific product features that drive sentiment.
""")

# ---- Next Steps ----
st.header("Next Steps")
st.write("""
- Expand the analysis to additional product categories.
- Integrate real-time sentiment monitoring from live customer reviews.
- Refine aspect-based sentiment classification using advanced BERT models.
""")
