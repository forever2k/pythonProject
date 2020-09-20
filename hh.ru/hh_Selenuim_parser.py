from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import pickle
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import csv
import os

URL = 'https://hh.ru'
FILE = 'hh_selenium_class'


class HHParser:

    def __init__(self, driver):
        self.driver = driver
        driver.implicitly_wait(4)

    def parse(self):
        self.prepare()
        self.search()

    def prepare(self):
        driver.get(URL)
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.find_element_by_link_text("Войти").click()
        # wait = WebDriverWait(driver, 5)
        # wait.until(expected_conditions.visibility_of_element_located((By.NAME, 'username')))
        # name2 = driver.find_element_by_name('username').send_keys(str(input("Введите логин  ")))
        # str_find = driver.find_elements_by_name('username')
        # date = []
        # for item in str_find:
        #     date.append(item.get_attribute('value'))
        #
        # time.sleep(0.5)
        # if date == ['forever2k@yandex.ru']:
        #     driver.find_element_by_name('password').send_keys(str(input("Введите пароль ")))
        # else:
        #     print('Некорректно введен логин')
        #
        # driver.find_element_by_class_name('bloko-button_primary').send_keys(Keys.ENTER)
        #
        # driver.find_element_by_class_name('bloko-icon-link').click()


    def search(self):
        wait1 = WebDriverWait(driver, 999)
        wait1.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'bloko-icon-link')))
        driver.find_element_by_class_name('bloko-icon-link').click()
        print('here1')
        # driver.find_element_by_class_name('bloko-form-item').send_keys('TEST')




def main():
    global driver
    chrome_options = Options()
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                                'like Gecko) Chrome/85.0.4183.83 Safari/537.36')
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(options=chrome_options)
    # driver.execute_cdp_cmd()
    parser = HHParser(driver)
    parser.parse()
    # os.startfile(FILE)


if __name__ == '__main__':
    main()
