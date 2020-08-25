import pygame, sys, time
from pygame.locals import *

#FPS = 30
WINDOWWIDTH = 600
WINDOWHEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

mousex = 0
mousey = 0

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (248, 248, 242)
BLACK = (39, 40, 34)

gameOver = False
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

space_7a = False
space_8a = False
space_9a = False
space_4a = False
space_5a = False
space_6a = False
space_1a = False
space_2a = False
space_3a = False

space_7b = False
space_8b = False
space_9b = False
space_4b = False
space_5b = False
space_6b = False
space_1b = False
space_2b = False
space_3b = False

DISPLAYSURF.fill(BLACK)
pygame.draw.line(DISPLAYSURF, WHITE, (200, 25), (200, 575), 3)
pygame.draw.line(DISPLAYSURF, WHITE, (400, 25), (400, 575), 3)
pygame.draw.line(DISPLAYSURF, WHITE, (25, 200), (575, 200), 3)
pygame.draw.line(DISPLAYSURF, WHITE, (25, 400), (575, 400), 3)

print('Player 1 is Os, player 2 is Xs')

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONUP:
            mousex, mousey = event.pos
            mouseClicked = True
            if mousex in range(0, 200):
                if mousey in range(0, 200):
                    if turn == True:
                        pygame.draw.circle(DISPLAYSURF, BLUE, (100, 100), 80, 5)
                        turn = False
                        space_7 = False
                        space_7a = True
                    else:
                        pygame.draw.line(DISPLAYSURF, RED, (25, 25), (175, 175), 5)
                        pygame.draw.line(DISPLAYSURF, RED, (25, 175), (175, 25), 5)
                        turn = True
                        space_7 = False
                        space_7b = True
                        
            if mousex in range(201, 400):
                if mousey in range(0, 200):
                    if turn == True:
                        pygame.draw.circle(DISPLAYSURF, BLUE, (300, 100), 80, 5)
                        turn = False
                        space_8 = False
                        space_8a = True
                    else:
                        pygame.draw.line(DISPLAYSURF, RED, (225, 25), (375, 175), 5)
                        pygame.draw.line(DISPLAYSURF, RED, (225, 175), (375, 25), 5)
                        turn = True
                        space_8 = False
                        space_8b = True
                    
            if mousex in range(401, 600):
                if mousey in range(0, 200):
                    if turn == True:
                        pygame.draw.circle(DISPLAYSURF, BLUE, (500, 100), 80, 5)
                        turn = False
                        space_9 = False
                        space_9a = True
                    else:
                        pygame.draw.line(DISPLAYSURF, RED, (425, 25), (575, 175), 5)
                        pygame.draw.line(DISPLAYSURF, RED, (425, 175), (575, 25), 5)
                        turn = True
                        space_9 = False
                        space_9b = True

            if mousex in range(0, 200):
                if mousey in range(201, 400):
                    if turn == True:
                        pygame.draw.circle(DISPLAYSURF, BLUE, (100, 300), 80, 5)
                        turn = False
                        space_4 = False
                        space_4a = True
                    else:
                        pygame.draw.line(DISPLAYSURF, RED, (25, 225), (175, 375), 5)
                        pygame.draw.line(DISPLAYSURF, RED, (25, 375), (175, 225), 5)
                        turn = True
                        space_4 = False
                        space_4b = True

            if mousex in range(201, 400):
                if mousey in range(201, 400):
                    if turn == True:
                        pygame.draw.circle(DISPLAYSURF, BLUE, (300, 300), 80, 5)
                        turn = False
                        space_5 = False
                        space_5a = True
                    else:
                        pygame.draw.line(DISPLAYSURF, RED, (225, 225), (375, 375), 5)
                        pygame.draw.line(DISPLAYSURF, RED, (225, 375), (375, 225), 5)
                        turn = True
                        space_5 = False
                        space_5b = True

            if mousex in range(401, 600):
                if mousey in range(201, 400):
                    if turn == True:
                        pygame.draw.circle(DISPLAYSURF, BLUE, (500, 300), 80, 5)
                        turn = False
                        space_6 = False
                        space_6a = True
                    else:
                        pygame.draw.line(DISPLAYSURF, RED, (425, 225), (575, 375), 5)
                        pygame.draw.line(DISPLAYSURF, RED, (425, 375), (575, 225), 5)
                        turn = True
                        space_6 = False
                        space_6b = True

            if mousex in range(0, 200):
                if mousey in range(401, 600):
                    if turn == True:
                        pygame.draw.circle(DISPLAYSURF, BLUE, (100, 500), 80, 5)
                        turn = False
                        space_1 = False
                        space_1a = True
                    else:
                        pygame.draw.line(DISPLAYSURF, RED, (25, 425), (175, 575), 5)
                        pygame.draw.line(DISPLAYSURF, RED, (25, 575), (175, 425), 5)
                        turn = True
                        space_1 = False
                        space_1b = True

            if mousex in range(201, 400):
                if mousey in range(401, 600):
                    if turn == True:
                        pygame.draw.circle(DISPLAYSURF, BLUE, (300, 500), 80, 5)
                        turn = False
                        space_2 = False
                        space_2a = True
                    else:
                        pygame.draw.line(DISPLAYSURF, RED, (225, 425), (375, 575), 5)
                        pygame.draw.line(DISPLAYSURF, RED, (225, 575), (375, 425), 5)
                        turn = True
                        space_2 = False
                        space_2b = True

            if mousex in range(401, 600):
                if mousey in range(401, 600):
                    if turn == True:
                        pygame.draw.circle(DISPLAYSURF, BLUE, (500, 500), 80, 5)
                        turn = False
                        space_3 = False
                        space_3a = True
                    else:
                        pygame.draw.line(DISPLAYSURF, RED, (425, 425), (575, 575), 5)
                        pygame.draw.line(DISPLAYSURF, RED, (425, 575), (575, 425), 5)
                        turn = True
                        space_3 = False
                        space_3b = True

                    
        
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_KP7 and space_7 == True:
                if turn == True:
                    pygame.draw.circle(DISPLAYSURF, BLUE, (100, 100), 80, 5)
                    turn = False
                    space_7 = False
                    space_7a = True
                else:
                    pygame.draw.line(DISPLAYSURF, RED, (25, 25), (175, 175), 5)
                    pygame.draw.line(DISPLAYSURF, RED, (25, 175), (175, 25), 5)
                    turn = True
                    space_7 = False
                    space_7b = True


            if event.key == K_KP8 and space_8 == True:
                if turn == True:
                    pygame.draw.circle(DISPLAYSURF, BLUE, (300, 100), 80, 5)
                    turn = False
                    space_8 = False
                    space_8a = True
                else:
                    pygame.draw.line(DISPLAYSURF, RED, (225, 25), (375, 175), 5)
                    pygame.draw.line(DISPLAYSURF, RED, (225, 175), (375, 25), 5)
                    turn = True
                    space_8 = False
                    space_8b = True


            if event.key == K_KP9 and space_9 == True:
                if turn == True:
                    pygame.draw.circle(DISPLAYSURF, BLUE, (500, 100), 80, 5)
                    turn = False
                    space_9 = False
                    space_9a = True
                else:
                    pygame.draw.line(DISPLAYSURF, RED, (425, 25), (575, 175), 5)
                    pygame.draw.line(DISPLAYSURF, RED, (425, 175), (575, 25), 5)
                    turn = True
                    space_9 = False
                    space_9b = True


            if event.key == K_KP4 and space_4 == True:
                if turn == True:
                    pygame.draw.circle(DISPLAYSURF, BLUE, (100, 300), 80, 5)
                    turn = False
                    space_4 = False
                    space_4a = True
                else:
                    pygame.draw.line(DISPLAYSURF, RED, (25, 225), (175, 375), 5)
                    pygame.draw.line(DISPLAYSURF, RED, (25, 375), (175, 225), 5)
                    turn = True
                    space_4 = False
                    space_4b = True


            if event.key == K_KP5 and space_5 == True:
                if turn == True:
                    pygame.draw.circle(DISPLAYSURF, BLUE, (300, 300), 80, 5)
                    turn = False
                    space_5 = False
                    space_5a = True
                else:
                    pygame.draw.line(DISPLAYSURF, RED, (225, 225), (375, 375), 5)
                    pygame.draw.line(DISPLAYSURF, RED, (225, 375), (375, 225), 5)
                    turn = True
                    space_5 = False
                    space_5b = True


            if event.key == K_KP6 and space_6 == True:
                if turn == True:
                    pygame.draw.circle(DISPLAYSURF, BLUE, (500, 300), 80, 5)
                    turn = False
                    space_6 = False
                    space_6a = True
                else:
                    pygame.draw.line(DISPLAYSURF, RED, (425, 225), (575, 375), 5)
                    pygame.draw.line(DISPLAYSURF, RED, (425, 375), (575, 225), 5)
                    turn = True
                    space_6 = False
                    space_6b = True


            if event.key == K_KP1 and space_1 == True:
                if turn == True:
                    pygame.draw.circle(DISPLAYSURF, BLUE, (100, 500), 80, 5)
                    turn = False
                    space_1 = False
                    space_1a = True
                else:
                    pygame.draw.line(DISPLAYSURF, RED, (25, 425), (175, 575), 5)
                    pygame.draw.line(DISPLAYSURF, RED, (25, 575), (175, 425), 5)
                    turn = True
                    space_1 = False
                    space_1b = True


            if event.key == K_KP2 and space_2 == True:
                if turn == True:
                    pygame.draw.circle(DISPLAYSURF, BLUE, (300, 500), 80, 5)
                    turn = False
                    space_2 = False
                    space_2a = True
                else:
                    pygame.draw.line(DISPLAYSURF, RED, (225, 425), (375, 575), 5)
                    pygame.draw.line(DISPLAYSURF, RED, (225, 575), (375, 425), 5)
                    turn = True
                    space_2 = False
                    space_2b = True


            if event.key == K_KP3 and space_3 == True:
                if turn == True:
                    pygame.draw.circle(DISPLAYSURF, BLUE, (500, 500), 80, 5)
                    turn = False
                    space_3 = False
                    space_3a = True
                else:
                    pygame.draw.line(DISPLAYSURF, RED, (425, 425), (575, 575), 5)
                    pygame.draw.line(DISPLAYSURF, RED, (425, 575), (575, 425), 5)
                    turn = True
                    space_3 = False
                    space_3b = True

                    
        if space_7a == True and space_8a == True and space_9a == True:
            pygame.draw.line(DISPLAYSURF, GREEN, (25, 100), (575, 100), 7)
            if gameOver == False:
                print('Player 1 has won the game')
                gameOver = True

        if space_4a == True and space_5a == True and space_6a == True:
            pygame.draw.line(DISPLAYSURF, GREEN, (25, 300), (575, 300), 7)
            if gameOver == False:
                print('Player 1 has won the game')
                gameOver = True

        if space_1a == True and space_2a == True and space_3a == True:
            pygame.draw.line(DISPLAYSURF, GREEN, (25, 500), (575, 500), 7)
            if gameOver == False:
                print('Player 1 has won the game')
                gameOver = True

        if space_7a == True and space_4a == True and space_1a == True:
            pygame.draw.line(DISPLAYSURF, GREEN, (100, 25), (100, 575), 7)
            if gameOver == False:
                print('Player 1 has won the game')
                gameOver = True

        if space_8a == True and space_5a == True and space_2a == True:
            pygame.draw.line(DISPLAYSURF, GREEN, (300, 25), (300, 575), 7)
            if gameOver == False:
                print('Player 1 has won the game')
                gameOver = True

        if space_9a == True and space_6a == True and space_3a == True:
            pygame.draw.line(DISPLAYSURF, GREEN, (500, 25), (500, 575), 7)
            if gameOver == False:
                print('Player 1 has won the game')
                gameOver = True

        if space_7a == True and space_5a == True and space_3a == True:
            pygame.draw.line(DISPLAYSURF, GREEN, (25, 25), (575, 575), 7)
            if gameOver == False:
                print('Player 1 has won the game')
                gameOver = True

        if space_1a == True and space_5a == True and space_9a == True:
            pygame.draw.line(DISPLAYSURF, GREEN, (575, 25), (25, 575), 7)
            if gameOver == False:
                print('Player 1 has won the game')
                gameOver = True



        if space_7b == True and space_8b == True and space_9b == True:
            pygame.draw.line(DISPLAYSURF, GREEN, (25, 100), (575, 100), 7)
            if gameOver == False:
                print('Player 2 has won the game')
                gameOver = True

        if space_4b == True and space_5b == True and space_6b == True:
            pygame.draw.line(DISPLAYSURF, GREEN, (25, 300), (575, 300), 7)
            if gameOver == False:
                print('Player 2 has won the game')
                gameOver = True

        if space_1b == True and space_2b == True and space_3b == True:
            pygame.draw.line(DISPLAYSURF, GREEN, (25, 500), (575, 500), 7)
            if gameOver == False:
                print('Player 2 has won the game')
                gameOver = True

        if space_7b == True and space_4b == True and space_1b == True:
            pygame.draw.line(DISPLAYSURF, GREEN, (100, 25), (100, 575), 7)
            if gameOver == False:
                print('Player 2 has won the game')
                gameOver = True

        if space_8b == True and space_5b == True and space_2b == True:
            pygame.draw.line(DISPLAYSURF, GREEN, (300, 25), (300, 575), 7)
            if gameOver == False:
                print('Player 2 has won the game')
                gameOver = True

        if space_9b == True and space_6b == True and space_3b == True:
            pygame.draw.line(DISPLAYSURF, GREEN, (500, 25), (500, 575), 7)
            if gameOver == False:
                print('Player 2 has won the game')
                gameOver = True

        if space_7b == True and space_5b == True and space_3b == True:
            pygame.draw.line(DISPLAYSURF, GREEN, (25, 25), (575, 575), 7)
            if gameOver == False:
                print('Player 2 has won the game')
                gameOver = True

        if space_1b == True and space_5b == True and space_9b == True:
            pygame.draw.line(DISPLAYSURF, GREEN, (575, 25), (25, 575), 7)
            if gameOver == False:
                print('Player 2 has won the game')
                gameOver = True




    pygame.display.update()
