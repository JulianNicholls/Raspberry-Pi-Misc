#!/usr/bin/env python
# -*- coding: utf8 -*-

import time
import RPi.GPIO as GPIO
import MFRC522
import signal

continue_reading = True

authorised  = (584186717269, 1040656224665)

blue_pin    = 36
green_pin   = 38
red_pin     = 40

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Convert a list of ints to one value
def to_int(uid):
    value = 0

    for i in range(len(uid)):
        value = value * 256 + uid[i]

    return value

def setup():
    # Hook the SIGINT
    signal.signal(signal.SIGINT, end_read)

    GPIO.setup(blue_pin, GPIO.OUT)
    GPIO.setup(red_pin, GPIO.OUT)
    GPIO.setup(green_pin, GPIO.OUT)

def led_on(pin, delay = 0):
    GPIO.output(pin, GPIO.HIGH)
    if delay > 0:
        time.sleep(delay)

def led_off(pin, delay = 0):
    GPIO.output(pin, GPIO.LOW)
    if delay > 0:
        time.sleep(delay)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print "Read RFID Card."
print "Press Ctrl-C to stop."

setup()

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    led_on(blue_pin)
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print
        print "Card detected"
        led_off(blue_pin)
    
    # Get the UID of the card
    (status, uid) = MIFAREReader.MFRC522_Anticoll()

    uid_value = to_int(uid)

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:
        # Print UID
#        print "Card read UID: ", uid
#        print "Card read UID: " + str(uid[0]) + ", " + str(uid[1]) + ", " + str(uid[2]) + ", " + str(uid[3]) + ", " + str(uid[4])
#        print "Card read UID: ", uid_value
        print "Card read UID: ", hex(uid_value)
    
        if uid_value in authorised:
            print('Come on in')
            led_on(green_pin, 2)
            led_off(green_pin)
        else:
            print('Go away!')
            led_on(red_pin, 2)
            led_off(red_pin)

        # This is the default key for authentication
#        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
        
        # Select the scanned tag
#        MIFAREReader.MFRC522_SelectTag(uid)

        # Authenticate
#        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

        # Check if authenticated
#        if status == MIFAREReader.MI_OK:
#            MIFAREReader.MFRC522_Read(8)
#            MIFAREReader.MFRC522_StopCrypto1()
#        else:
#            print "Authentication error"

#        time.sleep(1)
