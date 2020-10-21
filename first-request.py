import requests

site = requests.get("https://i.imgur.com/xsGnfjK.png")

with open('image.png', 'wb') as f:
    f.write(site.content)


