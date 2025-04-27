import requests
start ="https://parsinger.ru/3.3/4/1.html"
first_available_page = ''
last_available_page = ''

with requests.Session() as s:
    s.head(url=start)
    for i in range(1, 101):
        page_status = s.head(f"https://parsinger.ru/3.3/4/{i}.html").status_code
        if page_status == 200 and not first_available_page:
            first_available_page = i
        if page_status == 200:
            last_available_page = i

print(f"Первая доступная страница: {first_available_page}.html")
print(f"Последняя доступная страница: {last_available_page}.html")