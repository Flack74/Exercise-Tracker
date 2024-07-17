import requests
from datetime import datetime
import os


nutrition_API_KEY = os.environ.get("nutrition_API_KEY")
nutrition_APPID = os.environ.get("nutrition_APPID")

nutrition_api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

sheety_endpoint = os.environ.get("sheety_endpoint")

exercise = input("Tell me what exercise you did: ")

headers = {
    'Content-Type': 'application/json',
    'x-app-id': nutrition_APPID,
    'x-app-key': nutrition_API_KEY,
}

body_params = {
    "query": exercise,
}

response = requests.post(url=nutrition_api_endpoint, json=body_params, headers=headers)
response.raise_for_status()
response_data = response.json()

today = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%H:%M:%S")

for exercise in response_data['exercises']:
    try:
        duration = exercise['duration_min']
        calories = exercise['nf_calories']
        name = exercise['name']

        body = {
            "workout": {
                "date": today,
                "time": current_time,
                "exercise": name,
                "duration": duration,
                "calories": calories,
            }
        }

        res = requests.post(url=sheety_endpoint, json=body)
        res.raise_for_status()
        print(f"Added exercise: {name}")
        print(res.text)

    except KeyError as e:
        print(f"\nError: Missing key {e}")
        print("Unable to find all required data for this exercise.")
