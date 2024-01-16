# get_location.py
import requests
api_key = "2975cdf149a34e3450c631ea8be56385"
def get_weather_location(city_name, state_code, country_code, limit, api_key):
    base_url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        'q': f'{city_name},{state_code},{country_code}',
        'limit': limit,
        'appid': api_key
    }


    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_location = response.json()
        return weather_location
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

