# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 02:50:52 2026

@author: HP
"""

import requests
import pandas as pd
import os
from datetime import datetime

API_TOKEN = "3b23ad55260b0b1b21eee42cb1734ca21f3a1db7"
# Add your full list of 61 IDs here
sensor_ids = ["A471607", "A576556", "A254464"] 

def get_current_data(sid):
    url = f"https://api.waqi.info/feed/{sid}/?token={API_TOKEN}"
    try:
        r = requests.get(url, timeout=10).json()
        if r['status'] == 'ok':
            d = r['data']
            val = d['iaqi'].get('pm25', {}).get('v', 0)
            # Apply correction for 'A' (Citizen) sensors
            corrected = val * 0.524 if str(sid).startswith('A') else val
            return {
                'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M'),
                'Station_ID': sid,
                'Name': d['city']['name'],
                'PM25_Raw': val,
                'PM25_Corrected': round(corrected, 2)
            }
    except:
        return None

# Collect data
results = [get_current_data(sid) for sid in sensor_ids]
results = [res for res in results if res] # Remove None values

# Save/Append to CSV
df_new = pd.DataFrame(results)
file_path = 'lahore_hourly_log.csv'

if os.path.exists(file_path):
    df_old = pd.read_csv(file_path)
    df_final = pd.concat([df_old, df_new]).drop_duplicates()
    # Optional: Only keep the last 24-48 hours of data to keep file small
    df_final.to_csv(file_path, index=False)
else:
    df_new.to_csv(file_path, index=False)
