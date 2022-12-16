import os
from datetime import datetime
import requests
from dotenv import load_dotenv
from save_images import save_image


def fetch_nasa_epic(apikey):
    base_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {
        "api_key": apikey
    }
    response = requests.get(base_url, params=payload)
    response.raise_for_status()
    count = 8
    images = response.json()[:count]

    for image_index, image in enumerate(images):
        parsed_image_date = image['date']
        convert_image_date = datetime.strptime(
            parsed_image_date, "%Y-%m-%d %H:%M:%S")
        image_date = convert_image_date.strftime('%Y/%m/%d')

        image_name = image['image']
        epic_endpoint = f"{image_date}/png/{image_name}.png"

        new_link = f'https://epic.gsfc.nasa.gov/archive/natural/' \
                   f'{epic_endpoint}'
        response = requests.get(new_link)
        response.raise_for_status()

        filename = f'nasa_epic_{image_index}.png'
        image_path = f'{os.getcwd()}/images/{filename}'
        save_image(new_link, image_path)


def main():
    load_dotenv()
    try:
        apikey = os.environ["NASA_APIKEY"]
    except KeyError:
        apikey = None
        print("Add apikey from API NASA to the virtual \
            environment file <.env>")

    os.makedirs('images', exist_ok=True)

    fetch_nasa_epic(apikey)


if __name__ == '__main__':
    main()
