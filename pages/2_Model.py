import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

from utils.load_data import load_dataset

st.title("🤖 Model & Clustering")

# Load dataset
df = load_dataset()

# Pilih fitur numerik untuk clustering
features = [
    'danceability', 'energy', 'key', 'loudness', 'mode',
    'speechiness', 'acousticness', 'instrumentalness',
    'liveness', 'valence', 'tempo'
]

# Pastikan semua fitur tersedia
if not all(feature in df.columns for feature in features):
    st.error("Beberapa fitur tidak ditemukan di dataset. Pastikan dataset sudah benar.")
    st.write("Fitur yang dibutuhkan:", features)
    st.write("Kolom yang tersedia:", df.columns.tolist())
    st.stop()

df_features = df[features].dropna()

# Standarisasi data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_features)

# Pilih jumlah cluster
n_clusters = st.slider("Pilih jumlah cluster", min_value=2, max_value=10, value=4)

# KMeans clustering
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Visualisasi cluster
st.subheader("Visualisasi Cluster (2D PCA)")
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
components = pca.fit_transform(X_scaled)
df['pca1'] = components[:, 0]
df['pca2'] = components[:, 1]

plt.figure(figsize=(10, 6))
sns.scatterplot(x='pca1', y='pca2', hue='Cluster', data=df, palette='tab10')
plt.title("Visualisasi Cluster dengan PCA")
st.pyplot(plt)

# Tampilkan data hasil clustering
st.subheader("Contoh Hasil Klasterisasi")
st.dataframe(df[['name', 'artist', 'Cluster'] + features].head(20))
