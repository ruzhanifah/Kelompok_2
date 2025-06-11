import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("🔍 EDA dan Karakteristik Dataset")

# Load dataset
df = pd.read_csv("data/spotify_dataset.csv")

st.subheader("Cuplikan Dataset")
st.dataframe(df.head())

st.subheader("Statistik Deskriptif")
st.write(df.describe())

st.subheader("Korelasi Fitur Audio")
fig, ax = plt.subplots()
sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)
