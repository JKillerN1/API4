import os

import requests

from dowload_art_with_extension import define_extension
from dowload_art_with_extension import download_arts


def download_images_nasa():
    url_nasa_apod = 'https://api.nasa.gov/planetary/apod'
    param = {'api_key': os.getenv('API_KEY'), 'count': '5'}
    response = requests.get(url_nasa_apod, params=param)
    response.raise_for_status()
    art_links = response.json()
    for number, i in enumerate(art_links, start=1):
        art_link = i['url']
        filename = f'images_nasa/image{number}{define_extension(art_link)}'
        download_arts(art_link, filename)


def download_images_earth():
    url_earth = 'https://api.nasa.gov/EPIC/api/natural/images'
    param = {'api_key': os.getenv("API_KEY"), 'natural': 'Most Recent Natural Color'}
    response = requests.get(url_earth, params=param)
    response.raise_for_status()
    art_links = response.json()
    art_links = art_links[:5]
    for number, i in enumerate(art_links, start=1):
        image = i['image']
        date = i['date'].split()
        date = date[0].replace('-', '/')
        link = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image}.png?api_key={os.getenv("API_KEY")}'
        filename = f'images_earth/image{number}{defines_the_extension(link)}'
        download_arts(link, filename)
