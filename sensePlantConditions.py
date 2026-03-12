from sense_hat import SenseHat
import requests
import json
import time
from datetime import datetime, timezone
import random
#CSV manipulation
import csv
import os
#Sun conditions script
from functions import estimate_sunlight_hours, get_cpu_temp
#Get senseHat
sense = SenseHat()
#Time metrics
TIME_INTERVAL = 5
AVG_INTERVAL = 30
#PowerBI push url to connect with report
PUSH_URL = ""
#array to store temperatures
tempArray = []
#timer
start_time = time.time()
#csv storage
csv_file = "./data/conditionsData.csv"

os.makedirs("./data", exist_ok=True)

#Get orientation of the pi
orientation = sense.get_orientation()
yaw = orientation["yaw"]
#Call method to estimate sunlight time for Dublin
sun_hours = estimate_sunlight_hours(yaw)

while True:
    humidity = round(sense.get_humidity(), 2)
    pressure = round(sense.get_pressure(), 2)
    #To get a correct reading, deduct pi temperature from sensehat reading  
    temperature = round(sense.get_temperature(), 2)
    timestamp = datetime.now(timezone.utc).isoformat()
    cpu_temp = get_cpu_temp()
    
    finalTemp = round(temperature - ((cpu_temp - temperature) / 1.5),2)
    tempArray.append(finalTemp)

    data = [{
        "temperature": finalTemp,
        "humidity": humidity,
        "pressure": pressure,
        "sunlight_hours": sun_hours,
        "timestamp": timestamp
    }]

    log_to_csv(csv_file, finalTemp, humidity, pressure, sun_hours, timestamp)

    if time.time() - start_time >= AVG_INTERVAL:
        avg_time = sum(tempArray) / len(tempArray)        
        print("Avg temperature in ", AVG_INTERVAL, " seconds: ", avg_time)

       #Restart to new 30 seconds interval
        start_time = time.time()
        tempArray.clear()

    #response = requests.post(PUSH_URL, json=data)
    #print("Status:", response.status_code, "Sent:", data)
    print(data)
    time.sleep(5)
