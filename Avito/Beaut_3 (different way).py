import requests
from bs4 import BeautifulSoup

HOST = 'https://www.avito.ru/'
URL = 'https://www.avito.ru/moskva/avtomobili/bmw/x5'
HEADERS = {
              'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params = params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('div', class_='snippet-horizontal')
    time_items = soup.find_all('div', class_='snippet-date-info')
    price_items = soup.find_all('span', class_='snippet-price')

    cars = []
    for item in items:
        cars.append({
            'title': item.find('h3', class_='snippet-title').get_text(strip=True),
            'link': HOST + item.find('a', class_='snippet-link').get('href')
        })
    print(cars)

    cars_time = []
    for tc in time_items:
        cars_time.append(tc.attrs['data-tooltip'])

    price = []
    for pr in price_items:
        price.append(pr.get_text(strip=True))

    total = [(cars[i], cars_time[i], price[i]) for i in range(len(cars))]
    print(total)
    print(type(total))


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')

parse()

