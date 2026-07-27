import streamlit as st
import pandas as pd
import geocoder
import requests

st.set_page_config(layout="wide")

g = geocoder.ip('me')

if g.city and g.country:
    location_query = f"{g.city},{g.country}"

print(location_query)

location_query = st.text_input("Enter your city and country:", "")

API_KEY = "e456cfe7191e40819ea192102262707"
url = f"https://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={location_query}&days=7"

data = requests.get(url).json()

if "forecast" in data:
    df = pd.DataFrame([{"time": d["date"], "temperature_2m_max": d["day"]["maxtemp_c"], "temperature_2m_min": d["day"]["mintemp_c"]} for d in data["forecast"]["forecastday"]])

    df = df[["time", "temperature_2m_max"]]
    
    st.title("Weather Forecast")
    st.write("using location: " + str(location_query))
    st.write("### This week's weather")
    st.dataframe(df)
    
    st.write("### Representation of this week's weather")
    st.bar_chart(df, x="time", y="temperature_2m_max")
    
    st.write("### week's max temperatures")
    chart_data = df.set_index("time")[["temperature_2m_max"]].tail(7)
    st.line_chart(chart_data)
else:
    st.error("⚠️ Weather API block or error occurred.")
    st.write("Debug info from API:", data)






