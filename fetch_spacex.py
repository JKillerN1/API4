from pathlib import Path

import requests

from dowload_art_with_extension import define_extension
from dowload_art_with_extension import download_arts


def fetch_spacex_last_launch():
    url_link = 'https://api.spacexdata.com/v4/launches/latest'
    response = requests.get(url_link)
    response.raise_for_status()
    art_links = response.json()['links']['flickr']['original']
    for art_number, art in enumerate(art_links, start=1):
        filename = f'images/image{art_number+1}{define_extension(art)}'
        download_arts(art, filename)

if __name__ == '__main__':
    Path("images").mkdir(parents=True, exist_ok=True)

