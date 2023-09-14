import requests
from twilio.rest import Client

# endpoint = "https://pro.openweathermap.org/data/2.5/forecast/hourly"
endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "f632cefbfacc594278ac86d7f676b66b"
account_sid = ''
auth_token  = ''

params = {
    "lat": -1.248310,
    "lon": 36.664780,
    "appid": api_key,
    "exclude": 'current,minutely,daily'
}
res = requests.get(endpoint, params = params)
weather_data = res.json()
weather_slice = weather_data['hourly'][:12]
will_rain = False


for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

    if will_rain:
        client = Client(account_sid, auth_token)
        message = client.messages \
        .create(
            body="It's going to rain today, carry an umbrella", 
            from_= "number you get from twilio"
            to='number you sign up with')
        print(message.status)

