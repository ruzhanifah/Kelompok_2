import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

from utils.load_data import load_dataset

st.title("🎧 Rekomendasi Lagu Mirip")

# Load dataset
df = load_dataset()

# Fitur yang digunakan
features = [
    'danceability', 'energy', 'key', 'loudness', 'mode',
    'speechiness', 'acousticness', 'instrumentalness',
    'liveness', 'valence', 'tempo'
]

# Pastikan semua fitur ada
if not all(f in df.columns for f in features):
    st.error("Beberapa fitur tidak ditemukan di dataset.")
    st.write("Kolom tersedia:", df.columns.tolist())
    st.stop()

# Hapus data null dan siapkan fitur
df = df.dropna(subset=features)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[features])

# Input lagu yang dipilih
selected_song = st.selectbox("Pilih lagu favoritmu", df['name'] + " - " + df['artist'])

# Temukan index lagu tersebut
idx = df.index[(df['name'] + " - " + df['artist']) == selected_song][0]

# Hitung kemiripan
similarities = cosine_similarity([X_scaled[idx]], X_scaled)[0]

# Ambil top-N lagu paling mirip (selain dirinya sendiri)
df['similarity'] = similarities
recommended = df[df.index != idx].sort_values(by='similarity', ascending=False).head(5)

# Tampilkan rekomendasi
st.subheader("Lagu yang mirip:")
st.dataframe(recommended[['name', 'artist', 'genre', 'year', 'similarity']])
