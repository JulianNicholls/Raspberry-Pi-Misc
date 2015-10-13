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

a_pin_num   = 16
b_pin_num   = 22
c_pin_num   = 12
d_pin_num   = 18
e_pin_num   = 32
f_pin_num   = 38
g_pin_num   = 36
p5_pin_num  = 35

# Sizes and stuff

window_size = (750, 620)

# Colours

blue    = (  0,   0,  48)
white   = (255, 255, 255)
black   = (  0,   0,   0) 
off     = ( 32,  32,  32)
red     = (255,  50,  50)
amber   = (255, 255,  50)
green   = ( 50, 255,  50)
lblue   = ( 50,  50, 255)


# Bitmaps for displaying characters on the 7-segment display

digits  = [
    0b1111110, 0b0010100, 0b1011011, 0b1010111, 0b0110101,  # 0-4
    0b1100111, 0b1101111, 0b1010100, 0b1111111, 0b1110111,  # 5-9
]
    
letters = { # Included: ABCDEFGHIJ LNOP RS U YZ    Missing: KMQTVWX 
    'A': 0b1111101, 'a': 0b1011111, 'b': 0b0101111, 'C': 0b1101010, 
    'c': 0b0001011, 'd': 0b0011111, 'E': 0b1101011, 'F': 0b1101001, 
    'g': 0b1110111, 'H': 0b0111101, 'h': 0b0101101, 'I': 0b0010100, 
    'i': 0b0000100, 'J': 0b0010110, 'L': 0b0101010, 'n': 0b0001101, 
    'O': 0b1111110, 'o': 0b0001111, 'P': 0b1111001, 'r': 0b0001001, 
    'S': 0b1100111, 'U': 0b0111110, 'u': 0b0001110, 'y': 0b0110111, 
    'Z': 0b1011011
}

#----------------------------------------------------------------------------
# Initialisation functions

def initialise_gpio():
    gpio.setmode(gpio.BOARD)

def initialise_window():
    pygame.init()
    os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'

    pygame.display.set_caption("LED UI V3")

def add_digit_buttons():
    top     = 150
    left    = 300

    for i in range(len(digits)):
        buttons.append(CharButton(left, top, str(i), button_font, off, 50, 50, 20, 10, digits[i]))

        left += 65

        if left > 580:
            left = 300
            top += 60


def add_letter_buttons():
    top     = 290
    left    = 300

    for ltr in sorted(letters):
        buttons.append(CharButton(left, top, ltr, button_font, off, 50, 50, 20, 10, letters[ltr]))

        left += 65

        if left > 580:
            left = 300
            top += 60


#----------------------------------------------------------------------------# Main

initialise_gpio()
initialise_window()

screen      = pygame.display.set_mode(window_size)
button_font = pygame.font.Font(None, 36)

pins7       = [
    Pin(a_pin_num, False, True),
    Pin(b_pin_num, False, True),
    Pin(c_pin_num, False, True),
    Pin(d_pin_num, False, True),
    Pin(e_pin_num, False, True),
    Pin(f_pin_num, False, True),
    Pin(g_pin_num, False, True)
]        

buttons     = [
    PinButton( 20,  20, 'Red',   button_font, red,   off, 120, 75, 31, 22, Pin(red_pin)),
    PinButton(160,  20, 'Amber', button_font, amber, off, 120, 75, 22, 22, Pin(amber_pin)),
    PinButton(300,  20, 'Green', button_font, green, off, 120, 75, 22, 22, Pin(green_pin)),
    PinButton(440,  20, 'Blue',  button_font, lblue, off, 120, 75, 26, 22, Pin(blue_pin)),
    PinButton(580,  20, 'White', button_font, white, off, 120, 75, 22, 22, Pin(white_pin)),

    PinButton( 50, 150, 'a', button_font, red, off, 150,  30, 60,  0, pins7[0]),
    PinButton( 35, 190, 'b', button_font, red, off,  30, 150,  7, 50, pins7[1]),
    PinButton(190, 190, 'c', button_font, red, off,  30, 150,  7, 50, pins7[2]),
    PinButton( 50, 350, 'g', button_font, red, off, 150,  30, 60,  0, pins7[6]),
    PinButton( 35, 390, 'd', button_font, red, off,  30, 150,  7, 50, pins7[3]),
    PinButton(190, 390, 'e', button_font, red, off,  30, 150,  7, 50, pins7[4]),
    PinButton( 50, 550, 'f', button_font, red, off, 150,  30, 64,  0, pins7[5]),
]

# Add buttons for the digits 0-9 and various letters

add_digit_buttons()
add_letter_buttons()


# Set up the CharButton class with a set of pins

CharButton.pins = pins7

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

