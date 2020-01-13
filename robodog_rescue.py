# Robo-Dog Rescue
# January 9, 2020

# Imports
import sys
import pygame
import os
from classes import *

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
ty = 100
screen = pygame.display.set_mode((screenx, screeny))
background = pygame.image.load("background.png").convert_alpha()
backgroundbox = background.get_rect()
pygame.display.set_caption('Robo-Dog Rescue')

# Make a list of enemies
enemy_list = Level.enemy(1, 500, 570)
floor_list = Level.floor(1, 'block1_60x60.png')
platform_list = Level.platform(1, 'block1_60x60.png')

# Spawn person
grace = Person('tall_blue.png', 0, 570, enemy_list, floor_list, platform_list)
person_list = pygame.sprite.Group()
person_list.add(grace)
steps = 10

# Clock
clock = pygame.time.Clock()


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
                print('up')
                grace.move(0, -1*steps)
                
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
    grace.update()
    grace.gravity()
    person_list.draw(screen) # Refresh player position
    enemy_list.draw(screen)
    floor_list.draw(screen)
    platform_list.draw(screen)
    for enemy in enemy_list:
        enemy.move()
    clock.tick(30)
    pygame.display.flip()
            
