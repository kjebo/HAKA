import requests


response = requests.get("http://localhost:5002/cfigroup.se")
for item in response:
    print(item)       
