# In this file, all information for maps such as backgrounds, gravity or borders are stored
import pygame
import random

forum = {
    "background": pygame.image.load(r"recources/images/backgrounds/png/Forum.png"),
    "background_scale": 2,
    "plattforms": [
                    pygame.Rect(0, 200, 512, 12),
                    pygame.Rect(0, -4, 512, 1),
                    pygame.Rect(-1, 0, 1, 256),
                    pygame.Rect(513, 0, 1, 256),

                    pygame.Rect(50, 135, 50, 1)
                ],
    "P1_start_x": 0,
    "P1_start_y": 0,
    "P2_start_x": 480,
    "P2_start_y": 0,
    "speed": 2,
    "gravity": 3
}

klassenzimmer = {
    "background": pygame.image.load(r"recources/images/backgrounds/png/Klassenzimmer.png"),
    "background_scale": 2,
    "plattforms": [
                    pygame.Rect(0, 245, 512, 12),
                    pygame.Rect(0, -1, 512, 1),
                    pygame.Rect(-1, 0, 1, 256),
                    pygame.Rect(513, 0, 1, 256),

                    pygame.Rect(146, 183, 220, 1)
                ],
    "P1_start_x": 0,
    "P1_start_y": 0,
    "P2_start_x": 480,
    "P2_start_y": 0,
    "speed": 2,
    "gravity": 3
}

##########LIST##########
maps_list = {
    "forum": forum,
    "klassenzimmer": klassenzimmer
}

def random_map():
    index = random.randint(0, len(list(maps_list))-1)
    map_name = list(maps_list)[index]
    return map_name