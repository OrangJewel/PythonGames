import pygame, sys
from pygame.locals import *

pygame.init()

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BOXSIZE = 400

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

x2 = 120
y2 = 40

pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (x2, y2, BOXSIZE, BOXSIZE))

mousex = 0
mousey = 0

while True:

    mouseClicked = False
    
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            mouseClicked = True
            if mousex in range(120, 520):
                if mousey in range(40, 440):
                    DISPLAYSURF.fill(BGCOLOR)
                    pygame.draw.line(DISPLAYSURF, ORANGE, (40, 440), (600, 40), 5)
                    pygame.draw.line(DISPLAYSURF, ORANGE, (600, 440), (40, 40), 5)
            
    pygame.display.update()
