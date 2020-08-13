import pygame, sys
from pygame.locals import *

#FPS = 30
WINDOWWIDTH = 600
WINDOWHEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

#RED = (255, 0, 0)
#GREEN = (0, 255, 0)
#BLUE = (0, 0, 255)
WHITE = (248, 248, 242)
BLACK = (39, 40, 34)

#CIRCLE = 'circle'
#SQUARE = 'square'

while True:
    DISPLAYSURF.fill(BLACK)
    pygame.draw.line(DISPLAYSURF, WHITE, (200, 50), (200, 550), 4)
    pygame.draw.line(DISPLAYSURF, WHITE, (400, 50), (400, 550), 4)
    pygame.draw.line(DISPLAYSURF, WHITE, (50, 200), (550, 200), 4)
    pygame.draw.line(DISPLAYSURF, WHITE, (50, 400), (550, 400), 4)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        #    if event.key == K_KP7:
       #     if event.key == K_KP8:
      #      if event.key == K_KP9:
     #       if event.key == K_KP4:
    #        if event.key == K_KP5:
   #         if event.key == K_KP6:
  #          if event.key == K_KP1:
 #           if event.key == K_KP2:
#            if event.key == K_KP3:
    pygame.display.update()
