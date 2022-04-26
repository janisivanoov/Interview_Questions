import requests
import json

from requests.models import Response

print("search for: ")
search = input()

parameters = {
    "name": search
}

response = requests.get("https://www.swapi.tech/api/people", params=parameters)

def jprint(obj):
    text = json.dumps(obj, sort_keys = True , indent = 4)
    print(text)

jprint(response.json())

#test
data = response.text
parse = json.loads(data)
active_case = parse['result']
jprint(active_case)