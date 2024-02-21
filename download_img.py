import requests
import os
from PIL import Image


def download_image(url, directory, filename):
    response = requests.get(url)
    if response.status_code == 200:
        os.makedirs(directory, exist_ok=True)
        filepath = os.path.join(directory, filename)
        with open(filepath, 'wb') as f:
            f.write(response.content)
        print(f"Image downloaded and saved as {filepath}")
    else:
        print("Failed to download the image")


