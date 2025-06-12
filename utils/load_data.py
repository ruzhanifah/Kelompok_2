import os
import gdown
import pandas as pd

def load_dataset():
    file_id = "1ABCdEfGhIjKlMnO1234567890"  # Ganti dengan file ID dari Google Drive
    output_path = "data/spotify_dataset.csv"

    os.makedirs("data", exist_ok=True)

    # Unduh kalau belum ada
    if not os.path.exists(output_path):
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, output_path, quiet=False)

    df = pd.read_csv(output_path)
    return df
