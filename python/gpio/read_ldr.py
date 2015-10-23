#!/usr/bin/env python3

# Read a Light Dependent Resistor by using the RC charge time.

# --------------+----- +3.3v --------- Pin 1
#               |
#              +-+
#              | |   2.2k series resistor
#              | |
#              +-+
#               |
#              +-+  
#              | |  /
#              | | L      LDR
#              | |
#              +-+
#               |
#               +--------------------- GPIO 18 (Pin 12)
#               |
#              ===      0.1uF cap
#              ===
#               |
#               |
# --------------+----- GND ----------- e.g. Pin 14

# With a 0.1uF capacitor (marked 104), I got the following readings:

#   Indoors, dull afternoon     ~180
#   Pointed at white LED        ~25-60
#   Shaded                      ~10000-20000
#   Really Dark                 ~150000-500000

import RPi.GPIO as gpio
import time

ldr_pin = 18

gpio.setmode(gpio.BCM)

def read_analog(pin):
    counter = 0

    gpio.setup(pin, gpio.OUT)
    gpio.output(pin, gpio.LOW)  # Discharge Cap
    time.sleep(0.1)             # 100ms

    gpio.setup(pin, gpio.IN)

    while(gpio.input(pin) == gpio.LOW):
        counter += 1

    return counter

for i in range(50):
    print(i, ": ", read_analog(ldr_pin))
    time.sleep(0.5)

gpio.cleanup()

