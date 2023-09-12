import requests

# endpoint = "https://pro.openweathermap.org/data/2.5/forecast/hourly"
endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "f632cefbfacc594278ac86d7f676b66b"

params = {
    "lat": -1.248310,
    "lon": 36.664780,
    "appid": api_key
}
res = requests.get(endpoint, params = params)
print(res.status_code)
print(res.json())
