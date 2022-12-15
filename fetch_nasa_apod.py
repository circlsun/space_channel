import os
import requests
from dotenv import load_dotenv
from save_images import save_image, get_file_extension


def fetch_nasa_apod(apikey):
    count = 30
    base_url = 'https://api.nasa.gov/planetary/apod'
    payload = {
        "api_key": apikey,
        "count": count
    }
    response = requests.get(base_url, params=payload)
    base_url = response.json()
    response.raise_for_status()
    for num in range(count):
        nasa_url = base_url[num]['url']
        filename = f'nasa_apod_{num}{get_file_extension(nasa_url)}'
        image_path = f'{os.getcwd()}/images/{filename}'
        save_image(nasa_url, image_path)


def main():
    load_dotenv()
    try:
        apikey = os.environ["NASA_APIKEY"]
    except KeyError:
        apikey = None
        print("Add apikey from API NASA to the virtual \
            environment file <.env>")

    if not os.path.isdir('images'):
        os.mkdir('images')

    fetch_nasa_apod(apikey)


if __name__ == '__main__':
    main()
