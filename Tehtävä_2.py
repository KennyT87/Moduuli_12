import requests

def get_coordinates(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    lat = data['coord']['lat']
    lon = data['coord']['lon']
    return lat, lon

def get_weather(city_name, api_key):
    lat, lon = get_coordinates(city_name, api_key)
    base_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly,daily,alerts&appid={api_key}"
    response = requests.get(base_url)
    data = response.json()
    if 'current' in data:
        weather_description = data['current']['weather'][0]['description']
        temp_kelvin = data['current']['temp']
        temp_celsius = temp_kelvin - 273.15
        print(f"Säätila paikkakunnalla {city_name}: {weather_description}")
        print(f"Lämpötila: {temp_celsius:.2f}°C")
    else:
        print("API-vastaus ei sisällä 'current'-avainta. Tässä on koko vastaus:")
        print(data)


kaupunki = input("Anna paikkakunnan nimi: ")
get_weather(f"{kaupunki}", "bd877262c9e9e4381e134c02f65c1d22")