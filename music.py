import pygame
from sys import exit
from sys import argv

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode( (100, 100) )

channel = pygame.mixer.Channel(0)
music = pygame.mixer.Sound(argv[1])

channel.play(music, loops=-1)
while True:
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			exit()