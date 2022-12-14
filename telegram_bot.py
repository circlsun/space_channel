import os
import argparse
import time
import random
import telegram
from PIL import Image

from dotenv import load_dotenv
from pathlib import Path


def get_list_files():
    directory = 'images'
    files = Path(directory).glob('*')
    list_files = []
    for file in files:
        list_files.append(str(file))
    return list_files


def compress_image(image_name):
    quality = 90
    Mb = 1024 ** 2
    img = Image.open(image_name)
    image_size = os.path.getsize(image_name) / Mb
    if image_size > 1:
        filename, ext = os.path.splitext(image_name)
        filename = f"{filename}{ext}"
        img.save(filename, quality=quality, optimize=True)


def send_telegram_photo(token, chat_id, photo):
    compress_image(photo)
    bot = telegram.Bot(token=token)
    bot.send_photo(chat_id=chat_id,
                   photo=open(photo, 'rb'))


def main():
    load_dotenv()
    tg_token = os.environ['TELEGRAM_TOKEN']
    tg_chat_id = os.environ['TELEGRAM_CHAT_ID']
    friquency_publications = int(os.environ['FRIQUENCY'])

    parser = argparse.ArgumentParser(
        description='This script publishes NASA photos in Telegram-channel')
    parser.add_argument(
        'quantity', nargs='?', default='1',
        help='Quantity of published per 4 hour')
    args = parser.parse_args()
    quantity_per_hour = int(args.quantity)

    while True:
        print()
        count = len(get_list_files())
        list_photos = random.sample(get_list_files(), count)

        for num in range(count):
            print(list_photos[num])
            send_telegram_photo(tg_token, tg_chat_id, list_photos[num])
            time.sleep(friquency_publications / quantity_per_hour)


if __name__ == "__main__":
    main()
