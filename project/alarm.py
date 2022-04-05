import datetime
import time
from threading import Thread


class Alarm:
    def __init__(self, time_to_alarm, light_sensor, led):
        self.light_sensor = light_sensor
        self.led = led
        self.time_to_alarm = time_to_alarm
        self.hour_to_alarm = time_to_alarm[:2]
        self.minute_to_alarm = time_to_alarm[3:]
        self.was_alarm = False

    def start(self):
        while not self.was_alarm:
            time_now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3))).time()
            hours, minutes = time_now.hour, time_now.minute
            if str(hours) == self.hour_to_alarm and str(minutes) == self.minute_to_alarm:
                self.alarm()
                self.was_alarm = False
                print("Alarm")
            time.sleep(1)

    def start_alarm(self):
        new_thread = Thread(target=self.start)
        new_thread.start()

        if self.was_alarm:
            new_thread.join()

    def alarm(self):
        if self.light_sensor.is_dark():
            self.led.on()