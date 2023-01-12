import streamlit as st
import pandas as pd

from streamlit_pandas_profiling import st_profile_report

st.set_page_config(page_title="BoozeBreak", layout='wide')
st.title("Exploratory Data Analysis (EDA)")

uploaded_file = st.file_uploader("Upload a csv file", type=['csv'])

filter = st.selectbox(
    'Select filter',
    options=['None', 'Alcohol Addict', 'Non-alcohol Addict']
)

analyze = st.button(
    'Analyze'
)

if analyze & (uploaded_file is not None):
    if filter == 'Alcohol Addict':
        df = pd.read_csv(uploaded_file)
        df = df[df['addiction'] == 1]
    elif filter == 'Non-alcohol Addict':
        df = pd.read_csv(uploaded_file)
        df = df[df['addiction'] == 0]
    else:
        df = pd.read_csv(uploaded_file)
    report = df.profile_report()
    st_profile_report(report)
elif analyze & (uploaded_file is None):
    st.error('Please upload a file first')
