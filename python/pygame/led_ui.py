#!/usr/bin/env python3

"""
UI
"""

import pygame

pygame.init()
pygame.display.set_caption("LED UI")

window_size = (600, 600)

screen = pygame.display.set_mode(window_size)

blue = (0, 0, 80)

# screen = pygame.display.set_mode([screenWidth, screenHeight], 0, 32)
# background = pygame.Surface((screenWidth, screenHeight))

# Event Loop

running = True

while running:
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEMOTION:
        print("Mouse moved to (%d, %d)" % event.pos)

    screen.fill(blue)
    pygame.display.flip()

