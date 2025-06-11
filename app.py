import streamlit as st

st.set_page_config(page_title="Sistem Rekomendasi Lagu", page_icon="🎵")

st.title("🎵 Sistem Rekomendasi Lagu Spotify")

st.markdown("""
Selamat datang di dashboard rekomendasi lagu berbasis data mining!

Gunakan sidebar di kiri untuk menjelajahi halaman:

- 📊 **EDA & Dataset**: Menampilkan eksplorasi data dan visualisasi
- 🤖 **Model & Clustering**: Klasterisasi lagu berdasarkan fitur
- 🔍 **Prediksi Cluster Lagu**: Lihat lagu termasuk ke cluster mana
- 🎧 **Rekomendasi Lagu Mirip**: Temukan lagu-lagu yang mirip dengan favoritmu
""")
