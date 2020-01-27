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
		self.image = pygame.image.load("spikeFiller.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = xpos
		self.rect.y = ypos

class Powerup(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class LaserGun(pygame.sprite.Sprite):
	def __init__(self, xpos, ypos, facingRight):
		pygame.sprite.Sprite.__init__(self)
		self.image = None
		self.loadImage(facingRight)
		self.rect = self.image.get_rect()
		self.isFacingRight = facingRight
		if facingRight:
			self.rect.x = xpos + 43 
		else:
			self.rect.x = xpos - 14
		self.rect.y = ypos + 28

	def update(self, playerX, playerY, facingRight, space, platforms):
		if not self.isFacingRight == facingRight:
			self.loadImage(facingRight)
			self.isFacingRight = facingRight
		if facingRight:
			self.rect.x = playerX + 43
		else:
			self.rect.x = playerX - 14
		self.rect.y = playerY + 28


	def loadImage(self, facingRight):
		if facingRight:
			self.image = pygame.image.load("LaserGunRight.png").convert_alpha()
		else:
			self.image = pygame.image.load("LaserGunLeft.png").convert_alpha()


# Poweup class: it's a powerup class
class LaserGunBlock(Powerup):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.image = pygame.image.load("powerupGreen.png").convert()
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

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
					platforms.remove(block)
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
			self.rect.x = xpos - 10
			self.rect.y = ypos + 5
		elif self.imageName == "TazerLeftDown.png":
			self.rect.x = xpos - 10
			self.rect.y = ypos + 29
		elif self.imageName == "TazerRightUp.png":
			self.rect.x = xpos + 43
			self.rect.y = ypos + 5
		elif self.imageName == "TazerRightDown.png":
			self.rect.x = xpos + 47
			self.rect.y = ypos + 29

	def update(self, playerX, playerY, facingRight, space, platforms):
		if not self.isFacingRight == facingRight or not self.lastSpace == space:
			self.loadImage(facingRight, space)
			self.isFacingRight = facingRight
			self.lastSpace = space

		if self.imageName == "TazerLeftUp.png":
			self.rect.x = playerX - 10
			self.rect.y = playerY + 5
		elif self.imageName == "TazerLeftDown.png":
			self.rect.x = playerX - 30
			self.rect.y = playerY + 29
		elif self.imageName == "TazerRightUp.png":
			self.rect.x = playerX + 45
			self.rect.y = playerY + 5
		elif self.imageName == "TazerRightDown.png":
			self.rect.x = playerX + 47
			self.rect.y = playerY + 29
		self.collide(platforms)


	def collide(self, platforms):
		for block in platforms:
			if pygame.sprite.collide_rect(self, block):
				if isinstance(block, Characters.Enemy):
					platforms.remove(block)

	def loadImage(self, facingRight, space):
		self.image = pygame.image.load(self.imageSwap[int(facingRight)][int(space)]).convert_alpha()
		self.rect = self.image.get_rect()
		if space:
			self.rect.width = 30
			self.rect.height = 6
		else:
			self.rect.width = 12
			self.rect.height = 35
		self.imageName = self.imageSwap[int(facingRight)][int(space)]

# Poweup class: it's a powerup class
class LightningRodBlock(Powerup):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.image = pygame.image.load("powerupBlue.png").convert()
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
        self.image = pygame.image.load("coin.png").convert()
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
        	self.movex = 16
        else:
        	self.image = pygame.image.load("CosmoLeft1.png").convert_alpha()
        	self.movex = -16
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos
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
    			if isinstance(block, Characters.Enemy):
    				platforms.remove(block)
    			if isinstance(self, Platform):
    				return True
    	return False
        