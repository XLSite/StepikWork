import requests

count = 0
with requests.Session() as s:
    s.get('https://parsinger.ru/3.3/2')
    for i in range(1, 201):
        response = s.get('https://parsinger.ru/3.3/2/' + str(i) +'.html').status_code
        count += int(response)

print(count)


