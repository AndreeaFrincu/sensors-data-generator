import urllib

import generator
import requests
import json
import os

def post_sensor_data(endpoint, location, collector):
    payload = generator.gen_sensor_metric(location, collector)
    # print(payload)
    dump = json.dumps(payload)
    data = json.loads(dump)
    requests.post(url=endpoint, json=data)