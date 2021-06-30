import schedule
import post_data

def postData():
    post_data.post_sensor_data()

schedule.every(5).seconds.do(postData)

while True:
	schedule.run_pending()