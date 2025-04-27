import requests
from bs4 import BeautifulSoup
import lesson_csv
from random import choice

url = 'http://httpbin.org/user-agent'

with open('user_agent.txt') as file:
    lines = file.read().split('\n')

for line in lines:
    user_agent = {'user-agent': choice(lines)}
    response = requests.get(url=url, headers=user_agent)
    print(response.text)

#url = "https://comfer.ru/catalog/"
#r = requests.get(url)
#print(r.text)


# from requests.auth import HTTPBasicAuth
#
# # Указываем логин и пароль
# response = requests.get('https://www.example.com', auth=HTTPBasicAuth('user', 'pass'))
#
# # Создаем сессию
# with requests.Session() as s:
#     s.get('https://www.example.com/login')
#     response = s.get('https://www.example.com/data')

# try:
#     response = requests.get('https://www.example.com', timeout=1)
# except requests.Timeout:
#     print("Слишком долгое ожидание!")
# except requests.RequestException as e:
#     print(f"Произошла ошибка: {e}")
#
# # Открываем файл и отправляем его на сервер
# with open('file.txt', 'rb') as f:
#     files = {'file': f}
#     response = requests.post('https://www.example.com/upload', files=files)
#
# # Загрузка файла с сервера по частям
# with requests.get('https://www.example.com/file', stream=True) as r:
#     with open('file.txt', 'wb') as f:
#         for chunk in r.iter_content(chunk_size=8192):
#             f.write(chunk)

# Использование куки в сессии
# with requests.Session() as s:
#     s.get('https://www.example.com/login')
#     cookies = dict(cookies_are='working')
#     response = s.get('https://www.example.com/data', cookies=cookies)