import os
import time
from pathlib import Path
from random import choice

from dotenv import load_dotenv
import telegram

from fetch_nasa import download_earth_images
from fetch_nasa import download_nasa_images
from fetch_spacex import fetch_spacex_last_launch

if __name__ == '__main__':
    Path("images").mkdir(parents=True, exist_ok=True)
    Path("images_earth").mkdir(parents=True, exist_ok=True)
    Path("images_nasa").mkdir(parents=True, exist_ok=True)
    load_dotenv()
    api_key = os.getenv('API_KEY')
    download_nasa_images(api_key)
    download_earth_images(api_key)
    fetch_spacex_last_launch()
    bot = telegram.Bot(token=os.getenv('TOKEN_BOT'))
    names_directions = ['images_earth', 'images', 'images_nasa']
    timer = 10
    while True:
        time.sleep(timer)
        random_path = choice(names_directions)
        bot.send_document(chat_id=os.getenv('CHAT_ID'),
                          document=open(f'{random_path}/{choice(os.listdir(random_path))}', 'rb'))
