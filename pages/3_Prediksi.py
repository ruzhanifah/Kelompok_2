import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

st.title("🎶 Rekomendasi Lagu")

df = pd.read_csv("data/spotify_dataset.csv")
feature_cols = ['danceability', 'energy', 'valence', 'tempo']

song_titles = df['title'].unique()
selected_song = st.selectbox("Pilih lagu favorit kamu:", song_titles)

if selected_song:
    song_vector = df[df['title'] == selected_song][feature_cols].values
    all_vectors = df[feature_cols].values
    sim_scores = cosine_similarity(song_vector, all_vectors)[0]
    
    df['similarity'] = sim_scores
    rekomendasi = df.sort_values(by='similarity', ascending=False).head(6)[['title', 'artist', 'similarity']]
    rekomendasi = rekomendasi[df['title'] != selected_song]

    st.subheader("Lagu yang Direkomendasikan:")
    st.dataframe(rekomendasi.reset_index(drop=True))
