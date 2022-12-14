import os
import argparse
import time
import random
import telegram

from dotenv import load_dotenv
from pathlib import Path


def get_list_files():
    directory = 'images'
    files = Path(directory).glob('*')
    list_files = []
    for file in files:
        list_files.append(str(file))
    return list_files


def send_telegram_photo(token, chat_id, photo):
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
        help='Quantity of published per hour')
    args = parser.parse_args()
    quantity_per_hour = args.quantity

    count = len(get_list_files())
    while True:
        print()
        count = len(get_list_files())
        list_photos = random.sample(get_list_files(), count)

        while count > 0:
            count -= 1
            print(list_photos[count])
            send_telegram_photo(tg_token, tg_chat_id, list_photos[count])
            time.sleep(friquency_publications / quantity_per_hour)


if __name__ == "__main__":
    main()
