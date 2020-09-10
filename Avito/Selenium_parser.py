from selenium import webdriver
import time
import csv
import os

URL = 'https://www.avito.ru/' # TESTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT !!!!!
FILE = 'cars_selenium.csv'

from selenium import webdriver
import time
import csv
import os

URL = 'https://www.avito.ru/'
FILE = 'cars_selenium.csv'


def main():
    global driver
    driver = webdriver.Chrome()
    driver.get(URL)
    avito_elem = driver.find_element_by_name('category_id')
    avito_elem.send_keys("Автомобили")
    time.sleep(3)
    driver.find_element_by_link_text("BMW").click()
    time.sleep(3)
    url1 = driver.find_element_by_link_text("5 серия").click()
    time.sleep(2)
    return driver.current_url


def get_pagination_limit():
    main()
    container = driver.find_elements_by_class_name('pagination-item-1WyVp')
    if container:
        return int(container[-2].text)
    else:
        return 1


def parse():
    limit = get_pagination_limit()

    # a = driver.current_url
    # print(a)
    # driver.get(driver.current_url + '?cd=1&p=2')
    # b = driver.current_url
    # print(b)

    if limit == 1:
        parse_page(0, 1)
    else:
        parse_page(1, limit)


def parse_page(start_page, limit):
    for i in range(start_page, limit + 1):
        driver.get(driver.current_url + '?cd=1&p=' + str(i))
        name_find = driver.find_elements_by_class_name('snippet-title')
        name = []
        for item in name_find:
            name.append(item.text)
        # print(name)

        price_find = driver.find_elements_by_class_name('snippet-price')
        price = []
        for item in price_find:
            price.append(item.text)
        # print(price)

        date_find = driver.find_elements_by_class_name('snippet-date-info')
        date = []
        for item in date_find:
            date.append(item.get_attribute('data-tooltip'))
        # print(list(filter(None, date)))

        link_find = driver.find_elements_by_class_name('snippet-link')
        link = []
        for item in link_find:
            link.append(item.get_attribute('href'))
        # print(link)

        total = [(name[i], price[i], date[i], link[i]) for i in range(len(name))]

        with open(FILE, 'a', newline='', encoding='utf-16') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['Марка', 'Цена', 'Время', 'Ссылка'])
            for item in total:
                writer.writerow([item[0], item[1], item[2], item[3]])

    os.startfile(FILE)


if __name__ == '__main__':
    parse()
