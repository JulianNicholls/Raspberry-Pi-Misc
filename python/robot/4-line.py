#!/usr/bin/env python3

# Line detection

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pinLine = 25

GPIO.setup(pinLine, GPIO.IN)

try:
    while True:
        if GPIO.input(pinLine) == 0:
            print("Black or Nothing")
        else:
            print("White")

        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()

