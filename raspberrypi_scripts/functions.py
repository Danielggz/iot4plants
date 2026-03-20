import csv
import os

#get cpu temperature
def get_cpu_temp():
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        return int(f.read()) / 1000.0

#Sunlight estimates for Dublin
SUN_HOURS = {
    "N": 1,
    "NE": 2,
    "E": 3,
    "SE": 5,
    "S": 7,
    "SW": 5,
    "W": 3,
    "NW": 1
}

#get orientation based on yaw data
def yaw_to_direction(yaw):
    dirs = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
    idx = int((yaw + 22.5) // 45) % 8
    return dirs[idx]

#Get estimate based on orientation
def estimate_sunlight_hours(yaw):
    direction = yaw_to_direction(yaw)
    return SUN_HOURS[direction]

#csv writer
def log_to_csv(csv_path, temperature, humidity, pressure, sunlight_hours, timestamp):
    file_exists = os.path.exists(csv_path)

    with open(csv_path, "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["timestamp", "temperature", "humidity", "sunlight_hours", "pressure"])

        writer.writerow([timestamp, temperature, humidity, sunlight_hours, pressure])
