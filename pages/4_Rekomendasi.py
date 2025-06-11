import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("data/spotify_dataset.csv")

# Pilih fitur numerik
features = ['popularity', 'duration_ms', 'total_tracks', 'position']
df_features = df[features]

# Normalisasi data (optional tapi disarankan)
df_norm = (df_features - df_features.min()) / (df_features.max() - df_features.min())

st.title("🎧 Rekomendasi Lagu Mirip")

# Pilih lagu
selected_song = st.selectbox("Pilih lagu:", df['song'].unique())

# Temukan index lagu
song_idx = df[df['song'] == selected_song].index[0]

# Hitung kemiripan
similarity_scores = cosine_similarity([df_norm.loc[song_idx]], df_norm)[0]

# Ambil 5 lagu mirip teratas (selain diri sendiri)
top_indices = similarity_scores.argsort()[::-1][1:6]

st.subheader("Lagu yang Mirip:")
for i in top_indices:
    title = df.iloc[i]['song']
    artist = df.iloc[i]['artist']
    score = similarity_scores[i]
    st.markdown(f"**🎵 {title}** by *{artist}* (Skor kemiripan: `{score:.2f}`)")
