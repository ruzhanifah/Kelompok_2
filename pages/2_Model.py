import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

from utils.load_data import load_dataset

st.title("🤖 Model & Clustering Lagu Spotify")

# Load dataset
df = load_dataset()

# Tampilkan nama kolom untuk debugging (bisa dihapus nanti)
# st.write("Kolom dalam dataset:", df.columns.tolist())

# Ubah nama kolom agar konsisten (huruf kecil & underscore)
df.columns = df.columns.str.lower().str.replace(" ", "_")

# Fitur yang digunakan untuk clustering
features = [
    'danceability', 'energy', 'loudness', 'speechiness',
    'acousticness', 'instrumentalness', 'liveness',
    'valence', 'tempo'
]

# Pastikan semua kolom fitur tersedia
missing_cols = [col for col in features if col not in df.columns]
if missing_cols:
    st.error(f"Kolom berikut tidak ditemukan di dataset: {missing_cols}")
    st.stop()

# Ambil hanya kolom fitur
df_features = df[features]

# Normalisasi fitur
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df_features)

# Slider jumlah cluster
k = st.slider("Pilih jumlah cluster (K)", 2, 10, 4)

# Buat model KMeans
model = KMeans(n_clusters=k, random_state=42, n_init=10)
cluster_labels = model.fit_predict(scaled_features)

# Tambahkan hasil cluster ke DataFrame
df['cluster'] = cluster_labels

# PCA untuk visualisasi 2D
pca = PCA(n_components=2)
pca_result = pca.fit_transform(scaled_features)
df['pca1'] = pca_result[:, 0]
df['pca2'] = pca_result[:, 1]

# Visualisasi Cluster
st.subheader("📊 Visualisasi Cluster (PCA)")
fig, ax = plt.subplots()
sns.scatterplot(data=df, x='pca1', y='pca2', hue='cluster', palette='tab10', ax=ax)
plt.title("Visualisasi Cluster Lagu")
st.pyplot(fig)

# Tampilkan hasil klasterisasi
st.subheader("📝 Hasil Klasterisasi Lagu")
st.dataframe(df[['track_name', 'artist_name', 'cluster'] + features])
