from sense_hat import SenseHat
import requests
import json
import time
from datetime import datetime, timezone
import random

#Get senseHat
sense = SenseHat()

#Time metrics
TIME_INTERVAL = 5
AVG_INTERVAL = 30

#PowerBI push url to connect with report
#PUSH_URL = "Yhttps://api.powerbi.com/beta/6edb49c1-bf72-4eea-8b3f-a7fd0a25b68c/datasets/c8bb2909-769b-423d-8512-777289f7aed0/rows?experience=power-bi&key=2dMXreV%2F4Nlplb2qAcjgl3tAmxzDL4asoxwYu8W%2FwSgXi5%2BuxQILz14%2FMYciF20KrVM6z0J5ABd1o5Vx26Ym1A%3D%3D"

#array to store temperatures
tempArray = []

start_time = time.time()

while True:
    #get cpu temperature
    def get_cpu_temp():
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            return int(f.read()) / 1000.0
    
    humidity = round(sense.get_humidity(), 2)
    pressure = round(sense.get_pressure(), 2)
    #To get a correct reading, deduct pi temperature from sensehat reading  
    temperature = round(sense.get_temperature(), 2)
    cpu_temp = get_cpu_temp()
    
    finalTemp = temperature - ((cpu_temp - temperature) / 1.5)
    tempArray.append(finalTemp)

    data = [{
        "temperature": finalTemp,
        "humidity": humidity,
        "pressure": pressure,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }]

    if time.time() - start_time >= AVG_INTERVAL:
        avg_time = sum(tempArray) / len(tempArray)        
        print("Avg time ", AVG_INTERVAL, " seconds: ", avg_time)

        #Restart to new 30 seconds interval
        start_time = time.time()
        tempArray.clear()

    # response = requests.post(PUSH_URL, json=data)
    #print("Status:", response.status_code, "Sent:", data)
    print(data)
    time.sleep(5)
