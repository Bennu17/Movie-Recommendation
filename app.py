import streamlit as st
import pickle
import requests



movie=pickle.load(open('movie_list.pkl','rb'))
newst = pickle.load(open('similarity.pkl','rb'))
print(movie)

st.header("Movie Recommender")
select = st.selectbox("Select your movie",movie.title)


def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=79fe0a716e0fc8fcfdcdcd5040479e0b&language=en-US".format(movie_id)
     data=requests.get(url)
     data=data.json()
     poster_path = data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
     return full_path

def recommend(suggest):
         index=movie[movie['title']==suggest].index[0]
         recommend_poster=[]
         dist = sorted(list(enumerate(newst[index])),reverse=True,key=lambda vector:vector[1])
         print(dist)
         li=[]
         for i in dist[0:5]:
                  movies_id=movie.iloc[i[0]].id
                  recommend_poster.append(fetch_poster(movies_id))
                  li.append(movie.iloc[i[0]].title)
         return li,recommend_poster

if st.button("Recommend"):
         # print(select)
         x,poster=recommend(select)
         col1,col2,col3,col4,col5=st.columns(5)
         with col1:
                  st.text(x[0])
                  st.image(poster[0])
         with col2:
                  st.text(x[1])
                  st.image(poster[1])
         with col3:
                  st.text(x[2])
                  st.image(poster[2])
         with col4:
                  st.text(x[3])
                  st.image(poster[3])
         with col5:
                  st.text(x[4])
                  st.image(poster[4])


