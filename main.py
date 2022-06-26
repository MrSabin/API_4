import requests
import urllib.parse
import os
from pathlib import Path


def image_download(url, path, name):
    Path(path).mkdir(parents=True, exist_ok=True)
    filename = f"{path}{name}"

    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    url = "https://api.spacexdata.com/v3/launches/past"
    payload = {'flight_number': 13}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    answer = response.json()
    links = answer[0]['links']['flickr_images']

    for number, link in enumerate(links):
        path = './images/'
        name = f'spacex_{number}'
        image_download(link, path, name)


def url_to_extension(url):
    parsed = urllib.parse.urlsplit(url)
    unquoted = urllib.parse.unquote(parsed.path)
    file_path, file_name = os.path.split(unquoted)
    splitted_path, splitted_extension = os.path.splitext(file_name)
    return splitted_extension


url = "https://example.com/txt/hello%20world.txt?v=9#python"
url_to_extension(url)
