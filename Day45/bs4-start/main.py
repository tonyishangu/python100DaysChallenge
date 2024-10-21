from bs4 import BeautifulSoup
import requests

res = requests.get('https://news.ycombinator.com/')
yc_webpage = res.text

soup = BeautifulSoup(yc_webpage, 'html.parser')
print(soup.title)
article_tag = soup.find(name='a')
print(article_tag.get_text())
# article_link = article_tag.get('href')
# print(article_link)
article_vote = soup.find(name='span', class_='score').getText()
print(article_vote)
































# with open('website.html') as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')

# # print(soup.title.string)
# # print(soup.prettify())

# # get all anchor tags
# anchors = soup.find_all(name='a')
# print(anchors)

# # get text of the first anchor tag
# for tag in anchors:
#     print(tag.getText())
#     # get the links
#     print(tag.get('href'))

# # get item from an id
# heading = soup.find(name='h1', id='name')
# print('------------------------------')
# print(heading.get_text())

# # get company url
# company_url = soup.select_one('p a')
# print('--------------------------')
# print(company_url.get('href'))

# # using id in select
# name = soup.select_one('#name')
# print('--------------------------')
# print(name.get_text())

# # get all headings
# headings = soup.select('.heading')
# print('--------------------------')
# print(headings)  # returns a list of tags