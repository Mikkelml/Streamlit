import streamlit as st
import datetime as dt
import requests
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from datetime import date
from datetime import datetime

st.page_link('/Users/mikkelpedersen/Desktop/project_vs_studio/streamlit_app/Main_page.py', icon='🏛️', label='Home')


st.title('random ass shitt')




with st.container():
    st.write('This is a random ass shit')
    st.write('This is a random ass shit')
    st.write('This is a random ass shit')
    
    base_url = 'https://api.openweathermap.org/data/2.5/weather?'
    API_key = 'b765e9524535b7f51e9fbc2cce7f076d'    
    city = 'Frederiksberg'
    url = base_url + 'appid=' + API_key + '&q=' + city
    response = requests.get(url).json()  
    
    city_list = pd.read_csv('/Users/mikkelpedersen/Desktop/project_vs_studio/wheater_api/cities_list.csv', delimiter=';')
    st.write(city_list)
