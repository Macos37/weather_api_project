import requests


def get_coordinates(city_name):
    url = f'https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={city_name}&format=json'
    response = requests.get(url)
    data = response.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    if len(data.split(' ')) > 1:
        return {'lat': data.split(' ')[1], 'lon': data.split(' ')[0]}
    return None