# Robo-Dog-Rescue
# January 14, 2020 

# NOTE: Much of the code is copied from the stackoverflow thread located here: https://stackoverflow.com/questions/14354171/add-scrolling-to-a-platformer-in-pygame

# Imports
import sys
import pygame
import os
from Blocks import *
from Levels import *

# Class for protagonist
class Person(pygame.sprite.Sprite):
	def __init__(self, image, xpos, ypos):
		pygame.sprite.Sprite.__init__(self)
		# velocity in the x direction
		self.movex = 0
		# velocity in the y direction
		self.movey = 0 
		# boolean storing if the character is on the ground
		self.isOnGround = False
		# stores player's image
		self.image = pygame.image.load("tall_blue.png").convert_alpha()
		# stores player's rect object
		self.rect = pygame.Rect(xpos, ypos, 60, 90)
		# stores the number of gears the player has
		self.gearCount = 0
		# string holding what powerup the character is holding on to. choices: 'none', 'lighting rod', 'laser gun', 'cosmo'
		self.heldPowerup = "none"
		# boolean storing if the powerup state of the player changed
		self.powerupChange = False
		# stores the life state of the player
		self.isAlive = True

	# Handles any updates based on keyboard inputs and 
	# up -> boolean storing if the player moves up
	# down -> boolean storing if the player moves up
	# left -> boolean storing if the player moves up
	# right -> boolean storing if the player moves up
	# platforms -> list storing all the platforms
	def update(self, up, down, left, right, collect_powerup, level, platforms):
		if up:
			# only jumps if the player is on the ground
			if self.isOnGround:
				self.movey -= 20
		# if the down button if pressed 
		if down:
			pass
		if left:
			self.movex = -8
		if right:
			self.movex = 8
		if not self.isOnGround:
			# this is gravity
			self.movey += 1
			# caps max velocity in the y direction
			if self.movey > 100:
				self.movey = 100
		if not (left or right):
			self.movex = 0

		# increments in the x direction
		self.rect.left += self.movex
		# handles collisions in the x direction
		self.collide(self.movex, 0, collect_powerup, platforms)
		# increments in the y direction
		self.rect.top += self.movey
		# assuming player is in the air
		self.isOnGround = False
		# handles collisions in the y direction
		self.collide(0, self.movey, collect_powerup, platforms)
		# changes the player's image
		self.updatePlayerImage()
		
		# Scrolling screen: move everything a screen width to left or right
		if self.rect.x <= 10 and level.screenCount > 1:
			level.decrementScreenCount()
			self.rect.x = 870
			for p in platforms:
				p.rect.x = p.rect.x + 960
			print("screen count: " + str(level.screenCount))
		if self.rect.x >= 900 and level.screenCount < level.totalScreenCount:
			level.incrementScreenCount()
			self.rect.x = 30
			for p in platforms:
				p.rect.x = p.rect.x - 960
			print("screen count: " + str(level.screenCount))

	def updatePlayerImage(self):
		if self.powerupChange:
			if self.heldPowerup == "none":
				self.image = pygame.image.load("tall_blue.png").convert_alpha()
			if self.heldPowerup == "lighting rod":
				self.image = pygame.image.load("Player/PlayerLightingRod.png").convert_alpha()
			if self.heldPowerup == "laser gun":
				self.image = pygame.image.load("Player/PlayerLaserGun.png").convert_alpha()
			self.powerupChange = False
        
	def powerupChange(self):
		pass


	def incrementGear(self):
		if self.gearCount < 100:
			self.gearCount += 1
			print("Gear Count: " + str(self.gearCount))

	def collide(self, dx, dy, collect_powerup, platforms):
		for block in platforms:
			if pygame.sprite.collide_rect(self, block):
				if isinstance(block, LightingRod):
					if collect_powerup:
						self.heldPowerup = "lighting rod"
						self.powerupChange = True
						platforms.remove(block)
					return

				if isinstance(block, LaserGun):
					if collect_powerup:
						self.heldPowerup = "laser gun"
						self.powerupChange = True
						platforms.remove(block)
					return

				if isinstance(block, Gear):
					self.incrementGear()
					platforms.remove(block)
					return

				if isinstance(block, Enemy):
					self.isAlive = False
					return

				# ------------ Hitting Walls ---------------------
				# collision occured when players was moving right
				if dx > 0:
					self.rect.right = block.rect.left
					print("collide right")
				# collision occured when players was moving left
				if dx < 0:
					self.rect.left = block.rect.right
					print("collide left")
				# collision occured when players was moving down
				if dy > 0:
					self.rect.bottom = block.rect.top
					self.isOnGround = True
					self.movey = 0
					print("collide top")
				# collision occured when players was moving up
				if dy < 0:
					self.rect.top = block.rect.bottom
					self.movey = 0
					print("collide bottom")
				# ----------------------------------------------

        
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
        distance = 15
        speed = 10
        
        if self.counter >= 0 and self.counter <= distance:
            self.rect.x += speed
        elif self.counter >= distance and self.counter <= distance*2:
            self.rect.x -= speed
        else:
            self.counter = 0
            
        self.counter += 1
