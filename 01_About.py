import streamlit as st

st.set_page_config(page_title="BoozeBreak", layout='wide')
st.title("About")
st.markdown("#### BoozeBreak")
st.markdown("The BoozeBreak application can be used to predict whether an underage person has"
            " alcohol addiction based on a set of questions. The name BoozeBreak was inspired from the slang of alcohol"
            " which is \"**booze**\" and to \"**break**\" the cycle of alcohol addiction among underage people",
            unsafe_allow_html=True)
st.markdown("There are 3 main usages of BoozeBreak which are:<br>"
            "<ul><li>Single Prediction</li>"
            "<li>Multiple Prediction</li>"
            "<li>Exploratory Data Analysis (EDA)</li></ul>", unsafe_allow_html=True)
st.markdown("For further information on how to use this application, please head to the \"**How To Use**\" page")
st.markdown("#### Alcohol Addiction")
st.markdown("Alcohol addiction is a serious problem that does not discriminate as it affects people of all ages and"
            " cultures worldwide. Following are a few statistics that show the prevalence of alcohol addiction:")
st.markdown("<ul>"
            "<li>Approximately 3 million deaths occur worldwide due to harmful use of alcohol, representing 5.3% "
            " of all deaths <sup>[1]</sup></li>"
            "<li>Alcohol contributes to 5.1% of the global burden of disease and injury <sup>[1]</sup></li>"
            "<li>Estimated amount of people having alcohol addiction globally is 107 million <sup>[2]</sup></li>"
            "<li>In 2019, 4.2 million youths (ages 12-20) in the US reported binge drinking at least once in the "
            "past month <sup>[3]</sup></li>"
            "<li>The prevalence of current drinkers among Malaysians aged between 15 - 19 years 8.3% "
            "<sup>[4]</sup></li>"
            "</ul>",
            unsafe_allow_html=True)
st.markdown("#### Machine Learning")
st.markdown("Machine learning is the subset of artificial intelligence (AI) that focuses on building systems that "
            " learns or improve performances based on the data they consume. For BoozeBreak, Random Forest, which is"
            " a type of machine learning model, was trained using questionnaire data from Portuguese secondary school "
            " students. <sup>[5]</sup> The model was fed the data and was trained to classify addiction and non-addiction"
            " based on the answers from the questionnaire.",
            unsafe_allow_html=True)
st.markdown("#### Sources")
st.markdown("<sup>[1]</sup> *Alcohol* (2022) *World Health Organization.*"
            " Available at: https://www.who.int/news-room/fact-sheets/detail/alcohol (Accessed: November 6,  2022).",
            unsafe_allow_html=True)
st.markdown("<sup>[2]</sup> Ritchie, H. and Roser, M. (2018) *Alcohol consumption, Our World in Data.* "
            "Available at: https://ourworldindata.org/alcohol-consumption (Accessed: November 6, 2022)",
            unsafe_allow_html=True)
st.markdown("<sup>[3]</sup> SAMHSA, CBHSQ. 2019 National Survey on Drug Use and Health. Table 7.16A— Alcohol "
            "Use in Lifetime, Past Year, and Past Month among Persons Aged 12 to 20, by Gender: Numbers in Thousands, "
            "2002-2019. https://www.samhsa.gov/data/sites/default/files/reports/rpt29394/NSDUHDetailedTabs2019/NSDUHDetTabsSect7pe2019.htm#tab7-16a. "
            "(Accessed: November 6, 2022)",
            unsafe_allow_html=True)
st.markdown("<sup>[4]</sup> Robert Lourdes, T. G., Abd Hamid, H. A., Riyadzi, M. R., Rodzlan Hasani, W. S., Abdul Mutalip, "
            "M. H., Abdul Jabbar, N., ... & Mohd Yusoff, M. F. (2022). Findings from a Nationwide Study on Alcohol "
            "Consumption Patterns in an Upper Middle-Income Country. *International Journal of Environmental Research and"
            " Public Health, 19*(14), 8851.",
            unsafe_allow_html=True)
st.markdown("<sup>[5]</sup> Cortez, P., & Silva, A. (2008). Using data mining to predict secondary school student "
            "performance. *EUROSIS.*",
            unsafe_allow_html=True)