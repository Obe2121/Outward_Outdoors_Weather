# weather_api.py
import requests

def get_weather_info(api_key, lat, lon, units="imperial", exclude=''):
    base_url = 'https://api.openweathermap.org/data/3.0/onecall'
    params = {
        'lat': lat,
        'lon': lon,
        'exclude': exclude,
        'appid': api_key
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        print(weather_data)
        return weather_data
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None
