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

# Initalize the mixer
pygame.mixer.init()

# Initialize fonts
try:
	pygame.font.init()
except:
	print ("Fonts Unavailable")
	sys.exit()

# Game loop for start screen
def start():
    print('On start screen')
    background = pygame.image.load('startscreen.png').convert_alpha()
    backgroundbox = background.get_rect()

    # Buttons on the start screen
    buttons = []
    howtoplaybutton = Button(50, 640, 260, 30)
    buttons.append(howtoplaybutton)

    pygame.mixer.music.load("maintitletheme.wav")
    pygame.mixer.music.play()
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                mousePosition = pygame.mouse.get_pos()
                for button in buttons:
                    if button.isClicked(mousePosition):
                        pygame.mixer.music.stop()
                        # selectsound = pygame.mixer.Sound('optionselect2.wav')
                        # selectsound.play()
                        state = 'TUTORIAL'
                        return state
        screen.blit(background, backgroundbox)
        clock.tick(30)
        pygame.display.flip()

# Game loop for tutorial
def tutorial():
    print('In level one function')
    background = pygame.image.load("background.png").convert_alpha()
    backgroundbox = background.get_rect()

    # Music for tutorial level
    pygame.mixer.music.load('song1.mp3')
    pygame.mixer.music.play(-1)
    
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
    up = down = left = right = collect_powerup = False

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
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                	print("collect powerup")
                	collect_powerup = True
        
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
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                	print('stop collecting powerups')
                	collect_powerup = False
                if event.key == ord('q'):
                    print("Exiting Robo-Dog Rescue")
                    pygame.quit()
                    sys.exit()
                
            if event.type == pygame.QUIT:
                sys.exit()
                        
        screen.blit(background, backgroundbox)
        grace.update(up, down, left, right, collect_powerup, level, platform_list)
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
    print(state)
    if state == 'LEVELONE':
        pass
    if state == 'START':
        print('In the start state')
        state = start()
    if state == 'END':
        pass
    if state == 'TUTORIAL':
        tutorial()
    if state == 'PROLOGUE':
        pass
    if state == 'WIN':
        pass
    if state == 'LOSE':
        pass
