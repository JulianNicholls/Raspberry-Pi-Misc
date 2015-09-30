#!/usr/bin/env python3

"""
UI
"""

import pygame

pygame.init()

pygame.display.set_caption("LED UI")

window_size = (600, 600)

screen = pygame.display.set_mode(window_size)

# Colours

blue  = (0, 0, 64)
white = (255, 255, 255)
black = (0, 0, 0) 

# Font

font = pygame.font.Font(None, 64)

# Rectangle

x, y = 0, 0
w, h = 200, 200

# Event Loop

running = True

while running:
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEMOTION:
        print("Mouse moved to (%d, %d)" % event.pos)

    screen.fill(blue)
    pygame.draw.rect(screen, white, (x, y, w, h)) # Border is , 1)

    text_surface = font.render('%d, %d' % (x, y), 1, black)
    text_pos = (x + 10, y + 10)

    screen.blit(text_surface, text_pos)

    if x < window_size[1] - w:
        x += 1
        y += 1

    pygame.display.flip()

