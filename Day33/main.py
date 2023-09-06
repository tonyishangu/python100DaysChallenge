import requests

res = requests.get(url='http://api.open-notify.org/iss-now.json')
print(res.status_code)
print(res.json())

res.raise_for_status()          #return status code if not 200
data = res.json()
longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']
iss_position = (longitude, latitude)
print(iss_position)