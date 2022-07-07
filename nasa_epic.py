import os

import requests
from dotenv import load_dotenv
from download import download_image


def download_nasa_epic(token):
    api_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {'api_key': token}
    response = requests.get(api_url, params=payload)
    response.raise_for_status()
    return_object = response.json()
    image_urls = []
    for entry in return_object:
        name = entry['image']
        date = entry['date']
        splitted_date, splitted_time = date.split(' ')
        year, month, day = splitted_date.split('-')
        archive_url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{name}.png'
        image_urls.append(archive_url)
    for number, link in enumerate(image_urls):
        path = './images/'
        name = f'nasa_epic_{number}'
        download_image(link, path, name, token)


def main():
    load_dotenv()
    token = os.environ["NASA_TOKEN"]
    download_nasa_epic(token)


if __name__ == '__main__':
    main()
