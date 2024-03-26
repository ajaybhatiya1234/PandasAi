import pickle
from pathlib import Path
import pandas as pd
import streamlit as st

##For multiple dataset files with pkl format
# def load_file(path: str) -> pd.DataFrame:
#     with open(path, "rb") as f:
#         dataset = pickle.load(f)
#         return dataset


# @st.cache_data
# def load_data(folder: str) -> pd.DataFrame:
#     all_datasets = [load_file(file) for file in Path(folder).iterdir()]
#     df = pd.concat(all_datasets)
#     return df


@st.cache_data
def load_data(uploaded_file) -> pd.DataFrame:
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        return df
    else:
        print("Uploaded file is empty!!!")
    



