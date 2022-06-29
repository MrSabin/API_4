import os

import requests
from dotenv import load_dotenv


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


def fetch_nasa_apod(count, token):
    image_urls = []
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': f'{token}', 'count': count, 'hd': 'True'}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    answer = response.json()
    for image in answer:
        image_urls.append(image.get('hdurl'))
    for number, link in enumerate(image_urls):
        path = './images/'
        name = f'nasa_apod_{number}'
        image_download(link, path, name)


def main():
    load_dotenv()
    token = os.environ["NASA_TOKEN"]
    fetch_nasa_epic(token)


if __name__ == '__main__':
    main()
