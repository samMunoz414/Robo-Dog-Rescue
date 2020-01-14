# Robo-Dog Rescue
# January 13, 2020

# Imports
import sys
import pygame
import os

# NOTE: Much of the code is copied from the stackoverflow thread located here: https://stackoverflow.com/questions/14354171/add-scrolling-to-a-platformer-in-pygame

############# Classes Needed for Robodog Game ##############

# Class for protagonist
class Person(pygame.sprite.Sprite):
    def __init__(self, image, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)
        # velocity in the x direction
        self.movex = 0
        # velocity in the y direction
        self.movey = 0 
        # boolean storing if the character is on the ground
        self.isOnGround = False
        # stores player's image
        self.image = pygame.image.load("tall_blue.png").convert_alpha()
        # stores player's rect object
        self.rect = pygame.Rect(xpos, ypos, 60, 90)

<<<<<<< HEAD
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
            
=======
    # Handles any updates based on keyboard inputs and 
    def update(self, 
        # boolean storing if the player moves up
        up, 
        # boolean storing if the player moves up
        down, 
        # boolean storing if the player moves up
        left, 
        # boolean storing if the player moves up
        right, 
        # boolean storing if the player is running
        running, 
        # list storing all the platforms
        platforms):

            if up:
                # only jumps if the player is on the ground
                if self.isOnGround:
                    self.movey -= 10
            # if the down button if pressed 
            if down:
                pass
            if running:
                self.movex = 12
            if left:
                self.movex = -8
            if right:
                slef.movex = 8
            if not self.isOnGround:
                # this is gravity
                self.movey += 0.3
                # caps max velocity in the y direction
                if self.movey > 100:
                    self.movey = 100
            if not (left or right):
                self.movex = 0

            # increments in the x direction
            self.rect.left += self.movex
            # handles collisions in the x direction
            self.collide(self.movex, 0, platforms)
            # increments in the y direction
            self.rect.top += self.movey
            # assuming player is in the air
            self.isOnGround = False
            # handles collisions in the y direction
            self.collide(0, self.movex, platforms)
        
        def collide(self, dx, dy, platforms):
            collisions = pygame.sprite.spritecollide(self, platforms, False)
            for block in collisions:
                # collision occured when players was moving right
                if dx > 0:
                    self.rect.right = block.rect.left
                    print("collide right")
                # collision occured when players was moving left
                if dx < 0:
                    self.rect.left = block.rect.right
                    print("collide left")
                # collision occured when players was moving down
                if dy > 0:
                    self.rect.bottom = block.rect.top
                    self.isOnGround = True
                    self.movey = 0
                # collision occured when players was moving up
                if dy < 0:
                    self.rect.top = block.rect.bottom
>>>>>>> 356cf1f9e8e438bcb4abf68198ae3dd8b170caf1

        
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
