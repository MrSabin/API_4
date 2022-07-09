import argparse

import requests
from download import download_image


def download_spacex_photo(url):
    response = requests.get(url)
    response.raise_for_status()
    api_metadata = response.json()
    links = api_metadata['links']['flickr']['original']
    for number, link in enumerate(links):
        path = './images/'
        name = f'spacex_{number}'
        download_image(link, path, name)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', help='ID запуска')
    args = parser.parse_args()
    if args.id:
        url = f"https://api.spacexdata.com/v4/launches/{args.id}"
    else:
        url = "https://api.spacexdata.com/v4/launches/latest"
    download_spacex_photo(url)


if __name__ == '__main__':
    main()
