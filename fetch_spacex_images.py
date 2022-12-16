import os
import argparse
import requests
from save_images import save_image, get_file_extension


def fetch_spacex_last_launch(spacex_id):
    base_url = f"https://api.spacexdata.com/v5/launches/{spacex_id}"
    response = requests.get(base_url)
    response.raise_for_status()
    images_links = response.json()["links"]['flickr']['original']

    for image_number, images_link in enumerate(images_links):
        filename = f'spacex{image_number}'\
                   f'{get_file_extension(images_link)}'
        image_path = f'{os.getcwd()}/images/{filename}'
        save_image(images_link, image_path)


def main():
    parser = argparse.ArgumentParser(
        description='This script downloads photos of the SpaceX \
            launch of the input id')
    parser.add_argument(
        'id', nargs='?', default='latest',
        help='id SpaceX launch')
    args = parser.parse_args()
    spacex_id = args.id  # id for exsample = '61eefaa89eb1064137a1bd73'

    os.makedirs('images', exist_ok=True)

    fetch_spacex_last_launch(spacex_id)


if __name__ == '__main__':
    main()
