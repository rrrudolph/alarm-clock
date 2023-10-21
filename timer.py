import urequests

# I only need to make a network call once to get the current time. after that I can
# just count seconds

# correction, I don't need any network call. I'll just use the onboard time.

class Time():
    def __init__(self):
        for _ in range(5):
            try:
                r = urequests.get("http://worldtimeapi.org/api/timezone/America/Chicago")
                break
            except:
                pass
        dt = r.json()
        
        date = dt['datetime'].split('T')[0]
        time = dt['datetime'].split('T')[1]
        
        self.year = int(date.split('-')[0])
        self.month = int(date.split('-')[1])
        self.day = int(date.split('-')[2])
        self.day_of_year = dt['day_of_year']
        self.weekday = dt['day_of_week']  # saturday == 6
        self.hour = int(time.split(':')[0]) # 24 hour clock
        self.minute = int(time.split(':')[1])
        self.second = int(time.split(':')[2].split('.')[0])
        self.epoch = dt['unixtime']
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

        self.alarm = self.time + seconds_diff
        self.set_events()
    
    def set_events(self):
        hours = 60 * 60
        minutes = 60
        self.pemf_sleep = self.alarm - (4 * hours)
        self.pemf_awake = self.alarm - (27 * minutes)
        self.light_on = self.alarm - (3 * minutes)

    # def __gt__(self, other):
    #     if (
    #         self.day_of_year >= other.day_of_year and
    #         self.hour >= other.hour and
    #         self.minute >= other.minute
    #     ):
    #         return True
    
    # def __lt__(self, other):
    #     if (
    #         self.day_of_year <= other.day_of_year and
    #         self.hour <= other.hour and
    #         self.minute <= other.minute
    #     ):
    #         return True
    
    # def __sub__(self, other):
    #     """This is kinda just for testing purposes"""
    #     sec0 = self.epoch - other.epoch
    #     days = sec0 // 3600 * 24
    #     sec1 = sec0 % 3600 * 24
    #     hours = sec1 // 3600
    #     sec2 = sec1 % 3600
    #     minutes = sec2 // 60
    #     sec3 = sec2 % 60
    #     seconds = sec3
    #     return {
    #         'days': days, 'hours': hours, 'minutes': minutes, 'seconds': seconds
    #     }
    
    def __repr__(self):
        return f'Time({self.year}/{self.month}/{self.day}, {self.day_of_year}, {self.weekday}, {self.hour}:{self.minute}:{self.second})\nepoch:{self.epoch}, alarm:{self.alarm}'
        return f'Time({self.year}/{self.month}/{self.day}, {self.day_of_year}, {self.weekday}, {self.hour}:{self.minute}:{self.second})'

    # def copy(self, hour_delta=0, minute_delta=0):
    #     epoch = hour_delta * 3600 + minute_delta * 60
    #     copy = Time()
    #     copy.year = self.year 
    #     copy.month = self.month
    #     copy.day = self.day
    #     copy.day_of_year = self.day_of_year
    #     copy.weekday = self.weekday
    #     copy.hour = self.hour + hour_delta
    #     copy.minute = self.minute + minute_delta
    #     copy.second = self.second 
    #     copy.epoch = self.epoch + epoch

    #     return copy


