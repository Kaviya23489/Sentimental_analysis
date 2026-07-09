#Sentiment_app.py
# import frameworks
import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="Words Analyzer", page_icon="🎬")

st.title("🎭 Words Analyzer")
st.write("Analyze the emotional tone of your words review!")

# Input box
review = st.text_area("✍️ Enter your words here:", height=200)

if st.button("🧠 Analyze Sentiment"):
    if review:
        blob = TextBlob(review)
        sentiment_score = blob.sentiment.polarity

        if sentiment_score > 0.1:
            st.success("🌸 Positive Sentiment")
        elif sentiment_score < -0.1:
            st.error("💔 Negative Sentiment")
        else:
            st.info("😐 Neutral Sentiment")

        st.markdown(f"**Sentiment Score:** `{sentiment_score:.2f}`")
    else:
        st.warning("Please enter a review to analyze.")

