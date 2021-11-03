import os
from urllib.parse import urlparse

import requests

def expansion (url):
    image_expansion = os.path.splitext(urlparse(url).path)
    return image_expansion[1]

def dowlands_art (url, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)

def nasa ():
    url_link = 'https://api.nasa.gov/planetary/apod'
    param_1 = {'api_key': 'bReWmdwdfRQj9Pqec76LrkOudbW3XB6WlD27Zcj9', 'count': '3'}
    response = requests.get(url_link, params=param_1)
    response.raise_for_status()
    art_links = response.json()
    for number, i in enumerate(art_links):
        art_link = i['url']
        filename = f'images_nasa/image{number}{expansion(c)}'
        dowlands_art(art_link, filename)

def earth ():
    url_earth = 'https://api.nasa.gov/EPIC/api/natural/images'
    param = {'api_key': 'bReWmdwdfRQj9Pqec76LrkOudbW3XB6WlD27Zcj9', 'natural': 'Most Recent Natural Color'}
    response = requests.get(url_earth, params=param)
    response.raise_for_status()
    art_links = response.json()
    art_links = art_links[:5]
    for number, i in enumerate(art_links):
        image = i['image']
        date = i['date'].split()
        date = date[0].replace('-', '/')
        link = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image}.png?api_key=bReWmdwdfRQj9Pqec76LrkOudbW3XB6WlD27Zcj9'
        filename = f'images_earth/image{number}{expansion(link)}'
        dowlands_art(link, filename)


nasa()
earth()
