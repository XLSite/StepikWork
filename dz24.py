import requests
from bs4 import BeautifulSoup

url = "https://parsinger.ru/table/4/index.html"
response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table')

count = 0

rows = table.find_all('tr')[1:]
for row in rows:
    cells = row.find_all('td', class_="green")
    for cell in cells:
        count += float(cell.text)



print(count)