import os
import argparse
import time
import random
import telegram
from PIL import Image

from dotenv import load_dotenv
from pathlib import Path


def get_images():
    directory = 'images'
    files = Path(directory).glob('*')
    images = []
    [images.append(str(file)) for file in files]
    return images


def compress_image(image_name):
    quality = 90
    Megabytes = 1024 ** 2  # 1024 bit in one byte
    image = Image.open(image_name)
    image_size = os.path.getsize(image_name) / Megabytes
    if image_size > 20:  # Mb
        filename, ext = os.path.splitext(image_name)
        filename = f"{filename}{ext}"
        image.save(filename, quality=quality, optimize=True)


def send_telegram_photo(token, chat_id, photo):
    compress_image(photo)
    bot = telegram.Bot(token=token)
    with open(photo, "rb") as photo:
        bot.send_photo(chat_id=chat_id, photo=photo)


def main():
    load_dotenv()
    tg_token = os.environ['TELEGRAM_TOKEN']
    tg_chat_id = os.environ['TELEGRAM_CHAT_ID']
    sleep_time = int(os.environ['SLEEP_TIME']) * 3600  # 3600 sec in one hour

    parser = argparse.ArgumentParser(
        description='This script publishes NASA photos in Telegram-channel')
    parser.add_argument(
        'quantity', nargs='?', default='1',
        help=f'Quantity of published per {sleep_time} hour')
    args = parser.parse_args()
    quantity_per_sleep_time = int(args.quantity)

    while True:
        print()
        count = len(get_images())
        photos = random.sample(get_images(), count)

        for num in range(count):
            print(photos[num])
            send_telegram_photo(tg_token, tg_chat_id, photos[num])
            time.sleep(sleep_time / quantity_per_sleep_time)


if __name__ == "__main__":
    main()
