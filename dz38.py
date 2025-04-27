import requests
from bs4 import BeautifulSoup
import json

cat = "https://parsinger.ru/html/index2_page_1.html"
result = []

def get_html(url):
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    return soup

def get_card_data(s, link):
    name = s.find('p', id='p_header').text.strip()
    article = s.find('p', class_='article').text.strip().split(': ')[1].strip()
    count = s.find('span', id='in_stock').text.strip().split(': ')[1]
    price = s.find('span', id='price').text.strip()
    old_price =s.find('span', id='old_price').text.strip()
    desc = {}
    for tag in s.find('ul', id='description').find_all('li'):
        desc[tag.get('id')] = tag.text.strip().split(': ')[1].strip()
    card_data = {
        "categories": "mobile",
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
    soup = get_html(cat)
    pagination = ['https://parsinger.ru/html/' + x['href'] for x in soup.find('div', class_='pagen').find_all('a')]
    cards_url = []
    for page in pagination:
        soup = get_html(page)
        cards = ['https://parsinger.ru/html/' + p['href'] for p in soup.find_all('a', class_='name_item')]
        cards_url.extend(cards)
    return cards_url

cards_lst = get_cards_url(cat)
for card in cards_lst:
     soup = get_html(card)
     result.append(get_card_data(soup, card))

with open('res_mobile.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, indent=4, ensure_ascii=False)

