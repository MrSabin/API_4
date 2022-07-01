import argparse

import requests
from download import image_download

parser = argparse.ArgumentParser()
parser.add_argument('--id', help='ID запуска')
args = parser.parse_args()
if args.id:
    url = f"https://api.spacexdata.com/v4/launches/{args.id}"
else:
    url = "https://api.spacexdata.com/v4/launches/latest"
response = requests.get(url)
response.raise_for_status()
answer = response.json()
print(answer)
links = answer['links']['flickr']['original']
for number, link in enumerate(links):
    print(link)
    path = './images/'
    name = f'spacex_{number}'
    image_download(link, path, name)
