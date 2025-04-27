from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://parsinger.ru/selenium/3/3.html"

with webdriver.Chrome() as browser:
    browser.get(url)
    divs = browser.find_elements(By.CLASS_NAME, 'text')

    for i, div in enumerate(divs):
        first_p = div.find_element(By.XPATH, './p[1]')
        third_p = div.find_element(By.XPATH, './p[3]')

        print(f"Для div #{i + 1}, первый p: {first_p.text}, третий p: {third_p.text}")
