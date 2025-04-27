import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/selenium/1/1.html"

with webdriver.Chrome() as browser:
    browser.get(url)
    fields = browser.find_elements(By.CLASS_NAME, 'form_box')
    for field in fields:
        input_field = field.find_element(By.TAG_NAME, 'input').send_keys('Текст')
    button = browser.find_element(By.ID, 'btn')
    button.click()
    time.sleep(10)