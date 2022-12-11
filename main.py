import os
import requests


if not os.path.isdir('images'):
    os.mkdir('images')

filename = 'hubble.jpeg'
url_images = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
path_images = f'{os.getcwd()}/images/{filename}'


def save_images(url, path):
    response = requests.get(url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


save_images(url_images, path_images)
