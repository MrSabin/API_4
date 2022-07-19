import argparse
import os
from pathlib import Path

import requests
from dotenv import load_dotenv
from download import download_image


def download_nasa_apod(count, token):
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': token, 'count': count, 'hd': 'True'}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    api_metadata = response.json()
    for number, image in enumerate(api_metadata):
        image_url = image.get('hdurl')
        if image_url is None:
            print('Missing link in query. Skipping to next')
            continue
        path = Path.cwd() / 'images'
        name = f'nasa_apod_{number}'
        download_image(image_url, path, name)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--count', default=10, help='Количество фото')
    args = parser.parse_args()
    load_dotenv()
    token = os.environ["NASA_TOKEN"]
    download_nasa_apod(args.count, token)


if __name__ == '__main__':
    main()
