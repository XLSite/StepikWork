import requests

r = requests.get(url="https://parsinger.ru/3.4/3/dialog.json").json()
def get_posts(dct):
    # это словарь-счетчик юзеров и постов
    result = {}
    # частотная характеристика - подсчет количества юзеров в словаре
    result[dct['username']] = result.get(dct['username'], 0) + 1
    # если список dct['comments'] не пустой, перебираю все элементы el
    # этого списка, которые являются словарями
    if dct['comments']:
        for el in dct['comments']:
            # рекурсивный вызов функции get_posts
            for key, value in get_posts(el).items():
                result[key] = result.get(key, 0) + value
    return result

my_dict = get_posts(r)
res = {k: v for k, v in sorted(my_dict.items(), key=lambda item: (-item[1], item[0]))}
print(res)