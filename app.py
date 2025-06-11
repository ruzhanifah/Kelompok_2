import streamlit as st

st.set_page_config(page_title="Sistem Rekomendasi Lagu", layout="wide")

st.title("🎧 Sistem Rekomendasi Lagu")
st.write("""
Selamat datang di dashboard rekomendasi lagu berbasis data mining!  
Silakan gunakan sidebar kiri untuk menjelajahi halaman:
- EDA & Dataset
- Model & Clustering
- Form Rekomendasi
""")

import os
import gdown

DATA_PATH = "data/spotify_dataset.csv"
if not os.path.exists(DATA_PATH):
    url = "https://drive.google.com/file/d/12zWRkDSkljpMypSDtbh0V8jj630LKTOP/view?usp=drive_link"
    gdown.download(url, DATA_PATH, quiet=False)
