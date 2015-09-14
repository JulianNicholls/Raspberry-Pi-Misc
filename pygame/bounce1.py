#!/usr/bin/env python

"""
Bounce
"""

import time
import os, pygame, sys

pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
pygame.display.set_caption("Bounce 1")

screenWidth = 400
screenHeight = 400

screen = pygame.display.set_mode([screenWidth, screenHeight], 0, 32)
background = pygame.Surface((screenWidth, screenHeight))

# Define the colours

cBackground = (255, 255, 255)
cBlock = (0, 0, 0)
background.fill(cBackground)
dx = 5
dy = 10

def main():
    x = screenWidth / 2
    y = screenHeight / 2

    screen.blit(background, [0, 0])

    while True:
        checkForEvent()
        time.sleep(0.02)
        drawScreen(x, y)
        x += dx
        y += dy
        checkBounds(x, y)

def checkBounds(px, py):
    global dx, dy

    if px > screenWidth - 10 or px < 0:
        dx = -dx

    if py > screenHeight - 10 or py < 0:
        dy = -dy

def drawScreen(px, py):
    screen.blit(background, [0, 0])
    pygame.draw.rect(screen, cBlock, (px, py, 10, 10), 0)
    pygame.display.update()

def terminate():
    print "Closing down, please wait..."
    pygame.quit()
    sys.exit()

def checkForEvent():
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        terminate()

    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        terminate()


if __name__ == '__main__':
    main()

