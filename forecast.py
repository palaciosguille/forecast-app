import streamlit as st
import pandas as pd
import geocoder
import requests

st.set_page_config(layout="wide")

g = geocoder.ip('me')
# Fixed: Add fallback values so the app won't crash if geocoder returns empty coordinates
if g.latlng:
    latitude, longitude = g.latlng
else:
    latitude, longitude = 45.5946, -121.1787
    print("using default value temperature")

print(latitude)
print(longitude)

API_KEY = "e456cfe7191e40819ea192102262707"
url = f"https://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={latitude},{longitude}&days=7"

data = requests.get(url).json()

if "forecast" in data:
    df = pd.DataFrame([{"time": d["date"], "temperature_2m_max": d["day"]["maxtemp_c"], "temperature_2m_min": d["day"]["mintemp_c"]} for d in data["forecast"]["forecastday"]])

    df = df[["time", "temperature_2m_max"]]
    
    st.title("Weather Forecast")
    st.write("### This week's weather")
    st.dataframe(df)
    
    st.write("### Representation of this week's weather")
    st.bar_chart(df, x="time", y="temperature_2m_max")
    
    st.write("### week's max temperatures")
    chart_data = df.set_index("time")[["temperature_2m_max"]].tail(7)
    st.line_chart(chart_data, height=1500)
else:
    st.error("⚠️ Weather API block or error occurred.")
    st.write("Debug info from API:", data)






