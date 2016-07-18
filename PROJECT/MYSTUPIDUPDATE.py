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
    
    for event in eventList:
        print(event)
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: # Still need to make a tru jumping function, more than likely in GameLogic
                if GameLogic.y >= 360:
                    GameLogic.y -= 100
                #GameLogic.jump()
                GameLogic.pressUp = True

            elif event.key == pygame.K_LEFT:
                if GameLogic.x >= 5 and GameLogic.y != 0:
                    GameLogic.x -= 10
                    GameLogic.pressLeft = True
                if GameLogic.x <= 5 and GameLogic.y != 0:
                    GameLogic.pressLeft = False
            elif event.key == pygame.K_RIGHT:
                GameLogic.x += 10
                GameLogic.pressRight = True
            elif event.key == pygame.K_SPACE:
                GameLogic.y -= 10
                GameLogic.pressUp = True
            elif event.key != pygame.K_SPACE:
                GameLogic.pressUp = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP: 
                GameLogic.pressUp = False
            elif event.key == pygame.K_LEFT:
                GameLogic.pressLeft = False
            elif event.key == pygame.K_RIGHT:
                GameLogic.pressRight = False 
            elif event.key == pygame.K_SPACE:
                GameLogic.pressSpace = False

        if GameLogic.pressUp == True and GameLogic.pressRight == True:
                if GameLogic.y>=360:
                    GameLogic.y -= 50
                if GameLogic.x>=0:
                    GameLogic.x += 20
                GameLogic.pressUp = True
                GameLogic.pressRight = True
                
        if GameLogic.pressUp == True and GameLogic.pressLeft == True:
                if GameLogic.y>=360:
                    GameLogic.y -= 50
                if GameLogic.x>=0:
                    GameLogic.x -= 20
                GameLogic.pressUp=True
                GameLogic.pressLeft = True


#Dont need, as we have no want for passively continued mvmt
        
    GameLogic.updateGame()
    GameLogic.draw(screen)

    pygame.display.flip()

    clock.tick(60)

