import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('Hello world', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

keySurfaceObj = fontObj.render('I hope to god this works', True, BLUE, GREEN)
keyRectObj = keySurfaceObj.get_rect()
keyRectObj.center = (200, 250)

displayText = False


while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    
#    if displayText == True:
#        DISPLAYSURF.blit(keySurfaceObj, keyRectObj)
#        print('blit')

    if pygame.key.get_pressed()[pygame.K_a]:
        print('The a key is being held')
        DISPLAYSURF.blit(keySurfaceObj, keyRectObj)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_a:
                print ('The a key has been pressed')
                displayText = True
            if event.key == K_d:
                print ('The d key has been pressed')
                displayText = False
            if event.key == K_ESCAPE:
                print ('The Esc key has been pressed')
                pygame.quit()
                sys.exit()
                
    pygame.display.update()
