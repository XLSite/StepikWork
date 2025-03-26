import requests
from bs4 import BeautifulSoup
import csv

start_url = "https://parsinger.ru/html/index1_page_1.html"
data = []

def write_to_csv(data):
    """Пишем в файл .csv данные из списка data"""
    with open('all_cards_data.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for el in data:
            writer.writerow(el)

def get_html(url):
    """Получаем страницу с HTML"""
    session = requests.Session()
    response = session.get(url)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')

def get_cards_data(html):
    """Собираем данные с карточек и аппендим в дату"""
    cards = html.find_all('div', class_="item")
    for card in cards:
        lst = []
        lst.append(card.find('a', class_="name_item").text.strip())
        desc = card.find('div', class_="description").find_all('li')
        for i in desc:
            lst.append(i.text.split(': ')[1].strip())
        lst.append(card.find('p', class_="price").text.strip())
        data.append(lst)

soup = get_html(start_url)
# Обход по разделам
categories = soup.find('div', class_="nav_menu").find_all('a')
for cat in categories:
    cat_link = 'https://parsinger.ru/html/' + cat.get('href')
    soup = get_html(cat_link)
    pagination = soup.find('div', class_="pagen").find_all('a')
    for el in pagination:
        pg_link = 'https://parsinger.ru/html/' + el.get('href')
        sp = get_html(pg_link)
        get_cards_data(sp)

write_to_csv(data)