import RPi.GPIO as GPIO
import time

motor_pin   = 12    # Pin Number, GPIO 18
delay       = 0.2   # second

# Set up pin for output

GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor_pin, GPIO.OUT)

def motor_on():
    GPIO.output(motor_pin, GPIO.HIGH)

def motor_off():
    GPIO.output(motor_pin, GPIO.LOW)

try:
    while True:
        motor_on()
        raw_input("ON: ")
        motor_off()
        raw_input("Off: ")

except:
    pass

GPIO.cleanup()

