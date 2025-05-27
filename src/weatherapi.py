import requests

def get_weather(city):
    api_key = "51214d180a93bd48877c2342c3304098"
base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        temp = data["main"]["temp"]
        return f"{city}: {temp}°C"
    else:
        return f"Failed to get weather for {city}"
