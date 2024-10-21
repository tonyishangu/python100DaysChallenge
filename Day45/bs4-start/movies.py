import requests
from bs4 import BeautifulSoup

url = 'https://www.empireonline.com/movies/features/best-movies-2/'
res = requests.get(url)
content = res.text

soup = BeautifulSoup(content, 'html.parser')
all_movies = soup.find_all(name='h3', class_='listicleItem_listicle-item__title__BfenH')
# print(all_movies)
movie_titles = [movie.getText() for movie in all_movies]
movies = (movie_titles[::-1])

# for n in range(len(movie_titles) - 1, -1, -1):
#     # print(n)
#     print(movie_titles[n])


with open('movies.txt', mode='w') as file:
    for movie in movies:
        file.write(f'{movie}\n')