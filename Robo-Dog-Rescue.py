# Robo-Dog Rescue
# January 9, 2020

# Imports
import sys
import pygame
import os
from Levels import *
from Characters import *
from Blocks import *
from Buttons import *

# Initialize pygame
pygame.init()

# Initialize pygame mixer
pygame.mixer.init()

# Initialize fonts
try:
	pygame.font.init()
except:
	print ("Fonts Unavailable")
	sys.exit()

########################### METHODS FOR GAME LOOP ###########################

# Game loop for start screen
def start():
    print('On start screen')
    background = pygame.image.load('startscreen.png').convert_alpha()
    backgroundbox = background.get_rect()

    # Buttons on the start screen
    buttons = []
    howtoplaybutton = Button(50, 640, 260, 30, 'PROLOGUE')
    buttons.append(howtoplaybutton)

    # Music for start screen 
    pygame.mixer.music.load('maintitletheme.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1) # Infinite loop

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                mousePosition = pygame.mouse.get_pos()
                for button in buttons:
                    if button.isClicked(mousePosition):
                        pygame.mixer.music.stop()
                        return button.state
        screen.blit(background, backgroundbox)
        clock.tick(30)
        pygame.display.flip()

# Game loop for tutorial
def tutorial():
    print('In level one function')
    background = pygame.image.load("background.png").convert_alpha()
    backgroundbox = background.get_rect()
    
    # # Music for tutorial level
    pygame.mixer.music.load('song1.mp3')
    
    # create a level object
    level = Level()
        
    # Make a list of enemies
    platform_list = Level.platform(0)
    platform_list.add(Level.floor(0))
    platform_list.add(Level.powerups(0))
    enemy_list = Level.enemy(0)
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

def prologue():
    print('Prologue Screen')

    # Backgrounds for prologue
    backgrounds = [] # Put the backgrounds in a list
    for i in range(5):
        backgrounds.append('blue_background'+ str(i+1) + '.png')
    background = pygame.image.load(backgrounds[0]).convert_alpha()
    backgroundbox = background.get_rect()

    # Next image and button
    nextimage = pygame.image.load('green_button.png')
    nextbutton = Button(810, 630, 120, 60, 'TUTORIAL')

    # Skip image and button
    skipimage = pygame.image.load('skip_button.png')
    skipbutton = Button(810, 30, 120, 60, 'TUTORIAL')

    j = 1
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                mousePosition = pygame.mouse.get_pos()
                if nextbutton.isClicked(mousePosition):
                    if j<5:
                        background = pygame.image.load(backgrounds[j]).convert_alpha()
                        j += 1 
                    else:
                        return nextbutton.state
                if skipbutton.isClicked(mousePosition):
                    return skipbutton.state
        screen.blit(background, backgroundbox)
        screen.blit(nextimage, (810, 630))
        screen.blit(skipimage, (810, 30))
        clock.tick(30)
        pygame.display.flip()

        
#################### Create Content #######################

# Fields needed for running program
running = True
# state = 'START'
state = 'START'

# Create a screen (width, height)
screenx = 960
screeny = 720
screen = pygame.display.set_mode((screenx, screeny))
pygame.display.set_caption('Robo-Dog Rescue')

# Clock
clock = pygame.time.Clock()

while running:
    print(state)
    if state == 'START':
        print('In start screen')
        state = start()
    if state == 'END':
        pass
    if state == 'TUTORIAL':
        print('In tutorial')
        tutorial()
    if state == 'PROLOGUE':
        print("In prologue")
        state = prologue()
    if state == 'PROLOGUE2':
        print("In prologue")
    if state == 'WIN':
        pass
    if state == 'LOSE':
        pass
    if state == 'LEVELONE':
        pass
