import os
from urllib.parse import urlparse
from pathlib import Path

import requests

def extension (url):
    image_expansion = os.path.splitext(urlparse(url).path)
    return image_expansion[1]

def dowloands_art (url, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)

def fetch_spacex_last_launch ():
    url_link = 'https://api.spacexdata.com/v3/launches'
    response = requests.get(url_link)
    response.raise_for_status()
    art_links = response.json()[-1]['links']['flickr_images']
    for art_number, art in enumerate(art_links):
        filename = f'images/image{art_number+1}{extension(art)}'
        dowloands_art(art, filename)
        extension(art)

if __name__ == '__main__':
    Path("images").mkdir(parents=True, exist_ok=True)

