import urllib

import generator
import requests
import json
import os

def post_sensor_data():
    payload = generator.gen_sensor_metric()
    # print(payload)
    dump = json.dumps(payload)
    data = json.loads(dump)
    requests.post(url=os.environ['ENDPOINT'], json=data)