from pinmap import LIGHT
from utime import sleep

min_brightness = 0
max_brightness = 80
quarter_brightness = max_brightness * 0.25

class Light:
    def on(minutes=0):
        # most of the visible change in brightness happens very quickly so
        # extend out the first 1/4 of the range over 3/4 of the duration
        phase1_time = 60 * minutes * 0.75
        phase2_time = 60 * minutes * 0.25
        p1_time_per_step = (quarter_brightness - min_brightness) / phase1_time
        p2_time_per_step = (max_brightness - quarter_brightness) / phase2_time
        print('lights on')
        # Phase 1
        for i in range(min_brightness, quarter_brightness):
            LIGHT.duty(i) # duty for D1 mini, duty_u16 for pico
            sleep(p1_time_per_step)

        # Phase 2
        for i in range(quarter_brightness, max_brightness):
            LIGHT.duty(i) # duty for D1 mini, duty_u16 for pico
            sleep(p2_time_per_step)

    def off():
        LIGHT.duty(0)
