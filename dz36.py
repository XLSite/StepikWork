import requests
from bs4 import BeautifulSoup
import json

url = 'https://parsinger.ru/html/index4_page_1.html'

def get_html(url):
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    return soup


soup = get_html(url)
pagination = ['https://parsinger.ru/html/' + x['href'] for x in soup.find('div', class_='pagen').find_all('a')]

result = []
for page in pagination:
    soup = get_html(page)
    name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
    description = [x.text.strip().split('\n') for x in
                   soup.find_all('div', class_='description')]
    price = [x.text.strip() for x in soup.find_all('p', class_='price')]

    for list_item, price_item, name in zip(description, price, name):
        result.append({
            'Наименование': name,
            'Бренд': [x.split(':')[1].strip() for x in list_item][0],
            'Форм-фактор': [x.split(':')[1].strip() for x in list_item][1],
            'Ёмкость': [x.split(':')[1].strip() for x in list_item][2],
            'Объем буферной памяти': [x.split(':')[1].strip() for x in list_item][3],
            'Цена': price_item
        })


with open('res_hdd.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, indent=4, ensure_ascii=False)

