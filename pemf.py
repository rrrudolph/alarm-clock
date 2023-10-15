from pinmap import LED, SIGNAL
from utime import time, sleep_ms

DUTY_CYCLE = 0.15   #  0.15 = 15%

SIGNAL(0)

class PEMF:

    def on(frequency, hours=0, minutes=0):
        total_seconds = round((hours * 60 + minutes) * 60)
        print('total_seconds', total_seconds)

        hz_freq = 1000 / frequency
        ms_on_time = int(DUTY_CYCLE * hz_freq)
        ms_off_time = int((1 - DUTY_CYCLE) * hz_freq)

        print('playing freq', frequency)

        end = time() + total_seconds
        while time() < end:
            SIGNAL(1)
            sleep_ms(ms_on_time)
            SIGNAL(0)
            sleep_ms(ms_off_time)

    def off():
        SIGNAL(0)

