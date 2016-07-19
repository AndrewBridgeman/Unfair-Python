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
    def __init__(self, color, pointx, pointy, width, length, Fall = False): #Change widht and length
        self.width = width
        self.length = length
        self.x = pointx
        self.gridX = pointy//50
        self.y = pointy
        self.gridY = pointx//40
        self.color = color
        self.Fall = Fall
    def getX(self):
        self.x = pointx
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, ((self.x, self.y), (self.width, self.length)))

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