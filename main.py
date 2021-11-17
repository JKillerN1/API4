import os
import time
from pathlib import Path
from random import choice

from dotenv import load_dotenv
import telegram

from fetch_nasa import download_earth_images
from fetch_nasa import download_nasa_images
from fetch_spacex import fetch_spacex_last_launch

def sending_in_telegram_image(names_directions, bot):
    random_path = choice(names_directions)
    if len(os.listdir(random_path)) != 0:
        bot.send_photo(chat_id=os.getenv('CHAT_ID'),
                       photo=open(f'{random_path}/{choice(os.listdir(random_path))}', 'rb'))


if __name__ == '__main__':
    load_dotenv()
    api_key = os.getenv('API_KEY')
    names_directions = ['images_earth', 'images', 'images_nasa']
    Path(names_directions[1]).mkdir(parents=True, exist_ok=True)
    Path(names_directions[0]).mkdir(parents=True, exist_ok=True)
    Path(names_directions[2]).mkdir(parents=True, exist_ok=True)
    download_nasa_images(api_key)
    download_earth_images(api_key)
    fetch_spacex_last_launch()
    bot = telegram.Bot(token=os.getenv('TOKEN_BOT'))
    timer = 86400
    while True:
        sending_in_telegram_image(names_directions, bot)
        time.sleep(timer)
