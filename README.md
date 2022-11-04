# EXERCISE_UBER
Streamlit exercice for the 17/11/2022 Wyseday


## Useful functions in utility.py

### load_data(): return a dataframe with the following columns: 

#### - Latitude of the pickup
#### - Longitude of the pickup
#### - Hour of the pickup (HH:MM)


----------------------------
                                                              
- sample_data(data, sample_size): - return a sample of the dataframe [data] of size [sample_size]

- get_map(data, lat=None, lon=None): - return None but write a Pydeck plot including datapoints in data that must be of the form ["lat", "lon"]
                                     - lat and lon parameters are used to determine the initial center of the map plot
                                     
- get_famous_points(): return a dictionnary of the following shape: {"Famous point name": {"lat": val, "lon": val}}

- get_filtered_data(start_time, end_time, data): - return a dataframe with of the following shape: ["lat", "lon"]
                                                 - start_time and end_time must be of type datetime
                                                 - data must be of the shape ["date/time", "lat", "lon"] with "date/time" as string
                                           
