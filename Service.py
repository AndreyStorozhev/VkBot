import requests
from bs4 import BeautifulSoup
import random


class BotService:
    def get_weather(self):
        soup = self.__get_soup('https://yandex.ru/pogoda/kostroma')
        degrees = soup.find('span', class_='temp__value')
        precipitation = soup.find('div', class_='link__condition day-anchor i-bem')
        return degrees.text + " градусов, " + precipitation.text

    def get_movie(self):
        soup = self.__get_soup('https://www.filmpro.ru/movies')
        movies = soup.findAll('p', class_='b-maincinema__title')
        index = random.randint(0, len(movies) - 1)
        return movies[index].text

    def get_href_habr(self):
        soup = self.__get_soup('https://habr.com/ru/')
        article_links = soup.find_all('a', class_='post__title_link')
        index = random.randint(0, len(article_links) - 1)
        return article_links[index].get('href')

    def __get_soup(self, url):
        html = requests.get(url).text
        soup = BeautifulSoup(html, features='html.parser')
        return soup
