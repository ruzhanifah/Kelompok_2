import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

st.title("🤖 Model: Clustering Lagu")

df = pd.read_csv("data/spotify_dataset.csv")
features = df[['danceability', 'energy', 'valence', 'tempo']]

# Standarisasi
scaler = StandardScaler()
scaled = scaler.fit_transform(features)

# Clustering
kmeans = KMeans(n_clusters=5, random_state=42)
clusters = kmeans.fit_predict(scaled)
df['cluster'] = clusters

# PCA untuk visualisasi
pca = PCA(n_components=2)
pca_result = pca.fit_transform(scaled)
df['PCA1'] = pca_result[:, 0]
df['PCA2'] = pca_result[:, 1]

st.subheader("Visualisasi Cluster")
fig, ax = plt.subplots()
scatter = ax.scatter(df['PCA1'], df['PCA2'], c=df['cluster'], cmap='tab10')
st.pyplot(fig)
