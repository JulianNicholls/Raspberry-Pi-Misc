#!/usr/bin/env python3

"""
PyGame UI for connected LEDs
Version 3
"""

import pygame
import os
import RPi.GPIO as gpio

from pin    import Pin
from button import PinButton, CharButton

# LED pins

red_pin     = 11    # Pin Number, GPIO 17
amber_pin   = 13    # Pin Number, GPIO 27
green_pin   = 15    # Pin Number, GPIO 22
blue_pin    = 29    # Pin Number, GPIO 5    
white_pin   = 31    # Pin Number, GPIO 6

# 7-segment pins (See .../gpio/drive_7_segment.py for more details)

a_pin       = 16
b_pin       = 22
c_pin       = 12
d_pin       = 18
e_pin       = 32
f_pin       = 38
g_pin       = 36
p5_pin      = 35

# Sizes and stuff

window_size = (750, 620)

# Colours

blue    = (0, 0, 48)
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

    PinButton( 50, 150, Pin(a_pin, False, True), 'a', button_font, red, off, 150,  30, 60,  0),
    PinButton( 35, 190, Pin(b_pin, False, True), 'b', button_font, red, off,  30, 150,  7, 50),
    PinButton(190, 190, Pin(c_pin, False, True), 'c', button_font, red, off,  30, 150,  7, 50),
    PinButton( 50, 350, Pin(g_pin, False, True), 'g', button_font, red, off, 150,  30, 60,  0),
    PinButton( 35, 390, Pin(d_pin, False, True), 'd', button_font, red, off,  30, 150,  7, 50),
    PinButton(190, 390, Pin(e_pin, False, True), 'e', button_font, red, off,  30, 150,  7, 50),
    PinButton( 50, 550, Pin(f_pin, False, True), 'f', button_font, red, off, 150,  30, 64,  0),

    CharButton(300, 150, '0', button_font, off, 50, 50, 20, 10),
    CharButton(360, 150, '1', button_font, off, 50, 50, 20, 10),
    CharButton(420, 150, '2', button_font, off, 50, 50, 20, 10),
    CharButton(480, 150, '3', button_font, off, 50, 50, 20, 10),
    CharButton(540, 150, '4', button_font, off, 50, 50, 20, 10),

    CharButton(300, 210, '5', button_font, off, 50, 50, 20, 10),
    CharButton(360, 210, '6', button_font, off, 50, 50, 20, 10),
    CharButton(420, 210, '7', button_font, off, 50, 50, 20, 10),
    CharButton(480, 210, '8', button_font, off, 50, 50, 20, 10),
    CharButton(540, 210, '9', button_font, off, 50, 50, 20, 10),
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

