import requests
from bs4 import BeautifulSoup
import lxml

url = "https://parsinger.ru/html/hdd/4/4_1.html"
r = requests.get(url)
r.encoding = 'utf-8'

soup = BeautifulSoup(r.text, 'lxml')
old = int(soup.find('span', id="old_price").text.split()[0])
new = int(soup.find('span', id="price").text.split()[0])
sale = round((old - new) * 100 / old, 1)

print(sale)