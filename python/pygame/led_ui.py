#!/usr/bin/env python3

"""
PyGame UI for the traffic lights LEDs
Version 2
"""

import pygame
import os
import RPi.GPIO as gpio

# LED pins

red_pin     = 11    # Pin Number, GPIO 17
amber_pin   = 13    # Pin Number, GPIO 27
green_pin   = 15    # Pin Number, GPIO 22

# 7-segment pins (See drive_7_segment.py for more details)
#              a   b   c   d   e   f   g   p5
pins7       = [16, 22, 12, 18, 32, 38, 36, 35]

# Sizes and stuff

window_size = (680, 620)

# Colours

blue    = (0, 0, 64)
white   = (255, 255, 255)
black   = (0, 0, 0) 
off     = (32, 32, 32)
red     = (255, 50, 50)
amber   = (255, 255, 50)
green   = (50, 255, 50)


#----------------------------------------------------------------------------
# GPIO Pin class

class Pin(object):
    def __init__(self, number, active = False, active_low = False):
        self.number     = number
        self.active     = active
        self.active_low = active_low
        self.set_state()

    def set_state(self):
        if self.active != self.active_low:
            gpio.output(self.number, gpio.HIGH)
        else:
            gpio.output(self.number, gpio.LOW)

    def toggle(self):
        self.active = not self.active
        self.set_state()


#----------------------------------------------------------------------------
# Button Class

class PinButton(object):
    def __init__(self, x, y, pin, text, colour, width = 200, height = 100, x_offset = 50, y_offset = 30):
        self.x          = x
        self.y          = y
        self.pin        = pin
        self.text       = text
        self.colour     = colour
        self.width      = width
        self.height     = height
        self.x_offset   = x_offset
        self.y_offset   = y_offset

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour if self.pin.active else off, (self.x, self.y, self.width, self.height))

        text_surface = button_font.render(self.text, 1, black if self.pin.active else white) 
        screen.blit(text_surface, (self.x + self.x_offset, self.y + self.y_offset))

    def clicked(self, pos):
        return pos[0] >= self.x and pos[0] < self.x + self.width and \
               pos[1] >= self.y and pos[1] < self.y + self.height


#----------------------------------------------------------------------------
# Initialisation

def initialise_gpio():
    gpio.setmode(gpio.BOARD)

    led_pins = [red_pin, amber_pin, green_pin]
    
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


initialise_gpio()
initialise_window()

screen      = pygame.display.set_mode(window_size)
button_font = pygame.font.Font(None, 48)

buttons    = [
    PinButton( 20,  20, Pin(red_pin),   'Red',   red,   200, 100, 60, 30),
    PinButton(240,  20, Pin(amber_pin), 'Amber', amber, 200, 100, 50, 30),
    PinButton(460,  20, Pin(green_pin), 'Green', green, 200, 100, 50, 30),

    PinButton( 50, 150, Pin(pins7[0], False, True), 'a', red, 150,  35, 60,  -2),
    PinButton( 33, 195, Pin(pins7[1], False, True), 'b', red,  35, 150,  7, 50),
    PinButton(188, 195, Pin(pins7[2], False, True), 'c', red,  35, 150,  7, 50),
    PinButton( 50, 355, Pin(pins7[6], False, True), 'g', red, 150,  35, 60,  -4),
    PinButton( 33, 400, Pin(pins7[3], False, True), 'd', red,  35, 150,  7, 50),
    PinButton(188, 400, Pin(pins7[4], False, True), 'e', red,  35, 150,  7, 50),
    PinButton( 50, 560, Pin(pins7[5], False, True), 'f', red, 150,  35, 60,  -4),
]

# Event Loop

running = True

while running:
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        for b in buttons:
            if b.clicked(event.pos):
                b.pin.toggle()
                break

    screen.fill(blue)

    for b in buttons:
        b.draw(screen)

    pygame.display.flip()

gpio.cleanup()

