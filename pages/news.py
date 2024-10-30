import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 
import json
import requests
import datetime as dt 
from datetime import datetime, date
import re
import random
from pynytimes import NYTAPI
import warnings

st.set_page_config(page_title='Learning ToDo', page_icon='🤔', initial_sidebar_state='collapsed')

st.page_link('/Users/mikkelpedersen/Documents/GitHub/Streamlit/Main_page.py', icon='🏛️', label='Home')

st.title('News app')

api_id = 'xxx'
api_key = 'xxx'
api_secret = 'xxx'

nyt = NYTAPI(api_key, parse_dates=True)
