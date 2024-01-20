from datetime import datetime, timedelta
from django.utils import timezone
from django.db import models
import requests
import os
from dotenv import load_dotenv
from .utils import get_coordinates

load_dotenv()

api_key = os.getenv("YANDEX_APY_KEY")


class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.CharField(max_length=100)
    atm_pressure = models.CharField(max_length=100)
    wind_speed = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    @staticmethod
    def get_weather_data(city: str) -> dict:
        coordinates = get_coordinates(city)
        url = 'https://api.weather.yandex.ru/v2/forecast/'
        headers = {
            'X-Yandex-API-Key': api_key,
            'accept': 'application/json',
            'content-type': 'application/json'
        }
        lat = coordinates['lat']
        long = coordinates['lon']
        response = requests.get(f'{url}?lat={lat}&lon={long}&lang=ru_RU',
                                headers=headers)
        data = response.json()
        return {
            'temperature': data['fact']['temp'],
            'wind_speed': data['fact']['wind_speed'],
            'atm_pressure': data['fact']['pressure_mm'],
            }

    @classmethod
    def get_data(cls, city):
        current_time = timezone.localtime(timezone.now())
        weather_data = cls.objects.filter(city=city).first()
        if weather_data and weather_data.timestamp >= current_time - timedelta(minutes=30):
            return {'temperature': weather_data.temperature,
                    'atm_pressure': weather_data.atm_pressure,
                    'wind_speed': weather_data.wind_speed}
        else:
            data = cls.get_weather_data(city)
            cls.objects.update_or_create(city=city,
                                         defaults={'temperature': data['temperature'],
                                                   'atm_pressure': data['atm_pressure'],
                                                   'wind_speed': data['wind_speed']})
            return data
        
        
