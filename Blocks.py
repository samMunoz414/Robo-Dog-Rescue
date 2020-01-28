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

# Poweup class: it's a powerup class
class LaserGun(Powerup):
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
		if isFacingRight:
			self.movex = 16
		else:
			self.movex = -16

	def update(self, platforms):
		self.rect.x += self.movex
		if self.rect.x < 0 or self.rect.x > 960:
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

# Poweup class: it's a powerup class
class LightningRod(Powerup):
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

# Poweup class: it's a powerup class
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
        