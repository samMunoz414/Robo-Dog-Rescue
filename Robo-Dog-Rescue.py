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
                            sleep(0.7)
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
    skipimage = pygame.image.load('skipbutton.png')
    skipbutton = Button(860, 10, 120, 60, 'CUTSCENE')

    # Creates Soudn object to store music
    music_theme = pygame.mixer.Sound("songs1and2.wav")
    buttonMusic = pygame.mixer.Sound("optionselect2.wav")

    # create a level object
    level = Level()

    # Make a list platforms (enemies, floor, powerups, etc.)
    platform_list = Level.platform(0)
    platform_list.add(Level.floor(0))
    platform_list.add(Level.powerups(0))
    enemy_list = Level.enemy(0)
    platform_list.add(enemy_list)

    # Spawn person and add input booleans
    grace = Person('GraceMediumForward.png', 60, 570)
    person_list = pygame.sprite.Group()
    person_list.add(grace)

    # booleans for input
    up = down = left = right = powerup = False

    # Start playing music
    channelOne.set_volume(0.2)
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
    				channelTwo.play(buttonMusic)
    				sleep(0.1)
    				channelOne.stop() # Stop the music
    				return skipbutton.state

    		if event.type == pygame.QUIT:
    			sys.exit()

    	screen.blit(background, backgroundbox) # Add background to screen
    	screen.blit(skipimage, (860, 10))
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

# Cut scene - after the tutorial level and before the level selection screen
def cutscene():
    print("In cut scene")
    background = pygame.image.load("blue_background1.png").convert_alpha()
    backgroundbox = background.get_rect()

    # Next image and button
    nextimage = pygame.image.load('arrowbutton.png')
    nextbutton = Button(860, 650, 120, 60, 'SELECTLEVEL')

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                mousePosition = pygame.mouse.get_pos()
                if nextbutton.isClicked(mousePosition):
                    return nextbutton.state
        screen.blit(background, backgroundbox)
        screen.blit(nextimage, (860, 650))
        clock.tick(30)
        pygame.display.flip()

# Game loop for the prologue - goes through 5 screens with arrow button, can skip with skip button
def prologue():
    print('Prologue Screen')

    # Backgrounds for prologue
    backgrounds = [] # Put the backgrounds in a list
    for i in range(5):
        backgrounds.append('panel'+ str(i+1) + '.png')
    background = pygame.image.load(backgrounds[0]).convert_alpha()
    backgroundbox = background.get_rect()

    # Next image and button
    nextimage = pygame.image.load('arrowbutton.png')
    nextbutton = Button(860, 650, 120, 60, 'TUTORIAL')

    # Skip image and button
    skipimage = pygame.image.load('skipbutton.png')
    skipbutton = Button(860, 10, 120, 60, 'TUTORIAL')

    # Create sound objects to store music
    buttonMusic = pygame.mixer.Sound("optionselect2.wav")

    j = 1
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                mousePosition = pygame.mouse.get_pos()
                if nextbutton.isClicked(mousePosition):
                	channelOne.play(buttonMusic)
                	sleep(0.1)
                	if j<5:
                		background = pygame.image.load(backgrounds[j]).convert_alpha()
                		j += 1 
                	else:
                		return nextbutton.state
                if skipbutton.isClicked(mousePosition):
                	channelOne.play(buttonMusic)
                	sleep(0.1)
                	return skipbutton.state
        screen.blit(background, backgroundbox)
        screen.blit(nextimage, (860, 650))
        screen.blit(skipimage, (860, 10))
        clock.tick(30)
        pygame.display.flip()

# Win screen for the tutorial
def win():
    print("On win screen")
    background = pygame.image.load("green_background.png").convert_alpha()
    backgroundbox = background.get_rect()

    # List of buttons for the screen - Continue to next level and back to level select screen
    buttons = []
    continueimage = pygame.image.load("pink_block_40x40.png").convert_alpha()
    continuebutton = Button(460, 340, 40, 40, 'CUTSCENE')
    buttons.append(continuebutton)

    # Create sound object to store music
    buttonMusic = pygame.mixer.Sound("optionselect2.wav")

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                mousePosition = pygame.mouse.get_pos()
                for button in buttons:
                    if button.isClicked(mousePosition):
                        channelOne.play(buttonMusic)
                        sleep(0.1)
                        return button.state
                        
        screen.blit(background, backgroundbox)
        screen.blit(continueimage, (460, 340))
        clock.tick(30)
        pygame.display.flip()

# Lose screen
def lose():
    print("On lose screen")
    background = pygame.image.load("green_background.png").convert_alpha()
    backgroundbox = background.get_rect()

    # List of buttons - replay previous level and back to level select screen
    buttons = []
    replayimage = pygame.image.load("tall_orange.png").convert_alpha()
    replaybutton = Button(300, 300, 60, 90, 'LEVEL1')
    buttons.append(replaybutton)
    selectlevelimage = pygame.image.load("tall_yellow.png").convert_alpha()
    selectlevelbutton = Button(500, 300, 60, 90, 'SELECTLEVEL')
    buttons.append(selectlevelbutton)

    # Add Sound objects to store music
    buttonMusic = pygame.mixer.Sound("optionselect2.wav")

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                mousePosition = pygame.mouse.get_pos()
                for button in buttons:
                    if button.isClicked(mousePosition):
                    	channelOne.play(buttonMusic)
                    	sleep(0.1)
                    	return button.state

        screen.blit(background, backgroundbox)
        screen.blit(replayimage, (300, 300))
        screen.blit(selectlevelimage, (500, 300))
        clock.tick(30)
        pygame.display.flip()

# Allow the user to select what level they are on
def selectlevel(lvls):
    print("In select level screen")
    background = pygame.image.load("levelscreen.png").convert_alpha()
    backgroundbox = background.get_rect()

    # List of buttons
    buttons = []
    # Add three buttons, one for each level
    for i in range(3):
        button = Button(150+(i*240), 340, 180, 180, 'LEVEL'+str(i+1))
        buttons.append(button)

    # Make images for buttons and store in lists
    yesimages = []
    noimages = []
    for i in range(3):
        yesimage = pygame.image.load("green" + str(i+1) + ".png").convert_alpha()
        yesimages.append(yesimage)
        noimage = pygame.image.load("red" + str(i+1) + ".png").convert_alpha()
        noimages.append(noimage)

    # Sound objects to store music
    buttonMusic = pygame.mixer.Sound("optionselect2.wav")

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                mousePosition = pygame.mouse.get_pos()
                seenbuttons = buttons[:lvls] # User can only click on what levels they have achieved
                for button in seenbuttons:
                    if button.isClicked(mousePosition):
                    	channelOne.play(buttonMusic)
                    	sleep(0.1)
                    	return button.state
        screen.blit(background, backgroundbox)
        # Blit all the no images
        for i in range(3):
            screen.blit(noimages[i], (150+(i*240), 340))
        # Blit only the green images of the levels that the user can reach
        for i in range(lvls):
            screen.blit(yesimages[i], (150+(i*240), 340))
        clock.tick(30)
        pygame.display.flip()

# Level one of the game
def levelone():
    print("In level one")
    background = pygame.image.load("background.png").convert_alpha()
    backgroundbox = background.get_rect()

    # Create a level object
    level = Level()
    level.setTotalScreenCount(6) # Set number of screen

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
    		return 'LOSE', 1

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
        state = lose()
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
