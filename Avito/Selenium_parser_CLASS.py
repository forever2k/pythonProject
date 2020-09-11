from selenium import webdriver
import time
import csv
import os

URL = 'https://www.avito.ru/'
FILE = 'cars_selenium_class.csv'


class AvitoParser:

    def __init__(self, driver):
        self.driver = driver
        driver.implicitly_wait(4)

    def parse(self):
        limit = self.get_pagination_limit()
        if limit == 1:
            self.parse_page(0, 1)
        else:
            self.parse_page(1, limit)

    def go_to_car_page(self):
        driver.get(URL)
        avito_elem = driver.find_element_by_name('category_id')
        avito_elem.send_keys("Автомобили")
        time.sleep(3)
        driver.find_element_
        time.sleep(3)
        url1 = driver.find_element_by_link_text("5 серия").click()
        return driver.current_url

    def get_pagination_limit(self):
        self.go_to_car_page()
        container = driver.find_elements_by_class_name('pagination-item-1WyVp')
        if container:
            return int(container[-2].text)
        else:
            return 1

    def parse_page(self, start_page, limit):
        for i in range(start_page, limit + 1):
            driver.get(driver.current_url + '?cd=1&p=' + str(i))
            name_find = self.driver.find_elements_by_class_name('snippet-title')
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

            self.save_inf(total)

    def save_inf(self, total):
        with open(FILE, 'a', newline='', encoding='utf-16') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['Марка', 'Цена', 'Время', 'Ссылка'])
            for item in total:
                writer.writerow([item[0], item[1], item[2], item[3]])


def main():
    global driver
    driver = webdriver.Chrome()
    parser = AvitoParser(driver)
    parser.parse()
    os.startfile(FILE)


if __name__ == '__main__':
    main()
