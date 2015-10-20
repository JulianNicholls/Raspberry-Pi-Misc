#!/usr/bin/env python3

from gpiozero import LED, Button
import time

red_pin     = 17
amber_pin   = 27
green_pin   = 22

# Set up pins for output


red_pin	    = LED(17)
amber_pin   = LED(27)
green_pin   = LED(22)

walker_stop = LED(5)
walker_go   = LED(6)

button      = Button(21)

def check_button(seconds = 5):
    for i in range(2 * seconds):
        if button.is_pressed:
            return True

        time.sleep(0.5)

    return False

def stop():
    red_pin.on()
    amber_pin.off()
    green_pin.off()
    walker_stop.off()
    walker_go.on()
    
def ready():
    walker_go.off()
    walker_stop.on()
    amber_pin.on()
    time.sleep(0.75)
    
def go():
    red_pin.off()
    amber_pin.off()
    green_pin.on()
    
def prepare_to_stop():
    green_pin.off()
    amber_pin.on()
    time.sleep(0.75)
    
while True:
    stop()

    if check_button():
        break

    ready()

    go()
    check_button()
    
    prepare_to_stop()

