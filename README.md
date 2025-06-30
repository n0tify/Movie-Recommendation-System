# Movie-Recommendation-System

# 🎬 Cinematch: Your Personal Movie Recommendation System 🍿

Welcome to **Cinematch**, a content-based movie recommendation app that helps users discover new movies similar to the ones they already love!  

Built with **Python**, **Streamlit**, and the **TMDB API**, this app suggests top 5 movie recommendations based on similarity scores and provides posters, genres, ratings, and short overviews.

---

## ✨ Features

✅ Select any movie you like from a dropdown  
✅ Instantly get 5 visually engaging movie recommendations  
✅ View poster images, genres, ratings, and a short description  
✅ Simple, fast, and interactive UI built using **Streamlit**  
✅ Uses **Content-Based Filtering** (Cosine Similarity on Movie Features)  

---

## 📌 Technologies Used

- Python
- Pandas
- Scikit-Learn
- Pickle
- Streamlit
- TMDB API (for fetching posters, genres, ratings, and overviews)

---

## 🧠 How the Recommendation Works

This app uses **Content-Based Filtering** with **Cosine Similarity**:  

- Movie features (like genres, keywords, overview) were preprocessed and vectorized  
- The model calculates similarity scores between movies  
- When a user selects a movie, the system suggests other movies with the highest similarity  

---

## 🚀 Running Locally

1. **Clone the repo:**
   
git clone https://github.com/n0tify/Movie-Recommendation-System.git
cd Movie-Recommendation-System

2. Create Virtual Environment (optional but recommended):
   python -m venv venv
   venv\Scripts\activate   # For Windows

3. Install Dependencies:
   pip install -r requirements.txt

4. Set Your TMDB API Key:
 In your local environment, create a file called .streamlit/secrets.toml and add:
   [general]
TMDB_API_KEY = "your_actual_api_key_here"

5.Run the App:
  streamlit run app.py

App will open at:
http://localhost:8501

---

🌍 Deployed Live Demo
Check out the live version here 👉
https://cinematch-recommender.streamlit.app/

---

🛡️ API Key Security Note
The TMDB API Key is stored securely using Streamlit Secrets Management on deployment.

The app does not expose sensitive keys in GitHub or frontend code.

---

Folder Structure
.
├── app.py                # Streamlit App
├── artifacts/            # Pickled Model & Data Files
├── requirements.txt      # Python Dependencies
├── .gitignore
├── .gitattributes        # For Git LFS
└── README.md

---
📚 Learning Outcome
✅ Built a content-based recommendation system
✅ Integrated with external APIs (TMDB)
✅ Deployed live using Streamlit Community Cloud
✅ Practiced GitHub project workflow, LFS handling, and environment variable security

