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

st.page_link('/Users/mikkelpedersen/Documents/GitHub/Streamlit/Main_page.py', icon='🏛️', label='Home')


st.title('random ass shittt')




with st.container():
    base_url = 'https://api.openweathermap.org/data/2.5/weather?'
    API_key = 'b765e9524535b7f51e9fbc2cce7f076d'    
    city = 'Frederiksberg'
    url = base_url + 'appid=' + API_key + '&q=' + city
    response = requests.get(url).json()  
    
    
    st.write('Choose your city to see the weather forecast')
    city_list = pd.read_csv('/Users/mikkelpedersen/Desktop/project_vs_studio/wheater_api/cities_list.csv', delimiter=';')
    st.dataframe(city_list, width=800, height=500)


    def kelvin_to_celcius_fahrenhit(kelvin):
    celcius = kelvin - 273
    fahrenheit = celcius * (9/5) + 32
    return celcius, fahrenheit

    def see_forecast(city_name):
    url_forecast = base_url + 'appid=' + API_key + '&q=' + city_name
    wforecast = requests.get(url_forecast).json()  
    
    wfcity_name = wforecast['name']
    wflat_city = wforecast['coord']['lat']
    wflon_city = wforecast['coord']['lon']
    wfcountry = wforecast['sys']['country']

    wftemp_kelvin = wforecast['main']['temp']
    wftemp_celcius, wftemp_fahrenhit = kelvin_to_celcius_fahrenhit(wftemp_kelvin)
    wffeels_like = wforecast['main']['feels_like']
    wffeels_like_celsius, wffeels_like_fahrenhit = kelvin_to_celcius_fahrenhit(wffeels_like)
    wfhumidity = wforecast['main']['humidity']
    wfwindspeed = wforecast['wind']['speed']
    wfdescription = wforecast['weather'][0]['description']
    wfclouds = wforecast['clouds']['all']

    wfsunrise_time = dt.datetime.utcfromtimestamp(wforecast['sys']['sunrise'] + wforecast['timezone'])
    wfsunset_time = dt.datetime.utcfromtimestamp(wforecast['sys']['sunset'] + wforecast['timezone'])
    
    
    print(f'This is the city of which you are seeing the weather forecast: {wfcity_name}')
    print(f'This is the longtitude: {wflon_city} and latitude: {wflat_city} of the city')
    print(f'this is the county of the city: {wfcountry}')
    print(f'the temp is {round(wftemp_celcius,2)} in celsius, and {round(wftemp_fahrenhit, 2)} fahrenhit')
    print(f'The tempature feels like {round(wffeels_like_celsius,2)} in celsius and {round(wffeels_like_fahrenhit,2)} in fahrenhit')
    print(f'The humidity is: {wfhumidity}')
    print(f'The windspeed is: {wfwindspeed}')
    print(f'Today the weather is {wfdescription}')
    print(f'The amount of clouds is: {wfclouds}')
    print(f'Today the sun will rise at {wfsunrise_time} and set at {wfsunset_time}')
