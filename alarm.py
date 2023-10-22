import urequests
from time import time

# I only need to make a network call once to get the current time. after that I can
# just count seconds

# correction, I don't need any network call. I'll just use the onboard time.

class Alarm():
    def __init__(self):
        for _ in range(5):
            try:
                r = urequests.get("http://worldtimeapi.org/api/timezone/America/Chicago")
                break
            except:
                pass
        dt = r.json()
        
        date = dt['datetime'].split('T')[0]
        ttime = dt['datetime'].split('T')[1]
        
        self.year = int(date.split('-')[0])
        self.month = int(date.split('-')[1])
        self.day = int(date.split('-')[2])
        self.day_of_year = dt['day_of_year']
        self.weekday = dt['day_of_week']  # saturday == 6
        self.hour = int(ttime.split(':')[0]) # 24 hour clock
        self.minute = int(ttime.split(':')[1])
        self.second = int(ttime.split(':')[2].split('.')[0])
        self.epoch = dt['unixtime']
        self.onboard_time = time()
        self.alarm = 0
        self.pemf_sleep = 0
        self.pemf_wake = 0
        self.light_on = 0
    
    def set_alarm(self, alarm):
        """Will get passed in the string from the html form. Could be either a single
        number representing an hour or 3 numbers represting hour:minutes"""

        # for testing purposes I need to allow 4 digits to match the 24hr clock
        alarm_hour = int(alarm[0]) if len(alarm) < 4 else int(alarm[:2])
        alarm_minutes = int(alarm[-2:]) if len(alarm) > 1 else 0

        # find how many hours exist between current time and the alarm
        hours_diff = 0
        hour = self.hour
        while True:
            if hour == alarm_hour:
                break
            hour += 1
            hours_diff += 1
            hour = 0 if hour > 23 else hour
        print('hours_diff', hours_diff)

        # find how many minutes (If I set the alarm at 8:45 for 5:30 thats 45 minutes)
        minutes_diff = 0
        minute = self.minute
        while True:
            if minute == alarm_minutes:
                break
            minute += 1
            minutes_diff += 1
            minute = 0 if minute > 59 else minute
        print('minutes_diff', minutes_diff)

        seconds_diff = (hours_diff * 60 * 60) + minutes_diff * 60

        self.alarm = self.onboard_time + seconds_diff

        # set events
        hours = 60 * 60
        minutes = 60
        self.pemf_sleep = self.alarm - (4 * hours)
        self.pemf_awake = self.alarm - (27 * minutes)
        self.light_on = self.alarm - (3 * minutes)

    
    def __repr__(self):
        return f'Time({self.year}/{self.month}/{self.day}, {self.day_of_year}, {self.weekday}, {self.hour}:{self.minute}:{self.second})\ntime:{self.onboard_time}, alarm:{self.alarm}'
        return f'Time({self.year}/{self.month}/{self.day}, {self.day_of_year}, {self.weekday}, {self.hour}:{self.minute}:{self.second})'

