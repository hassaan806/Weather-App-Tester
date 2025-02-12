import requests
import json

def get_weather(city):
    API_KEY = "your_api_key_here"  # Replace with your OpenWeatherMap API key
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather = {
            "City": data["name"],
            "Temperature": f"{data['main']['temp']}°C",
            "Humidity": f"{data['main']['humidity']}%",
            "Weather": data["weather"][0]["description"].capitalize()
        }
        return weather
    else:
        return {"Error": "City not found or API error."}

if __name__ == "__main__":
    city = input("Enter city name: ")
    weather_info = get_weather(city)
    
    for key, value in weather_info.items():
        print(f"{key}: {value}")
