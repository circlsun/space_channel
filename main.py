import os
import requests


if not os.path.isdir('images'):
    os.mkdir('images')

filename = 'hubble.jpeg'
url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
images = f'{os.getcwd()}/images/{filename}'

response = requests.get(url)
response.raise_for_status()

with open(images, 'wb') as file:
    file.write(response.content)
