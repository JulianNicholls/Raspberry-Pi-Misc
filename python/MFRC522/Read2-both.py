#!/usr/bin/env python
# -*- coding: utf8 -*-

import time
import RPi.GPIO as GPIO
import MFRC522
import MFRC522sec
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

def status_str(status):
    global inner

    if status == inner.MI_OK:
        return "MI_OK"
    elif status == inner.MI_NOTAGERR:
        return "MI_NOTAGERROR"
    elif status == inner.MI_ERR:
        return "MI_ERR"
    
    return hex(status)

# Create an object of the class MFRC522
outer = MFRC522.MFRC522()
inner = MFRC522sec.MFRC522Sec()

# Welcome message
print "Read RFID Card."
print "Press Ctrl-C to stop."

setup()

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    led_on(blue_pin)
    # Scan for cards    
#    GPIO.output(22, 1)
#    GPIO.output(18, 0)
    outer.MFRC522_Init()
    (ostatus, oTagType) = outer.MFRC522_Request(inner.PICC_REQIDL)

    time.sleep(0.5)
#    GPIO.output(18, 1)
#    GPIO.output(22, 0)
    inner.MFRC522_Init()
    (istatus, iTagType) = inner.MFRC522_Request(inner.PICC_REQIDL)

    # If a card is found
    if ostatus == inner.MI_OK or istatus == inner.MI_OK:
        print
        print "Card detected - Outer: ", status_str(ostatus), ", Inner: ", status_str(istatus) 
        led_off(blue_pin)
    
        # Get the UID of the card
        if ostatus == inner.MI_OK:
            print "at Outer door"
            (status, uid) = outer.MFRC522_Anticoll()
        elif istatus == inner.MI_OK:
            print "at Inner door"
            (status, uid) = inner.MFRC522_Anticoll()
        else:
            print "Neither status is MI_OK"

        print "Anticoll Status: ", status_str(status)
        uid_value = to_int(uid)

    # If we have the UID, continue
#    if status == outer.MI_OK:
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
#        outer.MFRC522_SelectTag(uid)

        # Authenticate
#        status = outer.MFRC522_Auth(outer.PICC_AUTHENT1A, 8, key, uid)

        # Check if authenticated
#        if status == outer.MI_OK:
#            outer.MFRC522_Read(8)
#            outer.MFRC522_StopCrypto1()
#        else:
#            print "Authentication error"

#        time.sleep(1)
