import requests
from bs4 import BeautifulSoup
import json

url = "https://parsinger.ru/4.8/6/index.html"

def get_soup(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    return soup
soup = get_soup(url)
cars = []

rows = soup.find_all('tr')[1:]
for row in rows:
    cells = row.find_all('td')
    if int(cells[-1].text) <= 4000000 and int(cells[1].text) >= 2005 and cells[4].text == 'Бензиновый':
        cars.append({"Марка Авто": cells[0].text,
                     "Год выпуска": int(cells[1].text),
                     "Тип двигателя": cells[4].text,
                     "Стоимость авто": int(cells[-1].text)
                     })
sorted_cars = sorted(cars, key=lambda x: x["Стоимость авто"])
print(json.dumps(sorted_cars, indent=4, ensure_ascii=False))