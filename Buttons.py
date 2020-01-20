# Robo-Dog-Rescue
# January 16, 2020

import os
import sys
import pygame

# class that creates buttons
class Button:
	# buttons with no images
	def __init__(self, posx, posy, width, height, state):
		self.rect = pygame.Rect((posx, posy), (width, height))
		self.state = state

	# # buttons with images
	# def __init__(self, image, posx, posy):
	# 	self.image = pygame.image.load(image).convert_alpha()
	# 	self.rect = self.image.get_rect()
	# 	self.rect.move_ip((posx, posy))

	# checks if the mouses position interlaps with button's position
	def isClicked(self, mousePosition):
		return self.rect.collidepoint(mousePosition)

    # testing merging method one
    def event(self):
        pass
