import argparse
import os

import requests
from dotenv import load_dotenv
from download import download_image


def download_nasa_apod(count, token):
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': token, 'count': count, 'hd': 'True'}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return_object = response.json()
    for number, image in enumerate(return_object):
        image_url = image.get('hdurl')
        path = './images/'
        name = f'nasa_apod_{number}'
        download_image(image_url, path, name)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-count', help='Количество загружаемых фото')
    args = parser.parse_args()
    load_dotenv()
    token = os.environ["NASA_TOKEN"]
    download_nasa_apod(args.count, token)


if __name__ == '__main__':
    main()
