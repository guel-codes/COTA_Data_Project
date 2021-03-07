import streamlit as st
import numpy as np 
import pandas as pd

# Setting up page.
st.title('COTA Live Update App')
st.write('This app will ingest streamed data from the Smart Columbus website and show real-time COTA bus locations.')
st.subheader('Vehicle Series from Location DataFrame')

location_df =  pd.read_json('query_results.json')
trips = location_df['vehicle']



st.write(trips)


#Create map on webpage
st.map()





