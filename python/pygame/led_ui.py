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
# GPIO Pin class that holds a GPIO pin number, current state, and active
# low status.

class Pin(object):
    def __init__(self, number, active = False, active_low = False):
        """ Initialise with the pin number, start state, and active low status """
        self.number     = number
        self.active     = active
        self.active_low = active_low

        self.set_state()

    def set_state(self):
        """ Set the hardware pin based on state and active low """
        hilo = gpio.HIGH if self.active != self.active_low else gpio.LOW
        gpio.output(self.number, hilo)

    def toggle(self):
        """ Toggle the state and action it """
        self.active = not self.active
        self.set_state()


#----------------------------------------------------------------------------
# Generic Button class that knows how to draw itself and returns true if it
# has been clicked.

class Button(object):
    def __init__(self, x, y, text, colour, width, height, x_offset, y_offset):
        self.x, self.y          = x, y
        self.width, self.height = width, height
        self.x_off, self.y_off  = x_offset, y_offset

        self.text       = text
        self.colour     = colour

    def draw(self, screen):
        """ Draw the button rectangle and its text """
        pygame.draw.rect(screen, colour, (self.x, self.y, self.width, self.height))

        text_surface = button_font.render(self.text, 1, white) 
        screen.blit(text_surface, (self.x + self.x_off, self.y + self.y_off))

    def contains(self, pos):
        """ Return whether the passed position is part of the button """
        return pos[0] >= self.x and pos[0] < self.x + self.width and \
               pos[1] >= self.y and pos[1] < self.y + self.height

    def action(self):
        """ NULL Action """
        pass

#----------------------------------------------------------------------------
# PinButton Class that holds a Pin reference and draws based on it.

class PinButton(Button):
    def __init__(self, x, y, pin, text, colour, width = 200, height = 100, x_offset = 50, y_offset = 30):
        super().__init__(x, y, text, colour, width, height, x_offset, y_offset) 

        self.pin = pin

    def draw(self, screen):
        """ Draw the button rectangle and its text sewnsitive to pin status """
        pygame.draw.rect(screen, self.colour if self.pin.active else off, (self.x, self.y, self.width, self.height))

        text_surface = button_font.render(self.text, 1, black if self.pin.active else white) 
        screen.blit(text_surface, (self.x + self.x_off, self.y + self.y_off))

    def action(self):
        """ Toggle the pin state """
        self.pin.toggle()

#----------------------------------------------------------------------------
# Initialisation functions

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

buttons     = [
    PinButton( 20,  20, Pin(red_pin),   'Red',   red,   200, 100, 60, 30),
    PinButton(240,  20, Pin(amber_pin), 'Amber', amber, 200, 100, 50, 30),
    PinButton(460,  20, Pin(green_pin), 'Green', green, 200, 100, 50, 30),

    PinButton( 50, 150, Pin(pins7[0], False, True), 'a', red, 150,  35, 60,  -2),
    PinButton( 33, 195, Pin(pins7[1], False, True), 'b', red,  35, 150,  7, 50),
    PinButton(188, 195, Pin(pins7[2], False, True), 'c', red,  35, 150,  7, 50),
    PinButton( 50, 355, Pin(pins7[6], False, True), 'g', red, 150,  35, 60,  -4),
    PinButton( 33, 400, Pin(pins7[3], False, True), 'd', red,  35, 150,  7, 50),
    PinButton(188, 400, Pin(pins7[4], False, True), 'e', red,  35, 150,  7, 50),
    PinButton( 50, 560, Pin(pins7[5], False, True), 'f', red, 150,  35, 62,  -2),
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

