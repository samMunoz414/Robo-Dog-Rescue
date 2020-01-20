# Robo-Dog Rescue
# January 9, 2020

# Imports
import sys
import pygame
import os

from time import sleep
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
    howtoplaybutton = Button(50, 640, 260, 30, 'CONTROLS')
    buttons.append(howtoplaybutton)
    startbutton = Button(770, 640, 130, 30, 'PROLOGUE')
    buttons.append(startbutton)

    # Create Sound objects to store music
    mainMusic = pygame.mixer.Sound("maintitletheme.wav")
    buttonMusic = pygame.mixer.Sound("optionselect2.wav")
    woofwoof = pygame.mixer.Sound("woofwoof.wav")

    # Balance volumes between the channels
    channelOne.set_volume(0.2)

    # Run music
    channelOne.play(mainMusic, loops=-1)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                mousePosition = pygame.mouse.get_pos()
                for button in buttons:
                    if button.isClicked(mousePosition):
                    	if button.state == 'CONTROLS':
                    		channelTwo.play(buttonMusic)
                    		sleep(0.5)
                    	if button.state == 'PROLOGUE':
                            channelTwo.play(woofwoof)
                            sleep(0.5)
                    	channelOne.stop()
                    	channelTwo.stop()
                    	channelOne.set_volume(1.0)
                    	return button.state
        screen.blit(background, backgroundbox)
        clock.tick(30)
        pygame.display.flip()

# Show the controls to the player
def controls():
    print("In control screen")
    background = pygame.image.load("green_background.png").convert_alpha()
    backgroundbox = background.get_rect()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(background, backgroundbox)
        clock.tick(30)
        pygame.display.flip()

# Game loop for tutorial
def tutorial():
    print('In level one function')
    background = pygame.image.load("background.png").convert_alpha()
    backgroundbox = background.get_rect()

    # Skip image and button for corner of screen
    skipimage = pygame.image.load('skip_button.png')
    skipbutton = Button(810, 30, 120, 60, 'CUTSCENE')

    # Creates Soudn object to store music
    music_theme = pygame.mixer.Sound("song1.wav")

    # create a level object
    level = Level()

    # Make a list platforms (enemies, floor, powerups, etc.)
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
    up = down = left = right = powerup = False

    # Start playing music
    channelOne.play(music_theme, loops=-1)

    while 1:
    	# run death sequence if player dies
    	if not grace.isAlive:
    		print("You lose")
    		channelOne.stop()
    		return 'START' # Change to lose screen later

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
    				powerup = True

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
    				print("stop collecting powerup")
    				powerup = False

    			if event.key == ord('q'):
    				print("Exiting Robo-Dog Rescue")
    				pygame.quit()
    				sys.exit()

    		if event.type == pygame.MOUSEBUTTONUP:
    			mousePosition = pygame.mouse.get_pos()
    			if skipbutton.isClicked(mousePosition):
    				channelOne.stop() # Stop the music
    				return skipbutton.state

    		if event.type == pygame.QUIT:
    			sys.exit()

    	screen.blit(background, backgroundbox) # Add background to screen
    	screen.blit(skipimage, (810, 30))
    	grace.update(up, down, left, right, powerup, level, platform_list)
    	if grace.win == True:
    		channelOne.stop() # Stop the music
    		return 'WIN'
    	person_list.draw(screen)
    	platform_list.draw(screen)
    	for enemy in enemy_list:
    		enemy.move()
    	clock.tick(30)
    	pygame.display.flip()

# Game loop for the prologue - goes through 5 screens with arrow button, can skip with skip button
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

# Cut scene - after the tutorial level and before the level selection screen
def cutscene():
    print("In cut scene")
    background = pygame.image.load("blue_background1.png").convert_alpha()
    backgroundbox = background.get_rect()

    # Next image and button
    nextimage = pygame.image.load('green_button.png')
    nextbutton = Button(810, 630, 120, 60, 'SELECTLEVEL')

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                mousePosition = pygame.mouse.get_pos()
                if nextbutton.isClicked(mousePosition):
                    return nextbutton.state
        screen.blit(background, backgroundbox)
        screen.blit(nextimage, (810, 630))
        clock.tick(30)
        pygame.display.flip()

# Game loop for the prologue - goes through 5 screens with arrow button, can skip with skip button
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

# Cut scene - after the tutorial level and before the level selection screen
def cutscene():
    print("In cut scene")
    background = pygame.image.load("blue_background1.png").convert_alpha()
    backgroundbox = background.get_rect()

    # Next image and button
    nextimage = pygame.image.load('green_button.png')
    nextbutton = Button(810, 630, 120, 60, 'SELECTLEVEL')

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                mousePosition = pygame.mouse.get_pos()
                if nextbutton.isClicked(mousePosition):
                    return nextbutton.state
        screen.blit(background, backgroundbox)
        screen.blit(nextimage, (810, 630))
        clock.tick(30)
        pygame.display.flip()

# Win screen for the tutorial
def win():
    print("In control screen")
    background = pygame.image.load("green_background.png").convert_alpha()
    backgroundbox = background.get_rect()

    # List of buttons for the screen
    buttons = []
    continueimage = pygame.image.load("pink_block_40x40.png").convert_alpha()
    continuebutton = Button(460, 340, 40, 40, 'CUTSCENE')
    buttons.append(continuebutton)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                mousePosition = pygame.mouse.get_pos()
                for button in buttons:
                    if button.isClicked(mousePosition):
                        return button.state
        screen.blit(background, backgroundbox)
        screen.blit(continueimage, (460, 340))
        clock.tick(30)
        pygame.display.flip()

# Allow the user to select what level they are on
def selectlevel(lvls):
    print("In select level screen")
    background = pygame.image.load("background.png").convert_alpha()
    backgroundbox = background.get_rect()

    # List of buttons
    buttons = []
    # Add three buttons, one for each level
    for i in range(3):
        button = Button(400+(60*i), 340, 60, 60, 'LEVEL'+str(i+1))
        buttons.append(button)

    # Make image for buttons
    yesimages = []
    yeslevel1 = pygame.image.load("pink_block_40x40.png").convert_alpha()
    yesimages.append(yeslevel1)
    yeslevel2 = pygame.image.load("pink_block_40x40.png").convert_alpha()
    yesimages.append(yeslevel2)
    yeslevel3 = pygame.image.load("pink_block_40x40.png").convert_alpha()
    yesimages.append(yeslevel3)
    noimages = []
    nolevel1 = pygame.image.load("orange_block_40x40.png").convert_alpha()
    noimages.append(nolevel1)
    nolevel2 = pygame.image.load("orange_block_40x40.png").convert_alpha()
    noimages.append(nolevel2)
    nolevel3 = pygame.image.load("orange_block_40x40.png").convert_alpha()
    noimages.append(nolevel3)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                mousePosition = pygame.mouse.get_pos()
                seenbuttons = buttons[:lvls] # User can only click on what levels they have achieved
                for button in seenbuttons:
                    if button.isClicked(mousePosition):
                        return button.state
        screen.blit(background, backgroundbox)
        for i in range(3):
            screen.blit(noimages[i], (400+(60*i), 340))
        for i in range(lvls):
            screen.blit(yesimages[i], (400+(60*i), 340))
        clock.tick(30)
        pygame.display.flip()

# Level one of the game
def levelone():
    print("In level one")
    background = pygame.image.load("background.png").convert_alpha()
    backgroundbox = background.get_rect()

    # Create a level object
    level = Level()
    level.setTotalScreenCount(4) # Set number of screen

    # Make a list of platforms (floor, powerup, enemies, etc.)
    platform_list = Level.platform(1)
    platform_list.add(Level.floor(1))
    platform_list.add(Level.powerups(1))
    enemy_list = Level.enemy(1)
    platform_list.add(enemy_list)

    # Spawn person and add input booleans
    grace = Person('tall_blue.png', 60, 570)
    person_list = pygame.sprite.Group()
    person_list.add(grace)

    # booleans for input
    up = down = left = right = powerup = False

    while 1:
    	# run death sequence if player dies
    	if not grace.isAlive:
    		print("You lose")
    		channelOne.stop()
    		return 'START', 1

    	for event in pygame.event.get():
    		if event.type == pygame.QUIT:
    			sys.exit()
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
    				powerup = True

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
    				print("collect powerup")
    				powerup = False
    			if event.key == ord('q'):
    				print("Exiting Robo-Dog Rescue")
    				pygame.quit()
    				sys.exit()

    	screen.blit(background, backgroundbox)
    	grace.update(up, down, left, right, powerup, level, platform_list)
    	if grace.win == True:
    		return 'WIN', 2
    	person_list.draw(screen)
    	platform_list.draw(screen)
    	for enemy in enemy_list:
    		enemy.move()
    	clock.tick(30)
    	pygame.display.flip()
        
#################### Create Content #######################

# Fields needed for running program
running = True
# state = 'START'
state = 'START'
lvls = 1

# Create a screen (width, height)
screenx = 960
screeny = 720
screen = pygame.display.set_mode((screenx, screeny))
pygame.display.set_caption('Robo-Dog Rescue')

# Clock
clock = pygame.time.Clock()

# Creating channels to play music
channelOne = pygame.mixer.Channel(0)
channelTwo = pygame.mixer.Channel(1)

while running:
    print(state)
    if state == 'START':
        state = start()
    if state == 'TUTORIAL':
        state = tutorial()
    if state == 'PROLOGUE':
        state = prologue()
    if state == 'CUTSCENE':
        state = cutscene()
    if state == 'WIN':
        state = win()
    if state == 'LOSE':
        pass
    if state == 'LEVEL1':
        state, lvls = levelone()
    if state == 'LEVEL2':
        pass
    if state == 'LEVEL3':
        pass
    if state == 'CONTROLS':
        controls()
    if state == 'SELECTLEVEL':
        state = selectlevel(lvls)
    if state == 'END':
        pass
