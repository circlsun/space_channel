import os
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
import save_images as save


def save_images(url, path):
    response = requests.get(url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def get_file_extension(url):
    parsed_url = urlparse(url).path
    extension = os.path.splitext(parsed_url)[1]
    return extension


def fetch_nasa_apod(apikey):
    count = 30
    base_url = 'https://api.nasa.gov/planetary/apod'
    payload = {
        "api_key": apikey,
        "count": count
        }
    response = requests.get(base_url, params=payload)
    response.raise_for_status()
    for num in range(count):
        nasa_url = response.json()[num]['url']
        filename = f'nasa_apod_{num}{save.get_file_extension(nasa_url)}'
        path_images = f'{os.getcwd()}/images/{filename}'
        save.save_images(nasa_url, path_images)


def main():
    load_dotenv()
    try:
        apikey = os.environ["APIKEY"]
    except KeyError:
        apikey = None
        print("Add an apikey from API NASA to the virtual \
            environment file <.env>")

    if not os.path.isdir('images'):
        os.mkdir('images')

    fetch_nasa_apod(apikey)


if __name__ == '__main__':
    main()
