import RPi.GPIO as GPIO
import time

red_pin     = 12    # Pin Number, GPIO 18
orange_pin  = 26    # Pin Number, GPIO 7
delay       = 0.5   # second

# Set up pin for output

GPIO.setmode(GPIO.BOARD)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(orange_pin, GPIO.OUT)

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

led_on(orange_pin)
flash_led(red_pin, delay)
flash_led(red_pin, delay)

GPIO.cleanup()

