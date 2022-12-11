import os
import requests
from urllib.parse import urlparse


def save_images(url, path):
    response = requests.get(url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    id = '61eefaa89eb1064137a1bd73'
    base_url = f"https://api.spacexdata.com/v5/launches/{id}"
    response = requests.get(base_url)
    response.raise_for_status()
    images_links = response.json()["links"]['flickr']['original']

    for image_number, images_link in enumerate(images_links):
        filename = f'spacex{image_number}.jpg'
        path_images = f'{os.getcwd()}/images/{filename}'
        save_images(images_link, path_images)

def get_expansion(url):
    parsed_url = urlparse(url)
    


def main():
    if not os.path.isdir('images'):
        os.mkdir('images')
    fetch_spacex_last_launch()


if __name__=="__main__":
    main()