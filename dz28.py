import requests
from bs4 import BeautifulSoup

url = "https://parsinger.ru/4.8/8/index.html"

def get_soup(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    return soup

soup = get_soup(url)
cells = [int(el.text) for el in soup.find_all(lambda x: x.has_attr('colspan') and x.text.strip().isdigit())]

print(sum(cells))