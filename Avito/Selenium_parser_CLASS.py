from selenium import webdriver
import time

URL = 'https://www.avito.ru/'

class AvitoParser:

    def __init__(self, driver):
        self.driver = driver

    def parse(self):
        self.go_to_car_page()
        self.get_inf()

    def go_to_car_page(self):
        self.driver.get(URL)
        avito_elem = self.driver.find_element_by_name('category_id')
        avito_elem.send_keys("Автомобили")
        time.sleep(3)
        self.driver.find_element_by_link_text("BMW").click()
        time.sleep(3)
        url1 = self.driver.find_element_by_link_text("5 серия").click()
        return self.driver.current_url

    def get_inf(self):
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


def main():
    global driver
    driver = webdriver.Chrome()
    driver.get(URL)
    parser = AvitoParser(driver)
    parser.parse()


if __name__ == '__main__':
    main()
