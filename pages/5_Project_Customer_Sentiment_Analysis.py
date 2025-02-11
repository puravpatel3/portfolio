import streamlit as st
import pandas as pd
import plotly.express as px
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
By applying **natural language processing (NLP)**, I classify reviews as **positive, neutral, or negative**, determine sentiment trends over time, and identify specific aspects mentioned in the reviews.

The goal is to uncover actionable insights that businesses can use to improve **product offerings, marketing strategies, and customer satisfaction**.

- **Dataset**: [Amazon Reviews Dataset](https://github.com/puravpatel3/portfolio/blob/9120460482515ef843eee964f7278e5b81b889ee/files/final_amazon_sentiment_dataset.csv)
- **Timeframe Analyzed**: **10/26/2010 – 10/26/2012**
- **Key Insights**: Identify which products receive the best or worst sentiment and determine which aspects drive customer satisfaction or complaints.
""")

# ---- 3️⃣ Use Case ----
st.header("Use Case")
st.write("""
**Why analyze customer sentiment?**
- **Product Improvement**: Identify trends in feedback to refine product features.
- **Marketing Strategy**: Optimize ad campaigns by understanding what customers appreciate or dislike.
- **Customer Experience**: Address pain points in product quality or user experience.
- **Competitive Analysis**: Compare sentiment trends against competitor products.
- **Brand Reputation**: Monitor customer perceptions and respond proactively.
""")

# ---- 4️⃣ Key Technologies Used ----
st.header("Key Technologies Used")
st.write("""
- **Python**: Data processing and sentiment analysis.
- **pandas**: Data manipulation.
- **matplotlib & seaborn**: (Previously used for static charts.)
- **Plotly**: For interactive and dynamic visualizations.
- **Streamlit**: Interactive dashboard development.
- **VADER Sentiment Analysis**: Classifies overall sentiment.
- **spaCy NLP**: Extracts relevant product aspects.
- **Transformers (BERT)**: Performs Aspect-Based Sentiment Analysis (ABSA).
""")

# ---- 5️⃣ Project Steps ----
st.header("Project Steps")

with st.expander("Step 1: Data Cleaning & Preparation"):
    st.write("""
    - **Filtered the dataset** to include reviews from the most recent 2 years (10/26/2010 - 10/26/2012).
    - **Reduced file size** by retaining only the top 50 most-reviewed products.
    - **Converted timestamps** to human-readable review dates.
    - **Removed missing values** and irrelevant columns.
    """)

with st.expander("Step 2: Sentiment Analysis (VADER)"):
    st.write("""
    - Applied **VADER (Valence Aware Dictionary and sEntiment Reasoner)** to classify reviews as **Positive, Neutral, or Negative**.
    - Extracted **compound sentiment scores** to quantify sentiment intensity.
    - Performed **text preprocessing** (e.g., lowercasing, punctuation removal) to enhance accuracy.
    """)

with st.expander("Step 3: Aspect-Based Sentiment Analysis (ABSA)"):
    st.write("""
    - Extracted key **aspects** from review text using **spaCy NLP**.
    - Utilized a **BERT-based ABSA** approach to determine sentiment for each aspect.
    - Filtered out **stop words and irrelevant terms** to retain only meaningful aspects.
    """)

with st.expander("Step 4: Visualization & Insights"):
    st.write("""
    - Created a **Sentiment Distribution** visualization to show the proportions of positive, neutral, and negative reviews.
    - Developed a **Word Cloud** to display frequently mentioned aspects.
    - Plotted **Sentiment Over Time** (quarterly trend) to observe how sentiment evolves.
    - Enabled **interactive filters** for dynamic analysis of the review data.
    """)

# ---- Dataset Preview Section ----
st.header("Dataset Preview")
data_url = "https://github.com/puravpatel3/portfolio/raw/9120460482515ef843eee964f7278e5b81b889ee/files/final_amazon_sentiment_dataset.csv"
df = pd.read_csv(data_url)
df["review_date"] = pd.to_datetime(df["review_date"])
st.dataframe(df.head(), height=400)

st.markdown("""
**Field Descriptions for Model Input Features:**

- **Review_Text:** The text of the customer review.
- **Sentiment_Score:** A numerical score indicating the review's sentiment.
- **Polarity:** A measure of how positive or negative the review is.
- **Subjectivity:** A measure of the degree of personal opinion in the review.
- **Other Features:** Additional metadata such as review date, product category, etc.
""")

# ---- Sidebar Filters ----
st.sidebar.header("Filter Data")

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

# Define a color palette similar to the churn analysis
sentiment_palette = {"Positive": "#99ccff", "Neutral": "#cccccc", "Negative": "#ff9999"}

# Layout for Sentiment Charts
col1, col2 = st.columns(2)

# Sentiment Distribution Chart using Plotly Express
with col1:
    st.subheader("Sentiment Distribution")
    sentiment_counts = filtered_df["overall_sentiment"].value_counts().reset_index()
    sentiment_counts.columns = ["Sentiment", "Count"]
    fig = px.bar(sentiment_counts, x="Sentiment", y="Count", 
                 color="Sentiment", 
                 color_discrete_map=sentiment_palette,
                 hover_data={"Count": True},
                 title="Distribution of Overall Sentiment")
    fig.update_layout(xaxis_title="Sentiment", yaxis_title="Number of Reviews")
    st.plotly_chart(fig, use_container_width=True)

# Sentiment Over Time Chart using Plotly Express
with col2:
    st.subheader("Sentiment Over Time (Quarterly)")
    filtered_df["quarter"] = filtered_df["review_date"].dt.to_period("Q").astype(str)
    sentiment_trend = filtered_df.groupby(["quarter", "overall_sentiment"]).size().reset_index(name="Count")
    fig2 = px.line(sentiment_trend, x="quarter", y="Count", color="overall_sentiment",
                   markers=True, color_discrete_map=sentiment_palette,
                   hover_data={"Count": True},
                   title="Quarterly Sentiment Trend")
    fig2.update_layout(xaxis_title="Quarter", yaxis_title="Number of Reviews")
    st.plotly_chart(fig2, use_container_width=True)

# Product Pareto Chart using Plotly Express
col3, col4 = st.columns(2)

with col3:
    st.subheader("Top 10 Reviewed Products")
    product_counts = filtered_df["ProductId"].value_counts().head(10).reset_index()
    product_counts.columns = ["ProductId", "Review Count"]
    fig3 = px.bar(product_counts, x="Review Count", y="ProductId", orientation='h',
                  hover_data={"Review Count": True},
                  title="Top 10 Reviewed Products",
                  color_discrete_sequence=["#99ccff"])
    fig3.update_layout(xaxis_title="Number of Reviews", yaxis_title="Product ID")
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    st.subheader("Frequent Aspects in Reviews")
    aspect_text = " ".join(filtered_df["refined_aspects"].dropna().astype(str))
    wordcloud = WordCloud(width=800, height=400, background_color="white", colormap="Blues").generate(aspect_text)
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

- **Aspect-Based Insights Provide Granularity**
  - Aspect-based sentiment analysis offers detailed insights by identifying specific product features that drive sentiment.
""")

# ---- Next Steps ----
st.header("Next Steps")
st.write("""
- Expand the analysis to include additional product categories.
- Integrate real-time sentiment monitoring from live customer reviews.
- Refine aspect-based sentiment classification using advanced BERT models.
""")
