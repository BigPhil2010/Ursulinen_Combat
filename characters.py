# In this file, all information for characters such as speed, gravity or Sprites are stored
import pygame


##########Rittmann##########

spritesheet_LO_RITT = {
    "run": [[0, 0, 7, 0], 15, True],
    "idle": [[0, 1, 1, 1], 5, True],
    "jump": [[0, 3, 5, 3], 5, False],
    "hit_run": [[0, 4, 7, 4], 25, False],
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
    "looking_left": None,
    "keyset": None,
    "rect": None,
    "start_x": None,
    "start_y": None,
    "width": 32,
    "height": 32,
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

spritesheet_LO_KIEN = {
    "run": [[0, 0, 7, 0], 15, True],
    "idle": [[0, 1, 1, 1], 5, True],
    "jump": [[0, 2, 5, 2], 5, False],
    "hit_run": [[0, 3, 7, 3], 15, False],
    "hit_idle": [[0, 4, 1, 4], 5, False],
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
    "damage": 0.5,
    "damage_done": False,
    #animations
    "run": [],
    "idle": [],
    "jump": [],
    "hit_run": [],
    "hit_idle": [],
    "frame": 0,
    "cooldown": 0,
    "cooldown_count": 0,
    "looking_left": None,
    "keyset": None,
    "rect": None,
    "start_x": None,
    "start_y": None,
    "width": 32,
    "height": 32,
    "collision_bottom": False,
    "collision_left": False,
    "collision_right": False,
    "speed": 0.85,
    "gravity": 1,
    "jump_power": 1,
    "jump_frames": 30,
    "jump_frames_count": 0
}


##########Mutke##########

spritesheet_LO_MUTK = {
    "run": [[0, 0, 7, 0], 15, True],
    "idle": [[0, 1, 1, 1], 5, True],
    "jump": [[0, 3, 5, 3], 5, False],
    "hit_run": [[0, 4, 6, 4], 15, False],
    "hit_idle": [[0, 2, 7, 2], 20, False],
}

MUTK = {
    "name": "Mutke",
    "hp": 100,
    "hp_bar": None,
    "sprite": None,
    "flipped_sprite": None,
    "sprite_sheet": pygame.image.load(r"recources/images/sprites/png/mutke.png"),
    "sprite_sheet_layout": spritesheet_LO_MUTK,
    "animation": "run",
    "hit": False,
    "damage": 15,
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
    "looking_left": None,
    "keyset": None,
    "rect": None,
    "start_x": None,
    "start_y": None,
    "width": 32,
    "height": 32,
    "collision_bottom": False,
    "collision_left": False,
    "collision_right": False,
    "speed": 0.7,
    "gravity": 1,
    "jump_power": 1,
    "jump_frames": 30,
    "jump_frames_count": 0
}

##########Hammes##########

spritesheet_LO_HMMS = {
    "run": [[0, 0, 7, 0], 15, True],
    "idle": [[0, 1, 1, 1], 5, True],
    "jump": [[0, 3, 5, 3], 5, False],
    "hit_run": [[0, 4, 7, 4], 25, False],
    "hit_idle": [[0, 2, 7, 2], 20, False],
}

HMMS = {
    "name": "Hammes",
    "hp": 100,
    "hp_bar": None,
    "sprite": None,
    "flipped_sprite": None,
    "sprite_sheet": pygame.image.load(recources/images/sprites/png/Hammes.png),
    "sprite_sheet_layout": spritesheet_LO_HMMS,
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
    "looking_left": None,
    "keyset": None,
    "rect": None,
    "start_x": None,
    "start_y": None,
    "width": 32,
    "height": 32,
    "collision_bottom": False,
    "collision_left": False,
    "collision_right": False,
    "speed": 1,
    "gravity": 1,
    "jump_power": 1,
    "jump_frames": 30,
    "jump_frames_count": 0
}

##########Hamme##########

spritesheet_LO_HMME = {
    "run": [[0, 0, 7, 0], 15, True],
    "idle": [[0, 1, 1, 1], 5, True],
    "jump": [[0, 3, 5, 3], 5, False],
    "hit_run": [[0, 4, 7, 4], 25, False],
    "hit_idle": [[0, 2, 7, 2], 20, False],
}

HMME = {
    "name": "Hamme",
    "hp": 100,
    "hp_bar": None,
    "sprite": None,
    "flipped_sprite": None,
    "sprite_sheet": pygame.image.load(recources/images/sprites/png/Hamme.png),
    "sprite_sheet_layout": spritesheet_LO_HMME,
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
    "looking_left": None,
    "keyset": None,
    "rect": None,
    "start_x": None,
    "start_y": None,
    "width": 32,
    "height": 32,
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
    "KIEN": KIEN,
    "MUTK": MUTK,
    "HMMS": HMMS,
    "HMME": HMME
}
