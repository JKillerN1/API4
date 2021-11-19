import os

import requests

from dowload_art_with_extension import define_extension
from dowload_art_with_extension import download_art


def download_nasa_images(api_key, folder):
    apod_nasa_url = 'https://api.nasa.gov/planetary/apod'
    param = {'api_key': api_key, 'count': '5'}
    response = requests.get(apod_nasa_url, params=param)
    response.raise_for_status()
    art_links = response.json()
    for art_number, art in enumerate(art_links, start=1):
        art_link = art['url']
        filename = f'{folder}/image{art_number}{define_extension(art_link)}'
        download_art(art_link, filename)


def download_earth_images(api_key, folder):
    earth_image_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    param = {'api_key': api_key, 'natural': 'Most Recent Natural Color'}
    response = requests.get(earth_image_url, params=param)
    response.raise_for_status()
    art_links = response.json()
    art_links = art_links[:5]
    for art_number, art in enumerate(art_links, start=1):
        image = art['image']
        date = art['date'].split()
        date = date[0].replace('-', '/')
        link = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image}.png'
        link_param = {'api_key': api_key}
        filename = f'{folder}/image{art_number}{define_extension(link)}'
        download_art(link, filename, link_param)
