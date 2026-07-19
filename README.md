# AI Lab Project Short Report

**Project Topic:** A Personalized News Feed and Reels Recommender (TikTok & YouTube Algorithm Simulation)[cite: 2]

**Team Details:**
1. Asadullah Samo (Roll No: 2K23/CSEE/19) - [Team Leader][cite: 2]
2. Mudasir Dasti (Roll No: 2K23/CSEE/48) - [Team Member]

**Submitted To:** Mr. Rajesh Kumar[cite: 2]

---

### 1. Problem Statement
Social media applications like TikTok and YouTube Shorts work in a Partially Observable environment[cite: 2]. The app cannot read the user's mind directly[cite: 2]. It only tracks digital actions like video watch-time and clicks[cite: 2]. The main challenge is to recommend highly interesting videos to keep the user active, while filtering out dangerous clickbait or fake news[cite: 2]. Our project simulates how algorithms balance Engagement and Content Safety[cite: 2].

### 2. AI Methodology
Our simulation model uses a mathematical optimization formula called the Utility Function ($U$) to rank the videos[cite: 2]:

$$U = w_1 \cdot E(c) - w_2 \cdot S(c)$$[cite: 2]

* **$E(c)$ (Engagement Score):** Represents how viral or interesting a video is to the user[cite: 2].
* **$S(c)$ (Toxicity Score):** Represents the risk or clickbait level of the video[cite: 2].
* **$w_1$ and $w_2$ (Weights):** Tuning controls that adjust the algorithm's behavior[cite: 2].

The algorithm calculates the utility score for all available content and displays the highest-scoring items at the top of the user's mobile feed[cite: 2].

### 3. Visual UI and Explainability
We built a simple web application using Python and the Streamlit framework.
* **Interactive Controls:** Users can move two sliders to adjust the algorithm weights ($w_1$ and $w_2$) in real-time.
* **Visual Representation:** The ranked video feed is shown clearly inside a data table[cite: 1].
* **Explainability:** The system features an AI explanation box that tells the user exactly why the top video was chosen[cite: 1].

### 4. Evaluation and Results
Our app features an evaluation button[cite: 1]. Clicking it compares the current feed against a "Safe Mode" where the safety penalty ($w_2$) is doubled[cite: 1, 2]. The app automatically displays a visual Bar Chart[cite: 1]. The chart clearly proves that doubling the safety weight instantly drops the toxicity level of the recommended content, successfully creating a cleaner and safer user environment[cite: 1, 2].