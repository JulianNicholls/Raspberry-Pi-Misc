#!/usr/bin/env python3

"""
PyGame UI for the traffic lights LEDs
Version 2
"""

import pygame
import os
import RPi.GPIO as gpio

from pin import Pin
from button import PinButton

# LED pins

red_pin     = 11    # Pin Number, GPIO 17
amber_pin   = 13    # Pin Number, GPIO 27
green_pin   = 15    # Pin Number, GPIO 22
blue_pin    = 29    # Pin Number, GPIO 5    
white_pin   = 31    # Pin Number, GPIO 6

# 7-segment pins (See drive_7_segment.py for more details)
#              a   b   c   d   e   f   g   p5
pins7       = [16, 22, 12, 18, 32, 38, 36, 35]

# Sizes and stuff

window_size = (750, 620)

# Colours

blue    = (0, 0, 64)
white   = (255, 255, 255)
black   = (0, 0, 0) 
off     = (32, 32, 32)
red     = (255, 50, 50)
amber   = (255, 255, 50)
green   = (50, 255, 50)
lblue   = (50, 50, 255)


#----------------------------------------------------------------------------
# Initialisation functions

def initialise_gpio():
    gpio.setmode(gpio.BOARD)

    led_pins = [red_pin, amber_pin, green_pin, blue_pin, white_pin]
    
    for pin in led_pins:
        gpio.setup(pin, gpio.OUT)
        gpio.output(pin, gpio.LOW)

    for pin in pins7:
        gpio.setup(pin, gpio.OUT)
        gpio.output(pin, gpio.HIGH)     # Active Low

def initialise_window():
    pygame.init()
    os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'

    pygame.display.set_caption("LED UI V2")


#----------------------------------------------------------------------------
# Main

initialise_gpio()
initialise_window()

screen      = pygame.display.set_mode(window_size)
button_font = pygame.font.Font(None, 36)

buttons     = [
    PinButton( 20,  20, Pin(red_pin),   'Red',   button_font, red,   off, 120, 75, 30, 22),
    PinButton(160,  20, Pin(amber_pin), 'Amber', button_font, amber, off, 120, 75, 22, 22),
    PinButton(300,  20, Pin(green_pin), 'Green', button_font, green, off, 120, 75, 22, 22),
    PinButton(440,  20, Pin(blue_pin),  'Blue',  button_font, lblue, off, 120, 75, 25, 22),
    PinButton(580,  20, Pin(white_pin), 'White', button_font, white, off, 120, 75, 22, 22),

    PinButton( 50, 150, Pin(pins7[0], False, True), 'a', button_font, red, off, 150,  30, 60,  0),
    PinButton( 35, 190, Pin(pins7[1], False, True), 'b', button_font, red, off,  30, 150,  7, 50),
    PinButton(190, 190, Pin(pins7[2], False, True), 'c', button_font, red, off,  30, 150,  7, 50),
    PinButton( 50, 350, Pin(pins7[6], False, True), 'g', button_font, red, off, 150,  30, 60,  0),
    PinButton( 35, 390, Pin(pins7[3], False, True), 'd', button_font, red, off,  30, 150,  7, 50),
    PinButton(190, 390, Pin(pins7[4], False, True), 'e', button_font, red, off,  30, 150,  7, 50),
    PinButton( 50, 550, Pin(pins7[5], False, True), 'f', button_font, red, off, 150,  30, 64,  0),
]

# Event Loop

running = True

while running:
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        for b in buttons:
            if b.contains(event.pos):
                b.action()
                break

    screen.fill(blue)

    for b in buttons:
        b.draw(screen)

    pygame.display.flip()

gpio.cleanup()

