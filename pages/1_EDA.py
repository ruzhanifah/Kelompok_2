import streamlit as st
import pandas as pd
from utils.load_data import load_dataset

df = load_dataset()

st.title("📊 EDA & Dataset")
st.write(df.head())
