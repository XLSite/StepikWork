import requests
from bs4 import BeautifulSoup
#import lxml

url = "https://parsinger.ru/4.1/1/index5.html"
r = requests.get(url)
r.encoding = 'utf-8'
html = r.text

def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    email_lst = []
    # Допишите поиск и извлечение email
    emails = soup.select('div.email_field')
    for e in emails:
        mail = e.find('strong').next_sibling.strip()
        email_lst.append(mail)

    return email_lst

print(get_html(html))