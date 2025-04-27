import requests

for i in range(1, 161):
    r = requests.get(f"https://parsinger.ru/img_download/img/ready/{i}.png")
    with open(f'img//image-{i}.png', 'wb') as file:
        file.write(r.content)