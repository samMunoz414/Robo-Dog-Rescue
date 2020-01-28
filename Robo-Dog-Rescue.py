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

# Start screen
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

	# Balance volumes between the channels
	mainMusic.set_volume(0.2)
	woofwoof.set_volume(1.0)

	# Run music
	channelList[0].play(mainMusic, loops=-1)

	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEBUTTONUP:
				mousePosition = pygame.mouse.get_pos()
				for button in buttons:
					if button.isClicked(mousePosition):
						if button.state == 'CONTROLS':
							channelList[1].play(buttonMusic)
							sleep(0.5)
						if button.state == 'PROLOGUE':
							channelList[1].play(woofwoof)
							sleep(0.7)
						channelList[0].stop()
						channelList[1].stop()
						return button.state
		screen.blit(background, backgroundbox)
		clock.tick(30)
		pygame.display.flip()

# Show the controls to the player
def controls():
	print("In control screen")
	background = pygame.image.load("howtoplay.png").convert_alpha()
	backgroundbox = background.get_rect()

	# Button
	backbutton = Button(360, 590, 240, 120, 'START')
	backimage = pygame.image.load("backtitle.png").convert_alpha()

	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEBUTTONUP:
				mousePosition = pygame.mouse.get_pos()
				if backbutton.isClicked(mousePosition):
					channelList[1].play(buttonMusic)
					sleep(0.5)
					return backbutton.state

		screen.blit(background, backgroundbox)
		screen.blit(backimage, (360, 590))
		clock.tick(30)
		pygame.display.flip()

# Game loop for tutorial
def tutorial():
	print('In level one function')
	background = pygame.image.load("Tutorial_Background2.png").convert_alpha()
	backgroundbox = background.get_rect()

	# Skip image and button for corner of screen
	skipimage = pygame.image.load('skipbutton.png')
	skipbutton = Button(860, 10, 90, 60, 'CUTSCENE')

	# Stop all channels from playing music
	for i in range(8):
		channelList[i].stop()

	# create a level object
	level = Level()

	# Make a list platforms (enemies, floor, powerups, etc.)
	platform_list = Level.platform(0)
	platform_list.add(Level.floor(0))
	platform_list.add(Level.powerups(0))
	enemy_list = Level.enemy(0)
	platform_list.add(enemy_list)

	# Spawn person and add input booleans
	grace = Person('GraceRight2.png', 60, 570)
	person_list = pygame.sprite.Group()
	person_list.add(grace)

	# Creates bullet list
	bullet_list = pygame.sprite.Group()

	# booleans for input
	up = down = left = right = space = cosmo = powerup = False

	# Creates font to display information
	font = pygame.font.SysFont("Futura", 26)

	# Blit door on last screen
	door = pygame.image.load("Door.png").convert_alpha()

	frameCount = 0

	# Start playing music
	levelmusic.set_volume(0.2)
	channelList[0].play(levelmusic, loops=-1)
	jumpMusic.set_volume(0.1)
	buttonMusic.set_volume(1.0)

	startTime = pygame.time.get_ticks()

	while 1:

		seconds = (pygame.time.get_ticks() - startTime)//1000
		print("seconds: "+ str(seconds))

		minutes = seconds//60
		seconds_to_display = seconds % 60

		print("minutes: " + str(minutes))
		print("seconds to display" + str(seconds_to_display))


		# run death sequence if player dies
		if not grace.isAlive:
			print("You lose")
			channelList[0].stop()
			return 'CUTSCENE'

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
				if event.key == pygame.K_SPACE:
					print("activate powerup")
					space = True
				if event.key == ord('c'):
					print("activate cosmo")
					cosmo = True


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
				if event.key == ord('c'):
					print("deactivate cosmo")
					cosmo = False

				if event.key == ord('q'):
					print("Exiting Robo-Dog Rescue")
					pygame.quit()
					sys.exit()

			if event.type == pygame.MOUSEBUTTONUP:
				mousePosition = pygame.mouse.get_pos()
				if skipbutton.isClicked(mousePosition):
					channelList[1].play(buttonMusic)
					sleep(0.1)
					channelList[0].stop() # Stop the music
					return skipbutton.state

			if event.type == pygame.QUIT:
				sys.exit()

		screen.blit(background, backgroundbox) # Add background to screen
		screen.blit(skipimage, (860, 10))
		displayGearCount = font.render("GEARS: " + str(grace.gearCount), True, (255, 255, 255) )
		if seconds_to_display < 10:
			displayTime = font.render("TIME: " + str(minutes)+ ":0" + str(seconds_to_display), True, (255,255,255))
		else:
			displayTime = font.render("TIME: " + str(minutes)+ ":" + str(seconds_to_display), True, (255, 255, 255))

		if isinstance(grace.powerup, LaserGun):
			print("Display ammo")
			displayBulletCount = font.render("BULLETS: " + str(grace.powerup.ammo), True, (255, 255, 255) )
			screen.blit(displayBulletCount, (10, 85) )

		screen.blit(displayGearCount, (10 ,15))
		screen.blit(displayTime, (10, 50))
		if level.screenCount == level.totalScreenCount:
			screen.blit(door, (910, 570))
		grace.update(up, down, left, right, space, powerup, level, platform_list, channelList, jumpMusic, coinMusic, powerupMusic, zapMusic)
		if cosmo:
			grace.activateCosmo(channelList[5], woofwoof)
		for bullet in bullet_list:
			removeBullet= bullet.update(platform_list)
			if removeBullet:
				print("Removed bullet")
				bullet_list.remove(bullet)
		if not grace.cosmo == None:
			removeCosmo = grace.cosmo.update(platform_list)
			if removeCosmo:
				grace.cosmo = None
		if space:
			frameCount += 1
			if frameCount == 3:
				space = False
				frameCount = 0
			if isinstance(grace.powerup, LaserGun):
				if frameCount == 1:
					bullet = grace.fire(channelList[4], laserFiring)
					if not bullet == None:
						bullet_list.add(bullet)
		if grace.win == True:
			channelList[0].stop() # Stop the music
			return 'SELECTLEVEL'
		for enemy in enemy_list:
			removeEnemy = enemy.update()
			if removeEnemy:
				platform_list.remove(enemy)
		person_list.draw(screen)
		platform_list.draw(screen)
		bullet_list.draw(screen)
		if not grace.powerup == None:
			screen.blit(grace.powerup.image, grace.powerup.rect)
		if not grace.cosmo == None:
			screen.blit(grace.cosmo.image, grace.cosmo.rect)
		clock.tick(30)
		pygame.display.flip()

# Cut scene - after the tutorial level and before the level selection screen
def cutscene():
	print("In cut scene")
	background = pygame.image.load("panel5.png").convert_alpha()
	backgroundbox = background.get_rect()

	# Next image and button
	nextimage = pygame.image.load('nextpurple.png')
	nextbutton = Button(860, 650, 90, 60, 'SELECTLEVEL')

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

# End credits scene
def end():
	background = pygame.image.load("end.png").convert_alpha()
	backgroundbox = background.get_rect()

	# buttons
	buttons = []
	nextimage = pygame.image.load('nextpurple.png')
	nextbutton = Button(860, 650, 90, 60, 'CREDITS')
	buttons.append(nextbutton)


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
		screen.blit(nextimage, (860, 650))
		clock.tick(30)
		pygame.display.flip()

# Show the controls - can restart game
def credits():
	print("In credits screen")
	background = pygame.image.load("credits.png").convert_alpha()
	backgroundbox = background.get_rect()

	# Button
	backbutton = Button(710, 10, 240, 120, 'START')
	backimage = pygame.image.load("restartgame.png").convert_alpha()

	# Sound object to hold music
	buttonMusic = pygame.mixer.Sound("optionselect2.wav")

	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEBUTTONUP:
				mousePosition = pygame.mouse.get_pos()
				if backbutton.isClicked(mousePosition):
					channelList[1].play(buttonMusic)
					sleep(0.5)
					return backbutton.state, 1

		screen.blit(background, backgroundbox)
		screen.blit(backimage, (710, 10))
		clock.tick(30)
		pygame.display.flip()

# Prologue for the program		
def prologue():
	print('Prologue Screen')

	# Backgrounds for prologue
	backgrounds = [] # Put the backgrounds in a list
	for i in range(4):
		backgrounds.append('panel'+ str(i+1) + '.png')
	background = pygame.image.load(backgrounds[0]).convert_alpha()
	backgroundbox = background.get_rect()

	# Next image and button
	nextimage = pygame.image.load('nextpurple.png')
	nextbutton = Button(860, 650, 90, 60, 'TUTORIAL')

	# Skip image and button
	skipimage = pygame.image.load('skippurple.png')
	skipbutton = Button(860, 10, 90, 60, 'TUTORIAL')

	# sets the volume for each song
	backgroundMusic.set_volume(0.2)
	buttonMusic.set_volume(1.0)
	glassBreaking.set_volume(0.2)

	# Plays background music
	channelList[0].play(backgroundMusic, loops=-1)
	j = 1
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEBUTTONUP:
				mousePosition = pygame.mouse.get_pos()
				if nextbutton.isClicked(mousePosition):
					channelList[1].play(buttonMusic)
					sleep(0.1)
					if j<4:
						background = pygame.image.load(backgrounds[j]).convert_alpha()
						if j == 2:
							channelList[1].play(glassBreaking)
						j += 1 
					else:
						return nextbutton.state
				if skipbutton.isClicked(mousePosition):
					channelList[1].play(buttonMusic)
					sleep(0.1)
					return skipbutton.state
		screen.blit(background, backgroundbox)
		screen.blit(nextimage, (860, 650))
		screen.blit(skipimage, (860, 10))
		clock.tick(30)
		pygame.display.flip()

# Win screen for the tutorial
def win(level, score):
	print("On win screen")
	background = pygame.image.load("win.png").convert_alpha()
	backgroundbox = background.get_rect()

	lvl = level

	# Creates font to display information
	font = pygame.font.SysFont("Futura", 50)

	# List of buttons - replay previous level and back to level select screen
	buttons = []
	replayimage = pygame.image.load("nextlevel.png").convert_alpha()
	replaybutton = Button(360, 240, 240, 120, 'LEVEL'+str(lvl))
	buttons.append(replaybutton)
	selectlevelimage = pygame.image.load("backlevel.png").convert_alpha()
	selectlevelbutton = Button(360, 400, 240, 120, 'SELECTLEVEL')
	buttons.append(selectlevelbutton)
	startscreenimage = pygame.image.load("backtitle.png").convert_alpha()
	startscreenbutton = Button(360, 560, 240, 120, 'START')
	buttons.append(startscreenbutton)

	displayScore = font.render("SCORE: " + str(score), True, (0,0,0) )

	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEBUTTONUP:
				mousePosition = pygame.mouse.get_pos()
				for button in buttons:
					if button.isClicked(mousePosition):
						channelList[0].play(buttonMusic)
						sleep(0.1)
						print(button.state)
						return button.state

		screen.blit(background, backgroundbox)
		screen.blit(replayimage, (360, 240))
		screen.blit(selectlevelimage, (360, 400))
		screen.blit(startscreenimage, (360, 560))
		screen.blit(displayScore, (350, 160))

		clock.tick(30)
		pygame.display.flip()

# Lose screen
def lose(level):
	print("On lose screen")
	background = pygame.image.load("lose.png").convert_alpha()
	backgroundbox = background.get_rect()

	level = lvl

	# List of buttons - replay previous level and back to level select screen
	buttons = []
	replayimage = pygame.image.load("bluerestartlevel.png").convert_alpha()
	replaybutton = Button(360, 240, 240, 120, 'LEVEL'+str(lvl))
	buttons.append(replaybutton)
	selectlevelimage = pygame.image.load("bluebacklevel.png").convert_alpha()
	selectlevelbutton = Button(360, 400, 240, 120, 'SELECTLEVEL')
	buttons.append(selectlevelbutton)
	startscreenimage = pygame.image.load("bluebacktitle.png").convert_alpha()
	startscreenbutton = Button(360, 560, 240, 120, 'START')
	buttons.append(startscreenbutton)

	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEBUTTONUP:
				mousePosition = pygame.mouse.get_pos()
				for button in buttons:
					if button.isClicked(mousePosition):
						channelList[0].play(buttonMusic)
						sleep(0.1)
						return button.state

		screen.blit(background, backgroundbox)
		screen.blit(replayimage, (360, 240))
		screen.blit(selectlevelimage, (360, 400))
		screen.blit(startscreenimage, (360, 560))
		clock.tick(30)
		pygame.display.flip()

# Allow the user to select what level they are on
def selectlevel(lvls):
	print("In select level screen")
	background = pygame.image.load("selectscreen.png").convert_alpha()
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

	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.MOUSEBUTTONUP:
				mousePosition = pygame.mouse.get_pos()
				seenbuttons = buttons[:lvls] # User can only click on what levels they have achieved
				for button in seenbuttons:
					if button.isClicked(mousePosition):
						channelList[0].play(buttonMusic)
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

# Levels of the game
def level(level):
	lvl = level
	print("In level " + str(lvl))
	background = pygame.image.load("Background.png").convert_alpha()
	backgroundbox = background.get_rect()

	# Stop all channels from playing music
	for i in range(8):
		channelList[i].stop()

	# Create a level object
	level = Level()
	if lvl == 1 or lvl == 2:
		level.setTotalScreenCount(4) # Levels 1 and 2 have 4 screens
	if lvl == 3:
		level.setTotalScreenCount(6) # Level 3 has 6 screens

	# Creates font to display information
	font = pygame.font.SysFont("Futura", 26)

	# Make a list of platforms (floor, powerup, enemies, etc.)
	platform_list = Level.platform(lvl)
	platform_list.add(Level.floor(lvl))
	platform_list.add(Level.powerups(lvl))
	enemy_list = Level.enemy(lvl)
	platform_list.add(enemy_list)

	# Spawn person and add input booleans
	grace = Person('GraceRight2.png', 60, 570)
	person_list = pygame.sprite.Group()
	person_list.add(grace)

	# Create bullet list
	bullet_list = pygame.sprite.Group()

	# booleans for input
	up = down = left = right = space = cosmo = powerup = False

	frameCount = 0

	# Counts frames
	timeCount = 0
	seconds = 0
	minutes = 0

	# Blit door on last screen
	door = pygame.image.load("Door.png").convert_alpha()

	# balance channel volumes
	levelmusic.set_volume(0.2)
	jumpMusic.set_volume(0.1)
	channelList[0].play(levelmusic, loops=-1)

	startTime = pygame.time.get_ticks()

	while 1:

		seconds = (pygame.time.get_ticks() - startTime)//1000
		print("seconds: "+ str(seconds))

		minutes = seconds//60
		seconds_to_display = seconds % 60

		print("minutes: " + str(minutes))
		print("seconds to display" + str(seconds_to_display))

		# run death sequence if player dies
		if not grace.isAlive:
			print("You lose")
			channelList[0].stop()
			print('LOSE'+str(lvl))
			return 'LOSE'+str(lvl), lvl, 0

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
				if event.key == pygame.K_SPACE:
					print("activate powerup")
					space = True
				if event.key == ord('c'):
					print("activate cosmo")
					cosmo = True

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
				if event.key == ord('c'):
					print("deactivate cosmo")
					cosmo = False
				if event.key == ord('q'):
					print("Exiting Robo-Dog Rescue")
					pygame.quit()
					sys.exit()

		screen.blit(background, backgroundbox)
		displayGearCount = font.render("GEARS: " + str(grace.gearCount), True, (255, 255, 255) )
		if seconds_to_display < 10:
			displayTime = font.render("TIME: " + str(minutes)+ ":0" + str(seconds_to_display), True, (255,255,255))
		else:
			displayTime = font.render("TIME: " + str(minutes)+ ":" + str(seconds_to_display), True, (255, 255, 255))
		
		# Score of the game
		score = (minutes*60)+seconds_to_display - grace.gearCount

		if isinstance(grace.powerup, LaserGun):
			displayBulletCount = font.render("BULLETS: " + str(grace.powerup.ammo), True, (255, 255, 255) )
			screen.blit(displayBulletCount, (10, 85) )

		screen.blit(displayGearCount, (10 ,15))
		screen.blit(displayTime, (10, 50))
		if level.screenCount == level.totalScreenCount:
			if lvl == 1 or lvl == 2:
				screen.blit(door, (910, 570))
			if lvl == 3:
				screen.blit(door, (910, 20))
		grace.update(up, down, left, right, space, powerup, level, platform_list, channelList, jumpMusic, coinMusic, powerupMusic, zapMusic)
		if cosmo == True:
			grace.activateCosmo(channelList[5], woofwoof)
		for bullet in bullet_list:
			removeBullet = bullet.update(platform_list)
			print(removeBullet)
			if removeBullet:
				print("Removed bullet")
				bullet_list.remove(bullet)
		if not grace.cosmo == None:
			removeCosmo = grace.cosmo.update(platform_list)
			if removeCosmo:
				print("removed cosmo")
				grace.cosmo = None
		if space == True:
			frameCount += 1
			if frameCount == 3:
				space = False
				frameCount = 0
			if isinstance(grace.powerup, LaserGun):
				if frameCount == 1:
					bullet = grace.fire(channelList[4], laserFiring)
					if not bullet == None:
						bullet_list.add(bullet)
		if grace.win == True:
			print("Won! Win screen " + 'WIN' + str(lvl))
			if lvl == 1 or lvl == 2:
				return 'WIN' + str(lvl), lvl+1, score
		for enemy in enemy_list:
			removeEnemy = enemy.update()
			if removeEnemy:
				platform_list.remove(enemy)
		person_list.draw(screen)
		platform_list.draw(screen)
		bullet_list.draw(screen)
		if not grace.powerup == None:
			screen.blit(grace.powerup.image, grace.powerup.rect)
		if not grace.cosmo == None:
			screen.blit(grace.cosmo.image, grace.cosmo.rect)
		clock.tick(30)
		pygame.display.flip()
		
#################### Create Content #######################

# Fields needed for running program
running = True
# state = 'START'
state = 'TUTORIAL'
# state = 'LEVEL1'
# state = 'LEVEL2'
# state = 'LEVEL3'
# state = 'END'
lvls = 1
score = 0

# Create a screen (width, height)
screenx = 960
screeny = 720
screen = pygame.display.set_mode((screenx, screeny))
pygame.display.set_caption('Robo-Dog Rescue')

# Clock
clock = pygame.time.Clock()

# Creating channels to play music
channelList = []
for i in range(8):
	channelList.append(pygame.mixer.Channel(i))

# Create sound objects
jumpMusic = pygame.mixer.Sound("jump.wav")
mainMusic = pygame.mixer.Sound("maintitletheme.wav")
backgroundMusic = pygame.mixer.Sound("Varun - RoboDog Rescue 135 No Rythm.wav")
woofwoof = pygame.mixer.Sound("woofwoof.wav")
buttonMusic = pygame.mixer.Sound("optionselect2.wav")
glassBreaking = pygame.mixer.Sound("glassbreak.wav")
laserFiring = pygame.mixer.Sound("laser.wav")
zapMusic = pygame.mixer.Sound("zap.wav")
levelmusic = pygame.mixer.Sound('songs1and2.wav')
coinMusic = pygame.mixer.Sound("coin.wav")
powerupMusic = pygame.mixer.Sound("powerup.wav")


while running:
	if state == 'START':
		state = start()
	if state == 'TUTORIAL':
		state = tutorial()
	if state == 'PROLOGUE':
		state = prologue()
	if state == 'CUTSCENE':
		state = cutscene()
	# Win screen for levels
	if state == 'WIN1':
		state = win(2, score)
	if state == 'WIN2':
		state = win(3, score)
	# Three losing states of levels
	if state == 'LOSE1':
		state = lose(1)
	if state == 'LOSE2':
		state = lose(2)
	if state == 'LOSE3':
		state = lose(3)
	# Levels
	if state == 'LEVEL1':
		score = 0
		state, lvl, score = level(1)
		if lvl > lvls:
			lvls = lvl
	if state == 'LEVEL2':
		score = 0
		state, lvl, score = level(2)
		if lvl > lvls:
			lvls = lvl
	if state == 'LEVEL3':
		score = 0
		state, lvl, score = level(3)
		if lvl > lvls:
			lvls = lvl
	# Controls for game
	if state == 'CONTROLS':
		state = controls()
	# Select level screen
	if state == 'SELECTLEVEL':
		state = selectlevel(lvls)
	# End of the game
	if state == 'END':
		state = end()
	# Credits
	if state == 'CREDITS':
		state, lvls = credits()
