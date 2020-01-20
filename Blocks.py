 # Robo-Dog-Rescue
# January 14, 2020

# NOTE: Much of the code is copied from the stackoverflow thread located here: https://stackoverflow.com/questions/14354171/add-scrolling-to-a-platformer-in-pygame

# Imports
import sys
import pygame
import os

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
		self.image = pygame.image.load("SpikeFiller.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = xpos
		self.rect.y = ypos

class Powerup(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        print("Ran")

# Poweup class: it's a powerup class
class LaserGun(Powerup):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.image = pygame.image.load("orange_block_40x40.png").convert()
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

    # update method here if needed for later development
    def update(self):
    	pass

# Poweup class: it's a powerup class
class LightningRod(Powerup):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.image = pygame.image.load("pink_block_40x40.png").convert()
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
        self.image = pygame.image.load("block4_40x40.png").convert()
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

    # update method here if needed for later development
    def update(self):
        pass

# Poweup class: it's a powerup class
class Cosmo(Powerup):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.image = pygame.image.load("block4_40x40.png").convert()
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = xpos
        self.rect.y = ypos

    # update method here if needed for later development
    def update(self):
        pass