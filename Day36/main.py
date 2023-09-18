import requests

# 
api = 'ZYQHXFI5Y33TJND1'
newsapi = '60d90bdb6f1e4471bdfa3c7ae1400ca0'
symbol = 'TSLA'
company_name = 'Tesla'
params = {
    'function':'TIME_SERIES_INTRADAY',
    'symbol': symbol,
    'apikey': api
}
url = 'https://www.alphavantage.co/query?'
news_url = 'https://newsapi.org/v2/everything?'

res = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=ZYQHXFI5Y33TJND1')
print(res.status_code)
data = res.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]

day_before_yesterday = data_list[1]
day_before_closing_price = day_before_yesterday['4. close']
print('day_before_yesterday', day_before_closing_price)

ystd_data = data_list[0]
ystd_closing_price = ystd_data['4. close']
print('yesterday closing price', ystd_closing_price)

diff = abs(float(ystd_closing_price) - float(day_before_closing_price))
print('difference', diff)

diff_perc = (diff/float(ystd_closing_price))*100
print('percentage',diff_perc)

if diff_perc > 0:
    news_params = {
        'apikey': newsapi,
        'qInTitle': company_name
    }
    newsdata = requests.get(news_url, params=news_params)
    articles = newsdata.json()['articles']
    three_articles = articles[:3]
    print('news data\n', three_articles)