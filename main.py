import requests
from datetime import datetime
import os

NUT_APP_ID = os.environ.get('NUT_APP_ID')
NUT_APP_KEY = os.environ.get('NUT_APP_KEY')
SHEETY_API = os.environ.get('SHEETY_API')

CURRENT_DATE = datetime.now()

def adding_workout():
    is_continue = True
    while is_continue:
        headers ={
            "x-app-id" :NUT_APP_ID,
            "x-app-key":NUT_APP_KEY,
        }

        exercise_params = {
            "query": input("Tell me which exercises you did today? ")
        }

        language_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
        exercise_response = requests.post(url=language_exercise_endpoint,json=exercise_params, headers=headers)

        data_json = exercise_response.json()
        exercises = data_json["exercises"]

        # print(data_json)
        # print(exercises)

        for exercise in exercises:
            exercise_name = exercise["name"]
            calories = exercise["nf_calories"]
            duration = exercise["duration_min"]

            workouts  = {
                "workout": {
                "date": CURRENT_DATE.strftime("%d/%m/%Y"),
                "time": CURRENT_DATE.strftime("%H:%M:%S"),
                "exercise": exercise_name,
                "duration": duration,
                "calories": calories,
                "id": 00
                }
            
            }

            headers = {
                'Content-Type': 'application/json',
                'Authorization': SHEETY_API

            }

            sheety_endpoint = "https://api.sheety.co/719e26062f6797b5021b1760973cbe49/workoutTracking/workouts"
            response = requests.post(url=sheety_endpoint,headers=headers,json=workouts)
            response.raise_for_status()
            
            answer = input("Do you want to add more workout? Y/N: ").lower()
            
            if answer == 'n':
                print("Workout is saved in the google sheet!")
                exit()
         

adding_workout()
################################

# workouts  = {
#     "workout": {
#       "date": "21/07/2024",
#       "time": "15:00:00",
#       "exercise": "Benchpress",
#       "duration": 4,
#       "calories": 200,
#       "id": 3
#     }

# }

############################################

# headers ={
#     "x-app-id" :NUT_APP_ID,
#     "x-app-key":NUT_APP_KEY,
# }

# exercise_params = {
#     "query": input("Tell me which exercises you did today? ")
# }


# language_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
# exercise_response = requests.post(url=language_exercise_endpoint,json=exercise_params, headers=headers)

# data_json = exercise_response.json()
# exercises = data_json["exercises"]
