#!/usr/bin/env python3

from gpiozero import Robot, LED, Button
import time

robot   = Robot((9, 10), (8, 7))    # Left, Right
trig    = LED(17)                   # Ultrasonic Distance Trigger
echo    = Button(18)                # Ultrasonic Distance Echo


# Return the distance from the sensor at the front to any obstruction.

def distance():
    global trig, echo

    trig.off()
    time.sleep(0.01)

    trig.on()
    time.sleep(0.00001)
    trig.off()

    echo.wait_for_release()
    startTime = time.time()

    echo.wait_for_press(0.1)
    elapsed = time.time() - startTime
    distance = elapsed * 17163

    if elapsed > 0.04:
        print("Too close")
        distance = 0.1
    elif distance < 20.0:
        print("Distance %.1f" % distance)

    return distance


# Keep moving until any obstruction is closer than 10 cm.

def inch_forward():
    while distance() > 10:
        pass

    robot.stop()


# Get instructions from user
# f <n>   Forward for n steps
# f d     Forward until less than 10cm from obstacle
# b <n>   Backward for n steps
# l <n>   Left for n steps
# r <n>   Right for n steps

while True:
    text = input("Next: ").strip().lower()

    if text[0] =='q':
        break
    
    try:
        cmd, duration = text.split()
    except ValueError:
        duration = '0'

    if cmd[0] == 'f':
        print('Forward', end=' ')
        robot.forward(0.4)
        if duration == 'd':
            inch_forward()

    elif cmd[0] == 'b':
        print('Backward', end=' ')
        robot.backward(0.4)
    elif cmd[0] == 'l':
        print('Left', end=' ')
        robot.left(0.4)
    elif cmd[0] == 'r':
        print('Right', end=' ')
        robot.right(0.4)
    elif cmd[0] == 'd':
        print("Distance")
        distance()

    try:
        duration = float(duration)
    except ValueError:
        duration = 0

    if duration > 0:
        print(duration)

    time.sleep(duration / 7)
    robot.stop()

