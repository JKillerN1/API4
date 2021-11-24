import os
import time
from pathlib import Path
from random import choice

from dotenv import load_dotenv
import telegram

from fetch_nasa import download_earth_images
from fetch_nasa import download_nasa_images
from fetch_spacex import fetch_spacex_last_launch

def send_image_in_telegram(folder_names, bot):
    random_path = choice(folder_names)
    if os.listdir(random_path):
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
    download_nasa_images(api_key, folder_names[2])
    download_earth_images(api_key, folder_names[0])
    fetch_spacex_last_launch(folder_names[1])
    bot = telegram.Bot(token=os.getenv('TOKEN_BOT'))
    timer = 1
    while True:
        send_image_in_telegram(folder_names, bot)
        time.sleep(timer)
