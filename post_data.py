import generator
import requests
import os

def post_sensor_data():
    payload = generator.gen_sensor_metric()
    # print(payload)
    requests.post(url=os.environ['ENDPOINT'], json=payload)