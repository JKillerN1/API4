import os
from urllib.parse import urlparse

import requests

def extension (url):
    image_expansion = os.path.splitext(urlparse(url).path)
    return image_expansion[1]

def dowloands_art (url, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)

def nasa ():
    url_nasa_apod = 'https://api.nasa.gov/planetary/apod'
    param = {'api_key': os.getenv('API_KEY'), 'count': '5'}
    response = requests.get(url_nasa_apod, params=param)
    response.raise_for_status()
    art_links = response.json()
    for number, i in enumerate(art_links):
        art_link = i['url']
        filename = f'images_nasa/image{number}{extension(art_link)}'
        dowloands_art(art_link, filename)

def earth ():
    url_earth = 'https://api.nasa.gov/EPIC/api/natural/images'
    param = {'api_key': os.getenv("API_KEY"), 'natural': 'Most Recent Natural Color'}
    response = requests.get(url_earth, params=param)
    response.raise_for_status()
    art_links = response.json()
    art_links = art_links[:5]
    for number, i in enumerate(art_links):
        image = i['image']
        date = i['date'].split()
        date = date[0].replace('-', '/')
        link = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image}.png?api_key={os.getenv("API_KEY")}'
        filename = f'images_earth/image{number}{extension(link)}'
        dowloands_art(link, filename)



