import os
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv

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


def main():
    load_dotenv()
    apikey = os.environ["APIKEY"]

    fetch_nasa_apod(apikey)


if __name__ == '__main__':
    main()