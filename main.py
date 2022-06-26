import requests
from pathlib import Path


def image_download(url, path):
    Path(path).mkdir(parents=True, exist_ok=True)
    filename = f"{path}hubble.jpg"

    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


url = "https://api.spacexdata.com/v3/launches/past"
payload = {'flight_number': 13}
response = requests.get(url, params=payload)
response.raise_for_status()
answer = response.json()
links = answer[0]['links']['flickr_images']
print(links)
