import requests

url = "https://parsinger.ru/4.6/1/res.json"

response = requests.get(url).json()
result = {}
for item in response:
    sumprice = int(item['article'].strip()) *  item['description']['rating']
    if item['categories'] in result:
        result[item['categories']] += sumprice
    else:
        result[item['categories']] = sumprice
print(result)