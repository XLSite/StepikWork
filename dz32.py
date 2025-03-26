import requests
from bs4 import BeautifulSoup
import csv

url = "https://parsinger.ru/html/index1_page_1.html"

def get_html(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    return BeautifulSoup(response.text, 'lxml')

def write_to_csv(data):
    headers = ['Наименование', 'Артикул', 'Бренд', 'Модель', 'Тип', 'Технология экрана',
    'Материал корпуса', 'Материал браслета', 'Размер', 'Сайт производителя',
    'Наличие', 'Цена', 'Старая цена', 'Ссылка на карточку с товаром']
    with open('whatches.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(headers)
        for i in data:
            writer.writerow(i)

def get_card_data(link):
    soup = get_html(link)
    card_lst = []
    card_lst.append(soup.find('p', id="p_header").text.strip())
    card_lst.append(soup.find('p', class_="article").text.split(': ')[1].strip())
    lst = soup.find('ul', id = "description").find_all('li')
    for li in lst:
        card_lst.append(li.text.split(': ')[1].strip())
    card_lst.append(soup.find('span', id="in_stock").text.split(': ')[1].strip())
    card_lst.append(soup.find('span', id="price").text.strip())
    card_lst.append(soup.find('span', id="old_price").text.strip())
    card_lst.append(link)
    return card_lst

soup = get_html(url)
pages = soup.find('div', class_='pagen').find_all('a')

data = []
for page in pages:
    pagelink = 'https://parsinger.ru/html/' + page.get('href')
    s = get_html(pagelink)
    cards = s.find_all('div', class_="item")
    for card in cards:
        link = 'https://parsinger.ru/html/' + card.find('a', class_="name_item").get('href')
        data.append(get_card_data(link))

write_to_csv(data)
