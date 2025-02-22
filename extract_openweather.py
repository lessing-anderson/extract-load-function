import sys
from dotenv import load_dotenv
import os
import requests
from datetime import datetime
import json


class ExtractOpenWeather:
    base_url = "https://api.openweathermap.org/data/2.5"

    load_dotenv()
    api_key = os.getenv("OPENWEATHER_API_KEY")

    @classmethod
    def _geocoding(cls, city_name, state_name, country_code):

        payload = {"q" : f"{city_name}, {state_name}, {country_code}" , "limit" : "1" , "appid" : f"{cls.api_key}"}

        response_geocoding = requests.get(f"http://api.openweathermap.org/geo/1.0/direct", params=payload)

        response_geocoding.raise_for_status()
        response_geocoding_json = response_geocoding.json()

        latitude = response_geocoding_json[0]["lat"]
        longitude = response_geocoding_json[0]["lon"]

        return latitude, longitude
    
    @classmethod
    def _save_json_file(cls, folder_name, file_name, json_file):

        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        
        with open(f"./{folder_name}/{file_name}.json", "w", encoding="utf-8") as file:
            json.dump(json_file, file)

    @staticmethod
    def extract_weather(city_name, state_name, country_code):

        latitude, longitude = ExtractOpenWeather._geocoding(city_name, state_name, country_code)

        payload = {"lat" : f"{latitude}" , "lon" : f"{longitude}" , "units" : "metric" , "appid" : f"{ExtractOpenWeather.api_key}"}

        response_weather = requests.get(f"{ExtractOpenWeather.base_url}/weather", params=payload)

        response_weather.raise_for_status()
        response_weather_json = response_weather.json()

        file_name = city_name.replace(" ", "_")+"_"+datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f')

        ExtractOpenWeather._save_json_file("openweather/weather", file_name, response_weather_json)

    @staticmethod
    def extract_weather_forecast(city_name, state_name, country_code):

        latitude, longitude = ExtractOpenWeather._geocoding(city_name, state_name, country_code)

        payload = {"lat" : f"{latitude}" , "lon" : f"{longitude}" , "units" : "metric" , "appid" : f"{ExtractOpenWeather.api_key}"}

        response_weather_forecast = requests.get(f"{ExtractOpenWeather.base_url}/forecast", params=payload)

        response_weather_forecast.raise_for_status()
        response_weather_forecast_json = response_weather_forecast.json()

        file_name = city_name.replace(" ", "_")+"_"+datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f')

        ExtractOpenWeather._save_json_file("openweather/weather_forecast", file_name, response_weather_forecast_json)

    @staticmethod
    def extract_air_pollution(city_name, state_name, country_code):

        latitude, longitude = ExtractOpenWeather._geocoding(city_name, state_name, country_code)

        payload = {"lat" : f"{latitude}" , "lon" : f"{longitude}" , "appid" : f"{ExtractOpenWeather.api_key}"}
        
        response_air_pollution = requests.get(f"{ExtractOpenWeather.base_url}/air_pollution", params=payload)

        response_air_pollution.raise_for_status()
        response_air_pollution_json = response_air_pollution.json()
        
        file_name = city_name.replace(" ", "_")+"_"+datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f')

        ExtractOpenWeather._save_json_file("openweather/air_pollution", file_name, response_air_pollution_json)

    @staticmethod
    def extract_air_pollution_forecast(city_name, state_name, country_code):

        latitude, longitude = ExtractOpenWeather._geocoding(city_name, state_name, country_code)

        payload = {"lat" : f"{latitude}" , "lon" : f"{longitude}" , "appid" : f"{ExtractOpenWeather.api_key}"}
        
        response_air_pollution_forecast = requests.get(f"{ExtractOpenWeather.base_url}/air_pollution/forecast", params=payload)

        response_air_pollution_forecast.raise_for_status()
        response_air_pollution_forecast_json = response_air_pollution_forecast.json()
        
        file_name = city_name.replace(" ", "_")+"_"+datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f')

        ExtractOpenWeather._save_json_file("openweather/forecast_air_pollution", file_name, response_air_pollution_forecast_json)


if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Parameters must be: python extract_openweather.py <city_name> <state_name> <country_code>")
        sys.exit(1)
        
    city_name = sys.argv[1]
    state_name = sys.argv[2]
    country_code = sys.argv[3]

    ExtractOpenWeather.extract_weather(city_name, state_name, country_code)
    ExtractOpenWeather.extract_weather_forecast(city_name, state_name, country_code)
    ExtractOpenWeather.extract_air_pollution(city_name, state_name, country_code)
    ExtractOpenWeather.extract_air_pollution_forecast(city_name, state_name, country_code)