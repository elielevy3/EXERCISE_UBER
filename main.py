import streamlit as st
from utility import load_data, map
from datetime import time

st.set_page_config(page_title="Uber Pickup Exploration")
st.title("Welcome to NYC Uber data exploration")

# famous points selection
famous_points = {"Central Park": {'lat': 40.785091, 'lon': -73.968285},
                 "Brooklyn Bridge":{'lat': 40.7061, "lon": -73.9969},
                 "Empire State Building": {'lat': 40.7484, 'lon': -73.9857} , 
                 "Rockefeller Center": {'lat': 40.7587, 'lon': -73.9787}, 
                 "Time Square": {'lat': 40.7580, 'lon': -73.9855}, 
                 "Madison Square Garden": {'lat': 40.7505, "lon": -73.9934}, 
                 "Yankee Stadium": {"lat": 40.8296, "lon": -73.9262}, 
                 "JFK Airport": {'lat': 40.6413, "lon": -73.7781}}
famous_point_picked = st.selectbox("Pick a famous site", famous_points.keys())
picked_points_coordinates = famous_points[famous_point_picked]

# get time parameters
start_time, end_time = st.sidebar.slider("Pick your time interval", value=(time(0, 0), time(23, 59)), format="HH:mm")
start_time = str(start_time)
end_time = str(end_time)

# get and filter data
data = load_data()
filtered_data = data[(data["date/time"] < end_time) & (data["date/time"] > start_time)][["lat", "lon"]]

# display map
map(filtered_data, picked_points_coordinates["lat"], picked_points_coordinates["lon"])

# resampling option
sample_size = st.sidebar.number_input("Pcik a sample size", min_value=1, max_value=1000000)
st.sidebar.button("Wanna resample ?")



