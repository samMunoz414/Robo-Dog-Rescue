# Robo-Dog-Rescue
# January 16, 2020

import os
import sys
import pygame

# class that creates buttons
class Button:
	# buttons with no images
	def __init__(self, position, width, height):
		self.rect = pygame.Rect(position, (width, height))

	# buttons with images
	def __init__(self, image, position):
		self.image = pygame.image.load(image).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.move_ip(buttonPosition)

	# checks if the mouses position interlaps with button's position
	def isClicked(self, mousePosition):
		return self.rect.collidepoint(mousePosition)