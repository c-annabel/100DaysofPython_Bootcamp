# https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/

from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
movies = soup.find_all(name="h3", class_="title")

movie_texts = []

for movie_tag in movies:
        text = movie_tag.getText()
        movie_texts.append(text)

# also can be written as below:
# movie_texts = [movie.getText() for movie in moveies]

movie_titles = movie_texts[::-1]
# print(movie_titles)

with open("movies.txt", "w") as data_file:
    for movie in movie_titles:
        data_file.write(f"{movie}\n")