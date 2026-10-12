import urllib.request
import os

def download(url, file_name):
    urllib.request.urlretrieve(url, file_name)

    assert os.path.exists(file_name), f"Download failed: {file_name} not found"
    print(f"Downloaded {file_name}, bytes:", os.path.getsize(file_name))