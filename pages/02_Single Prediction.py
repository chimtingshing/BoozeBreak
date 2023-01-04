import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="BoozeBreak", layout='wide')
st.title("Single Prediction")
#model_path = "C:/Users/user/Desktop/UM Tutorial/Year 3/Tutorial (Semester 1)/DS Project/Data/RReliefF_rf.sav"

model_path = "C:/Users/user/Desktop/UM Tutorial/Year 3/Tutorial (Semester 1)/DS Project/Data/RF_RReliefF.sav"
model = pickle.load(open(model_path, 'rb'))

low = {
    1: 'Very low',
    2: 'Low',
    3: 'Average',
    4: 'High',
    5: 'Very high'
}
bad = {
    1: 'Very bad',
    2: 'Bad',
    3: 'Average',
    4: 'Good',
    5: 'Excellent'
}
edu = {
    0: 'None',
    1: 'Lower primary',
    2: 'Upper primary to lower secondary',
    3: 'Upper secondary',
    4: 'Higher education'
}
fail = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: 'More than 3'
}
travel = {
    1: 'Less than 15 minutes',
    2: '15 minutes to 30 minutes',
    3: '30 minutes to 1 hour',
    4: '>1 hour'
}
binary = {
    0: "No",
    1: "Yes"
}
gender = {
    0: "Female",
    1: "Male"
}
address = {
    0: "Rural",
    1: "Urban"
}

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox(
        'Question 1 - What is your gender',
        options = [0, 1],
        format_func=lambda x: gender.get(x)
    )
    age = st.number_input(
        'Question 2 - What is your age (range: 12 - 22)',
        min_value=12,
        max_value=22,
        value=15
    )
    address = st.selectbox(
        'Question 3 - Are you living in urban or rural area?',
        options = [0, 1],
        format_func=lambda x: address.get(x)
    )
    fail = st.selectbox(
        'Question 4 - How many times have you failed a class',
        options=[0, 1, 2, 3, 4],
        format_func=lambda x: fail.get(x)
    )
    travel = st.selectbox(
        'Question 5 - How long does it take for you to travel to school',
        options=[1, 2, 3, 4],
        format_func=lambda x: travel.get(x)
    )
    famsup = st.selectbox(
        'Question 6 - Does your family support you educationally',
        options=[0, 1],
        format_func=lambda x: binary.get(x)
    )

with col2:
    fedu = st.selectbox(
        'Question 7 - What is your father\'s highest education level',
        options=[0, 1, 2, 3, 4],
        format_func=lambda x: edu.get(x)
    )
    medu = st.selectbox(
        'Question 8 - What is your mother\'s highest education level',
        options=[0, 1, 2, 3, 4],
        format_func=lambda x: edu.get(x)
    )
    freetime = st.selectbox(
        'Question 9 - How much free time do you have after school',
        options=[1, 2, 3, 4, 5],
        format_func=lambda x: low.get(x)
    )
    higher = st.selectbox(
        'Question 10 - Do you want to take higher education',
        options=[0, 1],
        format_func=lambda x: binary.get(x)
    )
    famrel = st.selectbox(
        'Question 11 - How are your family relationships',
        options=[1, 2, 3, 4, 5],
        format_func=lambda x: bad.get(x)
    )

threshold = st.number_input(
    'Set % threshold from 0 to 100 to predict as positive (probability must be greater than threshold to be positive)',
    min_value=0,
    max_value=100,
    value=50
)

predict = st.button(
    'Predict'
)

if predict:
    #X = np.array([fail, travel, famsup, age, address, medu, freetime, higher, famrel, fedu, gender]).reshape(1, -1)
    X = np.array([gender, age, address, fail, travel, famsup, fedu, medu, freetime, higher, famrel]).reshape(1, -1)
    proba = model.predict_proba(X)
    title = '<p style="font-size: 26px;">Prediction results</p>'
    st.markdown(title, unsafe_allow_html=True)
    if round(proba[0, 1] * 100, 2) <= threshold:
        st.success("Not addicted")
    else:
        st.error("Addicted")
    title = '<p style="font-size: 26px;">Class probabilities</p>'
    st.markdown(title, unsafe_allow_html=True)
    not_addict = str(round(proba[0, 0] * 100, 2)) + "%"
    addict = str(round(proba[0, 1] * 100, 2)) + "%"
    st.success("Not addicted : " + not_addict)
    st.error("Addicted : " + addict)