import streamlit as st
import requests
import os
from dotenv import load_dotenv
from datetime import datetime
from utils import get_weather_icon, get_forecast

load_dotenv(override=True)

try:
    API_KEY = st.secrets["API_KEY"]
except:
    API_KEY = os.getenv("API_KEY")
    
st.set_page_config(page_title="Weather App", page_icon="🌦️")

st.markdown("""
<style>
.main {
    background-color: #0e1117;
}
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}
h1 {
    color: #4da6ff;
}
div[data-testid="metric-container"] {
    background-color: rgba(255,255,255,0.05);
    border-radius: 12px;
    padding: 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>🌦️ Weather App</h1>", unsafe_allow_html=True)
st.write("")
st.write("")

city = st.text_input("Enter city name",value ="Delhi")

def get_theme(condition):
    condition = condition.lower()
    if "rain" in condition:
        return "🌧 Rainy vibes outside!"
    elif "cloud" in condition:
        return "☁️ Cloudy skies today"
    elif "clear" in condition:
        return "☀️ Bright and sunny day!"
    elif "haze" in condition:
        return "🌫 Hazy conditions outside"
    else:
        return "🌍 Weather looks mixed"

def weather_banner(weather):
    weather = weather.lower()
    if "rain" in weather:
        return "🌧️ Carry an umbrella today!"
    elif "clear" in weather:
        return "☀️ Perfect day to go out!"
    elif "cloud" in weather:
        return "☁️ Calm cloudy weather"
    elif "haze" in weather:
        return "🌫 Low visibility today"
    else:
        return "🌍 Mixed weather conditions"


if st.button("Get Weather"): 
    if not city.strip():
        st.warning("Please enter a city name")
    elif not API_KEY:
        st.error("API key not found. Check your .env file")
    else:
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        forecast_data = get_forecast(city, API_KEY)

        try:
            with st.spinner(f"🌍 Fetching latest weather for {city}..."):
                response = requests.get(url,timeout=10)
                response.raise_for_status()
                data = response.json()
                country = data.get("sys", {}).get("country", "N/A")
                st.markdown(f"""
                ### 📍 {city}, {country}
                🌍 Live Weather Dashboard
                """)
            if str(data.get("cod")) != "200":
                st.error(f"❌ {data.get('message', 'City not found')}")
            else:
                temp = data["main"]["temp"]
                weather = data["weather"][0]["description"]
                st.info(get_theme(weather))
                st.info(weather_banner(weather))
                
                icon = get_weather_icon(weather)
                humidity = data["main"]["humidity"]
                wind = data["wind"]["speed"]
                
                st.markdown("---")
                st.subheader("🌤 Current Weather")
                sunrise = datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M")
                sunset = datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M")

                st.toast(f"✅ Showing weather for {city.capitalize()}")
                feels_like = data["main"]["feels_like"]

                country = data["sys"]["country"]
                st.markdown(f"## 📍 {city.capitalize()}")
                col1,col2,col3 =st.columns(3)

                with col1:
                    st.metric("🌡 Temperature", f"{round(temp,1)} °C")
                    st.metric("🤒 Feels Like", f"{round(feels_like,1)} °C")

                with col2:
                    st.metric("💧 Humidity", f"{humidity}%")
                    st.metric("🌬 Wind Speed", f"{round(wind,1)} m/s")

                with col3:
                    st.metric("🌤 Condition", f"{icon} {weather.capitalize()}")
                    st.metric("📍 Location", f"{city}, {country}")
                st.info(f"🌅 Sunrise: {sunrise} | 🌇 Sunset: {sunset}")
                
                st.subheader("📅 5-Day Forecast")
                st.markdown("----")
                st.subheader("🌤 Live Weather")

                seen_dates = set()

                st.markdown("---")

                for item in forecast_data["list"]:
                    date = item["dt_txt"].split(" ")[0]

                    hour = item["dt_txt"].split(" ")[1]

                    if date in seen_dates:
                        continue

                    if "12:00:00" not in hour:
                        continue

                    seen_dates.add(date)

                    temp = item["main"]["temp"]
                    desc = item["weather"][0]["description"].capitalize()
                    icon = get_weather_icon(desc)

                    st.markdown(f"""
                    <div style="
                        padding: 12px;
                        border-radius: 12px;
                        margin-bottom: 10px;
                        background: rgba(255,255,255,0.05);
                    ">
                        <h4>📅 {date}</h4>
                        <p>🌡 {round(temp,1)} °C</p>
                        <p>{icon} {desc}</p>
                    </div>
                    """, unsafe_allow_html=True)
        except requests.exceptions.RequestException as e:
            st.error(f"Network Error: {e}")
        except Exception as e:
            st.error(f"unexpected error: {e}")
