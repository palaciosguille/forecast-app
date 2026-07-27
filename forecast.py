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



if "daily" in data:
    df = pd.DataFrame(data["daily"])
    
    st.title("Weather Forecast")
    st.write("### This week's weather")
    st.dataframe(df)
    
    st.write("### Representation of this week's weather")
    st.bar_chart(df, x="time", y="temperature_2m_max")
    
    st.write("### today's max and min temperatures")
    chart_data = df.set_index("time")[["temperature_2m_max", "temperature_2m_min"]]
    st.line_chart(chart_data)
else:
    st.error("⚠️ Weather API block or error occurred.")
    st.write("Debug info from API:", data)





