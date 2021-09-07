import os
import json

import requests

API_URL = "https://api.voteptp.insidethesandbox.studio/responses"

def get_json():
    path = os.path.join(".", "data", "vote.json")
    response = requests.get(API_URL)
    json_data = response.json()
    with open(path, 'w') as json_file:
        json.dump(json_data, json_file, indent = 4)

if __name__=="__main__":
    get_json()