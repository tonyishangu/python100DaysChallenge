import requests
from datetime import datetime
import os

age = 25
height = 180
weight = 64
gender = 'male'
nutrition_api = '0618b8bff93862adbf6aadf76cd2cce5'
appid = '0f5eb669'
username= 'saigelo'
password='qwerty4567'
url = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheet_endpoint = 'https://api.sheety.co/58bb52ef8e6574e39e8d011a310c810e/myWorkoutSheet/workouts'

exercise_input = input('Which exercise have you done?\n')

header = {
    "x-app-id": appid,
    "x-app-key": nutrition_api
}
params ={
    "query":exercise_input,
    "gender":gender,
    "weight_kg":weight,
    "height_cm":height,
    'age':age
}

res = requests.post(url, json=params, headers=header)
results= res.json()

# ----------saving data to google sheets-----------
today = datetime.now().strftime('%d/%m/%Y')
now_time = datetime.now().strftime('%X')

for exercise in results['exercises']:
    sheet_inputs = {
        'workout' : {
            'date': today,
            'time': now_time,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }
    
    res=requests.post(url=sheet_endpoint, json=sheet_inputs, 
                      auth=(username,password))
    print(res.text)