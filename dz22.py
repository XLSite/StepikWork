import requests
from bs4 import BeautifulSoup

url = "https://parsinger.ru/table/2/index.html"
response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table')

count = 0

rows = table.find_all('tr')[1:]
for row in rows:
    count += float(row.find_all('td')[0].text)



print(count)