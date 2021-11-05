import os
import time
from random import choice

from dotenv import load_dotenv
import telegram

from fetch_nasa import earth
from fetch_nasa import nasa
from fetch_spacex import fetch_spacex_last_launch

def main():
    load_dotenv()
    nasa()
    earth()
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