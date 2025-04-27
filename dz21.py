import requests
from bs4 import BeautifulSoup

url = "https://parsinger.ru/table/1/index.html"
response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table')

myset = set()

rows = table.find_all('tr')[1:]
for row in rows:
    cells = row.find_all('td')
    for cell in cells:
        myset.add(float(cell.text))

print(sum(myset))