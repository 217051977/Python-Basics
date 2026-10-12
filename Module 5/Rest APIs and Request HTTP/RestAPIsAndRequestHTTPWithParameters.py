import requests
import pandas as pd

url='https://www.ibm.com/'
payload = {"name":"Joseph","ID":"123"}

print("Getting response from the url with the following payload: ", payload)
res=requests.get(url, params=payload)

response_url = res.url
response_headers = res.headers
print(f"\nGetting response url: {response_url}")
print(f"Getting request headers: {response_headers}")
print(pd.DataFrame(response_headers))
print(f"Getting response header 'Content-Type': {response_headers['Content-Type']}")

