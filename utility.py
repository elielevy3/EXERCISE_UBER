import streamlit as st
import pandas as pd
import pydeck as pdk
import numpy as np


# LOAD DATA ONCE
@st.experimental_singleton
def load_data(sample_size=10000):
    data = pd.read_csv(
        "uber-raw-data-sep14.csv.gz",
        nrows=sample_size,
        names=[
            "date/time",
            "lat",
            "lon",
        ],  # specify names directly since they don't change
        skiprows=1,  # don't read header since names specified directly
        usecols=[0, 1, 2],  # doesn't load last column, constant value "B02512"
        parse_dates=["date/time"],)

    data["date/time"] = pd.to_datetime(data["date/time"], format="%H:%M")
    data["date/time"] = data["date/time"].dt.strftime('%H:%M')
    return data

# lat and long correspond to the center of the plot
# we compute it by taking the average of lat and long from the data we recieve
def map(data, lat=None, lon=None):
    if lat is None:
        lat = np.average(data["lat"])
    if lon is None: 
        lon = np.average(data["lon"])

    st.write(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state={
                "latitude": lat,
                "longitude": lon,
                "zoom": 12,
                "pitch": 50,
            },
            layers=[
                pdk.Layer(
                    "HexagonLayer",
                    data=data,
                    get_position=["lon", "lat"],
                    radius=70,
                    elevation_scale=4,
                    elevation_range=[0, 1000],
                    pickable=True,
                    wireframe=True,
                    extruded=True,
                ),
            ],
        )
    )
