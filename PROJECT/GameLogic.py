import pygame
import GraphicsUtil as Graph
from GraphicsUtil import *

<<<<<<< Updated upstream
# x = 40
# y = 300
# vy = 0
# center = (x,y)
# img = Graph.someLoadedImage
=======
x = 40
y = 300
vy = 0
center = (x,y)
img = Graph.someLoadedImage
img2 = Graph.mongooseImage
img3 = Graph.flagImage
>>>>>>> Stashed changes
# Fl = Graph.Fl

class Hero:
    def __init__(self):
        self.x = 40
        self.y = 300
        self.img = Graph.someLoadedImage
        self.vy = 0

    def getPos(self):
        rect = self.img.get_rect()
        return (self.x , self.y , self.x + rect.w, self.y + rect.h)

    def update(self):
        if not self.land:
            self.y += self.vy
            self.vy += 0.5



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
<<<<<<< Updated upstream

def jump():
    if hero.land:
        hero.vy = -10
=======
        if levelList.level1[i][j] == 'E':
            lvl2 = Graph.Villain(j*40,i*50)
            villainList.append(lvl2)
        if levelList.level1[i][j] == 'G':
            lvl3 = Graph.Flag(j*40,i*50)
            flagList.append(lvl3)
        if levelList.level1[i][j] == 'S':
            lvl4 = Graph.Spike(j*40,i*50)
            spikeList.append(lvl4)
        
>>>>>>> Stashed changes

# update the game
def updateGame():
	# if you want to assign a global variable in Python, you need to let Python know
    hero.land = False
    for platform in platformList:
        hero.land = platform.checkCollision(hero)
        if hero.land:
            break
    print(hero.land)
    hero.update()

# A method that does all the drawing for you.
def draw(screen):
        #Background 
    background = pygame.image.load("jungle.jpg")
    backgroundTop = screen.get_height() - background.get_height()
    backgroundLeft = screen.get_width()/2 - background.get_width()/2

    screen.blit(background, (backgroundLeft,backgroundTop))
    # # copy the image of hero to the screen at the cordinate of hero
    screen.blit(hero.img, (hero.x, hero.y))

    screen.blit(Graph.deathSurface,(0,0))

    for p in platformList:
        p.draw(screen)
    for spike in spikeList:
        spike.draw(screen)
    for flag in flagList:
        flag.draw(screen)        
    for villain in villainList:
        villain.draw(screen)


isBetween = True

def death(someLoadedImage, mongooseImage):
    for snake, mongoose in [(someLoadedImage, mongooseImage), (mongooseImage, hero)]:
            if ((isPointInsideRect(snake.left, snake.top, mongooseImage)) or
               (isPointInsideRect(snake.left, snake.bottom, mongooseImage)) or
               (isPointInsideRect(snake.right, snake.top, mongooseImage)) or
              (isPointInsideRect(snake.right, snake.bottom, mongooseImage))):
              print ("True")
            else:
                print ("False")


# def Coll(): #Note, if you go under the platform at all, stops falling, need fix
#     global x,y
#     for a in range(len(Graph.rectList)):
#         if x >= Graph.rectList[a].getX() and x <= (Graph.rectList[a].getX() + Graph.rectList[a].width):
#             isBetween = True
            
#         else:
#             isBetween = False
            
#         if isBetween == True and y + 40 <= Graph.rectList[a].getY():
#             y += 1.5
#         if isBetween == False:
#             y += 1.5

#    if x >= Pl1.getX() and x <= (Pl1.getX() + Pl1.length):
#        isFalling = False