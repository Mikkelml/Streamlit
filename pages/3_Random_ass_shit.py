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


st.title("Weather Forecast")




with st.container():
    base_url = 'https://api.openweathermap.org/data/2.5/weather?'
    API_key = 'b765e9524535b7f51e9fbc2cce7f076d'    

    st.write('Choose your city to see the weather forecast')
    city_list = pd.read_csv('/Users/mikkelpedersen/Desktop/project_vs_studio/wheater_api/cities_list.csv', delimiter=';')
    st.dataframe(city_list, width=800, height=500)

    def kelvin_to_celcius_fahrenhit(kelvin):
        celcius = kelvin - 273.15
        fahrenheit = celcius * (9/5) + 32
        return celcius, fahrenheit
    
    city_name = st.text_input("Enter a city name you like:")

    def see_forecast(city_name):
        if city_name:
            url_forecast = f"{base_url}appid={API_key}&q={city_name}"
            try:
                wforecast = requests.get(url_forecast).json()

                wfcity_name = wforecast['name']
                wflat_city = wforecast['coord']['lat']
                wflon_city = wforecast['coord']['lon']
                wfcountry = wforecast['sys']['country']

                wftemp_kelvin = wforecast['main']['temp']
                wftemp_celcius, wftemp_fahrenheit = kelvin_to_celcius_fahrenhit(wftemp_kelvin)
                wffeels_like = wforecast['main']['feels_like']
                wffeels_like_celsius, wffeels_like_fahrenheit = kelvin_to_celcius_fahrenhit(wffeels_like)
                wfhumidity = wforecast['main']['humidity']
                wfwindspeed = wforecast['wind']['speed']
                wfdescription = wforecast['weather'][0]['description']
                wfclouds = wforecast['clouds']['all']

                timezone_offset = wforecast['timezone']
                wfsunrise_time = dt.datetime.utcfromtimestamp(wforecast['sys']['sunrise'] + timezone_offset)
                wfsunset_time = dt.datetime.utcfromtimestamp(wforecast['sys']['sunset'] + timezone_offset)
                
                col_uno, col_dos = st.columns(2)
                with col_uno:
                    st.write(f"### City info: {wfcity_name}")
                    st.write(f"**Country**: {wfcountry}")
                    st.write(f"**Coordinates**: Longitude {wflon_city}, Latitude {wflat_city}")
                    
                with col_dos:
                    st.write(f'### Weather info: ')
                    st.write(f"**Temperature**: {round(wftemp_celcius, 2)}°C / {round(wftemp_fahrenheit, 2)}°F")
                    st.write(f"**Feels Like**: {round(wffeels_like_celsius, 2)}°C / {round(wffeels_like_fahrenheit, 2)}°F")
                    st.write(f"**Humidity**: {wfhumidity}%")
                    st.write(f"**Wind Speed**: {wfwindspeed} m/s")
                    st.write(f"**Weather**: {wfdescription.capitalize()}")
                    st.write(f"**Cloud Cover**: {wfclouds}%")
                    st.write(f"**Sunrise**: {wfsunrise_time.strftime('%H:%M:%S')}")
                    st.write(f"**Sunset**: {wfsunset_time.strftime('%H:%M:%S')}")
            
            except KeyError:
                st.error("City not found. Please check the city name and try again.")
            except requests.exceptions.RequestException as e:
                st.error(f"Error: {e}")

    # Display the forecast when a city name is entered
    if city_name:
        see_forecast(city_name)

