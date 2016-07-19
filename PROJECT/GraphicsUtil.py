import pygame
import levelList

#Define COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 153, 0)
GREEN = (0,255,0)
PURPLE = (255, 51, 153)
BLUE = (0, 0, 255)
GREY = (128,128,128)



#pygame.draw.rect(Fl, BLUE, (250,0,200,40))

#pygame.draw.rect(Fl, WHITE, (0,0,200,40))


#Classes begin here
class Platform:
    def __init__(self, surface, color, pointx, pointy, width, length): #Change widht and length
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
    def getL(self):
        return self.x + self.length
    def draw(self):
        pygame.draw.rect(self.surface, self.color, ((self.x, self.y), (self.width, self.length)))

# Pl1 = Platform(Fl, WHITE, 0,350,200,40) #Change width and length
#Pl1.draw()

# Pl2 = Platform(Fl, WHITE, 300, 350, 200, 40)
#Pl2.draw()

# Pl3 = Platform(Fl, BLUE, 265, 310, 200, 40)
#Pl3.draw()

# rectList = [Pl1]

#making all of the rectangles based off of the grid


#Character Surface
someLoadedImage = pygame.image.load("Snake.png")
someLoadedImage = pygame.transform.scale(someLoadedImage, (80, 60))
someLoadedImage.set_colorkey(WHITE)

pygame.display.flip()
pygame.display.update()