import generator
import requests
import json

def post_sensor_data(endpoint, location, collector):
    data_to_post = generator.gen_sensor_metric(location, collector)
    dump = json.dumps(data_to_post)
    data = json.loads(dump)
    requests.post(url=endpoint, json=data)