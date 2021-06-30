import random

def gen_sensor_metric():
    locationString = ["smart home", "data center"]
    locationValue = random.choice(locationString)

    collectorValue = "raspberrypi-02"

    # metricTypeString = ["Luminosity", "Temperature", "Humidity", "Air quality"]
    metricTypeString = ["luminosity", "temperature", "humidity"]
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

    payload = {"location": locationValue, "collector": collectorValue, "metricType": metricType, "isSyncronized": "false", "value": str(value)}
    return payload