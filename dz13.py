import requests
from bs4 import BeautifulSoup
import lxml

r = requests.get('https://parsinger.ru/4.3/4/index.html')
r.encoding = 'utf-8'

soup = BeautifulSoup(r.text, 'lxml')
text = soup.find_all('p')
total_id_sum = 0
total_class_sum = 0
for i in text:
    l_txt = len(i.text.strip().replace(' ', ''))
    if l_txt % 2 == 0:
        total_id_sum += int(i.get('id'))
        total_class_sum += int(i.get('class')[0])
        print(f"id = {id_} --- class = {cls}")

