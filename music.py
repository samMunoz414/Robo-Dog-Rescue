import pygame
from sys import exit
from time import sleep

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode( (100,100) )

channelOne = pygame.mixer.Channel(0)
channelTwo = pygame.mixer.Channel(1)
mainMusic = pygame.mixer.Sound("maintitletheme.wav")
buttonMusic = pygame.mixer.Sound("optionselect2.wav")

channelOne.play(mainMusic, loops=-1)
while True:
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			channelTwo.play(buttonMusic)
			sleep(1)
			channelOne.stop()
			channelTwo.stop()
			exit()