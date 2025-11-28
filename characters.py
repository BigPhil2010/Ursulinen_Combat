# In this file, all information for characters such as speed, gravity or Sprites are stored
import pygame


##########Rittmann##########
keyset_RITT = {
    "left": pygame.K_a,
    "right": pygame.K_d,
    "jump": pygame.K_w,
    "hit": pygame.K_SPACE
}

spritesheet_LO_RITT = {
    "run": [[0, 0, 7, 0], 15, True],
    "idle": [[0, 1, 1, 1], 5, True],
    "jump": [[0, 3, 5, 3], 5, False],
    "hit_run": [[0, 4, 7, 4], 30, False],
    "hit_idle": [[0, 2, 7, 2], 20, False],
}

RITT = {
    
    "name": "Rittmann",
    "hp": 100,
    "hp_bar": None,
    "sprite": None,
    "flipped_sprite": None,
    "sprite_sheet": pygame.image.load(r"recources/images/sprites/png/rittmann.png"),
    "sprite_sheet_layout": spritesheet_LO_RITT,
    "animation": "run",
    "hit": False,
    "damage": 10,
    "damage_done": False,
    #animations
    "run": [],
    "idle": [],
    "jump": [],
    "hit_run": [],
    "hit_idle": [],
    "frame": 0,
    "cooldown": 30,
    "cooldown_count": 0,
    "looking_left": False,
    "keyset": keyset_RITT,
    "rect": None,
    "start_x": 0,
    "start_y": 0,
    "width": 32,
    "height": 32,
    "collision_top": False,
    "collision_bottom": False,
    "collision_left": False,
    "collision_right": False,
    "speed": 1,
    "gravity": 1,
    "jump_power": 1,
    "jump_frames": 30,
    "jump_frames_count": 0
}


##########Kienast##########
keyset_KIEN = {
    "left": pygame.K_LEFT,
    "right": pygame.K_RIGHT,
    "jump": pygame.K_UP,
    "hit": pygame.K_RETURN
}

spritesheet_LO_KIEN = {
    "run": [[0, 0, 7, 0], 15, True],
    "idle": [[0, 1, 1, 1], 5, True],
    "jump": [[0, 2, 5, 2], 5, False],
    "hit_run": [[0, 3, 7, 3], 30, False],
    "hit_idle": [[0, 4, 1, 4], 30, False],
}

KIEN = {
    "name": "Kienast",
    "hp": 100,
    "hp_bar": None,
    "sprite": None,
    "flipped_sprite": None,
    "sprite_sheet": pygame.image.load(r"recources/images/sprites/png/kienast.png"),
    "sprite_sheet_layout": spritesheet_LO_KIEN,
    "animation": "run",
    "hit": False,
    "damage": 10,
    "damage_done": False,
    #animations
    "run": [],
    "idle": [],
    "jump": [],
    "hit_run": [],
    "hit_idle": [],
    "frame": 0,
    "cooldown": 50,
    "cooldown_count": 0,
    "looking_left": True,
    "keyset": keyset_KIEN,
    "rect": None,
    "start_x": 480,
    "start_y": 0,
    "width": 32,
    "height": 32,
    "collision_top": False,
    "collision_bottom": False,
    "collision_left": False,
    "collision_right": False,
    "speed": 1,
    "gravity": 1,
    "jump_power": 1,
    "jump_frames": 30,
    "jump_frames_count": 0
}

##########LIST##########
character_list = {
    "RITT": RITT,
    "KIEN": KIEN
}