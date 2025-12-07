# In this file, all information for the screen is stored
import pygame
import json

#screensize
screen_hight = 256
screen_width = 512
game_scale = 1

#load gamescale
with open("settings.json", "r", encoding="utf-8") as file:
    settigs = json.load(file)
    game_scale = settigs["gamescale"]

#setup screen
screen = pygame.display.set_mode((screen_width*game_scale, screen_hight*game_scale))
pygame.display.set_caption('UrsulinenCombat')