#!/usr/bin/env python3

from gpiozero import Robot
import time

robot = Robot((7, 8), (10, 9))

robot.forward(0.4)
time.sleep(1.5)

robot.stop()
time.sleep(0.5)

robot.right(0.4)
time.sleep(1.5)

robot.stop()
time.sleep(0.5)

robot.left(0.4)
time.sleep(1.5)

