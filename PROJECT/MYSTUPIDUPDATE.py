#--------------------------
#Initialize pygame
#--------------------------
import pygame
from pygame.locals import *
#Actually initialize pygame
pygame.init()

#Initialize the clock for the game, get that 60fps
clock = pygame.time.Clock()

#Make a screen of 500x500 resolution
screen = pygame.display.set_mode((500,500))

#Make the game have the ability to be pressed and held
pygame.key.set_repeat(50,50)

#Get GameLogic in here
import GameLogic
#If you need GraphicsUtil, call as GameLogic.Graph

while True:
#Use all events received by pygame
    eventList = pygame.event.get()
    isFalling = True
    for event in eventList:
        print(event)
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: # Still need to make a tru jumping function, more than likely in GameLogic
                GameLogic.y -= 10
            elif event.key == pygame.K_LEFT:
                GameLogic.x -= 10
            elif event.key == pygame.K_RIGHT:
                GameLogic.x += 10




#Dont need, as we have no want for passively continued mvmt
        
    GameLogic.updateGame()
    GameLogic.draw(screen)

    pygame.display.flip()

    clock.tick(60)

