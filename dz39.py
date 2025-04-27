import requests
from bs4 import BeautifulSoup
import json

start_url = "https://parsinger.ru/html/index1_page_1.html"
result = []

def get_html(url):
    """Получаем страницу с HTML"""
    session = requests.Session()
    try:
        response = session.get(url)
        response.encoding = 'utf-8'
        return BeautifulSoup(response.text, 'lxml')
    except:
        TimeoutError('Сайт недоступен')


def get_card_data(s, cat_id, link):
    """Формируем данные для одной карточки товара"""
    try:
        name = s.find('p', id='p_header').text.strip()
    except:
        name = ''
    try:
        article = s.find('p', class_='article').text.split(': ')[1].strip()
    except:
        article = ''
    try:
        count = s.find('span', id='in_stock').text.split(': ')[1].strip()
    except:
        count = 0
    try:
        price = s.find('span', id='price').text.strip()
    except:
        price = ''
    try:
        old_price =s.find('span', id='old_price').text.strip()
    except:
        old_price = ''
    desc = {}
    for tag in s.find('ul', id='description').find_all('li'):
        desc[tag.get('id')] = tag.text.split(': ')[1].strip()
    card_data = {
        "categories": cat_id,
        "name": name,
        "article": article,
        "description": desc,
        "count": count,
        "price": price,
        "old_price": old_price,
        "link": link
    }
    return card_data


def get_cards_url(cat):
    """Получаем урлы всех товаров в категории"""
    soup = get_html(cat)
    pagination = ['https://parsinger.ru/html/' + x['href'] for x in soup.find('div', class_='pagen').find_all('a')]
    cards_url = []
    for page in pagination:
        soup = get_html(page)
        cards = ['https://parsinger.ru/html/' + p['href'] for p in soup.find_all('a', class_='name_item')]
        cards_url.extend(cards)
    return cards_url


categories = {}
navs = get_html(start_url).find('div', class_='nav_menu').find_all('a')
for nav in navs:
    categories[nav.find('div').get('id')] = 'https://parsinger.ru/html/' + nav['href']
for cat_id, cat_link in categories.items():
    cards_lst = get_cards_url(cat_link)
    for card in cards_lst:
        soup = get_html(card)
        result.append(get_card_data(soup, cat_id, card))


with open('res_full.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, indent=4, ensure_ascii=False)