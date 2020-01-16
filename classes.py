# Robo-Dog Rescue
# January 13, 2020

# Imports
import sys
import pygame
import os

############# Classes Needed for Robodog Game ##############

# Class for protagonist
class Person(pygame.sprite.Sprite):
    def __init__(self, image, xpos, ypos, e_list, b_list):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0 # move along x
        self.movey = 0 # move along y
        self.frame = 0 # count frames
        self.enemy_list = e_list
        self.block_list = b_list
        
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
        print("moving")
        self.movex += x
        self.movey += y

    # stops all motion
    def stop_x(self):
    	self.movex = 0
    
    # Simulate gravity
    def gravity(self):
        self.movey += 1 # How fast the player will fall
        
        # Go back to this -- need to figure out how to stop when we hit the ground/platform
        if self.rect.y > 570 and self.movey >= 0:
            self.movey = 0
            self.rect.y = 570
            

    # Update position
    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        hit_list = pygame.sprite.spritecollide(self, self.enemy_list, False)
        for enemy in hit_list:
            print("Collision Occurred!")
            # Could quit here
        collide_list = pygame.sprite.spritecollide(self, self.block_list, False)
        for block in collide_list:
            # checks if the player is moving right
            if self.movex > 0:
                if self.rect.x + self.rect.width >= block.rect.x and not (self.rect.x > block.rect.x):
                    print("Collided with block - moving right")
                    print("(" + str(block.rect.x) + ", " + str(block.rect.y) + ")\t(" + str(block.rect.x + block.rect.width) + ", " + str(block.rect.y + block.rect.height) + ")")
                    self.movex = 0
                    self.rect.x = block.rect.x - self.rect.width
			# checks if the player is moving left
            if self.movex < 0:
                if self.rect.x < block.rect.x + block.rect.width:
                    print("Collided with block - moving left")
                    print("(" + str(block.rect.x) + ", " + str(block.rect.y) + ")\t(" + str(block.rect.x + block.rect.width) + ", " + str(block.rect.y + block.rect.height) + ")")
                    self.movex = 0
                    self.rect.x = block.rect.x + block.rect.width
			# checks if the player is moving down onto a block
            if self.movey > 0:
                if self.rect.y + self.rect.height > block.rect.y:
                    print("Collided with block - moving down")
                    print("(" + str(block.rect.x) + ", " + str(block.rect.y) + ")\t(" + str(block.rect.x + block.rect.width) + ", " + str(block.rect.y + block.rect.height) + ")")
                    self.movey = 0
                    self.rect.y = block.rect.y - self.rect.height
			# checks if the player is hitting a block above their head
            if self.movey < 0:
                if self.rect.y < block.rect.y + block.rect.height:
                    print("Collided with block - moving up")
                    print("(" + str(block.rect.x) + ", " + str(block.rect.y) + ")\t(" + str(block.rect.x + block.rect.width) + ", " + str(block.rect.y + block.rect.height) + ")")
                    self.movey = 0
                    self.rect.y = block.rect.y + block.rect.height

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
                block = Block(image, (i+3)*60, 480)
                platform_list.add(block)
            for i in range(5):
                block = Block(image, (i+7)*60, 300)
                platform_list.add(block)
            for i in range(2):
                block = Block(image, (i+3)*60 + 550, 580)
                platform_list.add(block)
            
        if lvl == 2:
            print ("Level " + str(lvl))
            
        return platform_list
