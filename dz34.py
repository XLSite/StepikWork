import requests
from bs4 import BeautifulSoup
import csv

start_url = "https://parsinger.ru/html/index1_page_1.html"
data = []

def write_to_csv(data):
    """Пишем в файл .csv данные из списка data"""
    with open('cards_data.csv', 'w', encoding='utf-8', newline='') as file:
        headers = ['Наименование', 'Артикул', 'Бренд', 'Модель', 'Наличие', 'Цена', 'Старая цена',
                   'Ссылка на карточку с товаром']
        writer = csv.writer(file, delimiter=';')
        writer.writerow(headers)
        for el in data:
            writer.writerow(el)

def get_html(url):
    """Получаем страницу с HTML"""
    session = requests.Session()
    try:
        response = session.get(url)
        response.encoding = 'utf-8'
        return BeautifulSoup(response.text, 'lxml')
    except:
        TimeoutError('Сайт недоступен')

def create_link(element):
    link = 'https://parsinger.ru/html/' + element.get('href')
    soup = get_html(link)
    return soup

def get_cards_data(lnk, html):
    """Собираем данные с карточек и аппендим в дату"""
    lst = []
    lst.append(html.find('p', id="p_header").text.strip())
    lst.append(html.find('p', class_="article").text.split(': ')[1].strip())
    desc = html.find('div', class_="description").find_all('li')
    lst.append(desc[0].text.split(': ')[1].strip())
    lst.append(desc[1].text.split(': ')[1].strip())
    lst.append(html.find('span', id="in_stock").text.split(': ')[1].strip())
    lst.append(html.find('span', id="price").text.strip())
    lst.append(html.find('span', id="old_price").text.strip())
    lst.append(lnk)
    data.append(lst)

soup = get_html(start_url)
categories = soup.find('div', class_="nav_menu").find_all('a')
for cat in categories: # Обход по разделам
    soup = create_link(cat)
    pagen = soup.find('div', class_="pagen").find_all('a')
    for el in pagen: # Обход по пагинации
        soup = create_link(el)
        card_links = soup.find_all('a', class_="name_item")
        for card in card_links: # Переход в карточки
            link = 'https://parsinger.ru/html/' + card.get('href')
            sp = get_html(link)
            get_cards_data(link, sp)

write_to_csv(data)