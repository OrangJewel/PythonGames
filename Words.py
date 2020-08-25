import pygame, sys
from pygame.locals import *

pygame.init()
WINX = 700
WINY = 500
DISPLAYSURF = pygame.display.set_mode((WINX, WINY))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

fontObj = pygame.font.Font('freesansbold.ttf', 32)

BGCOLOR = WHITE

text = []

chanum = 0
shift = False
while True:
    DISPLAYSURF.fill(BGCOLOR)
    
    show = ''.join(text)
    textSurfaceObj = fontObj.render(show, True, BLACK, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.topleft = (25, 25)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYUP:

            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            
##            if event.key == K_q:
##                text.append('q')
##                chanum += 1
##                print(text)
##            if event.key == K_w:
##                text.append('w')
##                chanum += 1
##                print(text)
##            if event.key == K_e:
##                text.append('e')
##                chanum += 1
##                print(text)
##            if event.key == K_r:
##                text.append('r')
##                chanum += 1
##                print(text)
##            if event.key == K_t:
##                text.append('t')
##                chanum += 1
##                print(text)
##            if event.key == K_y:
##                text.append('y')
##                chanum += 1
##                print(text)
##            if event.key == K_u:
##                text.append('u')
##                chanum += 1
##                print(text)
##            if event.key == K_i:
##                text.append('i')
##                chanum += 1
##                print(text)
##            if event.key == K_o:
##                text.append('o')
##                chanum += 1
##                print(text)
##            if event.key == K_p:
##                text.append('p')
##                chanum += 1
##                print(text)
##            if event.key == K_a:
##                text.append('a')
##                chanum += 1
##                print(text)
##            if event.key == K_s:
##                text.append('s')
##                chanum += 1
##                print(text)
##            if event.key == K_d:
##                text.append('d')
##                chanum += 1
##                print(text)
##            if event.key == K_f:
##                text.append('f')
##                chanum += 1
##                print(text)
##            if event.key == K_g:
##                text.append('g')
##                chanum += 1
##                print(text)
##            if event.key == K_h:
##                text.append('h')
##                chanum += 1
##                print(text)
##            if event.key == K_j:
##                text.append('j')
##                chanum += 1
##                print(text)
##            if event.key == K_k:
##                text.append('k')
##                chanum += 1
##                print(text)
##            if event.key == K_l:
##                text.append('l')
##                chanum += 1
##                print(text)
##            if event.key == K_z:
##                text.append('z')
##                chanum += 1
##                print(text)
##            if event.key == K_x:
##                text.append('x')
##                chanum += 1
##                print(text)
##            if event.key == K_c:
##                text.append('c')
##                chanum += 1
##                print(text)
##            if event.key == K_v:
##                text.append('v')
##                chanum += 1
##                print(text)
##            if event.key == K_b:
##                text.append('b')
##                chanum += 1
##                print(text)
##            if event.key == K_n:
##                text.append('n')
##                chanum += 1
##                print(text)
##            if event.key == K_m:
##                text.append('m')
##                chanum += 1
##                print(text)
            if event.key == K_SPACE:
                text.append(' ')
                chanum += 1
                print(text)
            if event.key == K_COMMA:
                text.append(',')
                chanum += 1
                print(text)
            if event.key == K_PERIOD:
                text.append('.')
                chanum += 1
                print(text)
                
            if event.key == K_KP0 or event.key == K_0 and chanum >= 1:
                text.pop(0)
                chanum -= 1
                print(text)
            if event.key == K_KP1 or event.key == K_1 and chanum >= 2:
                text.pop(1)
                chanum -= 1
                print(text)
            if event.key == K_KP2 or event.key == K_2 and chanum >= 3:
                text.pop(2)
                chanum -= 1
                print(text)
            if event.key == K_KP3 or event.key == K_3 and chanum >= 4:
                text.pop(3)
                chanum -= 1
                print(text)
            if event.key == K_KP4 or event.key == K_4 and chanum >= 5:
                text.pop(4)
                chanum -= 1
                print(text)
            if event.key == K_KP5 or event.key == K_5 and chanum >= 6:
                text.pop(5)
                chanum -= 1
                print(text)
            if event.key == K_KP6 or event.key == K_6 and chanum >= 7:
                text.pop(6)
                chanum -= 1
                print(text)
            if event.key == K_KP7 or event.key == K_7 and chanum >= 8:
                text.pop(7)
                chanum -= 1
                print(text)
            if event.key == K_KP8 or event.key == K_8 and chanum >= 9:
                text.pop(8)
                chanum -= 1
                print(text)                
            if event.key == K_KP9 or event.key == K_9 and chanum >= 10:
                text.pop(9)
                chanum -= 1
                print(text)
            if event.key == K_BACKSPACE and chanum >= 1:
                text.pop(chanum - 1)
                chanum -= 1
                print(text)
            if event.key == K_RETURN:
                text.append('\n')
                chanum += 1

        if event.type == KEYDOWN:
            press = pygame.key.get_pressed()
            for i in xrange( pygame.K_a, pygame.K_z + 1 ): 
                    if press[i] == True:
                        name = pygame.key.name(i)
                        text.append(name)
                        chanum += 1
                        print(text)
            
    pygame.display.update()
