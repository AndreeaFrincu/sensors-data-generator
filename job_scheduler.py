import schedule
import post_data
import os

def postData(endpoint, location, collector):
    post_data.post_sensor_data(endpoint, location, collector)

schedule.every(5).seconds.do(postData, os.environ['ENDPOINT'], os.environ['LOCATION'], os.environ['COLLECTOR'])

while True:
    schedule.run_pending()