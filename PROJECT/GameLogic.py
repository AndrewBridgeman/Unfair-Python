import pygame
import GraphicsUtil as Graph
from GraphicsUtil import *

deathVar = 0
img = Graph.someLoadedImage
img2 = Graph.mongooseImage
img3 = Graph.flagImage
btnWidth = 150
btnHeight = 50
btnX = 51
btnY = 141
btnWidth1 = 150
btnHeight1 = 50
btnX1 = 950
btnY1 = 225
btnX2 = 48
btnY2 = 340

state = 'Main Menu'



class Hero:
    def __init__(self,x,y,grid):
        self.x = x
        self.y = y
        self.img = Graph.someLoadedImage
        self.jump = False
        self.vy = 0
        self.getEnd = False
        self.spikeDeath = False
        self.grid = grid
    def getPos(self):
        rect = self.img.get_rect()
        return (self.x , self.y , self.x + rect.w, self.y + rect.h)

    def update(self):
        global deathVar
        global vy
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 'H':
                    startx, starty = j*40,i*50
        #Landing Function

        if not self.land:
            self.y += self.vy
            self.vy += 1.0 #gravity
            self.jump = False
        else:
            if self.jump:
                self.vy = -15
                self.y -= 10
                self.land = False
            else:
                self.vy = 0

        #Death Function
        if not self.death:
            pass
        else:
            self.x,self.y = startx, starty
            deathVar += 1
        if not self.villainDeath:
            pass
        else:
            self.x,self.y = startx, starty
            deathVar += 1

        #Falling to death
        if hero.y >= 500:
            self.x,self.y = startx, starty
            deathVar += 1

        if not self.spikeDeath:
            pass
        else:
            self.x,self.y = startx,starty
            deathVar += 1

 
        
hero = Hero(0,0,levelList.level1)

pressUp = False
pressLeft = False
pressRight = False
pressSpace = False

platformList = []
villainList = []
flagList = []
spikeList = []
invisList = []
spawnList = []
def createGame(grid):
    global x, y, vy, deathVar, hero
    platformList.clear()
    villainList.clear()
    flagList.clear()
    spikeList.clear()
    invisList.clear()
    spawnList.clear()
    deathVar = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'P':
                lvl = Graph.Platform(BLUE, j*40, i*50, 40, 50)
                platformList.append(lvl)
            if grid[i][j] == 'I':
                other = Graph.invisiblePlatform(BLACK,j*40, i*50, 120, 50)
                invisList.append(other)
            if grid[i][j] == 'E':
                lvl2 = Graph.Villain(j*40,i*50)
                villainList.append(lvl2)
            if grid[i][j] == 'G': # Make cleaner and better ex. hero
                lvl3 = Graph.Flag(j*40,i*50)
                flagList.append(lvl3)
            if grid[i][j] == 'S':
                lvl4 = Graph.Spike(j*40,i*50)
                spikeList.append(lvl4)
            if grid[i][j] == 'H':
                hero = Hero(j*40,i*50,grid)
                
                

            # if grid[i][j] == 'Y':
            #     lvl5 = Graph.Col(j*40, i*50, BLACK,40, 130)
            #     colList.append(lvl5)

            


# def mMenu():
#     global screen
#     mainMenu = pygame.image.load('python.jpg')
#     mainMenu = pygame.transform.scale(mainMenu, (500,500))
#     mainMenu.set_colorkey(Graph.WHITE)
#     pygame.font.init()
#     screen.blit(mainMenu, (350,0))
#     font = pygame.font.Font(None, 36)
#     text1 = font.render ("Start Game", True, (255,0,0))
#     screen.blit(text1,(59,150))
#     text2 = font.render ("Exit", True, (255,0,0))
#     screen.blit(text2, (1000, 238))
#     text3 = font.render("Easy Mode",True,(255,0,0))
#     screen.blit(text3,(59,350))
#     startG = pygame.draw.rect(screen, Graph.WHITE, ((btnX,btnY), (btnWidth,btnHeight)),1)
#     endG = pygame.draw.rect(screen, Graph.WHITE, ((btnX1,btnY1), (btnWidth1, btnHeight1)),1)
#     middleG = pygame.draw.rect(screen,Graph.WHITE,((btnX2,btnY2),(btnWidth1,bthHeight1)),1)
# update the game
def updateGame():
    global deathVar
	# if you want to assign a global variable in Python, you need to let Python know
    hero.land = False
    for platform in platformList:
        hero.land = platform.checkCollision(hero)
        if hero.land:
            break
    hero.death = False
    for spike in spikeList:
        hero.spikeDeath = spike.checkCollision(hero)
        if hero.spikeDeath:
            break
    hero.villainDeath = False
    for villain in villainList:
        hero.villainDeath = villain.checkCollision(hero)
        if hero.villainDeath:
            break
    hero.getEnd = False
    for flag in flagList:
        hero.getEnd = flag.checkCollision(hero)
        if hero.death:
            break
    hero.update()



    

# A method that does all the drawing for you.
def draw(screen):
    global deathVar

    if state == 'Main Menu':
        mainMenu = pygame.image.load('python.jpg')
        mainMenu = pygame.transform.scale(mainMenu, (500,500))
        mainMenu.set_colorkey(Graph.WHITE)
        pygame.font.init()
        screen.blit(mainMenu, (350,0))
        font = pygame.font.Font(None, 36)
        fontSmall = pygame.font.Font(None, 16)
        text1 = font.render ("Start Game", True, (255,0,0))
        screen.blit(text1,(59,150))
        text2 = font.render ("Exit", True, (255,0,0))
        screen.blit(text2, (1000, 238))
        text3 = font.render("Easy Mode",True,(255,0,0))
        screen.blit(text3,(59,350))
        textD = fontSmall.render('(Demo)',True,(255,0,0))
        screen.blit(textD,(100,375))
        startG = pygame.draw.rect(screen, Graph.WHITE, ((btnX,btnY), (btnWidth,btnHeight)),1)
        endG = pygame.draw.rect(screen, Graph.WHITE, ((btnX1,btnY1), (btnWidth1, btnHeight1)),1)

        middleG = pygame.draw.rect(screen,Graph.WHITE,((btnX2,btnY2),(btnWidth1,btnHeight1)),1)
    elif state == 'Start':
            #Background 
        background = pygame.image.load("jungle.jpg")
        backgroundTop = screen.get_height() - background.get_height()
        backgroundLeft = screen.get_width()/2 - background.get_width()/2

        screen.blit(background, (backgroundLeft,backgroundTop))
            # # copy the image of hero to the screen at the cordinate of hero
        screen.blit(hero.img, (hero.x, hero.y))
            
            # Text
        pygame.font.init()
        font = pygame.font.Font(None,36)
        text = font.render ("Total Deaths: " + str(deathVar),True,(255,0,0))
        screen.blit(text,(1,1))

        for p in platformList:
            p.draw(screen)
        for spike in spikeList:
            spike.draw(screen)
        for flag in flagList:
            flag.draw(screen)        
        for villain in villainList:
            villain.draw(screen)
        for other in invisList:
            other.draw(screen)

    
    elif state == 'Easy':
            #Background 
        background = pygame.image.load("jungle.jpg")
        backgroundTop = screen.get_height() - background.get_height()
        backgroundLeft = screen.get_width()/2 - background.get_width()/2

        screen.blit(background, (backgroundLeft,backgroundTop))
            # # copy the image of hero to the screen at the cordinate of hero
        screen.blit(hero.img, (hero.x, hero.y))
            
            # Text
        pygame.font.init()
        font = pygame.font.Font(None,36)
        text = font.render ("Total Deaths: " + str(deathVar),True,(255,0,0))
        screen.blit(text,(1,1))

        for p in platformList:
            p.draw(screen)
        for spike in spikeList:
            spike.draw(screen)
        for flag in flagList:
            flag.draw(screen)        
        for villain in villainList:
            villain.draw(screen)
        for other in invisList:
            other.draw(screen)
        