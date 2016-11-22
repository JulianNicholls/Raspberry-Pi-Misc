#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import time

DEFAULT_KEY = [0xff, 0xff, 0xff, 0xff, 0xff, 0xff]
NEW_KEY_A   = [0x42, 0x65, 0x78, 0x34, 0x34, 0xff]
NEW_KEY_B   = [0x53, 0x65, 0x65, 0x64, 0xff, 0xff]
SECURITY    = [0xff, 0x07, 0x80, 0x69]
NEW_DATA    = NEW_KEY_A + SECURITY + NEW_KEY_B

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

    print "\nAuthenticating with default key..."

    status = reader.MFRC522_Auth(reader.PICC_AUTHENT1A, 59, DEFAULT_KEY, uid)

    if status == reader.MI_OK:
        print NEW_DATA
        reader.MFRC522_Read(59, True)
        reader.MFRC522_Write(59, NEW_DATA)
        reader.MFRC522_Read(59, True)

        reader.MFRC522_StopCrypto1()
    else:
        print "Authentication with default key failed for block 59"
        print "\nAuthenticating with new key A..."
        status = reader.MFRC522_Auth(reader.PICC_AUTHENT1A, 59, NEW_KEY_A, uid)
        if status == reader.MI_OK:
            reader.MFRC522_Read(59, True)
            reader.MFRC22_StopCrypto1()
        else:
            print "Authentication failed with new key A"

        print "\nAuthenticating with new key B..."
        status = reader.MFRC522_Auth(reader.PICC_AUTHENT1B, 59, NEW_KEY_B, uid)
        if status == reader.MI_OK:
            reader.MFRC522_Read(59, True)
            reader.MFRC22_StopCrypto1()
        else:
            print "Authentication failed with new key B"

        print "\nAuthenticating 57 with new key A..."
        status = reader.MFRC522_Auth(reader.PICC_AUTHENT1A, 57, NEW_KEY_A, uid)
        if status == reader.MI_OK:
            reader.MFRC522_Read(57, True)
            reader.MFRC22_StopCrypto1()
        else:
            print "Authentication failed with new key A"

else:
    print "Anti-Collision failed"

GPIO.cleanup()

