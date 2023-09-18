import requests

# --------------post request---------------

username = 'saigelo'
token = 'guukadvuiwfniuwef'
endpoint = 'https://pixe.la/v1/users'
user_params = {
    'token':token,
    'username': username,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
res = requests.post(url=endpoint, json=user_params)
print(res.text)

# --------------creating a graph-----------
graph_endpoint = f'{endpoint}/{username}/graphs'

graph_params = {
    'id': 'graphtest',
    'name': 'Cycling Graph',
    'unit': 'km',
    'type': 'float',
    'color': 'ajisai',
}
headers = {
    'X-USER-TOKEN': token
}
response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
print(response.text)