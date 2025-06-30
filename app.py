import streamlit as st
import pickle
import pandas as pd
import requests

# ✅ Load preprocessed data
movies = pickle.load(open('artifacts/movies.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))


API_KEY = st.secrets["TMDB_API_KEY"]  # ✅ Fetch API key securely

# ✅ Fetch movie details and poster from TMDB API
def fetch_movie_details(movie_id):
    try:
        url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US'
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            poster_path = data.get('poster_path')
            genres = ", ".join([g['name'] for g in data.get('genres', [])]) or "Unknown Genre"
            rating = data.get('vote_average', 'N/A')
            overview = data.get('overview', 'No overview available.')[:300] + '...'
            poster_url = f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else "https://via.placeholder.com/500x750?text=No+Image"
            return poster_url, genres, rating, overview
    except:
        pass
    return "https://via.placeholder.com/500x750?text=No+Image", "Unknown", "N/A", "No details available."

# ✅ Generate recommendations
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = sorted(enumerate(similarity[movie_index]), reverse=True, key=lambda x: x[1])[1:]

    recommended = []
    idx = 0
    while len(recommended) < 5 and idx < len(distances):
        i = distances[idx][0]
        movie_id = movies.iloc[i].movie_id
        poster, genres, rating, overview = fetch_movie_details(movie_id)

        if poster and 'No+Image' not in poster:
            recommended.append({
                'title': movies.iloc[i].title,
                'poster': poster,
                'genres': genres,
                'rating': rating,
                'overview': overview
            })
        idx += 1

    while len(recommended) < 5:
        recommended.append({
            'title': "No Title Found",
            'poster': "https://via.placeholder.com/500x750?text=No+Image",
            'genres': "N/A",
            'rating': "N/A",
            'overview': "No details available."
        })

    return recommended

# ✅ Streamlit Page Setup
st.set_page_config(page_title="🎬 Cinematch: Your Movie Matchmaker 🍿", layout="wide")

# ✅ Custom CSS for Styling
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #330000, #000000);
    color: white;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
h1, h2, h3 {
    color: #FF4C61;
    text-align: center;
    text-shadow: 2px 2px 6px black;
}
.movie-card {
    background: rgba(255, 255, 255, 0.06);
    backdrop-filter: blur(10px);
    border-radius: 12px;
    padding: 12px;
    margin: 12px;
    box-shadow: 0 8px 18px rgba(0,0,0,0.5);
    text-align: center;
    transition: 0.3s ease-in-out;
}
.movie-card:hover {
    transform: scale(1.04);
    box-shadow: 0 12px 24px rgba(255,76,97,0.7);
}
.stButton>button {
    background-color: #FF1E56;
    color: white;
    font-size: 16px;
    border-radius: 8px;
    padding: 8px 18px;
    border: none;
    transition: 0.3s ease-in-out;
}
.stButton>button:hover {
    background-color: #e60039;
    transform: scale(1.05);
}
img {
    border-radius: 10px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.4);
    transition: 0.2s;
}
img:hover {
    transform: scale(1.02);
}
</style>
""", unsafe_allow_html=True)

# ✅ Main App Title and Subheading
st.markdown('<h1>🍿 Cinematch: Your Personal Movie Matchmaker 🎥</h1>', unsafe_allow_html=True)
st.markdown('<h3>Tell us one movie you love... We’ll suggest five more you might vibe with!</h3>', unsafe_allow_html=True)

# ✅ Movie Dropdown
selected_movie = st.selectbox('🎯 Pick a Movie You Like:', movies['title'].values)

# ✅ On Button Click: Show Recommendations
if st.button('🚀 Get Recommendations'):
    with st.spinner('Loading movie magic... ✨'):
        results = recommend(selected_movie)

        st.markdown("## 🎬 Top 5 Movie Picks for You")

        cols = st.columns(5)
        for idx, movie in enumerate(results):
            with cols[idx]:
                st.markdown(f"<div class='movie-card'>", unsafe_allow_html=True)
                st.image(movie['poster'], use_container_width=True)
                st.markdown(f"### {movie['title']}", unsafe_allow_html=True)
                st.markdown(f"🎭 **Genre:** {movie['genres']}", unsafe_allow_html=True)
                st.markdown(f"⭐ **Rating:** {movie['rating']}", unsafe_allow_html=True)
                st.markdown(f"📝 **Overview:** {movie['overview']}", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
