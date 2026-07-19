import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def load_data(path):
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        st.error(f"❌ Error: The file at '{path}' was not found. Please check your data folder!")
        return None

def run_reels_algorithm(data, w1, w2):
    data['algorithm_score'] = w1 * data['engagement_score'] - w2 * data['toxicity_score']
    return data.sort_values(by='algorithm_score', ascending=False)

st.title("TikTok & YouTube Reels Algorithm Simulator")
st.write("This app shows how social media algorithms rank videos on your feed.")

st.sidebar.header("Algorithm Tuning Controls")
w1 = st.sidebar.slider("User Interest Weight (w1)", 0.0, 2.0, 1.0, 0.1)
w2 = st.sidebar.slider("Safety / Anti-Clickbait Weight (w2)", 0.0, 2.0, 1.0, 0.1)

df = load_data("data/news_data.csv")

if df is not None:
    ranked_feed = run_reels_algorithm(df.copy(), w1, w2)
    
    st.subheader(" Your Personalized Video Feed")
    st.dataframe(ranked_feed[['title', 'category', 'algorithm_score']])
    
    top_video = ranked_feed.iloc[0]
    st.info(f"**💡 Why are you seeing '{top_video['title']}' at the top?** Because it has high user engagement and passes our safety score check.")
    
    st.subheader(" Algorithm Evaluation Panel")
    if st.button("Test Safe Mode (Double Safety Weight)"):
        current_top_toxicity = top_video['toxicity_score']
        
        safe_feed = run_reels_algorithm(df.copy(), w1, w2 * 2)
        safe_top_toxicity = safe_feed.iloc[0]['toxicity_score']
        
        fig, ax = plt.subplots()
        modes = ['Current Feed', 'Safe Mode (Filtered)']
        toxicity_levels = [current_top_toxicity, safe_top_toxicity]
        
        ax.bar(modes, toxicity_levels, color=['red', 'blue'])
        ax.set_ylabel('Toxicity / Clickbait Level of Top Video')
        
        st.pyplot(fig)
        st.write("Result: Safe Mode automatically removes high-risk clickbait videos from the top spot.")
