import pygame
import GraphicsUtil as Graph
from GraphicsUtil import *

deathVar = 0
x = 40
y = 300
vy = 0
center = (x,y)
img = Graph.someLoadedImage
img2 = Graph.mongooseImage
img3 = Graph.flagImage
btnWidth = 150
btnHeight = 50
btnX = 50
btnY = 225
btnWidth1 = 150
btnHeight1 = 50
btnX1 = 950
btnY1 = 225
btnX2 = 1000
btnY2 = 100

state = 'Main Menu'



class Hero:
    def __init__(self):
        self.x = 40
        self.y = 300
        self.img = Graph.someLoadedImage
        self.jump = False
        self.vy = 0

    def getPos(self):
        rect = self.img.get_rect()
        return (self.x , self.y , self.x + rect.w, self.y + rect.h)

    def update(self):
        global deathVar
        global vy
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
            self.x,self.y = 40, 300
            deathVar += 1
        if not self.villainDeath:
            pass
        else:
            self.x, self.y = 40,300
            deathVar += 1


       
        #Falling to death
        if hero.y >= 500:
            hero.x, hero.y = 40, 300
            deathVar += 1

        #Lvl End
        if not self.getEnd:
            pass
        else:
            self.x, self.y = 40, 300

 
        
hero = Hero()

pressUp = False
pressLeft = False
pressRight = False
pressSpace = False

platformList = []
villainList = []
flagList = []
spikeList = []
invisList = []
colList = []
def createGame(grid):
    for i in range(len(grid)):
        for j in range(len(levelList.grid[i])):
            if levelList.grid[i][j] == 'P':
                lvl = Graph.Platform(BLUE, j*40, i*50, 40, 50)
                platformList.append(lvl)
            if levelList.grid[i][j] == 'I':
                other = Graph.invisiblePlatform(BLACK,j*40, i*50, 120, 50)
                invisList.append(other)
            if levelList.grid[i][j] == 'E':
                lvl2 = Graph.Villain(j*40,i*50)
                villainList.append(lvl2)
            if levelList.grid[i][j] == 'G':
                lvl3 = Graph.Flag(j*40,i*50)
                flagList.append(lvl3)
            if levelList.grid[i][j] == 'S':
                lvl4 = Graph.Spike(j*40,i*50)
                spikeList.append(lvl4)
            # if levelList.grid[i][j] == 'Y':
            #     lvl5 = Graph.Col(j*40, i*50, BLACK,40, 130)
            #     colList.append(lvl5)


            


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
        hero.death = spike.checkCollision(hero)
        if hero.death:
            break
    for villain in villainList:
        hero.villainDeath = villain.checkCollision(hero)
        if hero.death:
            break
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
        text1 = font.render ("Start Game", True, (255,0,0))
        screen.blit(text1,(59,238))
        text2 = font.render ("Exit", True, (255,0,0))
        screen.blit(text2, (1000, 238))
        text3 = font.render("Easy",True,(255,0,0))
        screen.blit(text3,(1000,100))
        startG = pygame.draw.rect(screen, Graph.WHITE, ((btnX,btnY), (btnWidth,btnHeight)),1)
        endG = pygame.draw.rect(screen, Graph.WHITE, ((btnX1,btnY1), (btnWidth1, btnHeight1)),1)
        # easyG = pygame.draw.rect(screen,Graph.WHITE,)



    elif state == 'level1':
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
        for col in colList:
            col.draw(screen)

    
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
        for col in colList:
            col.draw(screen)