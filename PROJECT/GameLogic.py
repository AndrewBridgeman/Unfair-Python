import pygame
import GraphicsUtil as Graph


x = 20
y = 360
img = Graph.heroSprite
Fl = Graph.Fl
x1 = 0
y1 = 200

pressUp = False
pressLeft = False
pressRight = False
pressSpace = False




# update the game
def updateGame():
	# if you want to assign a global variable in Python, you need to let Python know
    global x, y
    if y + 40 <= 400:
        x += 0
        y += 1.5


# A method that does all the drawing for you.
def draw(screen):
    # setup a differnt background, 
    screen.fill(Graph.GREY)
    # copy the image of hero to the screen at the cordinate of hero
    screen.blit(img, (x, y))
    screen.blit(Fl, (x1,y1))
    screen.blit(Graph.test, (275,360))

#def jump(#Need work, idk stuff)
#    pass
    
