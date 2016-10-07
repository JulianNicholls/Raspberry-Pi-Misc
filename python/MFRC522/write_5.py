#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import time

DEFAULT_KEY = [0xff, 0xff, 0xff, 0xff, 0xff, 0xff]
NEW_DATA    = [0x42, 0x65, 0x78, 0x34, 0x34, 0, 0x53, 0x65, 0x65, 0x64, 0x68, 0x75, 0x62, 0, 0, 0] 

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading

    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
reader = MFRC522.MFRC522()

looking = True

print "Scan your card"

while looking:
# Scan for cards    
    (status, TagType) = reader.MFRC522_Request(reader.PICC_REQIDL)

    # If a card is found
    if status == reader.MI_OK:
        print "Card detected"
        looking = False

(status, uid) = reader.MFRC522_Anticoll()

if status == reader.MI_OK:
    print "Card UID:",

    for i in range(4):
        print format(uid[i], '02x'),

    reader.MFRC522_SelectTag(uid)

    print "\nAuthenticating..."

    status = reader.MFRC522_Auth(reader.PICC_AUTHENT1A, 5, DEFAULT_KEY, uid)

    if status == reader.MI_OK:
        reader.MFRC522_Read(5, True)
        reader.MFRC522_Write(5, NEW_DATA)
        reader.MFRC522_Read(5, True)

        reader.MFRC522_StopCrypto1()
    else:
        print "Authentication failed for block 5"
else:
    print "Anti-Collision failed"

GPIO.cleanup()

