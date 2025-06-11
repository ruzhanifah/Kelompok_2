import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/spotify_dataset.csv")

st.title("🎵 Model: Clustering Lagu Spotify")

# Pilih fitur numerik untuk model
features = ['popularity', 'duration_ms', 'total_tracks', 'position']
df_features = df[features]

# Inisialisasi dan latih model KMeans
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(df_features)

# Visualisasi hasil clustering
st.subheader("Visualisasi Clustering")
fig, ax = plt.subplots()
sns.scatterplot(x='popularity', y='duration_ms', hue='cluster', data=df, palette='Set2', ax=ax)
st.pyplot(fig)

# Info cluster
st.subheader("Statistik Setiap Cluster")
st.write(df.groupby('cluster')[features].mean())
