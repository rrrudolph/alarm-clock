from pinmap import LIGHT
from utime import sleep

min_brightness = 0
max_brightness = 80
first_quarter = max_brightness * 0.25

class Light:
    def on(minutes=0):
        # most of the visible change in brightness happens very quickly so
        # extend out the first 1/4 of the range over 3/4 of the duration
        phase1 = 60 * minutes * 0.75
        phase2 = 60 * minutes * 0.25
        p1_time_per_step = (first_quarter - min_brightness) / phase1
        p2_time_per_step = (max_brightness - first_quarter) / phase2
        print('lights on')
        for i in range(min_brightness, first_quarter):
            LIGHT.duty(i) # duty for D1 mini, duty_u16 for pico
            sleep(p1_time_per_step)
        for i in range(first_quarter, max_brightness):
            LIGHT.duty(i) # duty for D1 mini, duty_u16 for pico
            sleep(p2_time_per_step)

    def off():
        LIGHT.duty(0)
