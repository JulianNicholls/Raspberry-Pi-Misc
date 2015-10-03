#!/usr/bin/env python3

"""
PyGame UI for the traffic lights LEDs
Version 2
"""

import pygame
import RPi.GPIO as gpio


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

pins = [[red_pin, 0, 'Red', red], [amber_pin, 0, 'Amber', amber], [green_pin, 0, 'Green', green]]

# Set up pins for output

gpio.setmode(gpio.BOARD)

for pin in pins:
    gpio.setup(pin[GPIO], gpio.OUT)
    gpio.output(pin[GPIO], gpio.LOW)

# Turn the LED on or off

def led_on(pin, delay = 0):
    gpio.output(pin, gpio.HIGH)

def led_off(pin, delay = 0):
    gpio.output(pin, gpio.LOW)

# Return the button indices

def button_pressed(pos):
    x_pos = (pos[0] - 20) // 220

    return x_pos

# Set the specified LED on or off.

def set_led(index):
    pin = pins[index]

    if pin[STATE] == OFF: 
        led_on(pin[GPIO])
        pin[STATE] = ON
    else:
        led_off(pin[GPIO])
        pin[STATE] = OFF

pygame.display.set_caption("LED UI V2")

screen = pygame.display.set_mode(window_size)

# Event Loop

running = True
last_index = -1

while running:
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        last_index = button_pressed(event.pos)

    screen.fill(blue)

    for x in range(3):
        x_pos = x * 220 + 20
        on = pins[x][STATE] == ON
        pygame.draw.rect(screen, pins[x][COLOUR] if on else off, (x_pos, 20, 200, 100))

        text_surface = button_font.render(pins[x][NAME], 1, black if on else white) 
        screen.blit(text_surface, (x_pos + 20, 50))

    if last_index != -1:
        set_led(last_index)
        last_index = -1

    pygame.display.flip()

gpio.cleanup()

