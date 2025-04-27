import requests

pages = []
with requests.Session() as s:
    s.get('https://parsinger.ru/3.3/1')
    for i in range(1, 201):
        response = s.get(f'https://parsinger.ru/3.3/1/{i}.html')
        if response.status_code == 200:
            pages.append(response.url)
            print(response.text)


print(*pages)
