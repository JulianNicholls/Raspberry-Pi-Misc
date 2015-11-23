#!/usr/bin/env python3

# CamJam EduKit 3 -Robotics
# Worksheet 3–Driving and Turning

import RPi.GPIO as GPIO # Import the GPIO Library
import time # Import the Time library

# Set the GPIO modes

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins

pinMotorAForwards = 7   # Left Motor
pinMotorABackwards= 8
pinMotorBBackwards= 9   # Right Motor
pinMotorBForwards =10

Frequency = 20
DutyCycleA = 30
DutyCycleB = 30
Stop = 0

# Set the GPIO Pin mode

GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)

# Set up motor PWM frequencies

pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency)
pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency)
pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency)
pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency)

# Start the software PWM with all motors off

pwmMotorAForwards.start(Stop) 
pwmMotorABackwards.start(Stop) 
pwmMotorBForwards.start(Stop) 
pwmMotorBBackwards.start(Stop) 

# Turn all motors off

def StopMotors():
    pwmMotorAForwards.ChangeDutyCycle(Stop) 
    pwmMotorABackwards.ChangeDutyCycle(Stop) 
    pwmMotorBForwards.ChangeDutyCycle(Stop) 
    pwmMotorBBackwards.ChangeDutyCycle(Stop) 
    
# Turn both motors forwards

def Forwards():
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA) 
    pwmMotorABackwards.ChangeDutyCycle(Stop) 
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB) 
    pwmMotorBBackwards.ChangeDutyCycle(Stop) 
   
# Turn both motors backwards

def Backwards():
    pwmMotorAForwards.ChangeDutyCycle(Stop) 
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA) 
    pwmMotorBForwards.ChangeDutyCycle(Stop) 
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB) 
    
# Turn Right

def TurnRight():
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA) 
    pwmMotorABackwards.ChangeDutyCycle(Stop) 
    pwmMotorBForwards.ChangeDutyCycle(Stop) 
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB) 
    
# Turn Left

def TurnLeft():
    pwmMotorAForwards.ChangeDutyCycle(Stop) 
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA) 
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB) 
    pwmMotorBBackwards.ChangeDutyCycle(Stop) 
    

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

