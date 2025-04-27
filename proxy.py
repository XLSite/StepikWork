import random
import requests
from fake_useragent import UserAgent

url = 'http://httpbin.org/ip'
with open('proxy.txt') as file:
    proxy_file = file.read().split('\n')
    random.shuffle(proxy_file)
    for proxy_ in proxy_file:
        try:
            ip = proxy_.strip()
            print(proxy_)

            proxy = {
                'http': f'http://{ip}',
                'https': f'https://{ip}'
            }

            response = requests.get(url=url, proxies=proxy, timeout=3)
            print(response.json(), 'Success connection')
        except Exception as _ex:

            # В случае неудачи пропускаем текущую итерацию
            continue
