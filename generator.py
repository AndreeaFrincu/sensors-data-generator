import random
import os

def gen_sensor_metric(location, collector):
    locationValue = location
    collectorValue = collector
    metricTypeString = []

    if locationValue == "smarthome":
        metricTypeString = ["luminosity", "temperature", "humidity"]
    elif locationValue == "datacenter":
        metricTypeString = ["air", "temperature", "humidity"]

    metricType = random.choice(metricTypeString)

    if metricType == "luminosity":
        value = random.randint(150, 500)
    elif metricType == "temperature":
        value = round(random.uniform(15, 40), 1)
    elif metricType == "humidity":
        value = round(random.uniform(30, 50), 1)
    else:
        value = random.randint(250, 2000)

    # print(collectorValue + ' ' + metricType + ' ' + str(value) )

    data_to_post = {"location": locationValue, "collector": collectorValue, "metricType": metricType, "isSyncronized": "false", "value": str(value)}
    return data_to_post