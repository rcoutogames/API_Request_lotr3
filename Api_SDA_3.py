
import requests
import json

headers = {
    "Authorization" : "Bearer ht4b6M6jOYJO5hIEIxQB" 
}

sda = requests.get("https://the-one-api.dev/v2/book", headers=headers)
sda = sda.json()

json_str =json.dumps(sda)
with open("sdabook.json", "w") as arquivo: arquivo.write(json_str)

