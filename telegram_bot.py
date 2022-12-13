import os
import telegram
from dotenv import load_dotenv


def main():
    load_dotenv()
    TG_TOKEN = os.environ['TELEGRAM_TOKEN']
    TG_CHAT_ID = os.environ['TELEGRAM_CHAT_ID']

    bot = telegram.Bot(token=TG_TOKEN)
    bot.send_photo(chat_id=TG_CHAT_ID, photo=open('images/nasa_apod_0.jpg', 'rb'))


if __name__ == "__main__":
    main()
