import streamlit as st
import pandas as pd
import geocoder


st.set_page_config(layout="wide")

g = geocoder.ip('me')
latitude, longitude = g.latlng
print(latitude)
print(longitude)

import requests

API_KEY = "e456cfe7191e40819ea192102262707"
url = f"https://weatherapi.com{API_KEY}&q={latitude},{longitude}&days=7"

data = requests.get(url).json()




if "forecast" in data:
    df = pd.DataFrame([
        {
            "time": day["date"],
            "temperature_2m_max": day["day"]["maxtemp_c"],
            "temperature_2m_min": day["day"]["mintemp_c"]
        } for day in data["forecast"]["forecastday"]
    ])
    
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





