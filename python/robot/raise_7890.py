# CamJam EduKit 3 - Robotics
# Worksheet 2 - Motor Test Code

import RPi.GPIO as GPIO # Import the GPIO Library
import time             # Import the Time library

# Set the GPIO modes

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set the GPIO Pin mode

GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

# Turn all pins on

GPIO.output(7, 0)
GPIO.output(8, 1)
GPIO.output(9, 0)
GPIO.output(10, 1)

time.sleep(120)

# Reset the GPIO pins (turns off motors too)

GPIO.cleanup()

