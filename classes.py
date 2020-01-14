# Robo-Dog Rescue
# January 13, 2020

# Imports
import sys
import pygame
import os

############# Classes Needed for Robodog Game ##############

# Class for protagonist
class Person(pygame.sprite.Sprite):
    def __init__(self, image, xpos, ypos, e_list, f_list, p_list):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0 # move along x
        self.movey = 0 # move along y
        self.frame = 0 # count frames
        self.enemy_list = e_list
        self.floor_list = f_list
        self.platform_list = p_list
        
        self.images = [] # List of images, nice for animation for future
        # Could have init take in a list of images for animation, and loop through to convert alpha
        img = pygame.image.load(os.path.join(image)).convert()
        # img.set_colorkey((255,255,255))
        self.images.append(img)
        self.image = self.images[0]
        
        self.rect = self.image.get_rect()
        self.rect.x = xpos # Starting x position
        self.rect.y = ypos # Starting y position
    
    # Control movement
    def move(self, x, y):
        self.movex += x
        self.movey += y
    
    # Simulate gravity
    def gravity(self):
        self.movey += 1 # How fast the player will fall

    # Update position
    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        
        enemy_collide = pygame.sprite.spritecollide(self, self.enemy_list, False)
#        for enemy in enemy_collide:
#            print("Collision with Enemy!")
            
        
        floor_collide = pygame.sprite.spritecollide(self, self.floor_list, False)
        for floor in floor_collide:
            if self.rect.y > floor.rect.y-90 and self.movey >= 0:
                self.movey = 0
                self.rect.y = floor.rect.y-90
        
        platform_collide = pygame.sprite.spritecollide(self, self.platform_list, False)
        for platform in platform_collide:
            print("Collision with platform! self %d %d  platform %d %d" % (self.rect.x, self.rect.y, platform.rect.x, platform.rect.y))
            if self.rect.x + 60 >= platform.rect.x and self.rect.x <= platform.rect.x + 60 and self.rect.y+90 <= platform.rect.y+5 and self.movey >= 0:
                print("above")
                self.movey = 0
                self.rect.y = platform.rect.y-90
            elif self.rect.y <= platform.rect.y + 60 - 5 and self.rect.y + 90 >= platform.rect.y + 5 and (self.rect.x + 60 <= platform.rect.x or self.rect.x <= platform.rect.x + 60):
                print("side")
                # Position
                self.movey = 0
            elif self.rect.x + 60 >= platform.rect.x and self.rect.x <= platform.rect.x + 60 and self.rect.y <= platform.rect.y+60 and self.movey <= 0:
                print("below")
                self.movey = 3
            else:
                print("else")
                
        # Scroll screen
        if self.rect.x >= 885:
            self.rect.x = 30 # Position the person on next "screen"
            for plat in self.platform_list:
                plat.rect.x = plat.rect.x - 960
            for enemy in self.enemy_list:
                enemy.rect.x = enemy.rect.x - 960
        if self.rect.x <= 15:
            self.rect.x = 870 # Position person on previous "screen"
            for plat in self.platform_list:
                plat.rect.x = plat.rect.x + 960
            for enemy in self.enemy_list:
                enemy.rect.x = enemy.rect.x + 960
            

        
# Class for enemy scientists
class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)
        
        self.images = []
        img = pygame.image.load(os.path.join(image)).convert()
        img.convert_alpha()
        self.images.append(img)
        self.image = self.images[0]
        
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.counter = 0
    
    # Control automated movement of enemy
    def move(self):
        # These variables can be changed to fine-tune game
        distance = 15
        speed = 10
        
        if self.counter >= 0 and self.counter <= distance:
            self.rect.x += speed
        elif self.counter >= distance and self.counter <= distance*2:
            self.rect.x -= speed
        else:
            self.counter = 0
            
        self.counter += 1
        
        
# Class for blocks/tiles
class Block(pygame.sprite.Sprite):
    def __init__(self, image, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(image)).convert()
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        
class Powerup(pygame.sprite.Sprite):
    def __init__(self, image, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(image)).convert()
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        
# Class for levels of the game
class Level():
    # Create enemies for a level
    def enemy(lvl, enemyx, enemyy):
        if lvl == 1:
            print("Level " + str(lvl))
            enemy = Enemy('tall_red.png', enemyx, enemyy)
            enemy_list = pygame.sprite.Group() # Create enemy group
            enemy_list.add(enemy)
            
        if lvl == 2:
            print("Level " + str(lvl))
            
        return enemy_list
    
    # Make a ground for the program
    def floor(lvl, image):
        floor_list = pygame.sprite.Group()
        i = 0
        if lvl == 1:
            print ("Level " + str(lvl))
            for i in range(16):
                block = Block(image, i*60, 660)
                floor_list.add(block)
        
        if lvl == 2:
            print ("Level " + str(lvl))
            
        return floor_list
    
    # Make a platform for the game
    def platform(lvl, image):
        platform_list = pygame.sprite.Group()
        if lvl == 1:
            print ("Level " + str(lvl))
            for i in range(4):
                block = Block(image, (i+4)*60, 480)
                platform_list.add(block)
            for i in range(5):
                block = Block(image, (i+8)*60, 300)
                platform_list.add(block)
            for i in range(5):
                block = Block(image, (i+20)*60, 360)
                platform_list.add(block)
            
        if lvl == 2:
            print ("Level " + str(lvl))
            
        return platform_list
