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
screen = pygame.display.set_mode((1200,500))

#Make the game have the ability to be pressed and held
pygame.key.set_repeat(50,50)

#Get GameLogic in here
import GameLogic
#If you need GraphicsUtil, call as GameLogic.hero.Graph

while True:
#Use all events received by pygame
    eventList = pygame.event.get()
    
    for event in eventList:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: # Still need to make a tru jumping function, more than likely in GameLogic
<<<<<<< Updated upstream
                # if GameLogic.hero.y >= 260: #Changed from 360 for testing
                #     GameLogic.hero.y -= 100 # Can continue jumping to fix fall, need that fixed
=======
                # if GameLogic.y >= 260: #Changed from 360 for testing
                #     GameLogic.y -= 100 # Can continue jumping to fix fall, need that fixed
>>>>>>> Stashed changes
                #doesnt like to jump with nothing already, print says it goes through, but no reaction
                GameLogic.jump()
                GameLogic.pressUp = True
            elif event.key == pygame.K_DOWN:
                GameLogic.hero.y += 5
            elif event.key == pygame.K_LEFT:
                if GameLogic.hero.x >= 5 and GameLogic.hero.y != 0:
                    GameLogic.hero.x -= 10
                    GameLogic.pressLeft = True
                if GameLogic.hero.x <= 5 and GameLogic.hero.y != 0:
                    GameLogic.pressLeft = False
                if GameLogic.hero.x <=5 and GameLogic.hero.y!=0:
                    GameLogic.pressLeft = False
            elif event.key == pygame.K_RIGHT:
                GameLogic.hero.x += 10
                GameLogic.pressRight = True
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
                if GameLogic.hero.y >= 360:
                    GameLogic.hero.y -= 50
                if GameLogic.hero.x >= 0:
                    GameLogic.hero.x += 20
                GameLogic.pressUp = True
                GameLogic.pressRight = True
                
        if GameLogic.pressUp == True and GameLogic.pressLeft == True:
                if GameLogic.hero.y>=360:
                    GameLogic.hero.y -= 50
                if GameLogic.hero.x>=0:
                    GameLogic.hero.x -= 20
                GameLogic.pressUp=True
                GameLogic.pressLeft = True


#Dont need, as we have no want for passively continued mvmt
        
    GameLogic.updateGame()
    GameLogic.draw(screen)

    pygame.display.flip()

    clock.tick(60)