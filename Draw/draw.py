import pygame, sys
from pygame.locals import *

pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Drawing')

# set up the colors
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
BEIGE = (245, 245, 220)
SBLUE = ( 0, 0, 255, 50)
SBEIGE = (245, 245, 220, 0)

#draw on the surface object
DISPLAYSURF.fill(BEIGE)
pygame.draw.polygon(DISPLAYSURF, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106), (90, 90)))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)
pygame.draw.circle(DISPLAYSURF, SBLUE, (146, 149), 20, 0)
pygame.draw.circle(DISPLAYSURF, SBEIGE, (146, 149), 8, 0)
pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)
pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))

# draw a semi-transparent shape
blue_image = pygame.Surface((50, 50), pygame.SRCALPHA)
#pygame.draw.rect(blue_image, SBLUE, blue_image.get_rect(), 10)
pygame.draw.circle(blue_image, SBLUE, (25, 25), 27, 0)
DISPLAYSURF.blit(blue_image, (75, 175))

pix0bj = pygame.PixelArray(DISPLAYSURF)
pix0bj[480][380] = BLACK
pix0bj[482][382] = BLACK
pix0bj[484][384] = BLACK
pix0bj[486][386] = BLACK
pix0bj[488][388] = BLACK
del pix0bj

#run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
