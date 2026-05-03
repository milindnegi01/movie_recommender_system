import streamlit as st
import pandas as pd
import pickle

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_list = movies['title'].values  

def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]  
    distance = similarity[movie_index]
    similar_movies = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies = []
    for i in similar_movies:
        recommend_movies.append(movies.iloc[i[0]].title) 
    return recommend_movies

st.title('Movie Recommendation System')
selected_movie_name = st.selectbox(
    'Select an option',
    movies_list)  

if st.button('recommend'):
    recommedations = recommend(selected_movie_name)
    for i in recommedations:
        st.write(i)
