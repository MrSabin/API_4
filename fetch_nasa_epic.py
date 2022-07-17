import os
from datetime import datetime

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
        taken_at = datetime.strptime(entry['date'], "%Y-%m-%d %H:%M:%S")
        image_date = datetime.strftime(taken_at, "%Y/%m/%d")
        archive_url = 'https://api.nasa.gov/EPIC/archive/natural'
        image_url = f'{archive_url}/{image_date}/png/{name}.png'
        print(image_url)
        path = './images/'
        name = f'nasa_epic_{number}'
        download_image(image_url, path, name, payload)


def main():
    load_dotenv()
    token = os.environ["NASA_TOKEN"]
    download_nasa_epic(token)


if __name__ == '__main__':
    main()
