import requests
import os
import pandas as pd
# from PIL import Image

url= 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'

print("Getting response from the url")
res=requests.get(url)

response_headers = res.headers
response_content = res.content
print(f"Getting response headers: {response_headers}")
print(pd.DataFrame(response_headers))
print(f"Getting response header 'Content-Type': {response_headers['Content-Type']}")
# print(f"Getting response content: {image_response_content}") # Ginormous

print("\nSave response to a file")
print("os.getcwd(): ", os.getcwd())
path=os.path.join(os.getcwd(),'image.png')
with open(path,'wb') as f:
    f.write(res.content)
# Image.open(path) # This does not work here, only on browser

print("\nSave response to a file")
print("os.getcwd(): ", os.getcwd())
path=os.path.join(os.getcwd(),'image.png')
with open(path,'wb') as f:
    f.write(res.content)
# Image.open(path) # This does not work here, only on browser

