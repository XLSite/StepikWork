import requests
from bs4 import BeautifulSoup

url = "https://parsinger.ru/4.8/7/index.html"

def get_soup(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    return soup
count = 0
soup = get_soup(url)
tables = soup.find_all('table')
for tbl in tables:
    tds = tbl.find_all('td')
    for i in tds:
        if int(i.text) % 3 == 0:
            count += int(i.text)

print(count)