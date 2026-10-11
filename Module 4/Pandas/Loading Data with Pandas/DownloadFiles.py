import urllib.request
import os

def download(url, file_name):
    urllib.request.urlretrieve(url, file_name)

    assert os.path.exists(file_name), f"Download failed: {file_name} not found"
    print(f"Downloaded {file_name}, bytes:", os.path.getsize(file_name))

download(
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv",
    "Product-sales.csv"
)

download(
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n9LOuKI9SlUa1b5zkaCMeg/Product-sales.xlsx",
    "Product-sales.xlsx"
)