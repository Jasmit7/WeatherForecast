import requests
from tabulate import tabulate
import time

api_key = '30d4741c779ba94c470ca1f63045390a'
previous_temperatures = []

while True:
    user_input = input("Enter city: ")

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

    if weather_data.json()['cod'] == '404':
        print("No City Found")
    else:
        weather_info = weather_data.json()
        temperature_fahrenheit = round(weather_info['main']['temp'])
        temperature_celsius = round((temperature_fahrenheit - 32) * 5 / 9)

        # Fetch previous temperature data for the last 5 days (replace with your own data source)
        previous_data = [82, 79, 77, 81, 83]

        previous_temperatures.extend(previous_data)

        # Keep only the last 7 temperature data points
        previous_temperatures = previous_temperatures[-7:]

        previous_temperatures.append(temperature_fahrenheit)

        weather = weather_info['weather'][0]['main']
        description = weather_info['weather'][0]['description']
        humidity = weather_info['main']['humidity']
        wind_speed_mph = weather_info['wind']['speed']
        wind_speed_kph = round(wind_speed_mph * 1.60934)
        cloudiness = weather_info['clouds']['all']
        visibility_meters = weather_info['visibility']
        visibility_kilometers = round(visibility_meters / 1000, 2)

        # Find the maximum and minimum temperature
        max_temperature = max(previous_temperatures)
        min_temperature = min(previous_temperatures)

        max_temperature_celsius = round((max_temperature - 32) * 5 / 9)
        min_temperature_celsius = round((min_temperature - 32) * 5 / 9)

        data = [
            ['Current weather', weather],
            ['Description', description],
            ['Temperature (ºF)', temperature_fahrenheit, f"{temperature_celsius} ºC"],
            ['Humidity (%)', humidity],
            ['Wind Speed (mph)', wind_speed_mph, f"{wind_speed_kph} km/h"],
            ['Cloudiness (%)', cloudiness],
            ['Visibility (meters)', visibility_meters, f"{visibility_kilometers} km"],
            ['Max Temperature (ºF)', max_temperature, f"{max_temperature_celsius} ºC"],
            ['Min Temperature (ºF)', min_temperature, f"{min_temperature_celsius} ºC"]
        ]

        print(f"Weather information for {user_input}:")
        print(tabulate(data, headers=["Parameter", "Value (Imperial)", "Value (Metric)"], tablefmt="grid"))

    time.sleep(1)  # Sleep for 1 second before updating the data
