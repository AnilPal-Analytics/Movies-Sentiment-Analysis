# 🎬 Movie Review Sentiment Analysis

A complete **Machine Learning + Streamlit** project that analyzes movie reviews and predicts whether the sentiment is **Positive 😊** or **Negative 😠**.

This project demonstrates an **end-to-end NLP workflow** including text preprocessing, model training, vectorization, model persistence, and deployment using **Streamlit**.

---

## 🚀 Project Overview

Movie reviews often contain valuable opinions. This application allows users to enter a movie review and instantly receive sentiment feedback using a trained machine learning model.

The project is divided into:
- **Model Training (Jupyter Notebook)**
- **Model Deployment (Streamlit Web App)**

---

## 🧠 Tech Stack

- **Programming Language:** Python
- **Libraries:**  
  - NumPy  
  - Pandas  
  - Scikit-learn  
  - NLTK  
  - Pickle  
- **NLP Techniques:**  
  - Text Cleaning  
  - Stopword Removal  
  - TF-IDF Vectorization  
- **Model:** Logistic Regression / ML Classifier
- **Frontend:** Streamlit
- **Version Control:** Git & GitHub

---

## 📂 Project Structure

```text
Movies-Sentiment-Analysis/
│
├── app.py                         # Streamlit application
├── sentiment_model.pkl            # Trained ML model
├── tfidf_vectorizer.pkl           # TF-IDF vectorizer
├── Movies Reviews Sentiment Analysis project.ipynb  # Model training notebook
├── requirements.txt               # Project dependencies
├── README.md                      # Project documentation
└── .gitignore                     # Ignored files


## ⚙️ Model Training (Jupyter Notebook)

The model training process includes:

- Loading and exploring the movie review dataset  
- Text preprocessing:
  - Lowercasing text
  - Removing special characters
  - Stopword removal
- Feature extraction using **TF-IDF Vectorizer**
- Model training using a machine learning classifier
- Saving the trained model and vectorizer using **Pickle**

### Saved Files
- `sentiment_model.pkl`
- `tfidf_vectorizer.pkl`

---

## 🌐 Streamlit Web Application

The Streamlit app provides a clean and professional user interface.

### Features
- Text area for movie review input
- Button to analyze sentiment
- Real-time sentiment prediction
- Clean UI with header and footer

### UI Highlights
- Centered layout
- Emoji-based sentiment feedback
- Professional footer credit

---

## 👨‍💻 Developed By

**Anil Pal**  
Aspiring Data Scientist | Machine Learning & NLP Enthusiast
