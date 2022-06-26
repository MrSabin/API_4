import requests
from pathlib import Path


def image_download(url, path, name):
    Path(path).mkdir(parents=True, exist_ok=True)
    filename = f"{path}{name}"

    response = requests.get(url)
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


fetch_spacex_last_launch()
