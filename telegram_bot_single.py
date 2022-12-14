import os
import argparse
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

    random_photo = random.sample(get_list_files(), len(get_list_files()))[0]

    parser = argparse.ArgumentParser(
        description='This script publishes one NASA photo in Telegram-channel')
    parser.add_argument(
        'image', nargs='?', default=random_photo,
        help='Name of photo for publish')
    args = parser.parse_args()
    photo = args.image
    send_telegram_photo(tg_token, tg_chat_id, photo)


if __name__ == "__main__":
    main()
