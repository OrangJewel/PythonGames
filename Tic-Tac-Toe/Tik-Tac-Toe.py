import pygame, sys
from pygame.locals import *

#FPS = 30
WINDOWWIDTH = 600
WINDOWHEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))



RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (248, 248, 242)
BLACK = (39, 40, 34)

turn = True
space_7 = True
space_8 = True
space_9 = True
space_4 = True
space_5 = True
space_6 = True
space_1 = True
space_2 = True
space_3 = True



DISPLAYSURF.fill(BLACK)
pygame.draw.line(DISPLAYSURF, WHITE, (200, 25), (200, 575), 3)
pygame.draw.line(DISPLAYSURF, WHITE, (400, 25), (400, 575), 3)
pygame.draw.line(DISPLAYSURF, WHITE, (25, 200), (575, 200), 3)
pygame.draw.line(DISPLAYSURF, WHITE, (25, 400), (575, 400), 3)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_KP7 and space_7 == True:
                if turn == True:
                    pygame.draw.circle(DISPLAYSURF, BLUE, (100, 100), 80, 5)
                    turn = False
                    space_7 = False
                else:
                    pygame.draw.line(DISPLAYSURF, RED, (25, 25), (175, 175), 5)
                    pygame.draw.line(DISPLAYSURF, RED, (25, 175), (175, 25), 5)
                    turn = True
                    space_7 = False

                    
            if event.key == K_KP8 and space_8 == True:
                if turn == True:
                    pygame.draw.circle(DISPLAYSURF, BLUE, (300, 100), 80, 5)
                    turn = False
                    space_8 = False
                else:
                    pygame.draw.line(DISPLAYSURF, RED, (225, 25), (375, 175), 5)
                    pygame.draw.line(DISPLAYSURF, RED, (225, 175), (375, 25), 5)
                    turn = True
                    space_8 = False

                    
            if event.key == K_KP9 and space_9 == True:
                if turn == True:
                    pygame.draw.circle(DISPLAYSURF, BLUE, (500, 100), 80, 5)
                    turn = False
                    space_9 = False
                else:
                    pygame.draw.line(DISPLAYSURF, RED, (425, 25), (575, 175), 5)
                    pygame.draw.line(DISPLAYSURF, RED, (425, 175), (575, 25), 5)
                    turn = True
                    space_9 = False

                    
            if event.key == K_KP4 and space_4 == True:
                if turn == True:
                    pygame.draw.circle(DISPLAYSURF, BLUE, (100, 300), 80, 5)
                    turn = False
                    space_4 = False
                else:
                    pygame.draw.line(DISPLAYSURF, RED, (25, 225), (175, 375), 5)
                    pygame.draw.line(DISPLAYSURF, RED, (25, 375), (175, 225), 5)
                    turn = True
                    space_4 = False

                    
            if event.key == K_KP5 and space_5 == True:
                if turn == True:
                    pygame.draw.circle(DISPLAYSURF, BLUE, (300, 300), 80, 5)
                    turn = False
                    space_5 = False
                else:
                    pygame.draw.line(DISPLAYSURF, RED, (225, 225), (375, 375), 5)
                    pygame.draw.line(DISPLAYSURF, RED, (225, 375), (375, 225), 5)
                    turn = True
                    space_5 = False

                    
            if event.key == K_KP6 and space_6 == True:
                if turn == True:
                    pygame.draw.circle(DISPLAYSURF, BLUE, (500, 300), 80, 5)
                    turn = False
                    space_6 = False
                else:
                    pygame.draw.line(DISPLAYSURF, RED, (425, 225), (575, 375), 5)
                    pygame.draw.line(DISPLAYSURF, RED, (425, 375), (575, 225), 5)
                    turn = True
                    space_6 = False

                    
            if event.key == K_KP1 and space_1 == True:
                if turn == True:
                    pygame.draw.circle(DISPLAYSURF, BLUE, (100, 500), 80, 5)
                    turn = False
                    space_1 = False
                else:
                    pygame.draw.line(DISPLAYSURF, RED, (25, 425), (575, 575), 5)
                    pygame.draw.line(DISPLAYSURF, RED, (25, 575), (575, 425), 5)
                    turn = True
                    space_1 = False

                    
            if event.key == K_KP2 and space_2 == True:
                if turn == True:
                    pygame.draw.circle(DISPLAYSURF, BLUE, (300, 500), 80, 5)
                    turn = False
                    space_2 = False
                else:
                    pygame.draw.line(DISPLAYSURF, RED, (225, 425), (375, 575), 5)
                    pygame.draw.line(DISPLAYSURF, RED, (225, 575), (375, 425), 5)
                    turn = True
                    space_2 = False

                    
            if event.key == K_KP3 and space_3 == True:
                if turn == True:
                    pygame.draw.circle(DISPLAYSURF, BLUE, (500, 500), 80, 5)
                    turn = False
                    space_3 = False
                else:
                    pygame.draw.line(DISPLAYSURF, RED, (425, 425), (575, 575), 5)
                    pygame.draw.line(DISPLAYSURF, RED, (425, 575), (575, 425), 5)
                    turn = True
                    space_3 = False

                    
    pygame.display.update()
