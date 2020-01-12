# Robo-Dog Rescue
# January 9, 2020

# Imports
import sys
import pygame
import os

# Initialize pygame
pygame.init()

# Initialize fonts
try:
	pygame.font.init()
except:
	print ("Fonts Unavailable")
	sys.exit()

######################## Classes ########################

# Class for protagonist
class Person(pygame.sprite.Sprite):
    def __init__(self, image, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0 # move along x
        self.movey = 0 # move along y
        self.frame = 0 # count frames
        self.collision = False # To see if the sprite has collided
        
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
        
        # Go back to this -- need to figure out how to stop when we hit the ground/platform
       
    # Update position
    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        hit_list = pygame.sprite.spritecollide(self, enemy_list, False)
        for enemy in hit_list:
            self.collision = True
            print("Collision Occurred!")
            # Could quit here
        
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
        distance = 20
        speed = 5
        
        if self.counter >= 0 and self.counter <= distance:
            self.rect.x += speed
        elif self.counter >= distance and self.counter <= distance*2:
            self.rect.x -= speed
        else:
            self.counter = 0
            
        self.counter += 1
        
# Class for Platforms
class Platform(pygame.sprite.Sprite):
    def __init__(self, image, xpos, ypos):
        self.image = pygame.image.load(os.path.join(image)).convert()
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        
# Class for levels of the game
class Level():
    # Create enemies for a level
    def create(lvl, enemyx, enemyy):
        if lvl == 1:
            print("Level " + str(lvl))
            enemy = Enemy('spider.png', enemyx, enemyy)
            enemy_list = pygame.sprite.Group() # Create enemy group
            enemy_list.add(enemy)
            
        if lvl == 2:
            print("Level " + str(lvl))
            
        return enemy_list
    
    # Make a ground for the program
    def ground(lvl, xpos, ypos, image):
        ground_list = pygame.sprite.Group()
        i = 0
        if lvl == 1:
            print ("Level " + str(lvl))
        
        if lvl == 2:
            print ("Level " + str(lvl))
            
        return ground_list
    
    # Make a platform for the game
    def platform(lvl, image):
        platform_list = pygame.sprite.Group()
        if lvl == 1:
            print ("Level " + str(lvl))
            
        if lvl == 2:
            print ("Level " + str(lvl))
            
        return platform_list
        
#################### Create Content #######################


# Create a screen (width, height)
screenx = 960
screeny = 720
ty = 100
screen = pygame.display.set_mode((screenx, screeny))
background = pygame.image.load("background.png").convert_alpha()
backgroundbox = background.get_rect()
pygame.display.set_caption('Robo-Dog Rescue')


# Spawn person
grace = Person('dog.png', 200, 0)
person_list = pygame.sprite.Group()
person_list.add(grace)
steps = 5

enemy_list = Level.create(1, 550, 550)


####################### Main Event Loop #########################
# go into a holding pattern until someone clicks a mouse or hits a key

while 1:
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left')
                grace.move(-steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right')
                grace.move(steps,0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('jump')
                grace.move(0, -5*steps)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left stop')
                grace.move(steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right stop')
                grace.move(-steps, 0)
            if event.key == ord('q'):
                print("Exiting Robo-Dog Rescue")
                pygame.quit()
                sys.exit()

        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.blit(background, backgroundbox)
    grace.gravity() # Check gravity
    grace.update() # Update player position
    person_list.draw(screen) # Refresh player position
    enemy_list.draw(screen)
    for enemy in enemy_list:
        enemy.move()
    pygame.display.flip()
            
