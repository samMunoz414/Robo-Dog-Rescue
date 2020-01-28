 # Robo-Dog-Rescue
# January 14, 2020

# NOTE: Much of the code is copied from the stackoverflow thread located here: https://stackoverflow.com/questions/14354171/add-scrolling-to-a-platformer-in-pygame

# Imports
import sys
import pygame
import os
import Characters

# Class for platform blocks
class Platform(pygame.sprite.Sprite):
    def __init__(self, image, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

    # update method here if needed for later development
    def update(self):
     	pass

class Spike(pygame.sprite.Sprite):
	def __init__(self, xpos, ypos):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("spikes.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = xpos
		self.rect.y = ypos

class Powerup(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class LaserGun(pygame.sprite.Sprite):
	def __init__(self, xpos, ypos, facingRight, ammo):
		pygame.sprite.Sprite.__init__(self)
		self.image = None
		self.loadImage(facingRight)
		self.rect = self.image.get_rect()
		self.isFacingRight = facingRight
		self.ammo = ammo
		if facingRight:
			self.rect.x = xpos + 17
		else:
			self.rect.x = xpos - 27
		self.rect.y = ypos + 28

	def update(self, playerX, playerY, facingRight, space, platforms, channel, zapMusic):
		if not self.isFacingRight == facingRight:
			self.loadImage(facingRight)
			self.isFacingRight = facingRight
		if facingRight:
			self.rect.x = playerX + 17
		else:
			self.rect.x = playerX - 27
		self.rect.y = playerY + 28

	def loadImage(self, facingRight):
		if facingRight:
			self.image = pygame.image.load("LaserGunRight.png").convert_alpha()
		else:
			self.image = pygame.image.load("LaserGunLeft.png").convert_alpha()


# Poweup class: it's a powerup class
class LaserGunBlock(Powerup):
    def __init__(self, xpos, ypos, ammo=10):
        super().__init__()
        self.image = pygame.image.load("powerupGreen.png").convert()
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
        self.ammo = ammo

    # update method here if needed for later development
    def update(self):
    	pass

class RedBullet(Powerup):
	def __init__(self, xpos, ypos, isFacingRight):
		super().__init__()
		self.image = pygame.image.load("redGunProjectile.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.width = self.rect.height = 7
		self.rect.x = xpos
		self.rect.y = ypos
		self.distanceTraveled = 0
		if isFacingRight:
			self.movex = 16
		else:
			self.movex = -16

	def update(self, platforms):
		self.rect.x += self.movex
		self.distanceTraveled += self.movex
		if self.rect.x < 0 or self.rect.x > 960:
			return True
		elif self.distanceTraveled >= 200 or self.distanceTraveled <= -200:
			return True
		return self.collide(platforms)

	def collide(self, platforms):
		for block in platforms:
			if pygame.sprite.collide_rect(self, block):
				if isinstance(block, Characters.Enemy):
					block.state = "death animation"
					return True
				if isinstance(block, Platform):
					return True
		return False

class LightningRod(pygame.sprite.Sprite):
	def __init__(self, xpos, ypos, facingRight, space):
		pygame.sprite.Sprite.__init__(self)
		self.image = None
		self.imageSwap = [
			# facing left
			# left is space = False, right is space = True
			["TazerLeftUp.png", "TazerLeftDown.png"],
			# facing right
			["TazerRightUp.png", "TazerRightDown.png"]
		]		
		self.image = None
		self.rect = None
		self.imageName = ""
		self.loadImage(facingRight, space)
		self.isFacingRight = facingRight
		self.lastSpace = space
		
		if self.imageName == "TazerLeftUp.png":
			self.rect.x = xpos - 25
			self.rect.y = ypos + 6
		elif self.imageName == "TazerLeftDown.png":
			self.rect.x = xpos - 44
			self.rect.y = ypos + 29
		elif self.imageName == "TazerRightUp.png":
			self.rect.x = xpos + 17
			self.rect.y = ypos + 6
		elif self.imageName == "TazerRightDown.png":
			self.rect.x = xpos + 17
			self.rect.y = ypos + 29

	def update(self, playerX, playerY, facingRight, space, platforms, channel, zapMusic):
		if not self.isFacingRight == facingRight or not self.lastSpace == space:
			self.loadImage(facingRight, space)
			self.isFacingRight = facingRight
			self.lastSpace = space

		if self.imageName == "TazerLeftUp.png":
			self.rect.x = playerX - 25
			self.rect.y = playerY + 6
		elif self.imageName == "TazerLeftDown.png":
			self.rect.x = playerX - 44
			self.rect.y = playerY + 29
		elif self.imageName == "TazerRightUp.png":
			self.rect.x = playerX + 17
			self.rect.y = playerY + 6
		elif self.imageName == "TazerRightDown.png":
			self.rect.x = playerX + 17
			self.rect.y = playerY + 29
		if space:
			self.collide(platforms, channel, zapMusic)


	def collide(self, platforms, channel, zapMusic):
		for block in platforms:
			if pygame.sprite.collide_rect(self, block):
				if isinstance(block, Characters.Enemy):
					channel.play(zapMusic)
					block.state = "death animation"

	def loadImage(self, facingRight, space):
		self.image = pygame.image.load(self.imageSwap[int(facingRight)][int(space)]).convert_alpha()
		self.rect = self.image.get_rect()
		if space:
			self.rect.width = 58
			self.rect.height = 8
		else:
			self.rect.width = 39
			self.rect.height = 35
		self.imageName = self.imageSwap[int(facingRight)][int(space)]

# Poweup class: it's a powerup class
class LightningRodBlock(Powerup):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.image = pygame.image.load("powerupBlue.png").convert_alpha()
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

    # update method here if needed for later development
    def update(self):
        pass

# Poweup class: it's a powerup class
class Gear(Powerup):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.image = pygame.image.load("coin.png").convert_alpha()
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

    # update method here if needed for later development
    def update(self):
        pass

# Defines Cosmo object
class Cosmo(Powerup):
    def __init__(self, xpos, ypos, isFacingRight):
        super().__init__()
        if isFacingRight:
        	self.image = pygame.image.load("CosmoRight1.png").convert_alpha()
        	self.rect = self.image.get_rect()
        	self.movex = 16
        	self.rect.x = xpos + 31
        else:
        	self.image = pygame.image.load("CosmoLeft1.png").convert_alpha()
        	self.rect = self.image.get_rect()
        	self.movex = -16
        	self.rect.x = xpos
        self.rect.y = ypos + 52
        self.rect.width = 51
        self.rect.height = 35
        self.animation = True

    def update(self, platforms):
    	self.rect.x += self.movex
    	if self.movex > 0:
    		if self.animation == True:
    			self.image = pygame.image.load("CosmoRight1.png").convert_alpha()
    		else:
    			self.image = pygame.image.load("CosmoRight2.png").convert_alpha()
    	else:
    		if self.animation == True:
    			self.image = pygame.image.load("CosmoLeft1.png").convert_alpha()
    		else:
    			self.image = pygame.image.load("CosmoLeft2.png").convert_alpha()
    	self.animation = not self.animation

    	if self.rect.x < 0 or self.rect.x > 960:
    		return True 
    	return self.collide(platforms)

    def collide(self, platforms):
    	for block in platforms:
    		if pygame.sprite.collide_rect(self, block):
    			if isinstance(block, Platform):
    				print("hit block")
    				return True
    			elif isinstance(block, Characters.Enemy):
    				block.state = "death animation"
    	return False
        