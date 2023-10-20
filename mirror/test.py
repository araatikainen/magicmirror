import requests
import json
from datetime import datetime

week_days = ['su','ma', 'ti', 'ke', 'to', 'pe', 'la']

current_date = datetime.now().strftime("%Y-%m-%d")

print(current_date)

url = 'https://api.open-meteo.com/v1/forecast?latitude=61.4991&longitude=23.7871&daily=temperature_2m_max,temperature_2m_min,rain_sum,windspeed_10m_max&timezone=Europe%2FMoscow&forecast_days=3'
response = requests.get(url)
print(response.status_code)
print(response.text)