from urllib.request import urlopen
html = urlopen("https://stepik.org/media/attachments/lesson/209717/1.html").read().decode('utf-8')
text = str(html)
py = int(html.count('Python'))
c = int(html.count('C++'))
if py > c:
    print('Python')
else:
    print('C++')