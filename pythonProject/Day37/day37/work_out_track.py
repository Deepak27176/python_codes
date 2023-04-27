# deepakabcdefghqwerty
# Authorization: Basic ZGVlcGFrMjcxNzY6ZGVlcGFrYWJjZGVmZ2hxd2VydHk=
import datetime
APP_ID = "7f68e814"
API_KEY = "4d480ff0f52491ae39ea3e162fd701aa"
import requests

GENDER = "male"
WEIGHT_KG = "50"
HEIGHT_CM = "173"
AGE = "21"


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": "running 5 miles",
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

sheet_url = "https://api.sheety.co/21779dc561d391c461aff9c643d7027f/myWorkoutS/workouts"
today_date = datetime.datetime.now()
today_date = today_date.strftime("%d/%m/%Y")
now_time = datetime.datetime.now()
now_time = now_time.strftime("%X")
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # sheet_response = requests.post(sheet_url, json=sheet_inputs)
    #
    # print(sheet_response.text)

    # Basic Authentication
    sheet_response = requests.post(
        sheet_url,
        json=sheet_inputs,
        auth=(
            "deepak27176",
       "deepakabcdefghqwerty",
        )
    )

    # Bearer Token Authentication
    # bearer_headers = {
    #     "Authorization": "Bearer YOUR_TOKEN"
    # }
    # sheet_response = requests.post(
    #     sheet_endpoint,
    #     json=sheet_inputs,
    #     headers=bearer_headers
    # )