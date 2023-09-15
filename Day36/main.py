import requests

# 
api = 'ZYQHXFI5Y33TJND1'
symbol = 'TSLA'
params = {
    'function':'TIME_SERIES_INTRADAY',
    'symbol': symbol,
    'apikey': api
}
url = 'https://www.alphavantage.co/query?'

res = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=ZYQHXFI5Y33TJND1')
print(res.status_code)
print(res.json())