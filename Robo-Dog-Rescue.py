# Robo-Dog Rescue
# January 9, 2020

# Imports
import sys
import pygame
import os
from Levels import *
from Characters import *
from Blocks import *

# Initialize pygame
pygame.init()

# Initialize fonts
try:
	pygame.font.init()
except:
	print ("Fonts Unavailable")
	sys.exit()
        
#################### Create Content #######################

# Create a screen (width, height)
screenx = 960
screeny = 720
# ty = 100
screen = pygame.display.set_mode((screenx, screeny))
background = pygame.image.load("background.png").convert_alpha()
backgroundbox = background.get_rect()
pygame.display.set_caption('Robo-Dog Rescue')

# Make a list of enemies
enemy_list = Level.enemy(1, 500, 570)
platform_list = Level.platform(1)
platform_list.add(Level.floor(1))

# Spawn person and add input booleans
grace = Person('tall_blue.png', 90, 570)
person_list = pygame.sprite.Group()
person_list.add(grace)
steps = 10
# booleans for input
up = down = left = right = False

# Clock
clock = pygame.time.Clock()

print("Number of sprites: " + str(len(platform_list.sprites())))


####################### Main Event Loop #########################
# go into a holding pattern until someone clicks a mouse or hits a key

while 1:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left')
                left = True
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right')
                right = True
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('up')
                up = True
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left stop')
                left = False
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right stop')
                right = False
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('up stop')
                up = False
            if event.key == ord('q'):
                print("Exiting Robo-Dog Rescue")
                pygame.quit()
                sys.exit()

        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.blit(background, backgroundbox)
    grace.update(up, down, left, right, platform_list, enemy_list)
    person_list.draw(screen)
    enemy_list.draw(screen)
    platform_list.draw(screen)
    for enemy in enemy_list:
        enemy.move()
    clock.tick(30)
    pygame.display.flip()
            
