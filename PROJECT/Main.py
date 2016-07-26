#--------------------------
#Initialize pygame
#--------------------------
import pygame
from pygame.locals import *
#Actually initialize pygame
pygame.init()

#Initialize the clock for the game, get that 60fps
clock = pygame.time.Clock()

#Make a screen of 1200x500 resolution
 
screen = pygame.display.set_mode((1200,500))

#Make the game have the ability to be pressed and held
pygame.key.set_repeat(50,50)

#Get GameLogic in here
import GameLogic
#If you need GraphicsUtil, call as GameLogic.hero.Graph
        
# pygame.mixer.music.load("Epic.mp3")
# pygame.mixer.music.play(-1,0.0)

while True:
#Use all events received by pygameB
    eventList = pygame.event.get()

    
    for event in eventList:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: 
                GameLogic.hero.jump = True
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
                if GameLogic.hero.x <= 1130 and GameLogic.hero.y != 0:
                    GameLogic.hero.x += 10
                    GameLogic.pressRight = True
                if GameLogic.hero.x > 1130 and GameLogic.hero.y != 0:
                    GameLogic.pressRight = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP: 
                GameLogic.pressUp = False
            elif event.key == pygame.K_LEFT:
                GameLogic.pressLeft = False
            elif event.key == pygame.K_RIGHT:
                GameLogic.pressRight = False 
            elif event.key == pygame.K_SPACE:
                GameLogic.pressSpace = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if GameLogic.state == 'Main Menu':
                if event.pos[0] >= GameLogic.btnX and event.pos[0] <= GameLogic.btnX + GameLogic.btnWidth and event.pos[1] >= GameLogic.btnY and event.pos[1] <= GameLogic.btnY + GameLogic.btnHeight:
                    GameLogic.state = 'Start'
                    GameLogic.createGame(GameLogic.levelList.level1)
                if event.pos[0] >= GameLogic.btnX1 and event.pos[0] <= GameLogic.btnX1 + GameLogic.btnWidth1 and event.pos[1] >= GameLogic.btnY1 and event.pos[1] <= GameLogic.btnY1 + GameLogic.btnHeight1:
                    exit()
                if event.pos[0]>=GameLogic.btnX2 and event.pos[0]<=GameLogic.btnX2 + GameLogic.btnWidth1 and event.pos[1] >=GameLogic.btnY2 and event.pos[1]<=GameLogic.btnY2+ GameLogic.btnHeight1:
                    GameLogic.state = 'Easy'
                    GameLogic.createGame(GameLogic.levelList.easylevel)
        if GameLogic.pressUp == True and GameLogic.pressRight == True:
                # if GameLogic.hero.y >= 360:
                #     GameLogic.hero.y -= 50
                if GameLogic.hero.x >= 0:
                    GameLogic.hero.x += 0
                GameLogic.pressUp = True
                GameLogic.pressRight = True

        if GameLogic.pressUp == True and GameLogic.pressLeft == True:
                # if GameLogic.hero.y>=360:
                #     GameLogic.hero.y -= 50
                if GameLogic.hero.x>=0:
                    GameLogic.hero.x -= 1
                GameLogic.pressUp=True
                GameLogic.pressLeft = True
    if GameLogic.hero.getEnd:
        pygame.time.wait(500)
        GameLogic.createGame(GameLogic.levelList.level2)
        print('Really work plz')




        
    GameLogic.updateGame()
    GameLogic.draw(screen)

    pygame.display.flip()

    clock.tick(20)