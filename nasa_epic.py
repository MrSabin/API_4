import requests
import os
from download import image_download
from dotenv import load_dotenv


load_dotenv()
token = os.environ["NASA_TOKEN"]
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
