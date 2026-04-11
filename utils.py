import requests

def get_weather_icon(condition):
    condition = condition.lower()
    if "cloud" in condition:
        return "☁️"
    elif "rain" in condition:
        return "🌧️"
    elif "clear" in condition:
        return "☀️"
    elif "haze" in condition:
        return "🌫️"
    else:
        return "🌍"


def get_forecast(city, API_KEY):
    try:
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except:
        return None