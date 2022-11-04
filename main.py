import streamlit as st
from utility import load_data, get_map, sample_data, get_famous_points, get_filtered_data
from datetime import time

st.set_page_config(page_title="Uber Pickups Exploration", layout="wide", page_icon="🚕",     menu_items={'Get Help': 'https://github.com/elielevy3/EXERCISE_UBER',})
st.title("Welcome to NYC Uber Pickups exploration 🚕!" )

# get data
raw_data = load_data()
# remove st.experimental_memo.clear to keep same sample for a given size
sample_size = st.sidebar.number_input("Select size of sample", min_value=100, max_value=len(raw_data), step=1000, on_change=st.experimental_memo.clear)
st.sidebar.write("-----------")
data = sample_data(raw_data, sample_size)

# get time parameters
start_time, end_time = st.sidebar.slider("Pick your time interval", value=(time(0, 0), time(23, 59)), format="HH:mm")
st.sidebar.write("------------")
filtered_data = get_filtered_data(start_time, end_time, data)

# famous points
famous_points = get_famous_points()
famous_point_picked = st.sidebar.selectbox("Pick a famous site to center the map", famous_points.keys())
picked_famous_points_coordinates = famous_points[famous_point_picked]

tab1, tab2 = st.columns([1, 2])

# display dataframe
with tab1:
    st.dataframe(filtered_data)
    st.write(len(filtered_data), "pickups")

# display map
with tab2:
    get_map(filtered_data, picked_famous_points_coordinates["lat"], picked_famous_points_coordinates["lon"])

# display code 
if st.checkbox("Display code"): 
    with open("./main.py", 'r') as file:
        st.code(file.read(), language='python')