#!/usr/bin/env python3

from RTk import GPIO
from time import sleep
 
GREEN_LED   = 5
RED_LED     = 6
BLUE_LED    = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(BLUE_LED, GPIO.OUT)
 
while True:
    GPIO.output(GREEN_LED, 0)
    GPIO.output(RED_LED, 0)
    GPIO.output(BLUE_LED, 0)
    sleep(0.5)

    GPIO.output(GREEN_LED, 1)
    sleep(0.5)

    GPIO.output(GREEN_LED, 0)
    GPIO.output(RED_LED, 1)
    sleep(0.5)

    GPIO.output(RED_LED, 0)
    GPIO.output(BLUE_LED, 1)
    sleep(0.5)

