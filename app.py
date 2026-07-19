import streamlit as st
import pandas as pd

# 1. Dataset Load Karne Ka Function
def load_data(path):
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        st.error(f"❌ Error: The file at '{path}' was not found. Please check your data folder!")
        return None

# 2. TikTok/YouTube Algorithm Logic
def run_reels_algorithm(data, w1, w2):
    # Formula: Score = (Engagement Weight * Engagement) - (Safety Weight * Toxicity)
    data['algorithm_score'] = w1 * data['engagement_score'] - w2 * data['toxicity_score']
    # Jis video ka score zyada hoga wo top par aayegi
    return data.sort_values(by='algorithm_score', ascending=False)

# UI Setup
st.title("TikTok & YouTube Reels Algorithm Simulator")
st.write("This app shows how social media algorithms rank videos on your feed.")

# Sidebar Settings (Tuning Weights)
st.sidebar.header("Algorithm Tuning Controls")
w1 = st.sidebar.slider("User Interest Weight (w1)", 0.0, 2.0, 1.0, 0.1)
w2 = st.sidebar.slider("Safety / Anti-Clickbait Weight (w2)", 0.0, 2.0, 1.0, 0.1)

# Load Data
df = load_data("data/news_data.csv")

if df is not None:
    # Run Algorithm
    ranked_feed = run_reels_algorithm(df.copy(), w1, w2)
    
    # Display the Feed to User
    st.subheader(" Your Personalized Video Feed")
    st.dataframe(ranked_feed[['title', 'category', 'algorithm_score']])
    
    # Explainability: Top Video Kyun Dikhayi?
    top_video = ranked_feed.iloc[0]
    st.info(f"**💡 Why are you seeing '{top_video['title']}' at the top?** Because it has high user engagement and passes our safety score check.")