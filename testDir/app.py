import pandas as pd
import streamlit as st
import requests
import pickle
import pandas

st.set_page_config(
   page_title="Movie Recommendation system",
   page_icon=":film:",
   layout="wide",
   initial_sidebar_state="expanded",
)
custom_css_playfair_display = """
    body {
        font-family: 'Playfair Display', serif;
        font-size: 16px;
    }
"""

st.markdown(f'<style>{custom_css_playfair_display}</style>', unsafe_allow_html=True)


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recomended_movies = []
    finalRecomendation = []
    for i in movies_list:
        recomended_movies.append(movies.iloc[i[0]].title)
        recomended_movies.append(movies.iloc[i[0]].popularity)
        tuples_list = [(recomended_movies[i], recomended_movies[i+1]) for i in range(0, len(recomended_movies), 2)]
        tuples_list = sorted(tuples_list, reverse=True, key=lambda x:x[1])
    for item in tuples_list:
        finalRecomendation.append(item[0])
    return finalRecomendation


movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))
popularity = movies['popularity']
st.title('Movie Recommendation system')

selected_movie_name = st.selectbox('Select a movie',movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)