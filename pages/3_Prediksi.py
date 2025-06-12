import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np

from utils.load_data import load_dataset

st.title("🔍 Prediksi Cluster Lagu")

# Load dataset
df = load_dataset()

# Definisikan fitur numerik
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

# Standarisasi data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[features].dropna())

# Melatih model
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(X_scaled)

# Form input pengguna
st.subheader("Masukkan Fitur Lagu")
input_data = {}
for feature in features:
    input_data[feature] = st.slider(feature, float(df[feature].min()), float(df[feature].max()), float(df[feature].mean()))

# Konversi ke DataFrame dan standarisasi
input_df = pd.DataFrame([input_data])
input_scaled = scaler.transform(input_df)

# Prediksi cluster
predicted_cluster = kmeans.predict(input_scaled)[0]
st.success(f"Lagu ini diprediksi masuk ke dalam **Cluster {predicted_cluster}**")
