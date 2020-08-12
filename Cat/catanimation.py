import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

#set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')
catx = 10
caty = 10
cdirection = 'right'

dogpic = pygame.image.load('doggo.png')
dogImg = pygame.transform.scale(dogpic, (70, 70))
dogx = -100
dogy = 0
ddirection = 'dright'

while True: # the main game loop
    DISPLAYSURF.fill(WHITE)

    if cdirection == 'right':
        catx += 5
        if catx == 280:
            cdirection = 'down'
    elif cdirection == 'down':
        caty += 5
        if caty == 220:
            cdirection = 'left'
    elif cdirection == 'left':
        catx -= 5
        if catx == 10:
            cdirection = 'up'
    elif cdirection == 'up':
        caty -= 5
        if caty == 10:
            cdirection = 'right'
    DISPLAYSURF.blit(catImg, (catx, caty))

    if ddirection == 'dright':
        dogx += 5
        if dogx == 280:
            ddirection = 'ddown'
    elif ddirection == 'ddown':
        dogy += 5
        if dogy == 220:
            ddirection = 'dleft'
    elif ddirection == 'dleft':
        dogx -= 5
        if dogx == 10:
            ddirection = 'dup'
    elif ddirection == 'dup':
        dogy -= 5
        if dogy == 10:
            ddirection = 'dright'
    DISPLAYSURF.blit(dogImg, (dogx, dogy))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
