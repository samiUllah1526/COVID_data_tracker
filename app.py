
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from custom_func import api_response, api_data_parser


# Hidding main menue and Footer mark of streamlit
hide_streamlit_style = """
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

url = "https://corona.lmao.ninja/v2/countries/Pakistan?yesterday&strict&query"
# Function from custom module
data = api_response(url)
stats, country_name, flag_url = api_data_parser(data)
labels = ["Cases reported today", "Deaths reported today", "Patients recovered today",
                "Active number of cases", "Patients in critical condition"]

# Showing COVID-19 stats in tabular form
st.markdown("<h1 style='text-align: center; color: Light Green;'>COVID-19 Stats</h1>", unsafe_allow_html=True)
st.subheader("Table of COVID-19 Stats")
st.markdown(" <span style='color:#cc0000'>Move the scroll bar to see complete table.</span>", unsafe_allow_html=True)
t = [stats]
table_df = pd.DataFrame(t, index=["Stats"], columns=labels)
st.write(table_df)

# Code for Graph
indexes = 1
val_of_y = stats

plt.style.use("ggplot")
# plt.title("COVID-19 Stats of Pakistan")
plt.ylabel("Number of patients or Cases")
# plt.xticks(ticks=indexes, labels=labels)
# Width of each bar on graph
width = 0.25

#todaycases
plt.bar(indexes, val_of_y[0], width=width,color='grey', label="Cases reported today")

#todaydeaths
plt.bar(indexes + width, val_of_y[1],color='red', width=width, label="Deaths reported today")

#todayRecovered
plt.bar(indexes + 2*width, val_of_y[2],color='green', width=width, label="Patients recovered today")

#ActiveCases
plt.bar(indexes + 3*width, val_of_y[3],color='#e6c34a', width=width, label="Active number of cases")

#criticalCases
plt.bar(indexes + 4*width, val_of_y[4],color='pink', width=width,label="Patients in critical condition")
plt.tight_layout()
plt.legend()
plt.yscale('log')
# fig = plt.show()


#streamlit app code
st.subheader("COVID-19 Data in Pakistan")
st.set_option('deprecation.showPyplotGlobalUse', False)
# fig, ax = plt.subplots()
st.pyplot()







