#!/usr/bin/env python3

from gpiozero import RGBLED
from time import sleep

led = RGBLED(18, 23, 24) 

colours = [
    (1, 0, 0), (0, 1, 0), (0, 0, 1),
    (1, 1, 0), (1, 0, 1), (0, 1, 1)
]

led.on()
sleep(1)

for rgb in colours:
    led.color = rgb
    sleep(1)

red = 0.5
dred = -0.1

blue = 0.5
dblue = 0.1

green = 0
dgreen = 0.1

for i in range(300):
    led.color = (red, green, blue)
    sleep(0.02)

    if i % 3 == 0:
        red += dred
        if red > 1:
            red = 1
            dred = -dred
        elif red < 0:
            red = 0
            dred = -dred

    if i % 3 == 1:
        green += dgreen
        if green > 1:
            green = 1
            dgreen = -dgreen
        elif green < 0:
            green = 0
            dgreen = -dgreen
    else:
        blue += dblue
        if blue > 1:
            blue = 1
            dblue = -dblue
        elif blue < 0:
            blue = 0
            dblue = -dblue

# fade out

while red > 0 or green > 0 or blue > 0:
    led.color=(max(red, 0), max(green, 0), max(blue, 0))

    red -= 0.05
    green -= 0.05
    blue -= 0.05

    sleep(0.02)


led.off()

