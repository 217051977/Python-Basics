import requests
import pandas as pd

url='https://httpbin.org/post'
data = {"name": "Joseph", "ID": "123"}

print("Getting response from the url with the following data: ", data)
res=requests.post(url, data=data)

response_url = res.url
request_body = res.request.body
response_headers = res.headers
response_json = res.json()
print(f"\nGetting response url: {response_url}")
print(f"Getting request body: {request_body}")
print(f"Getting response header 'Content-Type': {response_headers['Content-Type']}")
print(f"Getting response content as a dictionary: {response_json}")
print(pd.DataFrame(response_json))

