import urequests

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
        self.weekday = dt['day_of_week']
        self.hour = int(time.split(':')[0])
        self.minute = int(time.split(':')[1])
        self.second = int(time.split(':')[2].split('.')[0])
        self.epoch = dt['unixtime']
    
    def __gt__(self, other):
        if (
            self.day_of_year >= other.day_of_year and
            self.hour >= other.hour and
            self.minute >= other.minute
        ):
            return True
    
    def __lt__(self, other):
        if (
            self.day_of_year <= other.day_of_year and
            self.hour <= other.hour and
            self.minute <= other.minute
        ):
            return True
    
    def __sub__(self, other):
        """This is kinda just for testing purposes"""
        sec0 = self.epoch - other.epoch
        days = sec0 // 3600 * 24
        sec1 = sec0 % 3600 * 24
        hours = sec1 // 3600
        sec2 = sec1 % 3600
        minutes = sec2 // 60
        sec3 = sec2 % 60
        seconds = sec3
        return {
            'days': days, 'hours': hours, 'minutes': minutes, 'seconds': seconds
        }
    
    def __repr__(self):
        return f'Time({self.year}/{self.month}/{self.day}, {self.day_of_year}, {self.weekday}, {self.hour}:{self.minute}:{self.second})'

    def copy(self, hour_delta=0, minute_delta=0):
        epoch = hour_delta * 3600 + minute_delta * 60
        copy = Time()
        copy.year = self.year 
        copy.month = self.month
        copy.day = self.day
        copy.day_of_year = self.day_of_year
        copy.weekday = self.weekday
        copy.hour = self.hour + hour_delta
        copy.minute = self.minute + minute_delta
        copy.second = self.second 
        copy.epoch = self.epoch + epoch

        return copy
