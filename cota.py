import streamlit as st
import numpy as np 
import pandas as pd
from cota_app_interface import *


location_df =  pd.read_json('query_results.json')
trips = location_df['vehicle']


#lists to be put into DataFrame
route_id_list = []
lat_list = []
long_list = []


def map_bus_locations(trips):
    for trip in trips:
        route_id = trip['trip']['route_id']
        route_id_list.append(route_id)
        lat = float(trip['position']['latitude'])
        lat_list.append(lat)
        long = float(trip['position']['longitude'])
        long_list.append(long)
        

        new_location_df = pd.DataFrame({
        'route_id' : route_id_list,
        'latitude' : lat_list,
        'longitude': long_list
        })  
    
    return st.map(new_location_df)


    



map_bus_locations(trips)











