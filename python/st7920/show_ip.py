#!/usr/bin/env python

import socket
from st7920   import ST7920

screen = ST7920()

def get_internal_ip():
    # As an alternative, look into netifaces package - pip install netifaces
    # netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']

    ip = [(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
    return ip

ip = get_internal_ip()

screen.rect(0, 0, 127, 16)
screen.put_text("IP: " + str(ip), 12, 5)
screen.redraw()

