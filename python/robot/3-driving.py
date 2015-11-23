#!/usr/bin/env python3

# CamJam EduKit 3 -Robotics
# Worksheet 3–Driving and Turning

import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library

# Set the GPIO modes

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins

pinMotorAForwards = 7
pinMotorABackwards= 8
pinMotorBBackwards= 9
pinMotorBForwards =10

# Set the GPIO Pin mode

GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

# Turn all motors off

def StopMotors():
    GPIO.output(pinMotorAForwards,0)
    GPIO.output(pinMotorABackwards,0)
    GPIO.output(pinMotorBForwards,0)
    GPIO.output(pinMotorBBackwards,0)
    
# Turn both motors forwards

def Forwards():
    GPIO.output(pinMotorAForwards,1)
    GPIO.output(pinMotorABackwards,0)
    GPIO.output(pinMotorBForwards,1)
    GPIO.output(pinMotorBBackwards,0)
   
# Turn both motors backwards

def Backwards():
    GPIO.output(pinMotorAForwards,0)
    GPIO.output(pinMotorABackwards,1)
    GPIO.output(pinMotorBForwards,0)
    GPIO.output(pinMotorBBackwards,1)
    
# Turn Right

def TurnRight():
    GPIO.output(pinMotorAForwards,1)
    GPIO.output(pinMotorABackwards,0)
    GPIO.output(pinMotorBForwards,0)
    GPIO.output(pinMotorBBackwards,1)
    
# Turn Left

def TurnLeft():
    GPIO.output(pinMotorAForwards,0)
    GPIO.output(pinMotorABackwards,1)
    GPIO.output(pinMotorBForwards,1)
    GPIO.output(pinMotorBBackwards,0)
    
Forwards()
time.sleep(1)

StopMotors()
time.sleep(1)

TurnRight()
time.sleep(1)

TurnLeft()
time.sleep(1)

StopMotors()

GPIO.cleanup()

