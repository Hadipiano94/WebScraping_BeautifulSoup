from bs4 import BeautifulSoup
import requests


webpage_url = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(webpage_url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

movies = soup.find_all(class_="listicleItem_listicle-item__title__hW_Kn")
movies_list = []

for movie in movies:
    movies_list.append(movie.get_text().split(")")[1].strip())

movies_list.reverse()

with open("100_Movies.txt", mode="w", encoding="utf-8") as file:
    for i in range(0, 100):
        print(f"{i + 1}- {movies_list[i]}")
        file.write(f"{i + 1}- {movies_list[i]}\n")
