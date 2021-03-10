import streamlit as st
import numpy as np 
import pandas as pd
from cota_app_interface import *


location_df =  pd.read_json('query_results.json')
trips = location_df['vehicle']

st.write(trips)

def get_locations(trips):
    for trip in trips:
        lat = trip['position']['latitude']
        long = trip['position']['longitude']
        route_id = trip['trip']['route_id']
        location = route_id,lat,long
        
        st.write(location)


get_locations(trips)


#Create map on webpage
st.map()





