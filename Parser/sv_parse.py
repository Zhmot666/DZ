from bs4 import BeautifulSoup
import requests
from data_db import Sqlite


class SVparse:

    def __init__(self, url):
        self.soup = None
        self.request = None
        self.url = url
        self.sqlite = Sqlite()

    def get_soup(self):
        self.request = requests.get(self.url)
        self.soup = BeautifulSoup(self.request.content, 'html.parser')
        return self.soup

    def parse_today(self):
        main_list = list()
        response = requests.get(self.url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        start_block = soup.find('div', class_='news-head')
        tags_between = start_block.next_sibling.next_sibling
        while tags_between != start_block:
            if tags_between != '\n':
                if tags_between is None:
                    break
                include_dict = dict()
                include_dict['title'] = tags_between.contents[1].contents[1].contents[0].strip()
                include_dict['link'] = tags_between.attrs['href']
                include_dict['id'] = tags_between.attrs['data-id']
                main_list.append(include_dict)
            tags_between = tags_between.next_sibling
        return main_list

    def parse_series(self, id_series):
        return_dict = dict()
        # return_dict['title'] = self.sqlite.get_series_title(id_series)
        # return_dict['image'] = self.sqlite.parse_series_image(id_series)
        response = requests.get(self.url + self.sqlite.get_series_link(id_series))
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        images = soup.find('meta', attrs={'property': 'og:image'})
        return_dict['img'] = images['content']
        text = soup.find('meta', attrs={'name': 'description'})
        return_dict['description'] = text['content']
        link = soup.find('link', attrs={'itemprop': 'embedUrl'})
        return_dict['link'] = link['href']
        return return_dict

    def parse_head(self, id_series):
        pass
