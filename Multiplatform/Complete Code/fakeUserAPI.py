

import requests
import json
# Get Whole Random Users Data
url = 'https://randomuser.me/api/'
response = requests.get(url)
data = json.loads(response.text)
print(data)
# Get Male User Data
url = "https://randomuser.me/api/?gender=male"
response = requests.get(url)
data = json.loads(response.text)
print(data)
# Get User Data in CSV
url = "https://randomuser.me/api/?format=csv"
response = requests.get(url)
data = json.loads(response.text)
print(data)