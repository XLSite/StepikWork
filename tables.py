import requests
from bs4 import  BeautifulSoup

url = 'https://parsinger.ru/4.8/4/index.html'

response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table')
headers = ['Имя', 'Фамилия', 'Возраст', 'Контакты', 'Хобби', 'Foto']

rows = table.find_all('tr')[1:]
data = []

for row in rows:
    row_data = {}
    for header, cell in zip(headers, row.find_all('td')):
        if cell.find('a'):
            links = cell.find_all('a')
            if 'mailto' in links[0]['href']:
                row_data['Email'] = links[0].text
                row_data['Phone'] = links[1].text
            else:
                row_data[header] = cell.text
        elif cell.find('img'):
            row_data['Foto'] = cell.find('img')['src']
        else:
            row_data[header] = cell.text
    data.append(row_data)
for entry in data:
    print(entry)