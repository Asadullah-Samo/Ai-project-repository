# AI Lab Project Short Report

**Project Topic:** A Personalized News Feed and Reels Recommender (TikTok & YouTube Algorithm Simulation)

**Team Details:**

1. Asadullah Samo (Roll No: 2K23/CSEE/19) - Team Leader
2. Mudasir Dasti (Roll No: 2K23/CSEE/48) - Team Member

**Submitted To:** Mr. Rajesh Kumar

---

### 1. Problem Statement

Social media platforms like TikTok and YouTube operate in a "Partially Observable" environment. Since the application cannot directly read a user's mind, it relies on digital footprints like watch-time and clicks to guess their preferences. The main challenge these companies face is balancing two things: recommending highly engaging videos to keep the user active, while actively filtering out toxic content or dangerous clickbait. Our project simulates exactly how these background algorithms manage this balance between User Engagement and Content Safety.

### 2. AI Methodology

For our simulation, we implemented a Multi-Attribute Utility Optimization approach. We use a mathematical Utility Function ($U$) to score and rank the videos in the dataset:

$$U = w_1 \cdot E(c) - w_2 \cdot S(c)$$

* **$E(c)$ (Engagement Score):** This value shows how interesting or viral a video is.
* **$S(c)$ (Toxicity Score):** This value represents the clickbait or risk level of the video.
* **$w_1$ and $w_2$ (Weights):** These are our algorithm tuning controls.

The algorithm calculates the final utility score for every video in the database and pushes the ones with the highest scores to the top of the user's feed.

### 3. Visual UI and Explainability

To make the project interactive rather than just a terminal script, we built a web interface using Python's Streamlit library.

* **Interactive Controls:** We added dynamic sliders in the sidebar so the user can tweak the algorithm weights ($w_1$ and $w_2$) on the fly.
* **Visual Representation:** The re-ranked video feed is instantly updated and displayed in a clean data table.
* **Explainability (XAI):** We included an automated info box that explains in plain English why a specific video was chosen for the #1 spot, making the AI's decision-making process transparent.

### 4. Evaluation and Results

To prove that our algorithm actually works, we built an evaluation panel featuring a "Test Safe Mode" button. When clicked, the system doubles the safety penalty weight ($w_2$) and compares the new results with the baseline feed. A Matplotlib bar chart is automatically generated, visually proving to the user that increasing the safety parameter successfully drops the toxicity level of the top-ranked videos, resulting in a cleaner feed.