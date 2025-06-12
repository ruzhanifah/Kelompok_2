import streamlit as st
import pandas as pd
import os
import gdown

# ========== CONFIG ========== #
st.set_page_config(page_title="Sistem Rekomendasi Lagu", page_icon="🎵")

# ========== GOOGLE DRIVE SETUP ========== #
# Ganti ID ini dengan ID Google Drive kamu
file_id = "11hiZxaux6UxIdypqFR5BFY8qGSsiz0fa"  
output_path = "data/spotify_dataset.csv"

# Buat folder data jika belum ada
os.makedirs("data", exist_ok=True)

# Download dataset hanya jika belum ada
if not os.path.exists(output_path):
    with st.spinner("📥 Mengunduh dataset dari Google Drive..."):
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, output_path, quiet=False)

# ========== LOAD DATASET ========== #
try:
    df = pd.read_csv(output_path)
    dataset_loaded = True
except Exception as e:
    st.error(f"Gagal memuat dataset: {e}")
    dataset_loaded = False

# ========== TITLE DAN DESKRIPSI ========== #
st.title("🎵 Sistem Rekomendasi Lagu Spotify")

st.markdown("""
Selamat datang di dashboard rekomendasi lagu berbasis data mining!

Gunakan sidebar di kiri untuk menjelajahi halaman:

- 📊 **EDA & Dataset**: Menampilkan eksplorasi data dan visualisasi
- 🤖 **Model & Clustering**: Klasterisasi lagu berdasarkan fitur
- 🔍 **Prediksi Cluster Lagu**: Lihat lagu termasuk ke cluster mana
- 🎧 **Rekomendasi Lagu Mirip**: Temukan lagu-lagu yang mirip dengan favoritmu
""")

# ========== TAMPILKAN CUCI DATA ========== #
if dataset_loaded:
    st.markdown("### Contoh Isi Dataset:")
    st.dataframe(df.head())
