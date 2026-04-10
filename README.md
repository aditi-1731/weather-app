# 🌦️ Weather Dashboard App

A modern real-time weather forecasting web application built using **Streamlit** and the **OpenWeather API**.  
It provides live weather data, a clean interactive dashboard, and a 5-day forecast for any city in the world.

---

## 🚀 Live Demo
👉 Add your Streamlit deployment link here

---

## 📸 Preview

👉 Add screenshots of your app here (highly recommended for GitHub)

---

## ✨ Features

- 🌍 Search weather by city name  
- 🌡️ Real-time temperature, feels like, humidity, wind speed  
- 🌤️ Dynamic weather conditions with icons  
- 📅 5-day weather forecast  
- 🌅 Sunrise and sunset timings  
- 🎨 Clean dashboard UI using Streamlit  
- ⚡ Fast API-based live data fetching  
- 🧠 Error handling for invalid cities & network issues  

---

## 🛠️ Tech Stack

- Python 🐍  
- Streamlit 🎈  
- OpenWeather API 🌦️  
- Requests 🌐  
- python-dotenv 🔐  

---

## 📁 Project Structure

```bash
weather-app/
│── app.py
│── requirements.txt
│── .gitignore
│── README.md

1. Clone the repository
git clone https://github.com/aditi-1731/weather-app.git
cd weather-app
2. Install dependencies
pip install -r requirements.txt
3. Get API Key

Create a free API key from:
👉 https://openweathermap.org/api

4. Add API Key (LOCAL ONLY)

Create a .env file:

API_KEY=your_openweather_api_key
5. Run the app
streamlit run app.py
🌐 Deployment (Streamlit Cloud)

If deploying on Streamlit Cloud:

Add API key in Secrets:

API_KEY = "your_openweather_api_key"

And update your code:

API_KEY = st.secrets["API_KEY"]
🔑 API Used
OpenWeather Current Weather API
OpenWeather 5-Day Forecast API
👉 https://openweathermap.org/api
📊 What I Learned
Working with REST APIs in Python
Handling JSON responses
Streamlit UI development
Environment variables & secrets management
Debugging real-world API issues
Building interactive dashboards
🚀 Future Improvements
📍 Auto location detection
📊 Weather charts (temperature trends)
🌙 Dark/light theme toggle
🔔 Weather alerts system
📱 Mobile UI improvements
👨‍💻 Author

Aditi Tripathi
GitHub: https://github.com/aditi-1731


---

If you want next upgrade, I can help you make this repo:

🔥 look like a **top 1% GitHub portfolio project**  
with badges, banner, screenshots, and deployment polish

Just say: **“make it premium”** 😄
