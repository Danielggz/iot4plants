from sense_hat import SenseHat
from time import sleep
from random import randint
sense = SenseHat()

#clear display
sense.clear()


humidity = sense.get_humidity()
#print(humidity)

print(f"Current humidity: {humidity:.1f}%")