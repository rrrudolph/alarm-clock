import socket
import urandom
from html import html, html_confirm
from timer import Time
from pemf import PEMF
from lights import Light
from utime import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

def random_decimal():
    x = urandom.getrandbits(7)
    while x > 1:
        x /= 10
    
    return x

message = None
while True:
    if message:
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(html_confirm)
        conn.close()
        break
    
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    try:
        message = str(request).split('?message=')[1].split(' ')[0]

    except:  
        response = html
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()

alarm = Time()
alarm.set_alarm(message)
print(alarm)

sleep_frequency = 2 + random_decimal()
wakeup_frequency = 15 + random_decimal()

while True:
    if time() > alarm.pemf_sleep:
        print('starting pemf sleep')
        PEMF.on(sleep_frequency, hours=3.5)
        PEMF.on(wakeup_frequency, minutes=27)
        Light.on(minutes=3)
        break
        
PEMF.off()
Light.off()
