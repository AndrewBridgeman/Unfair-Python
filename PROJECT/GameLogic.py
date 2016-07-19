import pygame
import GraphicsUtil as Graph
from GraphicsUtil import *

x = 20
y = 300
vy = 0
center = (x,y)
img = Graph.someLoadedImage
# Fl = Graph.Fl


pressUp = False
pressLeft = False
pressRight = False
pressSpace = False


# update the game
def updateGame():
	# if you want to assign a global variable in Python, you need to let Python know
    global vy, y
    vy += 0.5
    y += vy

# A method that does all the drawing for you.
def draw(screen):
        #Background 
    background = pygame.image.load("/Users/BrionnaSlaughter1/Desktop/Python Programming/Python/Unfair-Python/PROJECT/jungle.jpg")
    backgroundTop = screen.get_height() - background.get_height()
    backgroundLeft = screen.get_width()/2 - background.get_width()/2

    screen.blit(background, (backgroundLeft,backgroundTop))
    # # copy the image of hero to the screen at the cordinate of hero
    screen.blit(img, (x, y))
    # screen.blit(Fl, (0,200))

    for i in range(len(levelList.level1)):
        for j in range(len(levelList.level1[i])):
            if levelList.level1[i][j] == 'P':
                pygame.draw.rect(screen, WHITE, (j*40, i*50, 40,30))

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