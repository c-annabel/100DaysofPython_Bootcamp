#https://openai.com/blog/openai-api/

# step 1. https://docs.google.com/spreadsheets/d/
# step 2. https://www.nutritionix.com/business/api:
# step 3. https://docs.google.com/document/
# step 4. https://sheety.co
# step 5. https://sheety.co/docs/requests
# step 6. authentication
# https://docs.google.com/spreadsheets/d/

import requests
import os
from datetime import datetime

APP_ID = "id"
#os.environ['APP_KEY']= "key"
# APP_KEY = "key"
APP_KEY = os.environ.get("APP_KEY")
SHEET_USER = "c-annabel"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

EXCERCISE_PARAMS = {
    "query": input("Tell me which exercises you did: "),
    "gender": "female",
    "weight_kg": 54,
    "height_cm": 165,
    "age": 43,
}

response = requests.post(url=exercise_endpoint, json=EXCERCISE_PARAMS, headers=headers)
response.raise_for_status()
result = response.json()
print(result)
#============================================================================#


sheet_endpoint = f"https://api.sheety.co/cf470ebc7fa12ee20ae8d9a36453c92c/workoutTracking/workouts"
# today_date = datetime.now().strftime("%d/%m/%Y")
today = datetime.now()
today_date = today.strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
         }
    }

    print(sheet_inputs)
    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs, auth=("c-annabel", APP_KEY,))
    print(sheet_response.text)
