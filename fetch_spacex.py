import requests

from dowload_art_with_extension import define_extension
from dowload_art_with_extension import download_art


def fetch_spacex_last_launch():
    api_spacex_url = 'https://api.spacexdata.com/v4/launches/latest'
    response = requests.get(api_spacex_url)
    response.raise_for_status()
    art_links = response.json()['links']['flickr']['original']
    for art_number, art in enumerate(art_links, start=1):
        filename = f'images/image{art_number}{define_extension(art)}'
        download_art(art, filename)


