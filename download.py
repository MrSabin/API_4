import os
import urllib.parse
from pathlib import Path

import requests


def download_image(url, path, name, token=None):
    Path(path).mkdir(parents=True, exist_ok=True)
    extension = url_to_extension(url)
    filename = f"{path}{name}{extension}"
    payload = {'api_key': f'{token}'}
    response = (
        requests.get(url)
        if token is None
        else requests.get(url, params=payload))
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


def url_to_extension(url):
    parsed = urllib.parse.urlsplit(url)
    unquoted = urllib.parse.unquote(parsed.path)
    file_path, file_name = os.path.split(unquoted)
    splitted_path, splitted_extension = os.path.splitext(file_name)
    return splitted_extension
