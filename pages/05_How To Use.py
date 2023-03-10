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
            " threshold set by user, without showing class probabilities. Results are flagged as addicted = 1, not"
            " addicted = 0")
st.markdown("- **Class probability**: Will not flag result, instead, will only show class probabilities")
st.markdown("- **Both classification and class probability**: Will flag result based on threshold set by user while"
            " also showing class probabilities")
st.markdown("**Filters**")
st.markdown("This will only be needed for Exploratory Data Analysis (EDA), as filters needs to be chosen")
st.markdown("- **None**: No filter will be applied on the data. The whole data will be used for EDA")
st.markdown("- **Alcohol Addiction**: Only alcohol addicts data will be used for EDA")
st.markdown("- **Both classification and class probability**: Only non alcohol addicts data will be used for EDA")


st.markdown("")

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
            "<li>Observe result distribution graph below (applies when <b>type prediction</b> is "
            "<b>classification</b> or <b>both</b>)</li>"
            "</ol>",
            unsafe_allow_html=True)
st.markdown("Prerequisites of using multiple prediction:")
st.markdown("<ol>"
            "<li>Please ensure the .csv file uploaded contains the following column names <br>"
            "<b>[gender</b>, <b>age</b>, <b>address</b>, <b>failures</b>, <b>traveltime</b>, "
            "<b>famsup</b>, <b>Fedu</b>, <b>Medu</b>, <b>freetime</b>, <b>higher</b>, <b>famrel]</b><br>"
            "The ordering does not matter, but the column names <b>must</b> follow the naming convention given,"
            " to prevent any errors</li>"
            "<li>Please ensure the columns follow the correct associated values by following the format "
            "as shown in table below:<br>"
            "<a href=https://drive.google.com/file/d/1-e1l2oPJ1Ezb4DLeM7KaRVsUmxxph7sA/view?usp=share_link>Link</a><br>"
            "The columns <b>must</b> follow the correct associated values and format to ensure correct prediction "
            " and to prevent any errors"
            "</li>"
            "<li>Please make sure there are <b>no empty or null</b> values in the attached csv file</li>"
            "</ol>",
            unsafe_allow_html=True)
st.markdown("")

st.markdown("#### Exploratory Data Analysis (EDA)")
st.markdown("To use the EDA function. Kindly follow the steps below:")
st.markdown("<ol>"
            "<li>Go to the \"<b>Exploratory Data Analysis (EDA)</b>\" page</li>"
            "<li>Upload a .csv file</li>"
            "<li>Select filter (None, Alcohol Addict or Non-alcohol Addict)</li>"
            "<li>Press <b>Analyze</b> button</li>"
            "<li>Observe the generated report</li>"
            "</ol>",
            unsafe_allow_html=True)
st.markdown("Prerequisites of using Exploratory Data Analysis (EDA):")
st.markdown("<ol>"
            "<li>If Alcohol Addict and Non-alcohol Addict are chosen as filters, please ensure that a column"
            " named \"<b>addiction</b>\" is present in the dataset, if not an error will occur</li>"
            "<li>The column \"<b>addiction</b>\" is only allowed to have binary values 0 and 1, with 0 meaning"
            " non-alcohol addict and 1 meaning alcohol addict</li>"
            "</ol>",
            unsafe_allow_html=True)