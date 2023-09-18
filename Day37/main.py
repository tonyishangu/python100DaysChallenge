import requests
from datetime import datetime

# --------------post request---------------

username = 'saigelo'
token = 'guukadvuiwfniuwef'
graphid = 'graphtest'
endpoint = 'https://pixe.la/v1/users'
user_params = {
    'token':token,
    'username': username,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
# res = requests.post(url=endpoint, json=user_params)
# print(res.text)

# --------------creating a graph-----------
graph_endpoint = f'{endpoint}/{username}/graphs'

graph_params = {
    'id': graphid,
    'name': 'Cycling Graph',
    'unit': 'km',
    'type': 'float',
    'color': 'ajisai',
}
headers = {
    'X-USER-TOKEN': token
}
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# ----------posting values to our graphs------------

pixel_endpoint = f'{endpoint}/{username}/graphs/{graphid}'

today = datetime.now()
graph_data = {
    'date': today.strftime('%Y%m%d'),
    'quantity': '21',
}

# res = requests.post(pixel_endpoint, json=graph_data, headers=headers)
# print(res.text)


# -------------update details------------------
update_endpoint = f'{endpoint}/{username}/graphs/{graphid}/{today.strftime("%Y%m%d")}'

new_graph_data = {
    'quantity': '34'
}

# res = requests.put(url=update_endpoint, json=new_graph_data, headers=headers)
# print(res.text)


# ---------------delete-------------
delete_endpoint = f'{endpoint}/{username}/graphs/{graphid}/{today.strftime("%Y%m%d")}'
del_res = requests.delete(url=delete_endpoint, headers=headers)
print(del_res.text)