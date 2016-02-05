#!/usr/bin/env python3

# code modified, tweaked and tailored from code by bertwert 
# on RPi forum thread topic 91796

import RPi.GPIO as GPIO
import time

# GPIO ports for the 7seg pins
# 7seg_segment_pins (11, 7, 4, 2, 1, 10, 5, 3) +  resistor inline

segments = (11, 4, 23, 8, 7, 10, 18, 25)

# GPIO ports for the digit 0-3 pins 
# 7seg_digit_pins (12, 9, 8, 6) digits 0-3 respectively

digits = (22, 27, 17, 24)

# These are actually reversed for a common anode quad 7 segment display

num = {
    ' ': (0, 0, 0, 0, 0, 0, 0), 
    '0': (1, 1, 1, 1, 1, 1, 0), 
    '1': (0, 1, 1, 0, 0, 0, 0), 
    '2': (1, 1, 0, 1, 1, 0, 1), 
    '3': (1, 1, 1, 1, 0, 0, 1), 
    '4': (0, 1, 1, 0, 0, 1, 1), 
    '5': (1, 0, 1, 1, 0, 1, 1), 
    '6': (1, 0, 1, 1, 1, 1, 1), 
    '7': (1, 1, 1, 0, 0, 0, 0), 
    '8': (1, 1, 1, 1, 1, 1, 1), 
    '9': (1, 1, 1, 1, 0, 1, 1)
}
 
# Initialise the GPIO ports

GPIO.setmode(GPIO.BCM)

for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 1)

for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 0)
 
try:
    while True:
        _time = time.ctime()
        n = _time[11:13] + _time[14:16]
        s = str(n).rjust(4)

        for digit in range(4):
            if(int(time.ctime()[18:19]) % 2 == 0) and (digit == 1):
                GPIO.output(25, 0)
            else:
                GPIO.output(25, 1)

            for loop in range(7):
                GPIO.output(segments[loop], 1 - num[s[digit]][loop])

            GPIO.output(digits[digit], 1)
            time.sleep(0.001)
            GPIO.output(digits[digit], 0)

finally:
    GPIO.cleanup()

