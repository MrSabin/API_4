import requests
from pathlib import Path


Path("./images").mkdir(parents=True, exist_ok=True)
filename = "./images/hubble.jpg"
url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"

response = requests.get(url)
print(response)
response.raise_for_status()

with open(filename, 'wb') as file:
    file.write(response.content)
