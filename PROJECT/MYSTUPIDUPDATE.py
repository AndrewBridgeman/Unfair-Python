import pygame
from pygame.locals import *
import GameLogic

#import GraphicsUtil 
#--Needs ball.png fix, id say to just comment your location of ball.png underneath so we all can run this and just sub in your path

#import GameLogic
#--CallsGraphicsUtil in, still has same problem

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

while True:
#Use all events received by pygame
    eventList = pygame.event.get()

    for event in eventList:
        print(event)
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                GameLogic.y -= 10
            elif event.key == pygame.K_DOWN:
                GameLogic.y += 10
            elif event.key == pygame.K_LEFT:
                GameLogic.x -= 10
            elif event.key == pygame.K_RIGHT:
                GameLogic.x += 10
    GameLogic.updateGame()

    x = 20
    y = 280
    pygame.draw.circle(screen, RED, (x,y), 20)

    pygame.draw.rect(screen, RED, (0,300,500,100))
    pygame.display.flip()


