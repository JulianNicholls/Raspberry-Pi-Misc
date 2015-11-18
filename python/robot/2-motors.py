#!/usr/bin/env python3
# CamJam EduKit 3 - Robotics
# Worksheet 2 - Motor Test Code

import RPi.GPIO as GPIO # Import the GPIO Library
import time             # Import the Time library

# Set the GPIO modes

GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)

# Set the GPIO Pin mode

pinLeft1    = 7
pinLeft2    = 8

pinRight1   = 9
pinRight2   = 10

GPIO.setup(pinLeft1, GPIO.OUT)
GPIO.setup(pinLeft2, GPIO.OUT)
GPIO.setup(pinRight1, GPIO.OUT)
GPIO.setup(pinRight2, GPIO.OUT)

# Turn all motors off

GPIO.output(pinLeft1, 0)
GPIO.output(pinLeft2, 0)
GPIO.output(pinRight1, 0)
GPIO.output(pinRight2, 0)

# Turn the right motor forwards

GPIO.output(pinRight1, 1)
GPIO.output(pinRight2, 0)

# Turn the left motor forwards

GPIO.output(pinLeft1, 1)
GPIO.output(pinLeft2, 0)

# Wait for 2 seconds

time.sleep(2)

# Turn all motors off

GPIO.output(pinLeft1, 0)
GPIO.output(pinLeft2, 0)
GPIO.output(pinRight1, 0)
GPIO.output(pinRight2, 0)

# Reset the GPIO pins (turns off motors too)

GPIO.cleanup()

