from sys import exit
import pygame

pygame.init()

gameClock = pygame.time.Clock()

resolution = r_width, r_height = (500,500)

screen = pygame.display.set_mode( resolution )

spider = pygame.image.load("Spider.png").convert_alpha()
broom = pygame.image.load("Broom.png").convert_alpha()
spiderRect = spider.get_rect()
broomRect = broom.get_rect()

spiderRect = pygame.Rect( (r_width/2 - spiderRect.width/2, r_height/2 - spiderRect.height/2), (spiderRect.width,spiderRect.height) )
	
screen.fill( (255,255,255) )
pygame.display.update()

refresh = []
while True:
	for event in pygame.event.get():
		if event.type == pygame.MOUSEMOTION:
			screen.fill( (255,255,255), broomRect)
		if event.type == pygame.MOUSEBUTTONDOWN:
			exit()
		if event.type == pygame.KEYDOWN:
			exit()
		if event.type == pygame.QUIT:
			exit()
	
	screen.blit(spider, spiderRect)
	pygame.display.update(spiderRect)
	
	if pygame.mouse.get_focused():
		# erases old image
		pygame.mouse.set_visible(False)
		
		# draws new image
		mousePosition = pygame.mouse.get_pos()
		broomRect = pygame.Rect( (mousePosition[0] - broomRect.width/2, mousePosition[1] - broomRect.height/2), (broomRect.width, broomRect.height) )
		screen.blit(broom, broomRect)
		pygame.display.update()			
		
	gameClock.tick(30)
	
		