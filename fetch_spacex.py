import os
from urllib.parse import urlparse
from pathlib import Path

import requests

Path("images").mkdir(parents=True, exist_ok=True)

def expansion (url):
    image_expansion = os.path.splitext(urlparse(url).path)
    return image_expansion[1]

def dowlands_art (url, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)

def fetch_spacex_last_launch ():
    url_link = 'https://api.spacexdata.com/v3/launches'
    response = requests.get(url_link)
    response.raise_for_status()
    art_links = response.json()[67]['links']['flickr_images']
    for art_number, art in enumerate(art_links):
        filename = f'images/image{art_number+1}{expansion(art)}'
        dowlands_art(art, filename)
        expansion(art)

fetch_spacex_last_launch()