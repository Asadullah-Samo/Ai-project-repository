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