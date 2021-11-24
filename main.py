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
    files_in_folder = os.listdir(random_path)
    if files_in_folder:
        with open(f'{random_path}/{choice(files_in_folder)}', 'rb') as image:
            art = image.read()
            bot.send_photo(chat_id=os.getenv('CHAT_ID'),
                        photo=art)


if __name__ == '__main__':
    load_dotenv()
    api_key = os.getenv('API_NASA_KEY')
    folder_names = ['images_earth', 'images', 'images_nasa']
    for image in folder_names:
        Path(image).mkdir(parents=True, exist_ok=True)
    download_nasa_images(api_key, folder_names[2])
    download_earth_images(api_key, folder_names[0])
    fetch_spacex_last_launch(folder_names[1])
    bot = telegram.Bot(token=os.getenv('TOKEN_BOT'))
    timer = 1
    while True:
        send_image_in_telegram(folder_names, bot)
        time.sleep(timer)
