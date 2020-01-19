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
            print("Level 0")
            enemy = Enemy('tall_red.png', 500, 570)
            enemy_list.add(enemy)
            enemy = Enemy('tall_red.png', 1400, 390)
            enemy_list.add(enemy)
            
        if lvl == 1:
            print("Level 1")
            enemy = Enemy('tall_red.png', 620, 570)
            enemy_list.add(enemy)
            enemy = Enemy('tall_red.png', 560, 30)
            enemy_list.add(enemy)
            
        return enemy_list
    
    def powerups(lvl):
        powerups_list = pygame.sprite.Group()
        if lvl == 0:
            print("Level 0")
            for i in range(3):
                gear = Gear(((i+22)*60)+10, 70)
                powerups_list.add(gear)
            lightingrod = LightningRod(800, 600)
            powerups_list.add(lightingrod)
            lasergun = LaserGun(430, 250)
            powerups_list.add(lasergun)
        if lvl == 1:
            print("Level 1")
            for i in range(4):
                gear1 = Gear(((i+3)*60)+10, 430)
                gear2 = Gear(((i+3)*60)+10, 610)
                powerups_list.add(gear1)
                powerups_list.add(gear2)
            for i in range(2):
                gear1 = Gear(((i+6)*60)+10, 250)
                gear2 = Gear(((i+9)*60)+10, 250)
                powerups_list.add(gear1)
                powerups_list.add(gear2)
            for i in range(3):
                gear1 = Gear(((i+10)*60)+10, 610)
                gear2 = Gear(((i+9)*60)+10, 70)
                powerups_list.add(gear1)
                powerups_list.add(gear2)
            lightingrod = LightningRod(490, 250)
            powerups_list.add(lightingrod)
        return powerups_list

    # Make a ground for the program
    def floor(lvl):
        floor_list = pygame.sprite.Group()
        if lvl == 0:
            print ("Level 0")
            for i in range(32): # 2 screens of floor blocks
                block = Platform("block1_60x60.png", i*60, 660)
                floor_list.add(block)
        if lvl == 1:
            print ("Level 1")
            for i in range(64): # 4 screens of floor blocks
                block = Platform("block1_60x60.png", i*60, 660)
                floor_list.add(block)
        return floor_list
    
    # Make a platform for the game
    def platform(lvl):
        platform_list = pygame.sprite.Group()
        if lvl == 0:
            print ("Level 0")
            for i in range(32): # Ceiling blocks
                block = Platform("block1_60x60.png", i*60, -60)
                platform_list.add(block)
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
            for i in range(12):
                block = Platform("block1_60x60.png", -60, i*60)
                platform_list.add(block)
            for i in range(12):
                block = Platform("block1_60x60.png", 1920, i*60)
                platform_list.add(block)
            
        if lvl == 1:
            print ("Level 1")
            for i in range(64):
                block = Platform("block1_60x60.png", i*60, -60)
                platform_list.add(block)
            for i in range(4):
                block = Platform("block1_60x60.png", (i+3)*60, 480)
                platform_list.add(block)
            for i in range(5):
                block = Platform("block1_60x60.png", (i+6)*60, 300)
                platform_list.add(block)
            for i in range(4):
                block = Platform("block1_60x60.png", (i+9)*60, 120)
                platform_list.add(block)
            for i in range(3):
                block = Platform("block1_60x60.png", (i+11)*60, 480)
                platform_list.add(block)
            
        return platform_list