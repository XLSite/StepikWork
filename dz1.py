import requests

url = "https://parsinger.ru/video_downloads/videoplayback.mp4"
r = requests.get(url=url, stream=True)
with open('video.mp4', 'wb') as file:
    file.write(r.content)