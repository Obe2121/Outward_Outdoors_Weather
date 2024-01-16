# duck_weather_gui.py
import requests
import tkinter as tk
from weather_api import get_weather_info
from get_location import get_weather_location
from wind_direction_con import wind_direction
from PIL import Image, ImageTk
import datetime
import pytz

# Replace 'your_api_key' with your actual API key
api_key = "2975cdf149a34e3450c631ea8be56385"

# Create the main application window
app = tk.Tk()
app.title("Weather App")

# Create and place widgets
tk.Label(app, text="Enter City:").pack()
city_entry = tk.Entry(app)
city_entry.pack()

tk.Label(app, text="Enter State:").pack()
state_entry = tk.Entry(app)
state_entry.pack()

# Load and convert the image using Pillow
image_path = r"/Users/mikeoberdick/Library/Mobile Documents/com~apple~CloudDocs/Outward Outdoors/Logos/duck.jpg"

# Load and resize the image using Pillow
original_img = Image.open(image_path)

# Choose the appropriate antialiasing method based on Pillow version
try:
    resized_img = original_img.resize((300, 300), Image.ANTIALIAS)
except AttributeError:
    resized_img = original_img.resize((300, 300), Image.BICUBIC)

img = ImageTk.PhotoImage(resized_img)

# Initialize image_label at the beginning with the default image
image_label = tk.Label(app, image=img)
image_label.image = img
image_label.pack(side="bottom")


# Initialize labels at the beginning
city_label = tk.Label(app)
state_label = tk.Label(app)
current_date_label = tk.Label(app)
wind_speed_label = tk.Label(app)
wind_direction_label = tk.Label(app)


def get_location():
    global city_label, state_label, current_date_label, wind_speed_label, wind_direction_label

    city = city_entry.get()
    state = state_entry.get()

    city_name = city
    state_code = state
    country_code = 'US'

    # Destroy existing labels
    city_label.destroy()
    state_label.destroy()
    wind_speed_label.destroy()
    wind_direction_label.destroy()
    current_date_label.destroy()

    weather_location = get_weather_location(city_name, state_code, country_code, api_key='2975cdf149a34e3450c631ea8be56385', limit=1)

    if weather_location:
        latitude = weather_location[0]["lat"]
        longitude = weather_location[0]["lon"]
        weather_info = get_weather_info(api_key, latitude, longitude)
        if weather_info:
            print(f"Weather: {weather_info}")

            # Fix the map URL construction
            layer = 'wind_new'
            z = 1
            x = int(abs(longitude))
            y = int(abs(latitude))
            map_url = f'https://tile.openweathermap.org/map/{layer}/{z}/{x}/{y}.png?appid={api_key}'

            print(f"Map URL: {map_url}")

            wind_direction_degrees = weather_info['current']['wind_deg']
            wind_cardinal_direction = wind_direction(wind_direction_degrees)
            print(f"Wind Direction: {wind_cardinal_direction}")

            utc_date_time = weather_info['current']['dt']
            utc_dt = datetime.datetime.fromtimestamp(int(utc_date_time), tz=pytz.utc)
            utc_timezone = pytz.utc
            est_timezone = pytz.timezone('US/Eastern')
            est_dt = utc_dt.astimezone(est_timezone)
            est_dt_only_date = str(est_dt)[:-15]


            city_label = tk.Label(app, text=f'City: {city}')
            city_label.pack()

            current_date_label = tk.Label(app, text=f'Curent Time: {est_dt_only_date}')
            current_date_label.pack()

            state_label = tk.Label(app, text=f'State: {state.upper()}')
            state_label.pack()

            wind_speed_label = tk.Label(app, text=f'Current Wind Speed: {weather_info["current"]["wind_speed"]}')
            wind_speed_label.pack()

            wind_direction_label = tk.Label(app, text=f'Current Wind Direction: {wind_direction_degrees} , {wind_cardinal_direction}')
            wind_direction_label.pack()



        else:
            print("Failed to retrieve weather information.")
    else:
        print("Failed to retrieve weather location.")

def clear_data():
    global city_label, state_label, wind_speed_label, wind_direction_label, current_date_label

    # Destroy existing labels
    city_label.destroy()
    state_label.destroy()
    current_date_label.destroy()
    wind_speed_label.destroy()
    wind_direction_label.destroy()

# Button to trigger weather retrieval
get_weather_button = tk.Button(app, text="Get Weather", command=get_location)
get_weather_button.pack()

# Button to clear displayed data
clear_button = tk.Button(app, text="Clear Data", command=clear_data)
clear_button.pack()

# Start the Tkinter event loop
app.mainloop()
