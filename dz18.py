import requests
from bs4 import BeautifulSoup
import lxml

result_lst = []

def get_names(soup):
    cards = soup.find_all('div', class_="item")
    pg_lst = []
    for card in cards:
        name = card.find('a', class_="name_item").text
        pg_lst.append(name)
    return pg_lst

for i in range(1,5):
    url = "https://parsinger.ru/html/index3_page_{n}.html".format(n = i)
    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')
    result_lst.append(get_names(soup))

print(result_lst)

