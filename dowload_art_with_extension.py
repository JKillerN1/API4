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