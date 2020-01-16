# Robo-Dog Rescue
# January 9, 2020

# Imports
import sys
import pygame
import os
from Levels import *
from Characters import *
from Blocks import *
from enum import Enum

# Initialize pygame
pygame.init()

# Initialize fonts
try:
	pygame.font.init()
except:
	print ("Fonts Unavailable")
	sys.exit()

# Game loop for start screen
def start():
	print('On start screen')
	background = pygame.image.load('startScreen.png').convert_alpha()
	backgroundbox = background.get_rect()
	while 1:
		screen.blit(background, backgroundbox)
		clock.tick(30)
		pygame.display.flip()

# Game loop for level one
def levelone():
    print('In level one function')
    background = pygame.image.load("background.png").convert_alpha()
    backgroundbox = background.get_rect()
    
    # create a level object
    level = Level()
        
    # Make a list of enemies
    platform_list = Level.platform(1)
    platform_list.add(Level.floor(1))
    platform_list.add(Level.powerups(1))
    enemy_list = Level.enemy(1, 500, 570)
    platform_list.add(enemy_list)
    
    # Spawn person and add input booleans
    grace = Person('tall_blue.png', 60, 570)
    person_list = pygame.sprite.Group()
    person_list.add(grace)
    
    # booleans for input
    up = down = left = right = False

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
        grace.update(up, down, left, right, level, platform_list)
        person_list.draw(screen)
        platform_list.draw(screen)
        # powerups_list.draw(screen)
        for enemy in enemy_list:
            enemy.move()
        clock.tick(30)
        pygame.display.flip()
        
#################### Create Content #######################

# Fields needed for running program
running = True
state = 'START'

# Create a screen (width, height)
screenx = 960
screeny = 720
screen = pygame.display.set_mode((screenx, screeny))
pygame.display.set_caption('Robo-Dog Rescue')

# Clock
clock = pygame.time.Clock()

while running:
    if state == 'LEVELONE':
        print('In level one state')
        levelone()
    if state == 'START':
        print('In the start state')
        start()
    if state == 'END':
        pass
    if state == 'TUTORIAL':
        pass
    if state == 'PROLOGUE':
        pass
    if state == 'WIN':
        pass
    if state == 'LOSE':
        pass
