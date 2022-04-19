import RPi.GPIO as GPIO
import time
from threading import Thread

class Led(Thread):
    def __init__(self, led, red_pin=16, green_pin=24):
        super().__init__()
        self.led = led
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(red_pin, GPIO.OUT)
        GPIO.setup(green_pin, GPIO.OUT)
        self.red = GPIO.PWM(red_pin, 75)
        self.green = GPIO.PWM(green_pin, 75)

    def on(self):
        self.start()

    def run(self):
        t = 5

        while True:
            print("Brightness = {t} %")
            self.led.value = t
            self.red.start((t))   #start red led
            self.green.start((t)) #start green led
            if t < 100:
                t += 5
            time.sleep(1)

        print("Led on")

    def off(self):
        self.red.stop()
        self.green.stop()
        GPIO.cleanup()
        print("Led off")
        self.join()