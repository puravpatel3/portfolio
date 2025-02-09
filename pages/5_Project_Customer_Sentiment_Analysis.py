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

# ---- Title ----
st.title("🛒 Customer Sentiment Analysis on Amazon Product Reviews")

# ---- Load Data ----
data_url = "https://github.com/puravpatel3/portfolio/raw/9120460482515ef843eee964f7278e5b81b889ee/files/final_amazon_sentiment_dataset.csv"
df = pd.read_csv(data_url)

# Convert review_date to datetime format
df["review_date"] = pd.to_datetime(df["review_date"])

# ---- Sidebar Filters ----
st.sidebar.header("🔍 Filter Data")

# Date Filter
min_date = df["review_date"].min()
max_date = df["review_date"].max()
date_range = st.sidebar.date_input("📅 Select Date Range", [min_date, max_date], min_value=min_date, max_value=max_date)

# Product ID Filter
product_options = df["ProductId"].unique()
selected_product = st.sidebar.selectbox("🛍️ Select Product ID", ["All"] + list(product_options))

# Sentiment Filter
sentiment_options = ["All", "Positive", "Neutral", "Negative"]
selected_sentiment = st.sidebar.selectbox("😊 Select Sentiment", sentiment_options)

# ---- Apply Filters ----
filtered_df = df[
    (df["review_date"] >= pd.to_datetime(date_range[0])) &
    (df["review_date"] <= pd.to_datetime(date_range[1]))
]

if selected_product != "All":
    filtered_df = filtered_df[filtered_df["ProductId"] == selected_product]

if selected_sentiment != "All":
    filtered_df = filtered_df[filtered_df["overall_sentiment"] == selected_sentiment]

# ---- Layout with Two Columns ----
col1, col2 = st.columns(2)

# ---- Sentiment Distribution ----
with col1:
    st.subheader("📊 Sentiment Distribution")
    sentiment_counts = filtered_df["overall_sentiment"].value_counts()
    fig, ax = plt.subplots(figsize=(5, 4))
    sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette={"Positive": "green", "Neutral": "gray", "Negative": "red"}, ax=ax)
    ax.set_xlabel("Sentiment")
    ax.set_ylabel("Number of Reviews")
    st.pyplot(fig)

# ---- Sentiment Over Time (Quarterly) ----
with col2:
    st.subheader("📈 Sentiment Over Time (Quarterly)")
    filtered_df["quarter"] = filtered_df["review_date"].dt.to_period("Q")
    sentiment_trend = filtered_df.groupby(["quarter", "overall_sentiment"]).size().unstack(fill_value=0)

    fig, ax = plt.subplots(figsize=(7, 4))
    sentiment_trend.plot(kind="line", marker="o", ax=ax, color={"Positive": "green", "Neutral": "gray", "Negative": "red"})
    ax.set_xlabel("Quarter")
    ax.set_ylabel("Number of Reviews")
    ax.legend(title="Sentiment")
    st.pyplot(fig)

# ---- Layout with Two Columns for Product Bar Chart & Word Cloud ----
col3, col4 = st.columns(2)

# ---- Product Review Count Bar Chart ----
with col3:
    st.subheader("🛍️ Top Reviewed Products")
    product_counts = filtered_df["ProductId"].value_counts().reset_index()
    product_counts.columns = ["ProductId", "Review Count"]

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(y=product_counts["ProductId"], x=product_counts["Review Count"], palette="viridis", ax=ax)
    ax.set_ylabel("Product ID")
    ax.set_xlabel("Number of Reviews")
    st.pyplot(fig)

# ---- Word Cloud of Extracted Aspects ----
with col4:
    st.subheader("🔍 Frequent Aspects in Reviews")
    aspect_text = " ".join(filtered_df["refined_aspects"].dropna().astype(str))
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(aspect_text)
    
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

# ---- Key Takeaways ----
st.header("💡 Key Takeaways")
st.write("""
- **📢 Positive Sentiment Dominates**
  - Most reviews are **positive**, meaning customers generally like the products.
  - This is useful for marketing teams to highlight strong product features.

- **🚨 Negative Reviews Offer Improvement Areas**
  - Negative reviews highlight **pain points** such as packaging issues, product quality, or misleading descriptions.
  - Companies can use this data to improve **customer experience**.

- **⏳ Sentiment Fluctuates Over Time**
  - Seasonal trends affect product sentiment (e.g., holiday season spikes).
  - Businesses can time **promotions and improvements** based on sentiment trends.

- **🛠 Aspect-Based Insights Provide Granularity**
  - Instead of a general positive/negative rating, **ABSA identifies which product features drive sentiment**.
  - Example: Coffee drinkers love "bold flavor" but dislike "weak aroma."
""")

# ---- GitHub Reference ----
st.write("🔗 **Want to see the code?** Check out the full implementation on [GitHub](https://github.com/puravpatel3/portfolio).")
