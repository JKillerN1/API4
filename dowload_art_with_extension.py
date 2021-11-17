import os
from urllib.parse import urlparse
from urllib.parse import unquote

import requests


def define_extension(url):
    image_expansion = os.path.splitext(unquote(urlparse(url).path))
    return image_expansion[1]


def download_art(url, filename, param=''):
    response = requests.get(url, param)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)
