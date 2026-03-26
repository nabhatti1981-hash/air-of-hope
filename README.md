# 🌬️ Lahore Hourly AQI Monitor (61 Sensors)

This project automatically tracks PM2.5 levels across 61 different locations in Lahore, Pakistan. It uses a GitHub Action to scrape real-time data from the World Air Quality Index (WAQI) API every hour.

## 📊 The Data
The historical log is stored in **`lahore_hourly_log.csv`**.

### Column Definitions:
| Column | Description |
| :--- | :--- |
| **Timestamp** | The time the data was recorded (PKT). |
| **Station_ID** | The unique WAQI ID (e.g., `@` for official, `A` for citizen/PurpleAir). |
| **Name** | The location name of the sensor. |
| **PM25_Raw** | The raw PM2.5 concentration reported by the sensor. |
| **PM25_Corrected** | The value adjusted using the EPA 2021 correction factor (for citizen sensors). |

## ⚙️ How it Works
1. **Scraper:** A Python script (`scraper.py`) queries the WAQI API for a list of 61 specific UIDs.
2. **Automation:** GitHub Actions runs this script at the start of every hour (`cron: '0 * * * *'`).
3. **Data Correction:** Citizen-grade sensors (IDs starting with 'A') are automatically adjusted by a factor of **0.524** to account for humidity interference and sensor bias.
4. **Storage:** New data is appended to the CSV, and the file is updated directly in this repository.

## 🚀 How to Use the Data
You can import the CSV directly into Excel, Google Sheets, or Python for analysis:

```python
import pandas as pd
df = pd.read_csv('[https://raw.githubusercontent.com/](https://raw.githubusercontent.com/)[YOUR_USERNAME]/[YOUR_REPO]/main/lahore_hourly_log.csv')
print(df.head())
