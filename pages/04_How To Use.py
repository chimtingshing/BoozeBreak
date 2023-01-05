import streamlit as st

st.set_page_config(page_title="BoozeBreak", layout='wide')
st.title("How To Use")
st.markdown("#### Understanding Technical Terms")
st.markdown("Before looking into how to use BoozeBreak, please try to understand the technical terms below which is"
            " used throughout the application to ensure full understanding of the functionality of BoozeBreak")
st.markdown("**Class Probability**")
st.markdown("- The machine learning model essentially predicts whether an underage person has alcohol addiction or"
            " not. Class probabilities shows the **probability** that someone is addicted or not addicted that is "
            " calculated by the machine learning model")
st.markdown("**Threshold**")
st.markdown("- Normally, when the calculated probability of addicted is **greater** than 50%, the results will"
            " be automatically flagged as addicted. However, BoozeBreak allows flexibility in setting the percentage "
            " mentioned earlier, which is what threshold is")
st.markdown("- For example, if you set the threshold to 60%, the machine learning model will only flag results as "
            " addicted only if the probability of addicted is **greater** than 60%. Probability **equal to or lower** "
            " than 60% will be flagged as not addicted")
st.markdown("**Type of Predictions**")
st.markdown("This will only be needed for multiple prediction, as type of prediction needs to be chosen")
st.markdown("- **Classification**: Will flag results as addicted or not addicted based on calculated probability and"
            " threshold set by user, without showing class probabilities")
st.markdown("- **Class probability**: Will not flag result, instead, will only show class probabilities")
st.markdown("- **Both classification and class probability**: Will flag result based on threshold set by user while"
            " also showing class probabilities")
st.markdown("#### Single Prediction")
st.markdown("To use the single prediction function. Kindly follow the steps below:")
st.markdown("<ol>"
            "<li>Go to the \"<b>Single Prediction</b>\" page</li>"
            "<li>Answer <b>all</b> 11 questions presented</li>"
            "<li>Set threshold</li>"
            "<li>Press <b>Predict</b> button</li>"
            "<li>Observe prediction results & class probabilities</li>"
            "</ol>",
            unsafe_allow_html=True)
st.markdown("")
st.markdown("#### Multiple Prediction")
st.markdown("To use the multiple prediction function. Kindly follow the steps below:")
st.markdown("<ol>"
            "<li>Go to the \"<b>Multiple Prediction</b>\" page</li>"
            "<li>Upload a .csv file</li>"
            "<li>Select type of prediction (classification, threshold or both) </li>"
            "<li>Set threshold if needed</li>"
            "<li>Press <b>Predict</b> button</li>"
            "<li>Preview output csv file</li>"
            "<li>Download output csv file</li>"
            "<li>Observe result distribution graph below (only for classification and both)</li>"
            "</ol>",
            unsafe_allow_html=True)
st.markdown("Prerequisites of using multiple prediction:")
st.markdown("<ol>"
            "<li>Please ensure the .csv file uploaded contains the following column names <br>"
            "[<b>gender</b>, <b>age</b>, <b>address</b>, <b>failures</b>, <b>traveltime</b>, "
            "<b>famsup</b>, <b>Fedu</b>, <b>Medu</b>, <b>freetime</b>, <b>higher</b>, <b>famrel</b>]<br>"
            "The ordering does not matter, but the column names <b>must</b> follow the naming convention given,"
            " to prevent any errors</li>"
            "<li>Please ensure the columns follow the correct associated values by following the format "
            "as shown in table below:<br>"
            "<a href=https://drive.google.com/file/d/1-e1l2oPJ1Ezb4DLeM7KaRVsUmxxph7sA/view?usp=share_link>Link</a><br>"
            "The columns <b>must</b> follow the correct associated values and format to ensure correct prediction "
            " and to prevent any errors"
            "</li>"
            "</ol>",
            unsafe_allow_html=True)
