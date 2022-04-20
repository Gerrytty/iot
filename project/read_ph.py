import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.OUT)
GPIO.output(2, 0)

GPIO.setup(2, GPIO.IN)
import time

while True:
    for i in range(0,5):
        print(GPIO.input(2))
        time.sleep(1)