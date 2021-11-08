import os
from urllib.parse import urlparse

import requests

def defines_the_extension(url):
    image_expansion = os.path.splitext(urlparse(url).path)
    return image_expansion[1]

def download_arts(url, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)