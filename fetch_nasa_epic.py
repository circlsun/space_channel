import os
import requests
from datetime import datetime
from dotenv import load_dotenv


def save_images(url, path):
    response = requests.get(url)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def fetch_nasa_epic(apikey):
    base_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {
        "api_key" : apikey
        }
    response = requests.get(base_url, params=payload)
    response.raise_for_status()
    count = 8
    images = response.json()[:count]

    for image_index, image in enumerate(images):
        data = image['date']
        img_date = datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
        imgdate = img_date.strftime('%Y/%m/%d')
        
        name = image['image']
        config = f"{imgdate}/png/{name}.png"
    
        new_link = f'https://epic.gsfc.nasa.gov/archive/natural/{config}'
        response = requests.get(new_link)
        response.raise_for_status()

        filename = f'nasa_epic_{image_index}.png'
        path_images = f'{os.getcwd()}/images/{filename}'
        save_images(new_link, path_images)


def main():
    load_dotenv()
    apikey = os.environ["APIKEY"]
    fetch_nasa_epic(apikey)


if __name__ == '__main__':
    main()