import requests
from bs4 import BeautifulSoup
import csv

url = "https://parsinger.ru/html/index4_page_1.html"

def get_html(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')

def write_to_csv(data):
    headers = ['Наименование', 'Бренд', 'Форм-фактор', 'Ёмкость', 'Объем буферной памяти', 'Цена']
    with open('hdd.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(headers)
        for i in data:
            writer.writerow(i)

soup = get_html(url)
pages = soup.find('div', class_='pagen').find_all('a')

data = []
for page in pages:
    pagelink = 'https://parsinger.ru/html/' + page.get('href')
    s = get_html(pagelink)
    cards = s.find_all('div', class_="item")
    for card in cards:
        name = card.find('a', class_="name_item").text.strip()
        brand = card.find('div', class_="description").find_all('li')[0].text.split(':')[1].strip()
        factor = card.find('div', class_="description").find_all('li')[1].text.split(':')[1].strip()
        capacity = card.find('div', class_="description").find_all('li')[2].text.split(':')[1].strip()
        memory = card.find('div', class_="description").find_all('li')[3].text.split(':')[1].strip()
        price = card.find('p', class_="price").text.strip()
        data.append([name, brand, factor, capacity, memory, price])

write_to_csv(data)
