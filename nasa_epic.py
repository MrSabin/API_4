import os

import requests
from dotenv import load_dotenv
from download import download_image


def download_nasa_epic(token):
    api_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {'api_key': token}
    response = requests.get(api_url, params=payload)
    response.raise_for_status()
    api_metadata = response.json()
    for number, entry in enumerate(api_metadata):
        name = entry['image']
        date = entry['date']
        splitted_date, splitted_time = date.split(' ')
        year, month, day = splitted_date.split('-')
        archive_url = 'https://api.nasa.gov/EPIC/archive/natural'
        image_url = f'{archive_url}/{year}/{month}/{day}/png/{name}.png'
        path = './images/'
        name = f'nasa_epic_{number}'
        download_image(image_url, path, name, token)


def main():
    load_dotenv()
    token = os.environ["NASA_TOKEN"]
    download_nasa_epic(token)


if __name__ == '__main__':
    main()
