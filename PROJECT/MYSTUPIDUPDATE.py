import pygame
from pygame.locals import *
#Initialize pygame & clock
pygame.init()
clock = pygame.time.Clock()

#Make a screen
screen = pygame.display.set_mode((500,500))

#Define COLORS
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#Use all events received by pygame
eventList = pygame.event.get()

for event in eventList:
    print(event)
    if event.type == pygame.QUIT:
        exit()


pygame.draw.circle(screen, RED, (20,20), 20)
pygame.display.flip()




