import pygame
import GraphicsUtil as Graph
from GraphicsUtil import *

x = 40
y = 300
vy = 0
center = (x,y)
img = Graph.someLoadedImage
# Fl = Graph.Fl

pressUp = False
pressLeft = False
pressRight = False
pressSpace = False


platformList = []
for i in range(len(levelList.level1)):
    for j in range(len(levelList.level1[i])):
        if levelList.level1[i][j] == 'P':
            lvl = Graph.Platform(BLACK, j*40, i*50, 40, 40)
            platformList.append(lvl)
        if levelList.level1[i][j] == 'I':
            other = Graph.Platform(BLUE, j*40, i*50, 40, 40, True)
            platformList.append(other)


# update the game
def updateGame():
	# if you want to assign a global variable in Python, you need to let Python know
    global vy, y, x
    # if you want to assign a global variable in Python, you need to let Python know
    heroGrid = (x//40, y//50)
    for platform in platformList:
        # #####print(platform.gridX, platform.gridY)
        if (heroGrid[0]+2 > platform.gridX and heroGrid[0] < platform.gridX + platform.width) and heroGrid[1] > platform.gridY -2:
            vy = 0
            # if platform.Fall == True:
            #     print("fall")
            #     y += 10
        # print(platform.gridX, platform.gridY - 1)
    y += vy
    vy += 0.5
	
# A method that does all the drawing for you.
def draw(screen):
        #Background 
    background = pygame.image.load("jungle.jpg")
    backgroundTop = screen.get_height() - background.get_height()
    backgroundLeft = screen.get_width()/2 - background.get_width()/2

    screen.blit(background, (backgroundLeft,backgroundTop))
    # # copy the image of hero to the screen at the cordinate of hero
    screen.blit(img, (x, y))

    for p in platformList:
        p.draw(screen)

isBetween = True

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