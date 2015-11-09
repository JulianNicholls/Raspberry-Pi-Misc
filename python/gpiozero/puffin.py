#!/usr/bin/env python3

from gpiozero import LED, Button
import time

# Set up pins for output

red_pin	    = LED(17)
amber_pin   = LED(27)
green_pin   = LED(22)

walker_stop = LED(5)
walker_go   = LED(6)

walker_wait = LED(12)

# Set up pedestrian request button for input

button      = Button(21)

def check_button(seconds = 5):
    for i in range(4 * seconds):
        if button.is_pressed:
            walker_wait.on()    # Show that button was pressed
            time.sleep(1)
            return True

        time.sleep(0.25)

    return False

# Cars to stop on Red, pedestrians to go, with the wait light out.
def stop():
    amber_pin.off()
    red_pin.on()

    walker_wait.off()
    walker_stop.off()
    walker_go.on()

# Turn out the pedestrian go light, so they shouldn't start to cross
def walker_dont_start():
    walker_go.off()
    
# Turn on the Amber to signify that Green is coming, tell pedestrians to stop
def ready():
    walker_stop.on()
    amber_pin.on()
    time.sleep(1)
    
# Cars go with Green, pedestrian stop light already on.
def go():
    red_pin.off()
    amber_pin.off()
    green_pin.on()
    
# Tell cars that Red is next
def prepare_to_stop():
    green_pin.off()
    amber_pin.on()
    time.sleep(1)
    
while True:
    stop()

    if check_button(3):
        break

    walker_dont_start()
    time.sleep(2)

    ready()

    go()
    check_button()
    
    prepare_to_stop()

