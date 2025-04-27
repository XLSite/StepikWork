import requests
from bs4 import BeautifulSoup
import lxml

def get_html(url):
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    return resp.text

def get_article(card_url):
    soup = BeautifulSoup(get_html(card_url), 'lxml')
    article = int(soup.find('p', class_='article').text.split()[-1])
    return article

total_sum = 0
for i in range(1, 5):
    url = f"https://parsinger.ru/html/index3_page_{i}.html"
    soup = BeautifulSoup(get_html(url), 'lxml')
    cards = soup.find_all('a', class_="name_item")
    for card in cards:
        card_url = 'https://parsinger.ru/html/' + card.get('href')
        total_sum += get_article(card_url)

print(total_sum)