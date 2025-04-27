import requests

url = "https://parsinger.ru/downloads/get_json/res.json"

response = requests.get(url).json()
result = {}
for item in response:
    sumprice = int(item['price'].split()[0].strip()) *  int(item['count'].strip())
    if item['categories'] in result:
        result[item['categories']] += sumprice
    else:
        result[item['categories']] = sumprice
print(result)
