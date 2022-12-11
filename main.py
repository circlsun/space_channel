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
        filename = f'spacex{image_number}{get_file_extension(images_link)}'
        path_images = f'{os.getcwd()}/images/{filename}'
        save_images(images_link, path_images)


def fetch_nasa_apod():
    count = 50
    apikey = "3KjCE10BlO1Qbq7odcILU9uKGpo0ltj0rWcgP7QT"
    base_url = f'https://api.nasa.gov/planetary/apod'
    payload = {
        "api_key" : apikey,
        "count" : count
        }
    response = requests.get(base_url, params=payload)
    response.raise_for_status()
    for num in range(count):
        nasa_url = response.json()[num]['url']
        filename = f'nasa_apod_{num}{get_file_extension(nasa_url)}'
        path_images = f'{os.getcwd()}/images/{filename}'
        save_images(nasa_url, path_images)


def get_file_extension(url):
    parsed_url = urlparse(url).path
    extension = os.path.splitext(parsed_url)[1]
    return extension
    

def main():
    test_url = 'https://apod.nasa.gov/apod/image/2212/iotruecolor_galileo_2796.jpg'

    if not os.path.isdir('images'):
        os.mkdir('images')
    # fetch_spacex_last_launch()
    fetch_nasa_apod()


if __name__=="__main__":
    main()