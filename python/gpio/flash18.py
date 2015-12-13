import RPi.GPIO as GPIO
import time

red_pin     = 18    # Pin Number, GPIO 18
delay       = 0.4   # second

# Set up pin for output

GPIO.setmode(GPIO.BCM)
GPIO.setup(red_pin, GPIO.OUT)

def led_on(pin, delay = 0):
    GPIO.output(pin, GPIO.HIGH)
    if delay > 0:
        time.sleep(delay)

def led_off(pin, delay = 0):
    GPIO.output(pin, GPIO.LOW)
    if delay > 0:
        time.sleep(delay)

def flash_led(pin, delay):
    led_on(pin, delay)
    led_off(pin, delay)

for i in range(6):
    flash_led(red_pin, delay)

led_on(red_pin, delay)
z = input("waiting for exit")

GPIO.cleanup()

