from pathlib import Path

import requests

from dowload_art_with_extension import defines_the_extension
from dowload_art_with_extension import download_arts

def fetch_spacex_last_launch():
    url_link = 'https://api.spacexdata.com/v3/launches'
    response = requests.get(url_link)
    response.raise_for_status()
    art_links = response.json()[65]['links']['flickr_images']
    for art_number, art in enumerate(art_links, start=1):
        filename = f'images/image{art_number+1}{defines_the_extension(art)}'
        download_arts(art, filename)

if __name__ == '__main__':
    Path("images").mkdir(parents=True, exist_ok=True)

