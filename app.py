import streamlit as st
import pickle
import requests

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_list = movies['title'].values

def fetch_poster(title):
    try:
        # Wikipedia API - fully accessible in India, no VPN needed
        url = "https://en.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "titles": f"{title} film",
            "prop": "pageimages",
            "format": "json",
            "pithumbsize": 300
        }
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        pages = data.get("query", {}).get("pages", {})
        for page in pages.values():
            thumbnail = page.get("thumbnail")
            if thumbnail:
                return thumbnail.get("source")
        # fallback
        return f"https://placehold.co/300x450/1a1a2e/white?text={requests.utils.quote(title)}"
    except Exception:
        return f"https://placehold.co/300x450/1a1a2e/white?text={requests.utils.quote(title)}"

def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distance = similarity[movie_index]
    similar_movies = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies = []
    recommend_movies_posters = []
    for i in similar_movies:
        title = movies.iloc[i[0]].title
        recommend_movies.append(title)
        recommend_movies_posters.append(fetch_poster(title))
    return recommend_movies, recommend_movies_posters

st.title('Movie Recommendation System')
selected_movie_name = st.selectbox('Select an option', movies_list)

if st.button('recommend'):
    names, posters = recommend(selected_movie_name)
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i], width=150)