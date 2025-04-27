import requests
from bs4 import BeautifulSoup
import json


url = 'https://parsinger.ru/html/index1_page_1.html'

def get_html(url):
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    return soup

pages = []
soup = get_html(url)
categories = ['https://parsinger.ru/html/' + x['href'] for x in soup.find('div', class_='nav_menu').find_all('a')]
for cat in categories:
    soup = get_html(cat)
    pagination = ['https://parsinger.ru/html/' + x['href'] for x in soup.find('div', class_='pagen').find_all('a')]
    pages.extend(pagination)

res_json = []

for page in pages:
    soup = get_html(page)
    name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
    description = soup.find('div', class_='description').find_all('li')
    list_item = {}
    for i in description:
        list_item[i.text.split(':')[0].strip()] = i.text.split(':')[1].strip()
    price = [x.text.strip() for x in soup.find_all('p', class_='price')]
    res_json.append({'Наименование': name} | list_item | {'Цена': price})
    # for list_item, price_item, name in zip(description, price, name):
    #     res_json.append({
    #         'Наименование': name,
    #
    #         'Цена': price_item
    #     })
print(res_json)

# with open('res_all.json', 'w', encoding='utf-8') as file:
#     json.dump(res_json, file, indent=4, ensure_ascii=False)