import requests

endpoint = 'https://pixe.la/v1/users'
user_params = {
    'token':'guukadvuiwfniuwef',
    'username': 'saigelo',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
res = requests.post(url=endpoint, json=user_params)
print(res.text)