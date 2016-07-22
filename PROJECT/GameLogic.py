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
# Fl = Graph.Fl

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
        #Landing Function
        if not self.land:
            self.y += self.vy
            self.vy += 0.5
            self.jump = False
        else:
            if self.jump:
                self.vy = -10
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

        if not self.villianDeath:
            pass
        else:
            self.x, self.y = 40,300
            deathVar += 1

        #Falling to death
        if hero.y >= 500:
            hero.x, hero.y = 40, 300
            deathVar += 1
        
hero = Hero()

pressUp = False
pressLeft = False
pressRight = False
pressSpace = False


platformList = []
villainList = []
flagList = []
spikeList = []
for i in range(len(levelList.level1)):
    for j in range(len(levelList.level1[i])):
        if levelList.level1[i][j] == 'P':
            lvl = Graph.Platform(BLACK, j*40, i*50, 200, 40)
            platformList.append(lvl)
        if levelList.level1[i][j] == 'I':
            other = Graph.Platform(BLUE, j*40, i*50, 40, 40, True)
            platformList.append(other)


        if levelList.level1[i][j] == 'E':
            lvl2 = Graph.Villain(j*40,i*50)
            villainList.append(lvl2)
        if levelList.level1[i][j] == 'G':
            lvl3 = Graph.Flag(j*40,i*50)
            flagList.append(lvl3)
        if levelList.level1[i][j] == 'S':
            lvl4 = Graph.Spike(j*40,i*50)
            spikeList.append(lvl4)
        


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
        hero.villianDeath = villain.checkCollision(hero)
        if hero.death:
            break
    hero.update()

# A method that does all the drawing for you.
def draw(screen):
    global deathVar
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


isBetween = True



class death:
    pass



    deathVar += 1
# def death(someLoadedImage, mongooseImage):
#     for snake, mongoose in [(someLoadedImage, mongooseImage), (mongooseImage, hero)]:
#             if ((isPointInsideRect(snake.left, snake.top, mongooseImage)) or
#                (isPointInsideRect(snake.left, snake.bottom, mongooseImage)) or
#                (isPointInsideRect(snake.right, snake.top, mongooseImage)) or
#               (isPointInsideRect(snake.right, snake.bottom, mongooseImage))):
#               print ("True")
#             else:
#                 print ("False")


