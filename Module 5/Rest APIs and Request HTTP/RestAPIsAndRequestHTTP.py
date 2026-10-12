import requests
import pandas as pd

# more information about requests: https://requests.readthedocs.io/en/master/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01

url='https://www.ibm.com/'

print("Getting response from the url")
res=requests.get(url)
print(res)

response_status_code = res.status_code
request_headers = res.request.headers
request_body = res.request.body
response_encoding = res.encoding
response_text = res.text
print(f"\nGetting response status code: {response_status_code}")
print(f"Getting request headers: {request_headers}")
print(pd.DataFrame(request_headers))
print("Getting request body:", request_body)
print(f"Getting request header 'User-Agent': {request_headers['User-Agent']}")
print(f"Getting request header 'Cookie': {request_headers['Cookie']}")
print(f"Getting response encoding: {response_encoding}")
print(f"Getting response text: {response_text[0:42]}")

