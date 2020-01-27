# Robo-Dog Rescue
# January 13, 2020

# Imports
import sys
import pygame
import os
from Characters import *
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
            enemy_list.add(Enemy('LeftFacingBlackScientist.png', 'RightFacingBlackScientist.png', 500, 601))
            # Second screen
            enemy_list.add(Enemy('LeftFacingBlackScientist.png', 'RightFacingBlackScientist.png', 1350, 241))
            enemy_list.add(Enemy('LeftFacingBlackScientist.png', 'RightFacingBlackScientist.png', 1600, 601))
            
        if lvl == 1:
            # First screen
            enemy_list.add(Enemy('LeftFacingBlackScientist.png', 'RightFacingBlackScientist.png', 680, 601))
            enemy_list.add(Enemy('LeftFacingBlackScientist.png', 'RightFacingBlackScientist.png', 560, 61))
            # Second screen
            enemy_list.add(Enemy('LeftFacingBlackScientist.png', 'RightFacingBlackScientist.png', 1150, 421))
            enemy_list.add(Enemy('LeftFacingBlackScientist.png', 'RightFacingBlackScientist.png', 1570, 421))
            # Third screen
            enemy_list.add(Enemy('LeftFacingBlackScientist.png', 'RightFacingBlackScientist.png', 2420, 421))
            enemy_list.add(Enemy('LeftFacingBlackScientist.png', 'RightFacingBlackScientist.png', 2580, 601))
            # Fourth screen
            enemy_list.add(Enemy('LeftFacingBlackScientist.png', 'RightFacingBlackScientist.png', 3350, 601))
            enemy_list.add(Enemy('LeftFacingBlackScientist.png', 'RightFacingBlackScientist.png', 3200, 601))
            enemy_list.add(Enemy('LeftFacingBlackScientist.png', 'RightFacingBlackScientist.png', 2950, 241))

        if lvl == 2:
            # First screen
            enemy_list.add(Enemy('LeftFacingBlackScientist.png', 'RightFacingBlackScientist.png', 560, 570))
            enemy_list.add(Enemy('LeftFacingBlackScientist.png', 'RightFacingBlackScientist.png', 310, 390))
            enemy_list.add(Enemy('tall_red.png', 560, 570))
            enemy_list.add(Enemy('tall_red.png', 310, 390))
            # Second screen
            enemy_list.add(Enemy('tall_red.png', 1200, 30))
            enemy_list.add(Enemy('tall_red.png', 1040, 210))
            # Third screen
            enemy_list.add(Enemy('tall_red.png', 2360, 210))
            enemy_list.add(Enemy('tall_red.png', 2600, 390))
            # Fourth screen
            enemy_list.add(Enemy('tall_red.png', 3320, 570))
            enemy_list.add(Enemy('tall_red.png', 3420, 210))
            enemy_list.add(Enemy('tall_red.png', 3060, 30))

        if lvl == 3:
            # First screen
            enemy_list.add(Enemy('tall_red.png', 190, 390))
            enemy_list.add(Enemy('tall_red.png', 420, 390))
            # Second screen
            enemy_list.add(Enemy('tall_red.png', 1560, 30))
            # Third screen
            enemy_list.add(Enemy('tall_red.png', 2060, 390))
            enemy_list.add(Enemy('tall_red.png', 2600, 390))
            # Fourth screen
            enemy_list.add(Enemy('tall_red.png', 3080, 390))
            enemy_list.add(Enemy('tall_red.png', 3220, 210))
            enemy_list.add(Enemy('tall_red.png', 3520, 390))
            # Fifth screen
            enemy_list.add(Enemy('tall_red.png', 4060, 390))
            enemy_list.add(Enemy('tall_red.png', 4340, 210))
            enemy_list.add(Enemy('tall_red.png', 4200, 570))
            # Sixth screen
            enemy_list.add(Enemy('tall_red.png', 4920, 390))
            enemy_list.add(Enemy('tall_red.png', 5300, 210))
            enemy_list.add(Enemy('tall_red.png', 5100, 210))
            enemy_list.add(Enemy('tall_red.png', 5360, 30))
            enemy_list.add(Enemy('tall_red.png', 5540, 390))
            enemy_list.add(Enemy('tall_red.png', 5180, 570))
            enemy_list.add(Enemy('tall_red.png', 5280, 570))
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
            powerups_list.add(LightningRodBlock(490, 250))
            # for i in range(25):
            # 	powerups_list.add(Gear(100, 610))
            powerups_list.add(LaserGunBlock(100, 610))

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
            powerups_list.add(LaserGunBlock(2290, 70))
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
            powerups_list.add(LightningRod(190,70))
            # Second screen
            for i in range(2):
                powerups_list.add(Gear(((i+17)*60)+10, 250))
                powerups_list.add(Gear(((i+9)*180)+10, 250))
            for i in range(3):
                powerups_list.add(Gear(((i+22)*60)+10, 70))
            for i in range(5):
                powerups_list.add(Gear(((i+22)*60)+10, 430))
                powerups_list.add(Gear(((i+23)*60)+10, 610))
            # Third screen
            for i in range(2):
                powerups_list.add(Gear(((i+34)*60)+10, 70))
                powerups_list.add(Gear(((i+37)*60)+10, 70))
                powerups_list.add(Gear(((i+18)*120)+10, 430))
            for i in range(3):
                powerups_list.add(Gear(((i+42)*60)+10, 430))
                powerups_list.add(Gear(((i+38)*60)+10, 250))
            powerups_list.add(LaserGun(2170, 70))
            # Fourth screen
            for i in range(3):
                powerups_list.add(Gear(((i+50)*60)+10, 70))
                powerups_list.add(Gear(((i+59)*60)+10, 250))
                powerups_list.add(Gear(((i+59)*60)+10, 610))
            for i in range(2):
                powerups_list.add(Gear(((i+27)*120)+10, 430))
            for i in range(4):
                powerups_list.add(Gear(((i+52)*60)+10, 610))

        if lvl == 3:
            # First screen
            for i in range(4):
                powerups_list.add(Gear(((i+8)*60)+10, 250))
                powerups_list.add(Gear(((i+11)*60)+10, 610))
            for i in range(2):
                powerups_list.add(Gear(((i+2)*60)+10, 430))
                powerups_list.add(Gear(((i+9)*120)+10, 430))
            powerups_list.add(LightningRod(250, 430))
            # Second screen
            for i in range(5):
                powerups_list.add(Gear(((i+21)*60)+10, 250))
            for i in range(3):
                powerups_list.add(Gear(((i+28)*60)+10, 70))
            for i in range(6):
                powerups_list.add(Gear(((i+19)*60)+10, 610))
            for i in range(2):
                powerups_list.add(Gear(((i+30)*60)+10, 610))
            # Third screen
            for i in range(4):
                powerups_list.add(Gear(((i+35)*60)+10, 610))
            for i in range(2):
                powerups_list.add(Gear(((i+39)*60)+10, 250))
                powerups_list.add(Gear(((i+34)*60)+10, 430))
            for i in range(3):
                powerups_list.add(Gear(((i+42)*60)+10, 430))
            powerups_list.add(LaserGun(2380, 60))
            # Fourth screen
            for i in range(2):
                powerups_list.add(Gear(((i+49)*60)+10, 610))
                powerups_list.add(Gear(((i+60)*60)+10, 430))
            for i in range(3):
                powerups_list.add(Gear(((i+50)*60)+10, 430))
                powerups_list.add(Gear(((i+56)*60)+10, 250))
            for i in range(4):
                powerups_list.add(Gear(((i+55)*60)+10, 610))
            # Fifth screen
            for i in range(2):
                powerups_list.add(Gear(((i+33)*120)+10, 250))
                powerups_list.add(Gear(((i+68)*60)+10, 430))
                powerups_list.add(Gear(((i+70)*60)+10, 70))
            for i in range(3):
                powerups_list.add(Gear(((i+72)*60)+10, 250))
            for i in range(4):
                powerups_list.add(Gear(((i+67)*60)+10, 610))
                powerups_list.add(Gear(((i+73)*60)+10, 610))
            # Sixth screen
            for i in range(3):
                powerups_list.add(Gear(((i+85)*60)+10, 250))
            for i in range(2):
                powerups_list.add(Gear(((i+89)*60)+10, 70))

        return powerups_list

    # Make a ground for the program
    def floor(lvl):
        floor_list = pygame.sprite.Group()
        if lvl == 0:
            for i in range(32): # 2 screens of floor blocks
                floor_list.add(Platform("block1_60x60.png", i*60, 660))

        if lvl == 1 or lvl == 2:
            # Used for levels 1 and 2
            for i in range(64): # 4 screens of floor blocks
                floor_list.add(Platform("block1_60x60.png", i*60, 660))

        if lvl == 3:
            # Used for level 3
            for i in range(96):
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
            
        if lvl == 1 or lvl == 2:
            # Ceiling blocks
            for i in range(64):
                platform_list.add(Platform("tempblock.png", i*60, -60))
            # Block off beginning of game
            for i in range(12):
                platform_list.add(Platform("tempblock.png", -60, i*60))

        if lvl == 3:
            # Ceiling blocks
            for i in range(96):
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
            # Spikes for all screens
            platform_list.add(Spike(300, 640))
            platform_list.add(Spike(840, 460))
            platform_list.add(Spike(1680, 280))
            platform_list.add(Spike(1740, 280))
            platform_list.add(Spike(1680, 640))
            platform_list.add(Spike(1740, 640))
            platform_list.add(Spike(1800, 640))
            platform_list.add(Spike(2220, 460))
            platform_list.add(Spike(3300, 460))
            for i in range(5):
                platform_list.add(Spike(((i+45)*60)+10, 640))
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
            # Second screen
            for i in range(4):
                platform_list.add(Platform("tempblock.png", (i+17)*60, 300))
            for i in range(5):
                platform_list.add(Platform("tempblock.png", (i+22)*60, 480))
            for i in range(5):
                platform_list.add(Platform("tempblock.png", (i+20)*60, 120))
            for i in range(4):
                platform_list.add(Platform("tempblock.png", (i+27)*60, 300))
            # Third screen
            for i in range(5):
                platform_list.add(Platform("tempblock.png", (i+34)*60, 120))
            for i in range(3):
                platform_list.add(Platform("tempblock.png", (i+36)*60, 480))
            for i in range(5):
                platform_list.add(Platform("tempblock.png", (i+38)*60, 300))
            for i in range(9):
                platform_list.add(Platform("tempblock.png", (i+42)*60, 480))
            # Fourth screen
            for i in range(5):
                platform_list.add(Platform("tempblock.png", (i+50)*60, 120))
            for i in range(3):
                platform_list.add(Platform("tempblock.png", (i+54)*60, 480))
            for i in range(5):
                platform_list.add(Platform("tempblock.png", (i+57)*60, 300))

        if lvl == 3:
            # Spikes for all screens
            for i in range(9):
                platform_list.add(Spike((i+2)*60, 640))
            platform_list.add(Spike(1140, 460))
            platform_list.add(Spike(1200, 280))
            platform_list.add(Spike(1560, 280))
            for i in range(3):
                platform_list.add(Spike((i+26)*60, 640))
            platform_list.add(Spike(2280, 280))
            platform_list.add(Spike(2460, 280))
            for i in range(5):
                platform_list.add(Spike((i+41)*60, 640))
            for i in range(4):
                platform_list.add(Spike((i+51)*60, 640))
                platform_list.add(Spike((i+59)*60, 640))
            platform_list.add(Spike(4020, 280))
            for i in range(3):
                platform_list.add(Spike((i+73)*60, 460))
            for i in range(5):
                platform_list.add(Spike((i+81)*60, 640))
            for i in range(4):
                platform_list.add(Spike((i+92)*60, 640))
            # First screen
            for i in range(9):
                platform_list.add(Platform("tempblock.png", (i+2)*60, 480))
            for i in range(4):
                platform_list.add(Platform("tempblock.png", (i+8)*60, 300))
            # Second screen
            for i in range(3):
                platform_list.add(Platform("tempblock.png", (i+18)*60, 480))
            for i in range(7):
                platform_list.add(Platform("tempblock.png", (i+20)*60, 300))
            for i in range(5):
                platform_list.add(Platform("tempblock.png", (i+26)*60, 120))
            # Third screen
            for i in range(4):
                platform_list.add(Platform("tempblock.png", (i+34)*60, 480))
            for i in range(5):
                platform_list.add(Platform("tempblock.png", (i+42)*60, 480))
            for i in range(4):
                platform_list.add(Platform("tempblock.png", (i+38)*60, 300))
            # Fourth screen
            for i in range(5):
                platform_list.add(Platform("tempblock.png", (i+50)*60, 480))
            for i in range(5):
                platform_list.add(Platform("tempblock.png", (i+54)*60, 300))
            for i in range(4):
                platform_list.add(Platform("tempblock.png", (i+59)*60, 480))
            # Fifth screen
            for i in range(3):
                platform_list.add(Platform("tempblock.png", (i+66)*60, 300))
            for i in range(3):
                platform_list.add(Platform("tempblock.png", (i+68)*60, 480))
            for i in range(2):
                platform_list.add(Platform("tempblock.png", (i+70)*60, 120))
            for i in range(3):
                platform_list.add(Platform("tempblock.png", (i+73)*60, 480))
            for i in range(4):
                platform_list.add(Platform("tempblock.png", (i+72)*60, 300))
            for i in range(8):
                platform_list.add(Platform("tempblock.png", (i+78)*60, 480))
            # Sixth screen
            for i in range(7):
                platform_list.add(Platform("tempblock.png", (i+85)*60, 300))
            for i in range(4):
                platform_list.add(Platform("tempblock.png", (i+89)*60, 120))
            for i in range(2):
                platform_list.add(Platform("tempblock.png", (i+94)*60, 120))
            for i in range(4):
                platform_list.add(Platform("tempblock.png", (i+92)*60, 480))
            
        return platform_list