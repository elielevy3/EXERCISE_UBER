import streamlit as st
from utility import load_data, map, sample_data
from datetime import time

st.set_page_config(page_title="Uber Pickup Exploration 🚕", layout="wide")
st.title("Welcome to NYC Uber data exploration ! 🚕")

# get data
raw_data = load_data()

sample_size = st.sidebar.number_input("Select size of sample", min_value=1000, max_value=len(raw_data), step=1000)
st.sidebar.write("-----------")

# sample data
data = sample_data(raw_data, sample_size)

# get time parameters
start_time, end_time = st.sidebar.slider("Pick your time interval", value=(time(0, 0), time(23, 59)), format="HH:mm")
start_time = str(start_time)
end_time = str(end_time)
filtered_data = data[(data["date/time"] <= end_time) & (data["date/time"] >= start_time)][["lat", "lon"]]

st.sidebar.write("------------")

# famous points selection
famous_points = {"Central Park": {'lat': 40.785091, 'lon': -73.968285},
                 "Brooklyn Bridge":{'lat': 40.7061, "lon": -73.9969},
                 "Empire State Building": {'lat': 40.7484, 'lon': -73.9857} , 
                 "Rockefeller Center": {'lat': 40.7587, 'lon': -73.9787}, 
                 "Time Square": {'lat': 40.7580, 'lon': -73.9855}, 
                 "Madison Square Garden": {'lat': 40.7505, "lon": -73.9934}, 
                 "Yankee Stadium": {"lat": 40.8296, "lon": -73.9262}, 
                 "JFK Airport": {'lat': 40.6413, "lon": -73.7781}}

famous_point_picked = st.sidebar.selectbox("Pick a famous site to center the map", famous_points.keys())
picked_points_coordinates = famous_points[famous_point_picked]

tab1, tab2 = st.columns([1, 2])

# display dataframe
with tab1:
    st.dataframe(filtered_data)
    # st.write(len(filtered_data), "pickups")

# display map
with tab2:
    map(filtered_data, picked_points_coordinates["lat"], picked_points_coordinates["lon"])

# display code 
if st.checkbox("Display code"): 
    with open("./main.py", 'r') as file:
        st.code(file.read(), language='python')