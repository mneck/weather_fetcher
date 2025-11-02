import requests
import json
import datetime
import pandas as pd

latitude=52.481388888889
longitude=13.435

response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,weather_code")

weather_data = json.loads(response.text)

weather_map = {
0:	"Clear sky",
1:	"Mainly clear",
2:	"Partly cloudy",
3:	"Overcast",
45:	"Fog",
48:	"Depositing rime fog",
51:	"Light drizzle",
53:	"Drizzle",
55:	"Dense drizzle",
61:	"Slight rain",
63:	"Rain",
65:	"Heavy rain",
80:	"Rain showers",
95:	"Thunderstorm"
}

location = "Berlin"
current_weather_code = int(weather_data['current']['weather_code'])
current_weather_description = weather_map.get(current_weather_code, "Unknown")
current_temperature = float(weather_data['current']['temperature_2m'])

df = pd.DataFrame({'location': [location],
                   'time': [datetime.datetime.now()],
                   'weather description': [current_weather_description],
                   'temperature': [current_temperature]
                   })

df.to_csv('weather_log.csv', header=False, mode='a', index=False)

print(f"Current weather in {location}: {current_weather_description}, {current_temperature} C at {datetime.datetime.now()}; data saved to weather_log.csv")