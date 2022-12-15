import os
import argparse
import time
import random

from dotenv import load_dotenv
from send_images import get_images, send_telegram_photo


def main():
    load_dotenv()
    tg_token = os.environ['TELEGRAM_TOKEN']
    tg_chat_id = os.environ['TELEGRAM_CHAT_ID']
    sleep_time = int(os.environ['SLEEP_TIME']) * 3600  # 3600 sec in one hour

    parser = argparse.ArgumentParser(
        description='This script publishes NASA photos in Telegram-channel')
    parser.add_argument(
        'quantity', type=int, nargs='?', default=1,
        help=f'Quantity of published per {sleep_time} hour')
    args = parser.parse_args()
    quantity_per_sleep_time = args.quantity

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
