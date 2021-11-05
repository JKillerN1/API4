import os
import time
from random import choice

from dotenv import load_dotenv
import telegram

from fetch_nasa import downloads_images_earth
from fetch_nasa import downloads_images_from_the_nasa
from fetch_spacex import fetch_spacex_last_launch

def main():
    load_dotenv()
    downloads_images_from_the_nasa()
    downloads_images_earth()
    fetch_spacex_last_launch()
    bot = telegram.Bot(token=os.getenv('TOKEN_BOT'))
    names_directions = ['images_earth', 'images', 'images_nasa']
    timer = 10
    while True:
        time.sleep(timer)
        random_path = choice(names_directions)
        bot.send_document(chat_id=os.getenv('CHAT_ID'), document=open(f'{random_path}/{choice(os.listdir(random_path))}', 'rb'))

if __name__ == '__main__':
    main()