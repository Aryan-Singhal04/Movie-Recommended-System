import streamlit as st
import requests
import pickle
import pandas 

def fetch_details(m_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(m_id)
    data = requests.get(url)
    data = data.json()
    rt="runtime " +str(data['runtime']) +"min"
    rdate= "release date: "+data['release_date']
    full_path = "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    return [full_path,rt,rdate]


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])[1:6]
    mt=[]
    mp=[]
    for  i in distances:
        mt.append(movies.iloc[i[0]].title)
        mp.append(fetch_details(movies.iloc[i[0]].movie_id))
    return mt,mp

movies=pickle.load(open('movie_list.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

st.image("https://miro.medium.com/max/1200/1*oRJYoC18Msc4tC6FExYRKQ.jpeg", width=500)
st.title("Movie Recommender System")

movie_list=movies['title'].values
s_movie=st.selectbox(
    'Choose the movie you watched recently:',
    movie_list
)
if st.button("Recommend"):
    names,details=recommend(s_movie)
    st.write("Movies you can also watch")
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(details[0][0])
        st.text(details[0][1])
        st.text(details[0][2])
    with col2:
        st.text(names[1])
        st.image(details[1][0])
        st.text(details[1][1])
        st.text(details[1][2])

    with col3:
        st.text(names[2])
        st.image(details[2][0])
        st.text(details[2][1])
        st.text(details[2][2])
    with col4:
        st.text(names[3])
        st.image(details[3][0])
        st.text(details[3][1])
        st.text(details[3][2])
    with col5:
        st.text(names[4])
        st.image(details[4][0])
        st.text(details[4][1])
        st.text(details[4][2])