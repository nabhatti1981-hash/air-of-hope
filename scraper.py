import requests
import json
from datetime import datetime

# 1. Configuration
API_TOKEN = "3b23ad55260b0b1b21eee42cb1734ca21f3a1db7"  # Replace with your actual WAQI token
CITY = "lahore"  # You can also use "punjab" or a specific station ID
URL = f"https://api.waqi.info/feed/{CITY}/?token={API_TOKEN}"

def get_hourly_pm25():
    try:
        response = requests.get(URL)
        data = response.json()

        if data['status'] == 'ok':
            # Extracting values
            aqi = data['data']['aqi']
            # PM2.5 is often nested in 'iaqi' (Individual Air Quality Index)
            pm25_val = data['data']['iaqi'].get('pm25', {}).get('v', 'N/A')
            station_name = data['data']['city']['name']
            timestamp = data['data']['time']['s']

            print(f"--- Data for {station_name} ---")
            print(f"Timestamp: {timestamp}")
            print(f"Overall AQI: {aqi}")
            print(f"PM2.5 Concentration: {pm25_val} µg/m³")
            
            return {
                "time": timestamp,
                "pm25": pm25_val,
                "station": station_name
            }
        else:
            print(f"Error from API: {data['data']}")
            
    except Exception as e:
        print(f"Connection Error: {e}")

if __name__ == "__main__":
    get_hourly_pm25()
