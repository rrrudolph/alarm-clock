import esp
esp.osdebug(None)
import network
import utime
from wifi_config import ssid, password
import gc
from pinmap import LED

gc.collect()
for _ in range(5):
    LED.on()
    utime.sleep(0.25)
    LED.off()
    utime.sleep(0.25)

# Connect to network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

for _ in range(10):
    if wlan.isconnected() == False:
        utime.sleep(1)

if wlan.isconnected():
    print('connected')
    print(wlan.ifconfig())
else:
    print('failed to connect')
