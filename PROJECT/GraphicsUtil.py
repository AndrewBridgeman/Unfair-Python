import pygame

#Define COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 153, 0)
GREEN = (0,255,0)
PURPLE = (255, 51, 153)
BLUE = (0, 0, 255)
GREY = (128,128,128)

<<<<<<< HEAD
Fl = pygame.Surface((450,40))
pygame.draw.rect(Fl, WHITE, (0,0,200,40))

Fl = pygame.Surface((500,150))
pygame.draw.rect(Fl, WHITE, (0,0,500,40))
pygame.draw.rect(Fl, BLUE, (200,5, 400, -50))
=======


heroSprite = pygame.Surface((40, 40))

pygame.draw.circle(heroSprite, RED, (20,20), 20)


Fl = pygame.Surface((500,400))
#pygame.draw.rect(Fl, BLUE, (250,0,200,40))

test = pygame.Surface((200,40))
pygame.draw.rect(test, BLUE, (0,0,200,40))



#pygame.draw.rect(Fl, WHITE, (0,0,200,40))



>>>>>>> origin/master


# set_colorkey(<COLOR>) configure <COLOR> to be transparent
<<<<<<< HEAD
=======
heroSprite.set_colorkey(BLACK)
Fl.set_colorkey(BLACK)
>>>>>>> origin/master

test = pygame.Surface ((200,40))

floor = pygame.Surface((200,100))
pygame.draw.rect(floor, WHITE, (0,400,200,50))

#Classes begin here
class Platform:
    def __init__(self, surface, color, pointx, pointy, width, length):
        self.width = width
        self.length = length
        self.x = pointx
        self.y = pointy
        self.color = color
        self.surface = surface
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def draw(self):
        pygame.draw.rect(self.surface, self.color, ((self.x, self.y), (self.width, self.length)))

Pl1 = Platform(Fl, WHITE, 0,200,200,40)
Pl1.draw()

Pl2 = Platform(Fl, WHITE, 300, 200, 200, 40)
Pl2.draw()

screen = pygame.display.set_mode((500,500))
#Floor Surface
Fl = pygame.Surface((500,150))
pygame.draw.rect(Fl, WHITE, (0,0,500,40))
pygame.draw.rect(Fl, BLUE, (200,5, 400, -50))

#Character Surface

background = pygame.Surface(screen.get_size())
background = background.convert()
background = ("/Users/BrionnaSlaughter1/Desktop/Python Programming/Python/Unfair-Python/PROJECT/game-background.jpg")


someLoadedImage = pygame.image.load("/Users/BrionnaSlaughter1/Desktop/Python Programming/Python/Unfair-Python/PROJECT/Snake.png")
someLoadedImage = pygame.transform.scale(someLoadedImage, (60, 40))
someLoadedImage.set_colorkey(WHITE)

pygame.display.flip()

# <<ADVANCED>> This can some how make screen.blit(someLoadedImage, (x, y)) much faster
# ============ because it convert someLoadedImage into a format based on the current resolution
#someLoadedImage = someLoadedImage.convert()

# ------------------------------
#ballSpriteOrange = pygame.Surface((20,20))
#pygame.draw.circle(ballSpriteOrange, ORANGE, (10, 10), 10)
#ballSpriteOrange.set_colorkey(BLACK)

# ------------------------------
#ballSpriteBLUE = pygame.Surface((20,20))
#pygame.draw.circle(ballSpriteBLUE, BLUE, (10, 10), 10)
#ballSpriteBLUE.set_colorkey(BLACK)

# a simple animation of only three frame
#animation = [someLoadedImage, ballSpriteBLUE, ballSpriteOrange]


# This loads an image as a surface. It takes name of the image file
#background = pygame.image.load("background.jpg")
#background = pygame.transform.scale(background, (500, 500))
#background = background.convert()


# ------------------------------
# on example of creating an animiation (a list of surface)
# initialize the animiation as an empty list
#shiningAnimation = []
# create an function that will append an customized frame to the shiningAnimation
# you can pass anything into this function, even another surface
#def addFrameToAnimation(color, radius):
#    frame = pygame.Surface((40, 40))
#    frame.set_colorkey(BLACK)
#    pygame.draw.circle(frame, color, (20, 20), radius)
    # append the created frame to the shiningAnimation
#    shiningAnimation.append(frame)
# call this function each time for one frame of the shiningAnimation
#for i in range(1, 10):
#	addFrameToAnimation(BLUE, i)
#for i in range(10, 15):
#	addFrameToAnimation(PURPLE, i)
#for i in range(15, 20):
#	addFrameToAnimation(RED, i)
#for i in range(20, 14, -1):
#	addFrameToAnimation(RED, i)
#for i in range(14, 9, -1):
#	addFrameToAnimation(PURPLE, i)
#for i in range(9, 0, -1):
#	addFrameToAnimation(BLUE, i)

#-----------------------------------------------------------------------#
#Starting Edits Here#
#-----------------------------------------------------------------------#

