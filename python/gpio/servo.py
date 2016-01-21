#!/usr/bin/env python3

import RPi.GPIO as GPIO
from time import sleep

up      = 16
down    = 20
sweep   = 21

GPIO.setmode(GPIO.BCM)

GPIO.setup(25, GPIO.OUT)
GPIO.setup(down, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(up, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(sweep, GPIO.IN, pull_up_down=GPIO.PUD_UP)

servo = GPIO.PWM(25, 50)    # Pin 25, 50Hz

dc = 7.5                # Should be mid position

servo.start(dc)

def ssweep(servo, start, end):
    inc = 0.1 if(end > start) else -0.1

    val = start

    while abs(val - end) > 0.05:
        servo.ChangeDutyCycle(val)
        sleep(0.03)
        val += inc

try:
    while True:
        servo.ChangeDutyCycle(dc)

        while GPIO.input(up) and GPIO.input(down) and GPIO.input(sweep):
            pass
    
        if GPIO.input(up) == GPIO.LOW:
            dc += 0.1
            print("Up %4.1f (~%4.2fms)" % (dc, dc / 5.0))
        elif GPIO.input(down) == GPIO.LOW:
            dc -= 0.1
            print("Down %4.1f (~%4.2fms)" % (dc, dc / 5.0))
        elif GPIO.input(sweep) == GPIO.LOW:
            print("Sweep")

            ssweep(servo, dc, 11.4)
            ssweep(servo, 11.4, 2.5)
            ssweep(servo, 2.5, dc)
    
        sleep(0.2)
    
except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()

