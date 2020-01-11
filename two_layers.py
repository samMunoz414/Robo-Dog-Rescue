# Author: Samuel Munoz
# Date: 01-09-2020

import pygame
from sys import exit

# loads pygame modules
pygame.init()

# creates a screen to display the game (this is our background layer)
screen = pygame.display.set_mode( (600, 600) )
screen.fill( (255, 255, 255) )
pygame.display.update()

# -------- creates a foreground layer (this is an image) to the screen --------
# creates a Surface object to draw stuff on
foreground = pygame.Surface( (500, 500), pygame.SRCALPHA ) # https://stackoverflow.com/questions/328061/how-to-make-a-surface-with-a-transparent-background-in-pygame
# makes the foreground visible on the screen
foreground.set_alpha(255)
# converts the Surface into an image
foregroundRect = foreground.get_rect()
# ----------------------------------------------------------------------------

# loading an image
dog = pygame.image.load("dog.png").convert_alpha()
dogRect = dog.get_rect()
foreground.blit(dog, dogRect)

# draw the Surface object onto the screen
screen.blit(foreground, foregroundRect)
pygame.display.update(foregroundRect)

# add clock to game
clock = pygame.time.Clock()

while True:

	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			exit()	
		if event.type == pygame.QUIT:
			exit()
			
		# pygame.display.update(foregroundRect)
		clock.tick(30)