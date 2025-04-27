import requests
from bs4 import BeautifulSoup
import lxml

url = "https://parsinger.ru/html/index1_page_1.html"

r = requests.get(url)
r.encoding = 'utf-8'

soup = BeautifulSoup(r.text, 'lxml')
total_price = 0
price_lst = soup.find_all('p', class_="price")
for price in price_lst:
    total_price += int(price.text.split()[0])

print(total_price)