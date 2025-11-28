# In this file, all information for maps such as backgrounds, gravity or borders are stored
import pygame

forum = {
    "background": pygame.image.load(r"recources/images/backgrounds/png/Forum.png"),
    "background_scale": 2,
    "plattforms": [
                    pygame.Rect(0, 200, 512, 12),
                    pygame.Rect(0, -1, 512, 1),
                    pygame.Rect(-1, 0, 1, 256),
                    pygame.Rect(513, 0, 1, 256),

                    pygame.Rect(50, 135, 50, 1)
                ],
    "speed": 2,
    "gravity": 3
}

##########LIST##########
maps_list = {
    "forum": forum
}