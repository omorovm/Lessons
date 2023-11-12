from datetime import datetime 
class Clock:
    def current_time(self):
        print(datetime.now().strftime('%H:%M:%S'))

class Alarm:
    def on(self):
        print("Будильник включен")

    def off(self):
        print('Будильник выключен')

class AlarmClock(Clock,Alarm):
    def alarm_on(self):
        super().on()

clock = AlarmClock()
clock.current_time() 
clock.alarm_on() 