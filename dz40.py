import requests

url = "https://parsinger.ru/downloads/get_json/res.json"

response = requests.get(url).json()
result = {}
for item in response:
    if item['categories'] in result:
        result[item['categories']] += int(item['count'])
    else:
        result[item['categories']] = int(item['count'])
print(result)