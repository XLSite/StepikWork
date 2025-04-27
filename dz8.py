import requests

my_dict = {}
r = requests.get(url="https://parsinger.ru/3.4/1/json_weather.json").json()
for i in r:
    my_dict[i['Дата']] = int(i['Температура воздуха'][:-2])

print( min(my_dict, key=my_dict.get))