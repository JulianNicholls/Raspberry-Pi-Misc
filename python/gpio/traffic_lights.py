import RPi.GPIO as GPIO
import time

red_pin     = 11    # Pin Number, GPIO 17
amber_pin   = 13    # Pin Number, GPIO 27
green_pin   = 15    # Pin Number, GPIO 22

# Set up pins for output

GPIO.setmode(GPIO.BOARD)

GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(amber_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)

def led_on(pin, delay = 0):
    GPIO.output(pin, GPIO.HIGH)
    if delay > 0:
        time.sleep(delay)

def led_off(pin, delay = 0):
    GPIO.output(pin, GPIO.LOW)
    if delay > 0:
        time.sleep(delay)

def stop():
    led_on(red_pin)
    led_off(amber_pin)
    led_off(green_pin)
    time.sleep(2)
    
def ready():
    led_on(amber_pin)
    time.sleep(0.75)
    
def go():
    led_off(red_pin)
    led_off(amber_pin)
    led_on(green_pin)
    time.sleep(2)
    
def prepare_to_stop():
    led_off(green_pin)
    led_on(amber_pin)
    time.sleep(0.75)
    
stop()
ready()
go()
prepare_to_stop()
stop()

raw_input("Press Enter ")

GPIO.cleanup()

