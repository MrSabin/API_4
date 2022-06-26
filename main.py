import requests
from pathlib import Path


def image_download(url, path):
    Path(path).mkdir(parents=True, exist_ok=True)
    filename = f"{path}hubble.jpg"

    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
path = "./images/"
image_download(url, path)
