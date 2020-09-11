from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import os

URL = 'https://hh.ru'
FILE = 'hh_selenium_class'


class HHParser:

    def __init__(self, driver):
        self.driver = driver
        driver.implicitly_wait(4)

    def prepare(self):
        driver.get(URL)
        driver.find_element_by_link_text("Войти").click()
        driver.find_element_by_name('username').send_keys(str(input("Введите логин")))
        driver.find_element_by_name('password').send_keys(str(input("Введите пароль")))
        name1 = driver.find_element_by_class_name('light-page-content')
        name2 = name1.find_element_by_class_name('bloko-button_primary').send_keys(Keys.ENTER)
        print(name2)
        # driver.find_element_by_class_name('bloko-form-row').send_keys(Keys.ENTER)

        # hh = driver.find_element_by_class_name('light-page-content')
        # hh2 = hh.find_element_by_class_name('bloko-form-row')
        # print(hh2)




def main():
    global driver
    driver = webdriver.Chrome()
    parser = HHParser(driver)
    parser.prepare()
    # os.startfile(FILE)


if __name__ == '__main__':
    main()
