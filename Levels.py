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
        # self.lvl = 1
        self.screenCount = 1
        self.totalScreenCount = 2

    # # allows the level to be reset
    # def setLvl(self, lvl):
    #     self.lvl = lvl

    def setTotalScreenCount(self, count):
        self.totalScreenCount = count

    # increases the screen count value by one
    def incrementScreenCount(self):
        self.screenCount += 1

    # decreases the screen count value by one
    def decrementScreenCount(self):
        self.screenCount -= 1

    # Create enemies for a level
    def enemy(lvl):
        enemy_list = pygame.sprite.Group() # Create enemy group
        if lvl == 0:
            # First screen
            enemy_list.add(Enemy('tall_red.png', 500, 570))
            # Second screen
            enemy_list.add(Enemy('tall_red.png', 1350, 210))
            enemy_list.add(Enemy('tall_red.png', 1600, 570))
            
        if lvl == 1:
            # First screen
            enemy_list.add(Enemy('tall_red.png', 680, 570))
            enemy_list.add(Enemy('tall_red.png', 560, 30))
            # Second screen
            enemy_list.add(Enemy('tall_red.png', 1150, 390))
            enemy_list.add(Enemy('tall_red.png', 1570, 390))
            # Third screen
            enemy_list.add(Enemy('tall_red.png', 2420, 390))
            enemy_list.add(Enemy('tall_red.png', 2580, 570))
            # Fourth screen
            enemy_list.add(Enemy('tall_red.png', 3350, 570))
            enemy_list.add(Enemy('tall_red.png', 3200, 30))
            enemy_list.add(Enemy('tall_red.png', 2950, 210))

        if lvl == 2:
            # First screen
            enemy_list.add(Enemy('tall_red.png', 560, 570))
            enemy_list.add(Enemy('tall_red.png', 310, 390))
            
        return enemy_list
    
    def powerups(lvl):
        powerups_list = pygame.sprite.Group()
        if lvl == 0:
            for i in range(3):
                powerups_list.add(Gear(((i+24)*60)+10, 70))
            powerups_list.add(LightningRod(1090, 430))
            powerups_list.add(LaserGun(430, 250))

        if lvl == 1:
            # First screen
            for i in range(4):
                powerups_list.add(Gear(((i+3)*60)+10, 430))
                powerups_list.add(Gear(((i+3)*60)+10, 610))
                powerups_list.add(Gear(((i+9)*60)+10, 610))
            for i in range(2):
                powerups_list.add(Gear(((i+6)*60)+10, 250))
                powerups_list.add(Gear(((i+9)*60)+10, 250))
                powerups_list.add(Gear(((i+9)*60)+10, 70))
            powerups_list.add(LightningRod(490, 250))
            # Second screen
            for i in range(2):
                powerups_list.add(Gear(((i+18)*60)+10, 430))
                powerups_list.add(Gear(((i+25)*60)+10, 430))
            for i in range(4):
                powerups_list.add(Gear(((i+23)*60)+10, 610))
            for i in range(3):
                powerups_list.add(Gear(((i+21)*60)+10, 70))
                powerups_list.add(Gear(((i+23)*60)+10, 250))
            # Third screen
            for i in range(2):
                powerups_list.add(Gear(((i+17)*120)+10, 430))
                powerups_list.add(Gear(((i+36)*60)+10, 70))
                powerups_list.add(Gear(((i+39)*60)+10, 70))
            for i in range(3):
                powerups_list.add(Gear(((i+34)*60)+10, 610))
                powerups_list.add(Gear(((i+41)*60)+10, 610))
                powerups_list.add(Gear(((i+42)*60)+10, 250))
            powerups_list.add(LaserGun(2290, 70))
            # Fourth screen
            for i in range(3):
                powerups_list.add(Gear(((i+49)*60)+10, 610))
                powerups_list.add(Gear(((i+53)*60)+10, 610))
                powerups_list.add(Gear(((i+56)*60)+10, 250))
            for i in range(2):
                powerups_list.add(Gear(((i+52)*60)+10, 70))
                powerups_list.add(Gear(((i+49)*60)+10, 250))
        if lvl == 2:
            # First screen
            for i in range(3):
                powerups_list.add(Gear(((i+2)*60)+10, 610))
                powerups_list.add(Gear(((i+11)*60)+10, 430))
            for i in range(2):
                powerups_list.add(Gear(((i+6)*60)+10, 610))
                powerups_list.add(Gear(((i+4)*60)+10, 430))
                powerups_list.add(Gear(((i+6)*60)+10, 250))
                powerups_list.add(Gear(((i+4)*60)+10, 70))
                powerups_list.add(Gear(((i+10)*60)+10, 250))
            powerups_list.add(LaserGun(190,70))

        return powerups_list

    # Make a ground for the program
    def floor(lvl):
        floor_list = pygame.sprite.Group()
        if lvl == 0:
            for i in range(32): # 2 screens of floor blocks
                floor_list.add(Platform("block1_60x60.png", i*60, 660))

        if lvl == 1 or lvl == 2 or lvl == 3:
            # Used for levels 1, 2 and 3
            for i in range(64): # 4 screens of floor blocks
                floor_list.add(Platform("block1_60x60.png", i*60, 660))
        return floor_list
    
    # Make a platform for the game
    def platform(lvl):
        platform_list = pygame.sprite.Group()
        if lvl == 0:
            # Ceiling blocks
            for i in range(32):
                platform_list.add(Platform("tempblock.png", i*60, -60))
            platform_list.add(Spike(180, 640))
            # First screen
            for i in range(3):
                platform_list.add(Platform("tempblock.png", (i+3)*60, 480))
            for i in range(3):
                platform_list.add(Platform("tempblock.png", (i+6)*60, 300))
            for i in range(3):
                platform_list.add(Platform("tempblock.png", (i+9)*60, 480))
            # Second screen
            for i in range(5):
                platform_list.add(Platform("tempblock.png", (i+21)*60, 300))
            for i in range(3):
                platform_list.add(Platform("tempblock.png", (i+17)*60, 480))
            for i in range(3):
                platform_list.add(Platform("tempblock.png", (i+24)*60, 120))
            # Block off beginning of game
            for i in range(12):
                platform_list.add(Platform("tempblock.png", -60, i*60))
            
        if lvl == 1 or lvl == 2 or lvl == 3:
            # Ceiling blocks
            for i in range(64):
                platform_list.add(Platform("tempblock.png", i*60, -60))
            # Block off beginning of game
            for i in range(12):
                platform_list.add(Platform("tempblock.png", -60, i*60))

        if lvl == 1:
            # Spikes
            platform_list.add(Spike(2100, 460))
            platform_list.add(Spike(3120, 640))
            # First screen
            for i in range(4):
                platform_list.add(Platform("tempblock.png", (i+3)*60, 480))
            for i in range(5):
                platform_list.add(Platform("tempblock.png", (i+6)*60, 300))
            for i in range(4):
                platform_list.add(Platform("tempblock.png", (i+9)*60, 120))
            # Second screen
            for i in range(5):
                platform_list.add(Platform("tempblock.png", (i+18)*60, 480))
            for i in range(3):
                platform_list.add(Platform("tempblock.png", (i+21)*60, 120))
            for i in range(3):
                platform_list.add(Platform("tempblock.png", (i+23)*60, 300))
            for i in range(5):
                platform_list.add(Platform("tempblock.png", (i+25)*60, 480))
            # Third screen
            for i in range(3):
                platform_list.add(Platform("tempblock.png", (i+34)*60, 480))
            for i in range(5):
                platform_list.add(Platform("tempblock.png", (i+36)*60, 120))
            for i in range(3):
                platform_list.add(Platform("tempblock.png", (i+42)*60, 300))
            for i in range(4):
                platform_list.add(Platform("tempblock.png", (i+40)*60, 480))
            # Fourth screen
            for i in range(5):
                platform_list.add(Platform("tempblock.png", (i+49)*60, 300))
            for i in range(5):
                platform_list.add(Platform("tempblock.png", (i+52)*60, 120))
            for i in range(3):
                platform_list.add(Platform("tempblock.png", (i+56)*60, 300))
            for i in range(4):
                platform_list.add(Platform("tempblock.png", (i+59)*60, 480))

        if lvl == 2:
            # Spikes
            platform_list.add(Spike(300, 640))
            platform_list.add(Spike(840, 460))
            # First screen
            for i in range(5):
                platform_list.add(Platform("tempblock.png", (i+4)*60, 480))
            for i in range(4):
                platform_list.add(Platform("tempblock.png", (i+11)*60, 480))
            for i in range(2):
                platform_list.add(Platform("tempblock.png", (i+6)*60, 300))
                platform_list.add(Platform("tempblock.png", (i+10)*60, 300))
            for i in range(3):
                platform_list.add(Platform("tempblock.png", (i+3)*60, 120))

        if lvl == 3:
            pass
            # First screen
            
        return platform_list