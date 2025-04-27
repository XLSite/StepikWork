import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/selenium/2/2.html"

with webdriver.Chrome() as browser:
    browser.get(url)
    link = browser.find_element(By.LINK_TEXT, '16243162441624')
    link.click()
    result = browser.find_element(By.ID, 'result').text
    time.sleep(5)
    print(result)