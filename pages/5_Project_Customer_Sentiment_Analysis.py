import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# -------------------- 🛠️ Load Data -------------------- #
# Load dataset from GitHub
data_url = "https://raw.githubusercontent.com/puravpatel3/portfolio/main/files/final_amazon_sentiment_dataset.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(data_url, encoding="utf-8")
    df['review_date'] = pd.to_datetime(df['review_date'])  # Convert to datetime for filtering
    return df

df = load_data()

# -------------------- 🎯 Sidebar Filters -------------------- #
st.sidebar.header("🔍 Filter Reviews")

# Product Selection
product_list = ["All"] + sorted(df["ProductId"].unique().tolist())
selected_product = st.sidebar.selectbox("📦 Select Product", product_list)

# Sentiment Selection
sentiment_list = ["All", "Positive", "Neutral", "Negative"]
selected_sentiment = st.sidebar.radio("📊 Sentiment", sentiment_list)

# Date Range Selection
min_date, max_date = df["review_date"].min(), df["review_date"].max()
start_date, end_date = st.sidebar.date_input("📅 Select Date Range", [min_date, max_date], min_value=min_date, max_value=max_date)

# Apply filters
filtered_df = df.copy()
if selected_product != "All":
    filtered_df = filtered_df[filtered_df["ProductId"] == selected_product]
if selected_sentiment != "All":
    filtered_df = filtered_df[filtered_df["overall_sentiment"] == selected_sentiment]
filtered_df = filtered_df[(filtered_df["review_date"] >= pd.Timestamp(start_date)) & (filtered_df["review_date"] <= pd.Timestamp(end_date))]

# -------------------- 🏆 Project Summary -------------------- #
st.title("📊 Customer Sentiment Analysis Dashboard")
st.write("""
This dashboard provides insights into Amazon product reviews using **Sentiment Analysis & Aspect-Based Sentiment Analysis (ABSA)**.  
Discover trends in **customer sentiment, review aspects, and product feedback** to make data-driven decisions.
""")

# -------------------- 📝 Instructions Section -------------------- #
st.header("📖 Instructions")
st.write("""
1️⃣ **Select Filters on the Sidebar**  
   - Choose a **specific product** or view all.  
   - Filter reviews by **Positive, Neutral, or Negative sentiment**.  
   - Adjust the **date range** to focus on recent reviews.

2️⃣ **Analyze Sentiment Trends**  
   - View **overall sentiment distribution** across selected reviews.  
   - Identify whether **feedback is mostly positive or negative**.

3️⃣ **Explore Aspect-Based Sentiment**  
   - See a **WordCloud of key aspects** mentioned in reviews.  
   - Identify top **positive & negative aspects** affecting customer satisfaction.

4️⃣ **Read Customer Reviews**  
   - View actual **customer review text** with their **sentiment classification**.  
   - Understand what **aspects drive positive or negative feedback**.

5️⃣ **Take Key Insights & Actions**  
   - Which products have the **best/worst customer sentiment**?  
   - What **factors influence positive or negative feedback**?  
   - How can this analysis **improve marketing, product design, and user experience**?
""")

# -------------------- 💡 Use Case Section -------------------- #
st.header("💼 Use Case: Why Analyze Customer Sentiment?")
st.write("""
🔹 **Product Improvement:** Identify key issues that customers frequently mention and improve product quality.  
🔹 **Marketing Strategy:** Understand how customers feel about your product and adjust messaging accordingly.  
🔹 **Competitive Benchmarking:** Compare sentiment trends with competitors to see where you stand.  
🔹 **Customer Experience Optimization:** Address common concerns to enhance customer satisfaction.  
🔹 **Early Warning System:** Detect emerging issues before they escalate into negative PR.
""")

# -------------------- 📊 Sentiment Breakdown -------------------- #
st.header("📈 Sentiment Distribution")
fig, ax = plt.subplots(figsize=(6,4))
sns.countplot(data=filtered_df, x="overall_sentiment", palette={"Positive": "green", "Neutral": "gray", "Negative": "red"}, ax=ax)
ax.set_xlabel("Sentiment")
ax.set_ylabel("Review Count")
st.pyplot(fig)

# -------------------- 🌟 Aspect-Based Sentiment (WordCloud) -------------------- #
st.header("💬 Most Discussed Review Aspects")

# Combine all extracted aspects into one large text corpus
aspect_text = " ".join(filtered_df["refined_aspects"].dropna().astype(str))
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(aspect_text)

fig, ax = plt.subplots(figsize=(8,4))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)

# -------------------- 📋 Display Customer Reviews -------------------- #
st.header("📝 Customer Reviews")
st.dataframe(filtered_df[["review_date", "ProductId", "overall_sentiment", "Summary", "Text", "refined_aspects"]])

# -------------------- 🎯 Key Takeaways -------------------- #
st.header("📢 Key Takeaways")
st.write("""
- **What products have the highest/lowest sentiment?**  
- **What aspects (taste, durability, shipping, etc.) are mentioned the most?**  
- **How does sentiment trend over time for each product?**  
- **How can brands use this data to improve customer experience?**
""")

# -------------------- ✅ Final Notes -------------------- #
st.write("📌 **Dataset Source:** [GitHub Link](https://github.com/puravpatel3/portfolio/blob/main/files/final_amazon_sentiment_dataset.csv)")
st.write("🚀 **Project by:** Purav Patel")
