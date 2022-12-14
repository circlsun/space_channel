import os
import argparse
import requests
import save_images as save


def fetch_spacex_last_launch(id):
    base_url = f"https://api.spacexdata.com/v5/launches/{id}"
    response = requests.get(base_url)
    response.raise_for_status()
    images_links = response.json()["links"]['flickr']['original']

    for image_number, images_link in enumerate(images_links):
        filename = f'spacex{image_number}'\
                   f'{save.get_file_extension(images_link)}'
        path_images = f'{os.getcwd()}/images/{filename}'
        save.save_images(images_link, path_images)


def main():
    parser = argparse.ArgumentParser(
        description='This script downloads photos of the SpaceX \
            launch of the input id')
    parser.add_argument(
        'id', nargs='?', default='latest',
        help='id SpaceX launch')
    args = parser.parse_args()
    spacex_id = args.id  # id for exsample = '61eefaa89eb1064137a1bd73'

    if not os.path.isdir('images'):
        os.mkdir('images')

    fetch_spacex_last_launch(spacex_id)


if __name__ == '__main__':
    main()
