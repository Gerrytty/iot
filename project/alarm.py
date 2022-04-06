import datetime
import time
from threading import Thread
from time_updater import TimeUpdater


class Alarm:
    def __init__(self, time_to_alarm, light_sensor, led):
        self.light_sensor = light_sensor
        self.led = led
        # self.time_to_alarm = time_to_alarm
        self.hour_to_alarm = time_to_alarm[:2]
        self.minute_to_alarm = time_to_alarm[3:]
        self.was_alarm = False
        self.alarm_time_updater = TimeUpdater("topic_2", ["localhost:9092"])
        self.alarm_time_updater.endless_consume()
        self._time_to_alarm = time_to_alarm

    @property
    def time_to_alarm(self):
        return self._time_to_alarm

    @time_to_alarm.setter
    def time_to_alarm(self, value):
        if value is None:
            self.hour_to_alarm = None
            self.minute_to_alarm = None
        else:
            self.hour_to_alarm = value[:2]
            self.minute_to_alarm = value[3:]
        self._time_to_alarm = value

    @time_to_alarm.getter
    def time_to_alarm(self):
        return self._time_to_alarm

    def start(self):
        while True:
            if self.alarm_time_updater.time_to_alarm is not None:
                self.time_to_alarm = self.alarm_time_updater.time_to_alarm
                self.was_alarm = False
                self.alarm_time_updater.time_to_alarm = None
            if not self.was_alarm:
                time_now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3))).time()
                hours, minutes = time_now.hour, time_now.minute
                if str(hours) == self.hour_to_alarm and str(minutes) == self.minute_to_alarm:
                    self.alarm()
                    self.was_alarm = False
                    self.time_to_alarm = None
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