#!/usr/bin/env python

"""
Bounce with sound
"""

import time
import os, pygame, sys

pygame.init()

pygame.mixer.quit()
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
bounceSound = pygame.mixer.Sound('sounds/bounce.ogg')

os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
pygame.display.set_caption("Bounce 2, with sound")

screenWidth  = 400
screenHeight = 400

screen      = pygame.display.set_mode([screenWidth, screenHeight], 0, 32)
background  = pygame.Surface((screenWidth, screenHeight))

# Define the colours

cBackground = (255, 255, 255)
cBlock = (0, 0, 0)
background.fill(cBackground)
box = [screenWidth - 40, screenHeight - 40]
delta = [5, 10]
hw = screenWidth // 2
hh = screenHeight // 2
position = [hw, hh]
limit = [0, 0, 0, 0]
ballRad = 8

def main():
    global position

    updateBox(0, 0)

    screen.blit(background, [0, 0])

    while True:
        checkForEvent()
        time.sleep(0.02)
        drawScreen(position)
        position = moveBall(position)

def moveBall(p):
    global delta

    p[0] += delta[0]
    p[1] += delta[1]

    if p[0] <= limit[0]:
        bounceSound.play()
        delta[0] = -delta[0]
        p[0] = limit[0]

    if p[0] >= limit[1]:
        bounceSound.play()
        delta[0] = -delta[0]
        p[0] = limit[1]

    if p[1] <= limit[2]:
        bounceSound.play()
        delta[1] = -delta[1]
        p[1] = limit[2]

    if p[1] >= limit[3]:
        bounceSound.play()
        delta[1] = -delta[1]
        p[1] = limit[3]

    return p

def drawScreen(p):
    screen.blit(background, [0, 0])
    pygame.draw.rect(screen, (255, 0, 0), (hw - box[0] / 2, hh - box[1] / 2, box[0], box[1]), 2)
    pygame.draw.circle(screen, cBlock, (p[0], p[1]), ballRad, 2)
    pygame.display.update()

def updateBox(d, amount):
    global box, limit

    box[d] += amount

    limit[0] = hw - box[0] // 2 + ballRad  # Left
    limit[1] = hw + box[0] // 2 - ballRad  # Right
    limit[2] = hh - box[1] // 2 + ballRad  # Top
    limit[3] = hh + box[1] // 2 - ballRad  # Right

def terminate():
    print("Closing down, please wait...")
    pygame.quit()
    sys.exit()

def checkForEvent():
    event = pygame.event.poll()

    if event.type == pygame.QUIT:
        terminate()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            terminate()

        if event.key == pygame.K_LEFT:
            updateBox(0, -5)
        if event.key == pygame.K_RIGHT:
            updateBox(0, 5)
        if event.key == pygame.K_DOWN:
            updateBox(1, -5)
        if event.key == pygame.K_UP:
            updateBox(1, 5)


if __name__ == '__main__':
    main()
