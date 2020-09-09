from bs4 import BeautifulSoup
import requests
from collections import namedtuple
import datetime
import time


InnerBlock = namedtuple('Blosck', 'title,price,date,url')

class Block(InnerBlock):

    def __str__(self):
        return f'{self.title}\t{self.price}\t{self.date}\t{self.url}'


class AvitoParser:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
              'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
        }

    def get_page(self, page: int = None):
        params = {
            'cd': 1,
            'radius': 0,
        }
        if page and page >0:
            params['p'] = 3
        url = 'https://www.avito.ru/moskva/avtomobili/bmw/5-seriya-ASgBAgICAkTgtg3klyjitg3UnCg?p=1'
        r = self.session.get(url, params = params)
        print(r.url)

    @staticmethod
    def parse_date(item: str):
        params = item.strip().split(' ')
        if len(params) == 2:
            day, time = params
            if day == 'Сегодня':
                date = datetime.date.today()
            elif day == 'Вчера':
                date = datetime.date.today() - datetime.timedelta(days = 1)
            else:
                print('Не смогли разобрать день:', item)
                return

            time = datetime.datetime.strptime(time, '%H:%M').time()
            return datetime.datetime.combine(date = date, time = time)

        elif len(params) == 3:
            day, month_hru, time = params
            day = int(day)
            months_map = {
                'января': 1,
                'февраля': 2,
                'марта': 3,
                'апреля': 4,
                'мая': 5,
                'июня': 6,
                'июля': 7,
                'августа': 8,
                'сентября': 9,
                'октября': 10,
                'ноября': 11,
                'декабря': 12,
            }
            month = months_map.get(month_hru)
            if not month:
                print('Не смогли разобрать месяц:', item)
                return

            today = datetime.datetime.today()
            time = datetime.datetime.strptime(time, '%H:%M')
            return datetime.datetime(day = day, month = month, year = today.year, hour = time.hour, minute = time.minute)

        else:
            print('Не смогли разобрать формат:', item)
            return

    def parse_block(self, item):
        url_block = item.select_one('a.snippet-link')
        href = url_block.get('href')
        if href:
            url = 'https://www.avito.ru' + href
        else:
            url = None

        # Выбрать блок с названием
        title_block = item.select_one('h3.snippet-title span')
        title = title_block.string.strip()
        # print(title)

        # Выбрать блок с ценой
        price_block = item.select_one('div.snippet-price-row span')
        for string in price_block.stripped_strings:
            price = string

        # Выбрать блок с датой размещения объявления
        date = None
        date_block = item.select_one('div.snippet-date-info')
        absolute_date = date_block.get('data-tooltip')
        if absolute_date:
            date = self.parse_date(item = absolute_date)

        return Block(
            url = url,
            title = title,
            price = price,
            date = date,
        )

    def get_pagination_limit(self):
        text = self.get_page()
        soup = BeautifulSoup(text, 'lxml')

        container = soup.select('span.pagination-item-1WyVp')
        if container:
            return int(container[-2].get_text())
        else:
            return 1

    def get_blocks(self, page: int = None):
        text = self.get_page(page = page)
        soup = BeautifulSoup(text, 'lxml')
        container = soup.select('div.snippet-horizontal.item-snippet-with-aside.item.item_table.clearfix.js-catalog'
                                '-item-enum.item-with-contact.js-item-extended')
        for item in container:
            block = self.parse_block(item = item)
            print(block)

    def parse_all(self):
        limit = self.get_pagination_limit()
        print(f'Всего страниц: {limit}')
        for i in range(1, limit + 1):
            self.get_blocks(page=i)
            time.sleep(3)


def main():
    p = AvitoParser()
    # p.parse_all()
    # p.get_blocks()
    p.get_page()


if __name__ == '__main__':
    main()




# HOST = 'https://minfin.com.ua/'
# URL = 'https://minfin.com.ua/cards/'
# HEADERS = {
#               'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
# }
#
#
# def get_html(url, params = ''):
#     r = requests.get(url, headers=HEADERS, params = params)
#     return r
#
# def get_content(html):
#     soup = BeautifulSoup(html, 'lxml')
#     items = soup.find_all('div', class_ = 'product-item')
#     cards = []
#     print(items)
#
# html = get_html(URL)
# get_content(html.text)