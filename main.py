import os
import time
from pathlib import Path
from random import choice

from dotenv import load_dotenv
import telegram

from fetch_nasa import download_earth_images
from fetch_nasa import download_nasa_images
from fetch_spacex import fetch_spacex_last_launch

def sending_in_telegram_image(folder_names, bot):
    random_path = choice(folder_names)
    if len(os.listdir(random_path)) != 0:
        with open(f'{random_path}/{choice(os.listdir(random_path))}', 'rb') as image:
            art = image.read()
            bot.send_photo(chat_id=os.getenv('CHAT_ID'),
                        photo=art)


if __name__ == '__main__':
    load_dotenv()
    api_key = os.getenv('API_KEY')
    folder_names = ['images_earth', 'images', 'images_nasa']
    for number in range(0, 3):
        Path(folder_names[number]).mkdir(parents=True, exist_ok=True)
    download_nasa_images(api_key)
    download_earth_images(api_key)
    fetch_spacex_last_launch()
    bot = telegram.Bot(token=os.getenv('TOKEN_BOT'))
    timer = 1
    while True:
        sending_in_telegram_image(folder_names, bot)
        time.sleep(timer)
