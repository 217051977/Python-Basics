import urllib.request
import os

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'Example1.txt'
urllib.request.urlretrieve(url, filename)

assert os.path.exists("Example1.txt"), "Download failed: Example1.txt not found"
print("Downloaded Example1.txt, bytes:", os.path.getsize("Example1.txt"))