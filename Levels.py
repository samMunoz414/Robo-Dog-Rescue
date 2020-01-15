# Robo-Dog Rescue
# January 13, 2020

# Imports
import sys
import pygame
import os
from Characters import Enemy
from Blocks import *

# Class for levels of the game
class Level():
    # sets basic variables
    def  __init__(self):
        self.lvl = 1
        self.screenCount = 1
        self.totalScreenCount = 2

    # returns the current level
    def getLvl(self):
        return self.lvl

    # allows the level to be reset
    def setLvl(self, lvl):
        self.lvl = lvl

    def getScreenCount(self):
        return self.screenCount

    # increases the screen count value by one
    def incrementScreenCount(self):
        self.screenCount += 1

    # decreases the screen count value by one
    def decrementScreenCount(self):
        self.screenCount -= 1

    def getTotalScreenCount(self):
        return self.totalScreenCount

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
    
    def powerups(lvl):
    	powerups_list = pygame.sprite.Group()
    	if lvl == 1:
    		print("Level 1")
    		for i in range(3):
    			gear = Gear(((i+22)*60)+10, 70)
    			powerups_list.add(gear)
    	return powerups_list

    # Make a ground for the program
    def floor(lvl):
        floor_list = pygame.sprite.Group()
        if lvl == 1:
            print ("Level " + str(lvl))
            for i in range(32):
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
            for i in range(3):
                block = Platform("block1_60x60.png", (i+3)*60, 480)
                platform_list.add(block)
            for i in range(3):
                block = Platform("block1_60x60.png", (i+6)*60, 300)
                platform_list.add(block)
            for i in range(3):
                block = Platform("block1_60x60.png", (i+9)*60, 480)
                platform_list.add(block)
            for i in range(5):
                block = Platform("block1_60x60.png", (i+22)*60, 480)
                platform_list.add(block)
            for i in range(3):
                block = Platform("block1_60x60.png", (i+19)*60, 300)
                platform_list.add(block)
            for i in range(3):
                block = Platform("block1_60x60.png", (i+22)*60, 120)
                platform_list.add(block)
            for i in range(32):
                block = Platform("block1_60x60.png", i*60, -60)
                platform_list.add(block)
            for i in range(12):
                block = Platform("block1_60x60.png", -60, i*60)
                platform_list.add(block)
            for i in range(12):
                block = Platform("block1_60x60.png", 1920, i*60)
                platform_list.add(block)
            
        if lvl == 2:
            print ("Level " + str(lvl))
            
        return platform_list