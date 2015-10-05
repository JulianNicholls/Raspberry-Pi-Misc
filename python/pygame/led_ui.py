#!/usr/bin/env python3

"""
PyGame UI for the traffic lights LEDs
Version 2
"""

import pygame
import RPi.GPIO as gpio


class Button(object):
    def __init__(self, x, y, pin, text, colour, width = 200, height = 100):
        self.x      = x
        self.y      = y
        self.pin    = pin
        self.text   = text
        self.colour = colour
        self.width  = width
        self.height = height
        self.active = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour if self.active else off, (self.x, self.y, self.width, self.height))

        text_surface = button_font.render(self.text, 1, black if self.active else white) 
        screen.blit(text_surface, (self.x + 20, self.y + 30))

    def clicked(self, pos):
        return pos[0] >= self.x and pos[0] < self.x + self.width and \
               pos[1] >= self.y and pos[1] < self.y + self.height



pygame.init()

# Sizes and stuff

window_size = (680, 150)

# Colours

blue    = (0, 0, 64)
white   = (255, 255, 255)
black   = (0, 0, 0) 
off     = (32, 32, 32)
red     = (255, 70, 70)
amber   = (255, 255, 70)
green   = (70, 255, 70)

# Fonts

button_font = pygame.font.Font(None, 48)

# LED pins

red_pin     = 11    # Pin Number, GPIO 17
amber_pin   = 13    # Pin Number, GPIO 27
green_pin   = 15    # Pin Number, GPIO 22

OFF         = 0
ON          = 1

GPIO        = 0
STATE       = 1
NAME        = 2
COLOUR      = 3

buttons    = [
    Button( 20, 20, red_pin,   'Red',   red),
    Button(240, 20, amber_pin, 'Amber', amber),
    Button(460, 20, green_pin, 'Green', green)
]

pins = [red_pin, amber_pin, green_pin]

# Set up pins for output

gpio.setmode(gpio.BOARD)

for pin in pins:
    gpio.setup(pin, gpio.OUT)
    gpio.output(pin, gpio.LOW)

# Turn the LED on or off

def led_on(pin, delay = 0):
    gpio.output(pin, gpio.HIGH)

def led_off(pin, delay = 0):
    gpio.output(pin, gpio.LOW)

# Set the specified LED on or off.

def set_led(button):
    pin = button.pin

    if button.active: 
        led_off(pin)
    else:
        led_on(pin)

    button.active = not button.active

pygame.display.set_caption("LED UI V2")

screen = pygame.display.set_mode(window_size)

# Event Loop

running = True

while running:
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        for b in buttons:
            if b.clicked(event.pos):
                set_led(b)
                break

    screen.fill(blue)

    for b in buttons:
        b.draw(screen)

    pygame.display.flip()

gpio.cleanup()

