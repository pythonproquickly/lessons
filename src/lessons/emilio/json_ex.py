import json

import requests

URL = 'https://api.covid19india.org/state_district_wise.json'


def download_json_file(url):
    response_API = requests.get(url)
    print(response_API.status_code)
    data = response_API.text
    parse_json = json.loads(data)
    return parse_json


myjson_data = download_json_file(URL)
