import os
import argparse
import random

from dotenv import load_dotenv
from send_images import get_images, send_telegram_photo


def main():
    load_dotenv()
    tg_token = os.environ['TELEGRAM_TOKEN']
    tg_chat_id = os.environ['TELEGRAM_CHAT_ID']

    photos = get_images()
    random.shuffle(photos)

    parser = argparse.ArgumentParser(
        description='This script publishes one NASA photo in Telegram-channel')
    parser.add_argument(
        'image', nargs='?', default=photos[0],
        help='Name of photo for publish')
    args = parser.parse_args()
    photo = args.image
    print(photos[0])
    send_telegram_photo(tg_token, tg_chat_id, photo)


if __name__ == "__main__":
    main()
