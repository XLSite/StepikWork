import requests
from itertools import cycle

# Список прокси
proxies_list = [
    {'http': 'http://88.198.212.91:3128', 'https': 'https://88.198.212.91:3128'},
    {'http': 'http://222.252.194.204:8080', 'https': 'https://222.252.194.204:8080'},
    {'http': 'http://116.203.15.29:3128', 'https': 'https://116.203.15.29:3128'},
    # ... и так далее
]

proxy_pool = cycle(proxies_list)

url = "http://example.org"

# Создание сессии
session = requests.Session()

for i in range(1, 6):  # Попробуем сделать 5 запросов
    proxy = next(proxy_pool)
    session.proxies.update(proxy)  # Обновление прокси для сессии
    try:
        response = session.get(url, timeout=5)  # Используем сессию для выполнения запроса
        print(f"Request {i}: Success!")
    except requests.exceptions.RequestException as e:
        print(f"Request {i}: Failed, switching proxy. {proxy}")