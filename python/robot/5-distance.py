#!/usr/bin/env python3

# Test the ultrasonic distance sensor

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pinTrig = 17
pinEcho = 18

print("Ultrasonic Measurement")

GPIO.setup(pinTrig, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)

try:
    while True:
        GPIO.output(pinTrig, False)

        time.sleep(0.01)
        
        # send 10uS pulse to trigger (Not a hope!)
        GPIO.output(pinTrig, True)
        time.sleep(0.00001)
        GPIO.output(pinTrig, False)

        startTime = time.time()

        # The start time starts when the echo goes high
        while GPIO.input(pinEcho) == 0:
            startTime = time.time()

        # Time until the pin goes low
        while GPIO.input(pinEcho) == 1:
            stopTime = time.time()

            if stopTime - startTime >= 0.04:
                print("Too close")
                stopTime = startTime
                break

        elapsed = stopTime - startTime

        # Distance travelled = time * speed of sound in cms-1

        distance = elapsed * 17163      # There and back = 34326

        print("Distance: %.1f" % distance)

        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()

