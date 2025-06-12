import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

from utils.load_data import load_dataset

st.title("🤖 Model & Clustering Lagu")

# Load data
df = load_dataset()

# Fitur yang digunakan untuk clustering
features = [
    'danceability', 'energy', 'loudness', 'speechiness',
    'acousticness', 'instrumentalness', 'liveness',
    'valence', 'tempo'
]

# Pastikan semua fitur tersedia
missing_cols = [col for col in features if col not in df.columns]
if missing_cols:
    st.error(f"Kolom berikut tidak ditemukan di dataset: {missing_cols}")
    st.stop()

# Preprocessing
df_features = df[features]
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df_features)

# KMeans clustering
k = st.slider("Pilih jumlah cluster (K)", 2, 10, 4)
model = KMeans(n_clusters=k, random_state=42)
df['Cluster'] = model.fit_predict(scaled_features)

st.subheader("📊 Visualisasi Cluster")

# Visualisasi pakai 2D PCA (opsional)
try:
    from sklearn.decomposition import PCA
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(scaled_features)
    df['PCA1'] = pca_result[:, 0]
    df['PCA2'] = pca_result[:, 1]

    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x='PCA1', y='PCA2', hue='Cluster', palette='tab10', ax=ax)
    st.pyplot(fig)
except:
    st.warning("Gagal visualisasi PCA. Pastikan `scikit-learn` dan `matplotlib` sudah terpasang.")

# Tampilkan data hasil clustering
st.subheader("📝 Hasil Klasterisasi")
st.dataframe(df[['track_name', 'artist_name', 'Cluster'] + features])
