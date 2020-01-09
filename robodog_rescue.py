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

# Class for main sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0 # move along x
        self.movey = 0 # move along y
        self.frame = 0 # count frames
        self.images = [] # List of images, nice for animation for future
        img = pygame.image.load(os.path.join('dog.png')).convert() # Image we want to load
        img.convert_alpha()
        img.set_colorkey((255,255,255))
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 540
    
    # Control Sprite movement
    def move(self, x, y):
        self.movex += x
        self.movey += y
       
    # Update sprite position
    def update(self):
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey

# Create a screen (width, height)
screen = pygame.display.set_mode((960, 720))
screen.fill((255,255,255))

# Add rectangles to the screen
pygame.draw.rect(screen, (70, 210, 80), pygame.Rect((240, 240, 120, 120)))
pygame.draw.rect(screen, (70, 210, 80), pygame.Rect((360, 240, 120, 120)))

grace = Player() # Create Grace Ada Clarke
steps = 5 # How many pixels to move
player_list = pygame.sprite.Group()
player_list.add(grace)

# Update the screen
pygame.display.update()


####################### Main Event Loop #########################
# go into a holding pattern until someone clicks a mouse or hits a key

while 1:
    
    screen.fill(pygame.Color('white'))
    grace.update() # Update player position
    player_list.draw(screen)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            screen.fill((255,255,255), grace.rect)
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left')
                grace.move(-steps,0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right')
                grace.move(steps,0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('jump')
                
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
            
    pygame.display.update()
