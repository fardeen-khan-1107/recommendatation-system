import streamlit as st
import pickle
import pandas as pd
import requests

def fetch(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8dff1e6867e1639420c3533f0235cc04'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch(movie_id))
    return recommended_movies, recommended_movies_poster

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("Recommendation System")

option = st.selectbox(
    'Select a movie for recommendation:',
    movies['title'].values)

if st.button('Recommend'):
    recommendation, posters = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)  # Corrected function name
    with col1:
        st.header(recommendation[0])
        st.image(posters[0])
    with col2:
        st.header(recommendation[1])
        st.image(posters[1])
    with col3:
        st.header(recommendation[2])
        st.image(posters[2])
    with col4:
        st.header(recommendation[3])
        st.image(posters[3])
    with col5:
        st.header(recommendation[4])
        st.image(posters[4])
