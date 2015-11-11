#!/usr/bin/env python3

from gpiozero import RGBLED
from time import sleep

led = RGBLED(18, 23, 24) 

colours = [
    (1, 0, 0),
    (1, 0.55, 0),
    (0.7, 0.7, 0), 
    (0, 1, 0),
    (0, 0.7, 0.7),
    (0, 0, 1),
    (0.7, 0, 0.7)

]

def constrain(low, high, value):
    return max(low, min(high, value))

def fade_out(led, time):
    steps = 20
    delay = time / steps
    delta = max(led.red, led.green, led.blue) / steps

    while led.red > delta or led.green > delta or led.blue > delta:
        if led.red >= delta:
            led.red -= delta

        if led.green >= delta:
            led.green -= delta

        if led.blue >= delta:
            led.blue -= delta
    
        sleep(delay)
    
def fade_to(led, colour, time):
    steps = 20
    delay = time / steps

    dred   = (colour[0] - led.red) / steps
    dgreen = (colour[1] - led.green) / steps
    dblue  = (colour[2] - led.blue) / steps
    
    for i in range(steps):
        led.red   = constrain(0, 1, led.red   + dred)
        led.green = constrain(0, 1, led.green + dgreen)
        led.blue  = constrain(0, 1, led.blue  + dblue)
        
        sleep(delay)

    led.color = colour

led.on()
sleep(1)

for rgb in colours:
    fade_to(led, rgb, 1)
    sleep(1)

fade_out(led, 1)

led.off()

