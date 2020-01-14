# Robo-Dog Rescue
# January 13, 2020

# Imports
import sys
import pygame
import os
from Characters import Enemy
from Blocks import Platform

# Class for levels of the game
class Level():
    # Create enemies for a level
    def enemy(lvl, enemyx, enemyy):
        if lvl == 1:
            print("Level " + str(lvl))
            enemy = Enemy('tall_red.png', enemyx, enemyy)
            enemy_list = pygame.sprite.Group() # Create enemy group
            enemy_list.add(enemy)
            
        if lvl == 2:
            print("Level " + str(lvl))
            
        return enemy_list
    
    # Make a ground for the program
    def floor(lvl):
        floor_list = pygame.sprite.Group()
        i = 0
        if lvl == 1:
            print ("Level " + str(lvl))
            for i in range(16):
                block = Platform("block1_60x60.png", i*60, 660)
                floor_list.add(block)
        
        if lvl == 2:
            print ("Level " + str(lvl))
            
        return floor_list
    
    # Make a platform for the game
    def platform(lvl):
        platform_list = pygame.sprite.Group()
        if lvl == 1:
            print ("Level " + str(lvl))
            for i in range(4):
                block = Platform("block1_60x60.png", (i+3)*60, 480)
                platform_list.add(block)
            for i in range(5):
                block = Platform("block1_60x60.png", (i+7)*60, 300)
                platform_list.add(block)
            
        if lvl == 2:
            print ("Level " + str(lvl))
            
        return platform_list