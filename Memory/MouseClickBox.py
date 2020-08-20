import pygame, sys
from pygame.locals import *

pygame.init()

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BOXSIZE = 400
XMARGIN = 10
YMARGIN = 10

NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
BLUE     = (  0,   0, 255)
ORANGE   = (255, 128,   0)

BGCOLOR = NAVYBLUE
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE
SYMBOLCOLOR = ORANGE

DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
DISPLAYSURF.fill(BGCOLOR)

while True:

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
            
    pygame.display.update()
