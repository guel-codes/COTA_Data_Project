import streamlit as st
import numpy as np 
import pandas as pd
from cota_app_interface import *


location_df =  pd.read_json('query_results.json')
trips = location_df['vehicle']


#lists to be put into DataFrame
lat_list = []
long_list = []
route_id_list = []

def get_locations(trips):
    for trip in trips:
        route_id = trip['trip']['route_id']
        route_id_list.append(route_id)
        lat = float(trip['position']['latitude'])
        lat_list.append(lat)
        long = float(trip['position']['longitude'])
        long_list.append(long)
        
        location_df = pd.DataFrame({
            'route_id' : route_id_list,
            'latitude' : lat_list,
            'longitude': long_list
        })
    #Create map on webpage
    st.map(location_df)
      


get_locations(trips)











