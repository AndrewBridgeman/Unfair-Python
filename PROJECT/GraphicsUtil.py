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





#Classes begin here
class Platform:
    def __init__(self, color, pointx, pointy, width, length, Fall = False): #Change widht and length
        self.width = width
        self.length = length
        self.x = pointx
        self.gridX = pointx//40
        self.y = pointy
        self.gridY = pointy//50
        self.color = color
        self.Fall = Fall

    def getX(self):
        self.x = pointx

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, ((self.x, self.y), (self.width, self.length)))
    
    def getPos(self):
        return (self.x, self.y , self.x + self.width, self.y + self.length)

    def checkCollision(self, hero):
        x1, y1, x2, y2 = hero.getPos()
        px1, py1, px2, py2 = self.getPos()
        if x2 <= px1:
            return False 
        if x1 >= px2:
            return False
        if y2 < py1:
            return False
        if y1 >= py2:
            return False
        if y2 >= py1 and y1 < py1:
            if x1 >= px1 and x2 <= px2:
                hero.y = y1 - y2 + py1
                return True
            d = y2 - py1
            dleft = x2 - px1
            dright = px2 - x1
            if (d < dleft and x1 < px1) or (d < dright and x2 > px2):
                hero.y = y1 - y2 + py1
                return True
        if x2 > px1 and x1 < px1:
            hero.x = x1 - x2 + px1
            return False
        if x1 < px2 and x2 > px2:
            hero.x = px2
            return False
        hero.vy = 1
        return False





class invisiblePlatform:
    def __init__(self):
        self.x = x
        self.y = y
    def draw(self,screen):
        screen.blit(screen,(((self.x, self.y), (self.width, self.length))))

    def getPos(self):
        return (self.x, self.y , self.x + self.width, self.y + self.length)

    # def checkCollision(self, hero):
    #     x1, y1, x2, y2 = hero.getPos()
    #     px1, py1, px2, py2 = self.getPos()
    #     if x2 <= px1:
    #         return False 
    #     if x1 >= px2:
    #         return False
    #     if y2 < py1:
    #         return False
    #     if y1 >= py2:
    #         return False
    #     if y2 >= py1 and y1 < py1:
    #         if x1 >= px1 and x2 <= px2:
    #             hero.y = y1 - y2 + py1
    #             return False
    #         d = y2 - py1
    #         dleft = x2 - px1
    #         dright = px2 - x1
    #         if (d < dleft and x1 < px1) or (d < dright and x2 > px2):
    #             hero.y = y1 - y2 + py1
    #             return False
    #     if x2 > px1 and x1 < px1:
    #         hero.x = x1 - x2 + px1
    #         return False
    #     if x1 < px2 and x2 > px2:
    #         hero.x = px2
    #         return False
    #     return False








#making all of the rectangles based off of the grid

#Spikes

#Finish Flag
flagImage = pygame.image.load("flag.png")
flagImage = pygame.transform.scale(flagImage,(80,80))
flagImage.set_colorkey(WHITE)

class Flag:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def draw(self,screen):
        screen.blit(flagImage,(self.x,self.y))

#Spikes
spike = pygame.image.load("spikes.png")
spike = pygame.transform.scale(spike,(40,50))
spike.set_colorkey(WHITE)

class Spike:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def draw(self,screen):
        screen.blit(spike,(self.x,self.y))
    def getPos(self):
        return (self.x, self.y, self.x + 40, self.y + 50)
    def checkCollision(self, hero):
        x1, y1, x2, y2 = hero.getPos()
        px1, py1, px2, py2 = self.getPos()
        if x2 < px1:
            return False 
        if x2 == px1 and y2 >= py1 and y2 <= py2:
            return True
        if x1 == px2 and y2 <= py2 and y1 >= py1:
            return True
        if y2 < py1:
            return False
        if y1 >= py2:
            return False
        if y2 >= py1 and y1 < py1:
            if x1 >= px1 and x2 <= px2:
                hero.y = y1 - y2 + py1
                return True
            d = y2 - py1
            dleft = x2 - px1
            dright = px2 - x1
            if (d < dleft and x1 < px1) or (d < dright and x2 > px2):
                hero.y = y1 - y2 + py1
                return True
        if x2 > px1 and x1 < px1:
            hero.x = x1 - x2 + px1
            return False
        if x1 < px2 and x2 > px2:
            hero.x = px2
            return False
        return False


    

#Villain Surface
mongooseImage = pygame.image.load("Rikki_Tikki_Tavi.png")
mongooseImage = pygame.transform.scale(mongooseImage,(60,60))
mongooseImage.set_colorkey(WHITE)

class Villain:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def draw(self,screen):
        screen.blit(mongooseImage,(self.x,self.y))
    def getPos(self):
        return (self.x + 10, self.y, self.x + 50, self.y + 60)
    def checkCollision(self, hero):
        x1, y1, x2, y2 = hero.getPos()
        px1, py1, px2, py2 = self.getPos()
        if x2 < px1:
            return False 
        if x2 == px1 and y2 >= py1 and y2 <= py2:
            return True
        if x1 == px2 and y2 <= py2 and y1 >= py1:
            return True
        if y2 < py1:
            return False
        if y1 >= py2:
            return False
        if y2 >= py1 and y1 < py1:
            if x1 >= px1 and x2 <= px2:
                hero.y = y1 - y2 + py1
                return True
            d = y2 - py1
            dleft = x2 - px1
            dright = px2 - x1
            if (d < dleft and x1 < px1) or (d < dright and x2 > px2):
                hero.y = y1 - y2 + py1
                return True
        if x2 > px1 and x1 < px1:
            hero.x = x1 - x2 + px1
            return False
        if x1 < px2 and x2 > px2:
            hero.x = px2
            return False
        return False


#Hero Surface
someLoadedImage = pygame.image.load("Snake.png")
someLoadedImage = pygame.transform.scale(someLoadedImage, (60, 50))
someLoadedImage.set_colorkey(WHITE)

# class Hero:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def draw(self,screen):
#         screen.blit(hero,(self.x,self.y))

# class Col:
#     def __init__(self,x,y,color,w,h):
#         self.x = x
#         self.y = y
#         self.color = color
#         self.w = width
#         self.h = height
#     def draw(self, screen):
#          pygame.draw.rect(screen, self.color, self.x,self.y, self.w, self.h)



    
pygame.display.flip()
pygame.display.update()