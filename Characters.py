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
		self.image = pygame.image.load(image).convert_alpha()
		# stores player's rect object
		self.rect = self.image.get_rect()
		# sets starting position for character
		self.rect.x = xpos
		self.rect.y = ypos
		self.rect.width = 31
		self.rect.height = 87
		# stores the number of gears the player has
		self.gearCount = 0
		# Object holding powerup object
		self.powerup = None
		# object holding cosmo when activiated
		self.cosmo = None
		# boolean tracks recent powerup changes
		self.recentPowerupChange = False
		# stores the life state of the player
		self.isAlive = True
		# stores if the player is alive
		self.win = False
		# animation boolean
		self.animation = True
		# boolean storing what direction Grace is facing
		self.isFacingRight = True
		# constant 3D array to store all image names
		self.imageSwap = [ # [P][M][A]
			# powerup 'None'
			[
				# moving left
				[
					# left: animation True; right: animation False
					"assets/GraceLeft1.png", "assets/GraceLeft2.png", 
				],
				# moving right
				[
					# left: animation True; right: animation False
					"assets/GraceRight1.png", "assets/GraceRight2.png"
				],
			],

			# powerup not 'None'
			[
				# moving left
				[
					# left: animation True; right: animation False
					"assets/GraceLeft1MissingArm.png", "assets/GraceLeft2MissingArm.png", 
				],
				# moving right
				[
					# left: animation True; right: animation False
					"assets/GraceRight1MissingArm.png", "assets/GraceRight2MissingArm.png"
				],
			]
		]

	# Handles any updates based on keyboard inputs and 
	# up -> boolean storing if the player moves up
	# down -> boolean storing if the player moves up
	# left -> boolean storing if the player moves up
	# right -> boolean storing if the player moves up
	# platforms -> list storing all the platforms
	def update(self, up, down, left, right, space, powerup, level, platforms, channel, jumpMusic, coinMusic, powerupMusic, zapMusic):
		if up:
			# only jumps if the player is on the ground
			if self.isOnGround:
				self.movey -= 20
				channel[1].play(jumpMusic)
		# if the down button if pressed 
		if down:
			pass
		if left and not right:
			self.movex = -8
		elif right and not left:
			self.movex = 8
		# sets velocity to zero when either the left or right key are pressed
		elif not (left or right):
			self.movex = 0
		if not self.isOnGround:
			# this is gravity
			self.movey += 1
			# caps max velocity in the y direction
			if self.movey > 100:
				self.movey = 100

		if powerup == False:
			self.recentPowerupChange = False

		# increments in the x direction
		self.rect.left += self.movex
		# handles collisions in the x direction
		self.collide(self.movex, 0, space, powerup, platforms, channel, coinMusic, powerupMusic)
		# increments in the y direction
		self.rect.top += self.movey
		# assuming player is in the air
		self.isOnGround = False
		# handles collisions in the y direction
		self.collide(0, self.movey, space, powerup, platforms, channel, coinMusic, powerupMusic)

		# Changes the image of Grace
		self.changeImage(left, right, space)

		# updates the weapon variable
		if not self.powerup == None:
			self.powerup.update(self.rect.x, self.rect.y, self.isFacingRight, space, platforms, channel[4], zapMusic)
		
		# Scrolling screen: move everything a screen width to left or right
		if self.rect.x <= 10 and level.screenCount > 1:
			level.decrementScreenCount()
			self.rect.x = 870
			for p in platforms:
				p.rect.x = p.rect.x + 960
			print("screen count: " + str(level.screenCount))
		if self.rect.x >= 920 and level.screenCount < level.totalScreenCount:
			level.incrementScreenCount()
			self.rect.x = 30
			for p in platforms:
				p.rect.x = p.rect.x - 960
			print("screen count: " + str(level.screenCount))

		if self.rect.x >= 920 and level.screenCount == level.totalScreenCount:
			self.win = True
        
	def mapPowerup(self):
		if isinstance(self.powerup, type(None)):
			return 0
		elif isinstance(self.powerup, LightningRod) or isinstance(self.powerup, LaserGun):
			return 1

	def mapMotion(self, left, right):
		if left and not right:
			self.isFacingRight = False
			return 0
		elif not left and right:
			self.isFacingRight = True
			return 1
		else:
			if not self.isFacingRight:
				return 0
			else:
				return 1

	def changeImage(self, left, right, space):
		powerup = self.mapPowerup()
		motion = self.mapMotion(left, right)
		imageName = self.imageSwap[powerup][motion][int(self.animation)]
		self.image = pygame.image.load(imageName).convert_alpha()
		if self.isOnGround == True and not (not left and not right):
			self.animation = not self.animation

	def createNewPowerup(self, blockType, xpos, ypos):
		if isinstance(blockType, LightningRod):
			return LightningRodBlock(xpos, ypos)
		elif isinstance(blockType, LaserGun):
			return LaserGunBlock(xpos, ypos, self.powerup.ammo)

	def incrementGear(self):
		if self.gearCount < 100:
			self.gearCount += 1

	def fire(self, channel, music):
		if self.powerup.ammo <= 0:
			self.powerup = None
			return None
		else:
			self.powerup.ammo -= 1
			if self.powerup.ammo == 0:
				self.powerup = None
				self.rect.width = 31
			if self.isFacingRight == True:
				channel.play(music)
				return RedBullet(self.rect.x + self.rect.width + 26, self.rect.y + 26, self.isFacingRight)
			else:
				channel.play(music)
				return RedBullet(self.rect.x - 30, self.rect.y + 26, self.isFacingRight)


	def activateCosmo(self, channel, music):
		if self.gearCount >= 25:
			self.gearCount -= 25
			channel.play(music)
			self.cosmo = Cosmo(self.rect.x, self.rect.y, self.isFacingRight)

	def collide(self, dx, dy, space, powerup, platforms, channel, coinMusic, powerupMusic):
		for block in platforms:
			if pygame.sprite.collide_rect(self, block):
				if isinstance(block, LightningRodBlock):
					if powerup:
						channel[2].play(powerupMusic)
						if isinstance(self.powerup, type(None)):
							self.powerup = LightningRod(self.rect.x, self.rect.y, self.isFacingRight, space)
							platforms.remove(block)
						else:
							if self.recentPowerupChange == False:
								platforms.add(self.createNewPowerup(self.powerup, block.rect.x, block.rect.y))
								self.powerup = LightningRod(self.rect.x, self.rect.y, self.isFacingRight, space)
								platforms.remove(block)
								self.recentPowerupChange = True
					return

				if isinstance(block, LaserGunBlock):
					if powerup:
						channel[2].play(powerupMusic)
						if isinstance(self.powerup, type(None)):
							self.powerup = LaserGun(self.rect.x, self.rect.y, self.isFacingRight, block.ammo)
							platforms.remove(block)
						else:
							if self.recentPowerupChange == False:
								platforms.add(self.createNewPowerup(self.powerup, block.rect.x, block.rect.y))
								self.powerup = LaserGun(self.rect.x, self.rect.y, self.isFacingRight, block.ammo)
								platforms.remove(block)
								self.recentPowerupChange = True
					return

				if isinstance(block, Gear):
					self.incrementGear()
					channel[3].play(coinMusic)
					platforms.remove(block)
					return

				if isinstance(block, Enemy):
					if block.state == "alive":
						self.isAlive = False
					return

				if isinstance(block, Spike):
					self.isAlive = False
					return

				# ------------ Hitting Walls ---------------------
				# collision occured when players was moving right
				if dx > 0:
					self.rect.right = block.rect.left
				# collision occured when players was moving left
				if dx < 0:
					self.rect.left = block.rect.right
				# collision occured when players was moving down
				if dy > 0:
					self.rect.bottom = block.rect.top
					self.isOnGround = True
					self.movey = 0
				# collision occured when players was moving up
				if dy < 0:
					self.rect.top = block.rect.bottom
					self.movey = 0
				# ----------------------------------------------
        
# Class for enemy scientists
class Enemy(pygame.sprite.Sprite):
    def __init__(self, leftImage, rightImage, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)
        self.leftImage = leftImage
        self.rightImage = rightImage
        self.isRight = True
        self.image = pygame.image.load(rightImage).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.rect.width = 37
        self.rect.height = 59
        self.counter = 0
        self.state = "alive"
        self.frameCount = 0

    def update(self):
    	if self.state == "alive":
    		self.move()
    		return False
    	elif self.state == "death animation":
    		self.deathAnimation()
    		return False
    	elif self.state == "dead":
    		return True
    
    # Control automated movement of enemy
    def move(self):
        # These variables can be changed to fine-tune game
        distance = 15
        speed = 10
        
        if self.counter >= 0 and self.counter <= distance:
            if self.isRight == False:
            	self.image = pygame.image.load(self.rightImage).convert_alpha()
            	self.isRight = True
            self.rect.x += speed
        elif self.counter >= distance and self.counter <= distance*2:
            if self.isRight == True:
            	self.image = pygame.image.load(self.leftImage).convert_alpha()
            	self.isRight = False
            self.rect.x -= speed
        else:
            self.counter = 0
            
        self.counter += 1

    def deathAnimation(self):
    	if self.frameCount == 0:
    		self.image = pygame.image.load("assets/DeadBlackScientist.png").convert_alpha()
    	self.frameCount += 1
    	if self.frameCount == 15:
    		self.state = "dead"
