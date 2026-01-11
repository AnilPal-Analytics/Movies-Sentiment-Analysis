import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords
import os

# ================= LOAD NLTK ================= #

nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

# ================= LOAD MODEL ================= #

with open("sentiment_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# ================= CLEAN TEXT FUNCTION ================= #

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z]", " ", text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

# ================= STREAMLIT UI ================= #

# ================= PAGE CONFIG ================= #
st.set_page_config(
    page_title="Movie Sentiment Analysis",
    page_icon="🎬",
    layout="centered"
)

# ================= HEADER ================= #
st.markdown(
    "<h1 style='text-align: center;'>🎬 Movie Review Sentiment Analysis</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; color: gray;'>Analyze movie reviews and detect sentiment instantly</p>",
    unsafe_allow_html=True
)

# ================= INPUT SECTION ================= #
st.subheader("✍️ Enter Review")

review = st.text_area(
    label="",
    placeholder="Type your movie review here...",
    height=150
)

# ================= ACTION SECTION ================= #
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    analyze_btn = st.button("🔍 Analyze Sentiment", use_container_width=True)

# ================= RESULT SECTION ================= #

if analyze_btn:
    if review.strip() == "":
        st.warning("⚠️ Please enter a review!")
    else:
        cleaned_review = clean_text(review)
        vectorized_review = vectorizer.transform([cleaned_review])
        prediction = model.predict(vectorized_review)[0]

        if prediction == 1:
            st.success("😊 **Positive Sentiment**")
        else:
            st.error("😠 **Negative Sentiment**")

# ================= FOOTER ================= #
st.markdown(
    "<hr style='margin-top: 40px;'>"
    "<p style='text-align: center; color: gray;'>"
    "Developed by <b>Anil Pal</b>"
    "</p>",
    unsafe_allow_html=True
)
