import os
import requests
from urllib.parse import urlparse
from datetime import datetime
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
    

def main():
        load_dotenv()
    try:
        apikey = os.environ["BITLY_TOKEN"]
    except KeyError:
        apikey = None
        print("Add a apikey from API NASA to the virtual environment file <.env>")

    if not os.path.isdir('images'):
        os.mkdir('images')
    fetch_spacex_last_launch(id)
    fetch_nasa_apod(apikey)
    fetch_nasa_epic(apikey)


if __name__=="__main__":
    main()