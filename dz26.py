import requests
from bs4 import BeautifulSoup

url = "https://parsinger.ru/table/5/index.html"

response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'lxml')
table = soup.find('table')
headers = []
thead = table.find_all('tr')[0].find_all('th')
for el in thead:
    headers.append(el.text)
rows = []
tbody = table.find_all('tr')[1:]
for tr in tbody:
    lst = [x.text for x in tr.find_all('td')]
    rows.append(lst)
result = {}
for i in range(15):
    count = 0
    for row in rows:
        count += float(row[i])
    result[headers[i]] = round(count, 3)
print(result)
