import os
import telegram
from dotenv import load_dotenv

load_dotenv()
TG_TOKEN = os.environ['TELEGRAM_TOKEN']
TG_CHAT_ID = os.environ['TELEGRAM_CHAT_ID']

print(TG_TOKEN, TG_CHAT_ID)

bot = telegram.Bot(token=TG_TOKEN)
updates = bot.get_updates()
print(updates[0])
