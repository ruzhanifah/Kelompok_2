import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans

# Load dataset dan model
df = pd.read_csv("data/spotify_dataset.csv")
features = ['popularity', 'duration_ms', 'total_tracks', 'position']
df_features = df[features]

kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(df_features)

st.title("🔮 Prediksi Cluster Lagu")

# Pilih lagu dari daftar
selected_song = st.selectbox("Pilih lagu:", df['song'].unique())

# Temukan baris lagu tersebut
song_data = df[df['song'] == selected_song]

if not song_data.empty:
    cluster = song_data.iloc[0]['cluster']
    st.success(f"Lagu **{selected_song}** termasuk ke dalam Cluster **{int(cluster)}** 🎧")

    st.markdown("### Info Lagu:")
    st.write(song_data[['artist', 'popularity', 'duration_ms', 'position', 'cluster']])
else:
    st.error("Lagu tidak ditemukan dalam dataset.")
