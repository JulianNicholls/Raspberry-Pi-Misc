#!/usr/bin/env python3

from gpiozero import PWMLED, Button
import time
import random

led = PWMLED(18)   # GPIO Number

# Currently, there's a bug in gpiozero which causes a problem with setting up
# the event detection for a button.

button = None

while not button:
    try:
        button = Button(21, bounce_time=0.5)
    except RuntimeError:
        pass

def fade_in_out():
    for i in range(3):
        fade_in()
        fade_out()

def fade_in():
    led.off()
    for i in range(20):
        led.value = i / 20
        time.sleep(0.1)

def fade_out():
    led.on()
    for i in range(20):
        led.value = (19 - i) / 20
        time.sleep(0.1)

def flash():
    led.blink(on_time=0.3, off_time=0.3, n=10, background=False)

def fast_flash():
    led.blink(on_time=0.15, off_time=0.15, n=20, background=False)

while True:
    if button.is_pressed:
        exit()

    which = random.randrange(5)

    if which == 0:
        fade_in_out()
    elif which == 1:
        fade_in()
        fade_out()
    elif which == 2:
        fade_out()
        fade_in()
    elif which == 3:
        flash()
    elif which == 4:
        fast_flash()

