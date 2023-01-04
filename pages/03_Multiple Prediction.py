import streamlit as st
import pandas as pd
import pickle
import plotly.graph_objects as go

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder


def plot_distribution(df):
    value_counts = df['prediction'].value_counts().rename_axis("Prediction").reset_index(name="Counts")
    fig = go.Figure(go.Bar(
        x=['Not addicted (0)', 'Addicted (1)'],
        y=value_counts['Counts'],
        marker_color='#456973'
    ))
    fig.update_layout(template='plotly_white', title=dict(text='Result distribution'))
    fig.update_traces(hovertemplate = '<b>Prediction: </b>%{x}<br><b>Count: </b>%{y}<extra></extra>')
    fig.update_xaxes(title='Prediction')
    fig.update_yaxes(title='Count')
    return fig


def encode_df(df):
    # column transformer to encode data
    column_transformer = ColumnTransformer(
        [('categorical', OrdinalEncoder(), ['gender', 'famsup', 'higher', 'address'])],
        remainder='passthrough'
    )
    column_transformer.set_output(transform="pandas")
    df_encoded = column_transformer.fit_transform(df)
    df_encoded.columns = [col.replace('categorical__', '') for col in df_encoded.columns]
    df_encoded.columns = [col.replace('remainder__', '') for col in df_encoded.columns]
    return df_encoded


def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False, header=True).encode('utf-8')


def calculate_classification(df):
    df_predict = set_failure(df)
    proba = model.predict_proba(df_predict)
    proba = proba[:, 1]
    proba[proba <= (threshold / 100)] = 0
    proba[proba > (threshold / 100)] = 1
    df['prediction'] = proba
    csv = convert_df(df)
    return df, csv


def calculate_threshold(df):
    df_predict = set_failure(df)
    proba = model.predict_proba(df_predict)
    df['addicted_proba'] = proba[:, 1].round(4)
    df['not_addicted_proba'] = proba[:, 0].round(4)
    csv = convert_df(df)
    return df, csv


def calculate_classification_threshold(df):
    df_predict = set_failure(df)
    proba = model.predict_proba(df_predict)
    df['addicted_proba'] = proba[:, 1].round(4)
    df['not_addicted_proba'] = proba[:, 0].round(4)
    proba_addict = proba[:, 1]
    proba_addict[proba_addict <= (threshold / 100)] = 0
    proba_addict[proba_addict > (threshold / 100)] = 1
    df['prediction'] = proba_addict
    csv = convert_df(df)
    return df, csv


def set_failure(df):
    df_copy = df.copy()
    df_copy.loc[df_copy['failures'] > 3, 'failures'] = 4
    return df_copy


st.set_page_config(page_title="BoozeBreak", layout='wide')
st.title("Multiple Prediction")
model_path = "RF_RReliefF.sav"
model = pickle.load(open(model_path, 'rb'))

uploaded_file = st.file_uploader("Upload a csv file", type=['csv'])

type = st.selectbox(
    'Select type of prediction',
    options=['Classification', 'Class probability', 'Both classification & class probability']
)

if type != 'Threshold':
    threshold = st.number_input(
        'Set % threshold from 0 to 100 to predict as positive (probability must be greater than threshold to be positive)',
        min_value=0,
        max_value=100,
        value=50
    )

predict = st.button(
    'Predict'
)

if predict & (uploaded_file is not None):
    df = pd.read_csv(uploaded_file)
    df = encode_df(df)
    df = df[['gender', 'age', 'address', 'failures', 'traveltime', 'famsup', 'Fedu', 'Medu',
            'freetime', 'higher', 'famrel']]
    if type == 'Classification':
        df, csv = calculate_classification(df)
        st.write(df)
        st.download_button(
            'Download data as csv',
            data=csv,
            file_name="classification.csv"
        )
        fig = plot_distribution(df)
        st.plotly_chart(fig, theme='streamlit')
    elif type == 'Class probability':
        df, csv = calculate_threshold(df)
        st.write(df)
        st.download_button(
            'Download data as csv',
            data=csv,
            file_name="threshold.csv"
        )
    else:
        df, csv = calculate_classification_threshold(df)
        st.write(df)
        st.download_button(
            'Download data as csv',
            data=csv,
            file_name="classification_and_probability.csv"
        )
        fig = plot_distribution(df)
        st.plotly_chart(fig, theme='streamlit')
elif predict & (uploaded_file is None):
    st.error('Please upload a file first')
