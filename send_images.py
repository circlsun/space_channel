import os
from pathlib import Path
import telegram
from PIL import Image


def get_images():
    directory = 'images'
    files = Path(directory).glob('*')
    images = []
    [images.append(str(file)) for file in files]
    return images


def compress_image(image_name):
    quality = 90
    megabytes = 1024 ** 2  # 1024 bit in one byte
    image = Image.open(image_name)
    image_size = os.path.getsize(image_name) / megabytes
    if image_size > 20:  # Mb
        filename, ext = os.path.splitext(image_name)
        filename = f"{filename}{ext}"
        image.save(filename, quality=quality, optimize=True)


def send_telegram_photo(token, chat_id, photo):
    compress_image(photo)
    bot = telegram.Bot(token=token)
    with open(photo, "rb") as photo:
        bot.send_photo(chat_id=chat_id, photo=photo)
