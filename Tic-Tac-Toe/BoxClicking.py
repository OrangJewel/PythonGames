import pygame, sys
from pygame.locals *

WINDOWWIDTH = 600
WINDOWHEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

RED = (255, 0, 0)
WHITE = (248, 248, 242)
BLACK = (39, 40, 34)


mousex = 0
mousey = 0

def main()
    DISPLAYSURF.fill(BLACK)
    surface_2 = pygame.Surface((400, 400), pygame.SRCALPHA)
    pygame.draw.rect(surface_2, WHITE, surface_2.get_rect(), 10)
    DISPLAYSURF.blit(surface_2, (300, 300))
    while True:
        mouseClicked = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
        boxx, boxy = getBoxAtPixel
        pygame.display.update()
                
