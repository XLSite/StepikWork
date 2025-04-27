import requests
from bs4 import BeautifulSoup
import lxml


def get_html(url):
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    return resp.text

def get_sum(card_url):
    soup = BeautifulSoup(get_html(card_url), 'lxml')
    instock = int(soup.find('span', id='in_stock').text.split()[-1])
    price = int(soup.find('span', id='price').text.split()[0])
    return instock * price

start_url = "https://parsinger.ru/html/index1_page_1.html"
total_sum = 0
for i in range(1, 6):
    ln = f"https://parsinger.ru/html/index{i}_page_"
    for j in range(1, 5):
        link_page = f"{ln}{j}.html"
        soup = BeautifulSoup(get_html(link_page), 'lxml')
        cards = soup.find_all('a', class_="name_item")
        for card in cards:
            card_url = "https://parsinger.ru/html/" + card.get('href')
            total_sum += get_sum(card_url)

print(total_sum)