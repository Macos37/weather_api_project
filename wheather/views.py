from django.http import JsonResponse
from .models import WeatherData


def get_weather(request):
    city_name = request.GET.get('city')
    if city_name:
        weather_data = WeatherData.get_data(city_name)
        response = {
            'temperature': weather_data['temperature'],
            'atm_pressure': weather_data['atm_pressure'],
            'wind_speed': weather_data['wind_speed'],
        }
        return JsonResponse(response)
    return JsonResponse({'error': 'City not found'}, status=404)