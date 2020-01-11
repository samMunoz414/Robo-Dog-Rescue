# Author: Samuel Munoz
# Date: 01-11-2020

import pygame
from sys import exit

# starting up the pygame module 
pygame.init()

try:
    pygame.font.init()
except:
    print("Fonts unavailable")
    exit()

# not used, but useful for later use: this method prints every font type that pygame has stored
def printAllFonts():
	fonts = pygame.font.get_fonts()
	for oneFont in fonts: 
		print(oneFont)

screen = pygame.display.set_mode( (600, 600) )
screen.fill( (255, 255, 255) )

# class that creates buttons
class Button:
	# draws circle on screen and stores the rect object of circle
	def __init__(self, imageName, buttonPosition, dogPosition):
		self.image = pygame.image.load(imageName).convert_alpha()
		self.imageRect = self.image.get_rect()
		self.imageRect.move_ip(buttonPosition)
		self.dogImage = pygame.image.load("dog.png").convert_alpha()
		self.dogImageRect = self.image.get_rect()
		self.dogPosition = dogPosition
		screen.blit(self.image, self.imageRect)

	# checks if the mouses position interlaps with button's position
	def isClicked(self, mousePosition):
		return self.imageRect.collidepoint(mousePosition)

	# runs the event that occurs when the button has been pressed
	def event(self):
		screen.blit(self.dogImage, self.dogPosition)

# creating two buttons and storing them in a list
buttons = []
coffeeButton = Button( "coffee-cup.gif", (540, 5), (0, 397)) # http://www.afactor.net/adapted/20x20/20cuppa.gif
buttons.append(coffeeButton)
pinButton = Button( "pin.gif", (570, 5), (351, 397)) # http://www.afactor.net/adapted/20x20/20pin.gif
buttons.append(pinButton)

# update the screen to show the drawings
pygame.display.update()

while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == ord('q'):
				exit()

		# checks if a button has been clicked
		if event.type == pygame.MOUSEBUTTONUP:
			mousePosition = pygame.mouse.get_pos()
			for button in buttons:
				if button.isClicked(mousePosition):
					button.event()
		# source: https://stackoverflow.com/questions/10990137/pygame-mouse-clicking-detection#10992212

		if event.type == pygame.QUIT:
			exit()

		pygame.display.update()
