from bs4 import BeautifulSoup
import requests
from data_db import Sqlite


class KufarParse:

    def __init__(self, url):
        self.url = url
        self.sqlite = Sqlite()

    def get_soup(self):
        self.request = requests.get(self.url)
        self.soup = BeautifulSoup(self.request.content, 'html.parser')
        return self.soup

    def parse_iphone(self, iphone):
        title = iphone.find('h3').text
        price = ''.join(iphone.find('p', class_='styles_price__G3lbO').text.split()[:-1])
        link = iphone['href']
        return {'title': title, 'price': price, 'link': link}


    def parse(self):

        self.soup = self.get_soup()
        self.results = [self.parse_iphone(iphone) for iphone in self.soup.find_all('a', class_='styles_wrapper__5FoK7')]
        return self.results


    def save_to_sqlite(self):
        self.sqlite.insert([list(value.values()) for value in self.parse()])

    def save_to_excel(self):
        pass

    def save_to_google_sheets(self):
        pass