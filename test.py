import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit_dynamic_filters import DynamicFilters
import mysql.connector
mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="",
 database='Redbus'
)
print(mydb)

mycursor = mydb.cursor(buffered=True)

r = st.sidebar.radio('Navigation',['Home','Bus_Details'])

if r =='Home':
 st.image('C:/Users/User/Downloads/download.png')
 name = st.text_input('Enter your name: ')
 if st.button('CLICK'):
    st.write("Welcome",name)
     
if r=='Bus_Details':
 st.image('C:/Users/User/Downloads/download.png')
 #data = pd.read_csv(r"C:\Users\User\Desktop\GUVI\Redbus.csv")
 mycursor.execute('select * from Redbus.bus_routes')
 g=mycursor.fetchall()
 columns=[desc[0] for desc in mycursor.description]
 h=pd.DataFrame(g,columns=columns)
 dynamic_filters = DynamicFilters(h, filters=['State','Routename', 'Busname', 'Bustype','Departing_time','Duration','Reaching_time','Price','Bus_Rating'])

 with st.sidebar:
    dynamic_filters.display_filters()

 dynamic_filters.display_df()
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #ff000050;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    "## This is the sidebar"