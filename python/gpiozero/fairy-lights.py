#!/usr/bin/env python3

from gpiozero import LED, Button
from signal import pause
import time

led = LED(18)   # GPIO Number
button = Button(21)

while True:
    button.wait_for_press()
    led.on()
    button.wait_for_release()

    button.wait_for_press()
    led.off()
    button.wait_for_release()

