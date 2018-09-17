import secret
import requests

def get_weather():
  # New York
  city_id         = "5128581"
  # long_island_city = "5125125"

  weather_url = "https://api.openweathermap.org/data/2.5/weather"
  weather_params = {"id":    city_id,
                    "APPID": secret.OPENWEATHER_API_KEY,
                    "units": "imperial"}
  weather_request = requests.get(weather_url, params = weather_params)

  if weather_request.status_code == requests.codes.ok:

    weather_json = weather_request.json()

    """
    Example JSON Response

      {'base': 'stations',
       'clouds': {'all': 1},
       'cod': 200,
       'coord': {'lat': 40.71, 'lon': -74.01},
       'dt': 1537145760,
       'id': 5128581,
       'main': {'humidity': 71,
                'pressure': 1023,
                'temp': 295.26,
                'temp_max': 297.05,
                'temp_min': 293.15},
       'name': 'New York',
       'sys': {'country': 'US',
               'id': 2121,
               'message': 0.0074,
               'sunrise': 1537180722,
               'sunset': 1537225293,
               'type': 1},
       'visibility': 16093,
       'weather': [{'description': 'clear sky',
                    'icon': '01n',
                    'id': 800,
                    'main': 'Clear'}],
       'wind': {'deg': 173.002, 'speed': 2.71}}
    """

    temperature  = str(int(weather_json['main']['temp']))
    high         = str(int(weather_json['main']['temp_max']))
    low          = str(int(weather_json['main']['temp_min']))

    text         = weather_json['weather'][0]['main']
    description  = weather_json['weather'][0]['description']

    wind_speed   = str(int(weather_json['wind']['speed']))
    return {
        'temp':        temperature,
        'high':        high,
        'low':         low,
        'text':        text,
        'description': description,
        'wind_speed':  wind_speed
    }
