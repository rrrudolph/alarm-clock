from machine import Pin, Signal, PWM

class Pinmap:
    D0 = Pin(16, Pin.OUT)
    D1 = Pin(5, Pin.OUT)
    D2 = Pin(4, Pin.OUT)
    D3 = Pin(0, Pin.OUT)
    D4 = Pin(2, Pin.OUT)
    D5 = Pin(14, Pin.OUT)
    D6 = Pin(12, Pin.OUT)
    D7 = Pin(13, Pin.OUT)
    D8 = Pin(15, Pin.OUT)

# LED = Signal(Pinmap.D4, invert=True)
SIGNAL = Pinmap.D4
LIGHT = PWM(Pinmap.D3)
