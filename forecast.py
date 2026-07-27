import streamlit as st
import pandas as pd
import geocoder


st.set_page_config(layout="wide")

g = geocoder.ip('me')
latitude, longitude = g.latlng
print(latitude)
print(longitude)

import requests

url = (
    f"https://api.open-meteo.com/v1/forecast"
    f"?latitude={latitude}"
    f"&longitude={longitude}"
    f"&daily=temperature_2m_max,temperature_2m_min"
    f"&timezone=auto"
)

data = requests.get(url).json()
df = pd.DataFrame(data["daily"])



st.title("Weather Forecast")

st.markdown("#### ") 

st.write("### This week's weather")

st.dataframe(df)

st.markdown("### ") 

st.write("### Representation of this week's weather")

st.bar_chart(df, x="time", y="temperature_2m_max")

st.markdown("### ") 

st.write("### today's max and min temperatures")

st.line_chart(df[["temperature_2m_max", "temperature_2m_min"]])





