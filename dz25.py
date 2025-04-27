import requests
from bs4 import BeautifulSoup

url = "https://parsinger.ru/table/5/index.html"
response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table')

count = 0

rows = table.find_all('tr')[1:]
for row in rows:
    orange = float(row.find('td', class_='orange').text)
    blue = float(row.find_all('td')[-1].text)
    count += orange * blue

print(count)