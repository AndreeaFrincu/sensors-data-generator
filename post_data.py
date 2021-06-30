import urllib

import generator
import requests
import json

def post_sensor_data():
    payload = generator.gen_sensor_metric()
    # print(payload)
    dump = json.dumps(payload)
    data = json.loads(dump)
    requests.post(url="http://192.168.0.102:8080/api/metrics", json=data)