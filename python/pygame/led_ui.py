#!/usr/bin/env python3

"""
PyGame UI for the traffic lights LEDs
"""

import pygame
import RPi.GPIO as GPIO


pygame.init()

# Sizes and stuff

window_size = (680, 300)

buttons = ("Red ON", "Amber ON", "Green ON", "Red Off", "Amber Off", "Green Off")

# Colours

blue  = (0, 0, 64)
white = (255, 255, 255)
black = (0, 0, 0) 

# Fonts

button_font = pygame.font.Font(None, 48)
info_font   = pygame.font.Font(None, 24)

# LED pins

red_pin     = 11    # Pin Number, GPIO 17
amber_pin   = 13    # Pin Number, GPIO 27
green_pin   = 15    # Pin Number, GPIO 22

pins = (red_pin, amber_pin, green_pin)

# Set up pins for output

GPIO.setmode(GPIO.BOARD)

GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(amber_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)

GPIO.output(red_pin, GPIO.LOW)
GPIO.output(amber_pin, GPIO.LOW)
GPIO.output(green_pin, GPIO.LOW)

# Turn the LED on or off

def led_on(pin, delay = 0):
    GPIO.output(pin, GPIO.HIGH)

def led_off(pin, delay = 0):
    GPIO.output(pin, GPIO.LOW)

# Return the button indices

def button_pressed(pos):
    x_pos = (pos[0] - 20) // 220
    y_pos = (pos[1] - 20) // 120

    return (x_pos, y_pos)

# Set the specified LED on or off.

def set_led(index):
    pin = pins[index[0]]
    if index[1] == 0:
        led_on(pin)
    else:
        led_off(pin)

pygame.display.set_caption("LED UI")

screen = pygame.display.set_mode(window_size)

# Event Loop

running = True
last_index = ()

while running:
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        print("Mouse clicked on (%d, %d)" % event.pos)
        last_index = button_pressed(event.pos)

    screen.fill(blue)

    for y in range(2):
        for x in range(3):
            x_pos = x * 220 + 20
            y_pos = y * 120 + 20
            pygame.draw.rect(screen, white, (x_pos, y_pos, 200, 100))

            text_surface = button_font.render(buttons[y * 3 + x], 1, black, white) 
            screen.blit(text_surface, (x_pos + 20, y_pos + 20))

    if last_index != ():
        set_led(last_index)
        last_index = ()

    pygame.display.flip()

GPIO.cleanup()

