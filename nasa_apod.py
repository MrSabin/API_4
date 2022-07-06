import argparse
import os

import requests
from dotenv import load_dotenv
from download import download_image

parser = argparse.ArgumentParser()
parser.add_argument('-count', help='Количество загружаемых фото')
args = parser.parse_args()
load_dotenv()
token = os.environ["NASA_TOKEN"]
image_urls = []
url = 'https://api.nasa.gov/planetary/apod'
payload = {'api_key': token, 'count': args.count, 'hd': 'True'}
response = requests.get(url, params=payload)
response.raise_for_status()
answer = response.json()
for image in answer:
    image_urls.append(image.get('hdurl'))
for number, link in enumerate(image_urls):
    path = './images/'
    name = f'nasa_apod_{number}'
    download_image(link, path, name)
