import requests
import urllib.parse
import os
from dotenv import load_dotenv
from pathlib import Path


def image_download(url, path, name, token=False):
    Path(path).mkdir(parents=True, exist_ok=True)
    extension = url_to_extension(url)
    filename = f"{path}{name}{extension}"
    payload = {'api_key': f'{token}'}
    response = requests.get(url, params = payload) if token else requests.get(url)
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


def fetch_nasa_epic(token):
    api_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {'api_key': f'{token}'}
    response = requests.get(api_url, params=payload)
    response.raise_for_status()
    answer = response.json()
    image_urls = []
    for entry in answer:
        name = entry.get('image')
        date = entry.get('date')
        splitted_date, splitted_time = date.split(' ')
        year, month, day = splitted_date.split('-')
        archive_url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{name}.png'
        image_urls.append(archive_url)
    for number, link in enumerate(image_urls):
        path = './images/'
        name = f'nasa_epic_{number}'
        image_download(link, path, name, token)


def main():
    load_dotenv()
    token = os.environ["NASA_TOKEN"]
    fetch_nasa_epic(token)


if __name__ == '__main__':
    main()
