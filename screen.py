# In this file, all information for the screen is stored

import pygame

#screensize
screen_hight = 256
screen_width = 512
game_scale = 2

#setup screen
screen = pygame.display.set_mode((screen_width*game_scale, screen_hight*game_scale))
pygame.display.set_caption('UrsulinenCombat')