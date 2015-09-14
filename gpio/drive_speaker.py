import RPi.GPIO as GPIO
import time

speaker     = 12    # Pin Number, GPIO 18
delay       = 0.001

# Set up pin for output

GPIO.setmode(GPIO.BOARD)
GPIO.setup(speaker, GPIO.OUT)

def led_on(pin, delay = 0):
    GPIO.output(pin, GPIO.HIGH)
    if delay > 0:
        time.sleep(delay)

def led_off(pin, delay = 0):
    GPIO.output(pin, GPIO.LOW)
    if delay > 0:
        time.sleep(delay)

def drive_speaker(pin, delay):
    led_on(pin, delay)
    led_off(pin, delay)

for i in range(1000):
    drive_speaker(speaker, delay)

GPIO.cleanup()

