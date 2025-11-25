import pygame    #this project runs on most versions of python 3.10
import time

pygame.init()
pygame.mixer.init()

######################### VARIABLES #########################

#screensize
screen_hight = 256
screen_width = 512
game_scale = 2
BG = None

#setup screen
screen = pygame.display.set_mode((screen_width*game_scale, screen_hight*game_scale))
pygame.display.set_caption('UrsulinenCombat')

#gamestates
clock = pygame.time.Clock()
run = True

#timer
game_duration = 60
timer = game_duration
start_time = time.time()

#setup FPS & delta time
FPS = 60
last_time = time.time()

#movement norms
speed = 2 * game_scale
gravity = 3 * game_scale

#keysets
keyset1 = {
    "left": pygame.K_a,
    "right": pygame.K_d,
    "jump": pygame.K_w,
    "hit": pygame.K_SPACE
}

keyset2 = {
    "left": pygame.K_LEFT,
    "right": pygame.K_RIGHT,
    "jump": pygame.K_UP,
    "hit": pygame.K_RETURN
}

#sprite sheet layout
spritesheetLO = {
    "run": [[0, 0, 7, 0], 15, True],
    "idle": [[0, 1, 1, 1], 5, True],
    "hit": [[0, 2, 7, 2], 30, False],
    "jump": [[0, 3, 5, 3], 5, False]
}
spritesheetLO2 = {
    "run": [[0, 0, 7, 0], 15, True],
    "idle": [[0, 1, 1, 1], 5, True],
    "jump": [[0, 2, 5, 2], 5, False],
    "hit_run": [[0, 3, 7, 3], 30, False],
    "hit_idle": [[0, 4, 1, 4], 30, False],
}

#player values
player1 = {
    "score": 0,
    "sprite": None,
    "flipped_sprite": None,
    "sprite_sheet": None,
    "sprite_sheet_layout": spritesheetLO2,
    "animation": "run",
    "hit": False,
    #animations
    "run": [],
    "idle": [],
    "jump": [],
    "hit_run": [],
    "hit_idle": [],
    "frame": 0,
    "cooldown": 60,
    "cooldown_count": 0,
    "looking_left": False,
    "keyset": keyset1,
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
    "jump_frames": 60,
    "jump_frames_count": 0
}

player2 = {
    "score": 0,
    "sprite": None,
    "flipped_sprite": None,
    "sprite_sheet": None,
    "sprite_sheet_layout": spritesheetLO2,
    "animation": "run",
    #animations
    "run": [],
    "idle": [],
    "jump": [],
    "hit": [],
    "frame": 0,
    "cooldown": 20,
    "cooldown_count": 0,
    "looking_left": False,
    "keyset": keyset2,
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

#set player rects
player1["rect"] = pygame.Rect(player1["start_x"]*game_scale, player1["start_y"]*game_scale, player1["width"]*game_scale, player1["height"]*game_scale)
player2["rect"] = pygame.Rect(player2["start_x"]*game_scale, player2["start_y"]*game_scale, player2["width"]*game_scale, player2["height"]*game_scale)


plattforms = [
    pygame.Rect(0, 257, 512, 1),
    pygame.Rect(0, -1, 512, 1),
    pygame.Rect(-1, 0, 1, 256),
    pygame.Rect(513, 0, 1, 256),

    pygame.Rect(62, 129, 379, 32)
]

#colors
black = (0, 0, 0)
white = (255, 255, 255)

#load fonts
pixelfont = pygame.font.Font(r"recources/fonts/Minecraft.ttf", 15*game_scale) 

#load images
test_sprite_sheet = pygame.image.load(r"recources/images/sprites/png/animation.png").convert_alpha()
test_BG = pygame.image.load(r"recources/images/backgrounds/png/test_BG.png").convert_alpha()
test_overlay = pygame.image.load(r"recources/images/overlays/png/Test_Overlay.png")

rittmann_sprite_sheet = pygame.image.load(r"recources/images/sprites/png/rittmann.png")
kinast_sprite_sheet = pygame.image.load(r"recources/images/sprites/png/kienast.png")

#load sounds
#sound = pygame.mixer.Sound("")
#sound.play()

#set spriteSheet
player1["sprite_sheet"] = kinast_sprite_sheet
player2["sprite_sheet"] = kinast_sprite_sheet


######################### FUNCTIONS #########################

#image processing
def get_image(sheet, sprite_x, sprite_y, width, height, scale):
    image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
    image.blit(sheet, (0, 0), (sprite_x * width, sprite_y * height, sprite_x * width + width, sprite_y * height + height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    return image

def flip_image(image):
    if image == None:
        return None
    else:
        return pygame.transform.flip(image, True, False)

def check_player_collision(player):

    #reset collision
    player["collision_left"] = False
    player["collision_right"] = False
    player["collision_top"] = False
    player["collision_bottom"] = False

    for plattform in plattforms:
        #check collision
        if player["rect"].colliderect(plattform):

            #overlap distance
            overlap_right = player["rect"].right - plattform.left
            overlap_left = plattform.right - player["rect"].left
            overlap_bottom = player["rect"].bottom - plattform.top
            overlap_top = plattform.bottom - player["rect"].top

            #get smallest overlap
            min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)

           

            #get ovl direction
            if min_overlap == overlap_right:
                player["collision_right"] = True

            elif min_overlap == overlap_left:
                player["collision_left"] = True

            elif min_overlap == overlap_bottom:
                player["collision_bottom"] = True

            elif min_overlap == overlap_top:
                player["collision_top"] = True
    if player["collision_top"]:
        player["jump_frames_count"] = 2

def toggle_num(x):
    if x == abs(x):
        return -x
    else:
        return abs(x)

def apply_gravity(object, delta):
    global gravity
    if object["collision_bottom"] == False and gravity*object["gravity"] == abs(gravity*object["gravity"]):
        object["rect"].y += gravity*object["gravity"] * delta
    elif object["collision_top"] == False and gravity*object["gravity"] != abs(gravity*object["gravity"]):
        object["rect"].y += gravity*object["gravity"] * delta

def jump(object):
    if object["jump_frames_count"] > 0:
        object["jump_frames_count"] -= 1
        if object["jump_frames_count"] == 1:
            object["gravity"] = abs(object["gravity"]/object["jump_power"])

def hit(player):
    if player["cooldown_count"] == 0:
        player["cooldown_count"] = player["cooldown"]
        player["hit"] = True

def check_input(player, delta):
    key = pygame.key.get_pressed() 
    key_just = pygame.key.get_pressed() 
    key_just_released = pygame.key.get_just_released()

    #check input jump
    if key_just[player["keyset"]["jump"]]:
        if player["collision_top"] == False:
            if player["collision_bottom"] == True:
                player["animation"] = "jump"
                player["gravity"] = -abs(player["gravity"]*player["jump_power"])
                player["jump_frames_count"] = player["jump_frames"]

    #check input left
    elif key[player["keyset"]["left"]]:
        #update animation
        player["looking_left"] = True
        if player["collision_bottom"] == True:
            if player["animation"] != "run":
                player["frame"] = 0
            player["animation"] = "run"
        #update position
        if player["collision_left"] == False:
            player["rect"].x -= speed*player["speed"] * delta

    #check input right
    elif key[player["keyset"]["right"]]:
        #update animation
        player["looking_left"] = False
        if player["collision_bottom"] == True:
            if player["animation"] != "run":
                player["frame"] = 0
            player["animation"] = "run"
        #update position
        if player["collision_right"] == False:
            player["rect"].x += speed*player["speed"] * delta

    #check input hit
    if key[player["keyset"]["hit"]]:
        if player["cooldown_count"] == 0:
            hit(player)

    if player["animation"] == "jump":
        if player["collision_bottom"] == False:
            player["animation"] = "jump"

    if not key[player["keyset"]["left"]]:
        if not key[player["keyset"]["right"]]:
            if not key[player["keyset"]["jump"]]:
                if not key[player["keyset"]["hit"]]:
                    if player["collision_bottom"]:
                            if player["animation"] != "idle":
                                player["frame"] = 0
                            player["animation"] = "idle"

def scale_plattforms(plattforms):
    scaled = []
    for plattform in plattforms:
        scaled_x = plattform.x * game_scale
        scaled_y = plattform.y * game_scale
        scaled_w = plattform.w * game_scale
        scaled_h = plattform.h * game_scale

        scaled.append(pygame.Rect(scaled_x, scaled_y, scaled_w, scaled_h))
    return scaled

def text_to_img(text, font, color, width, height):
    img = pygame.Surface((width * game_scale, height * game_scale), pygame.SRCALPHA).convert_alpha()
    font_img = font.render(str(text), True, color)
    font_width = font_img.get_width()
    font_height = font_img.get_height()
    font_x = (width * game_scale - font_width)/2
    font_y = (height * game_scale - font_height)/2
    img.blit(font_img, (font_x, font_y))
    return img

def timer_to_str(time):
    min = 0
    sec = time

    while sec >= 60:
        min += 1
        sec -= 60
    
    if len(str(sec)) == 1:
        return str(min) + ":0" + str(sec)
    else:
        return str(min) + ":" + str(sec)
    
def game_over():
    print("game Over")

def update_timer():
    global timer
    global start_time
    if timer > 0:
        current_time = time.time()
        time_over = current_time-start_time
        timer = round(game_duration-time_over)
    else:
        timer = 0
        game_over()
        
def set_sprites(player, animation):
    sprite_y = player["sprite_sheet_layout"][animation][0][1]
    sprites_x = []
    count = 0
    while count < player["sprite_sheet_layout"][animation][0][2]+1:
        sprites_x.append(count)
        count += 1
    for sprite_x in sprites_x:
        player[animation].append(get_image(player["sprite_sheet"], sprite_x, sprite_y, player["width"], player["height"], game_scale))

def update_sprites(player, animation):
    global FPS
    animation_playing = animation
    animation_fps = player["sprite_sheet_layout"][animation_playing][1]
    addition_per_frame = 1/FPS*animation_fps
    player["frame"] += addition_per_frame

    if player["hit"] == True: 
        if animation != "jump":
            animation_playing = str("hit_" + str(animation))
    else:
        animation_playing = animation
    
    loop = player["sprite_sheet_layout"][animation_playing][2]

    if player["frame"] >= player["sprite_sheet_layout"][animation_playing][0][2]+1:
        if loop == True:
            player["frame"] = 0
        else:
            player["animation"] = "idle"
            player["frame"] = 0
            player["hit"] = False

    player["sprite"] = player[animation_playing][int(player["frame"])]
    player["flipped_sprite"] = flip_image(player["sprite"])



#########################  UPDATE #########################

#set BG & OL
BG = get_image(test_BG, 0, 0, 512, 256, game_scale)
OL = get_image(test_overlay, 0, 0, 512, 256, game_scale)

#scale up plattforms
plattforms = scale_plattforms(plattforms)

#set sprites
set_sprites(player1, "run")
set_sprites(player1, "idle")
set_sprites(player1, "jump")
set_sprites(player1, "hit_run")
set_sprites(player1, "hit_idle")

set_sprites(player2, "run")
set_sprites(player2, "idle")
set_sprites(player2, "jump")

######################### GAMELOOP #########################

while run:
    #update player sprites
    update_sprites(player1, player1["animation"])
    #update_sprites(player2, player2["animation"])

    #messure delta time
    delta = time.time() - last_time
    delta *= FPS
    last_time = time.time()

    #reset screen
    screen.fill(white)
    screen.blit(BG, (0, 0))

    #draw plattforms
    for plattform in plattforms:
        pygame.draw.rect(screen, (0, 0, 0), plattform)

    #draw players
    if player1["looking_left"]:
        screen.blit(player1["flipped_sprite"], (player1["rect"]))
    else:
        screen.blit(player1["sprite"], (player1["rect"]))

    #if player2["looking_left"]:
    #    screen.blit(player2["flipped_sprite"], (player2["rect"]))
    #else:
    #    screen.blit(player2["sprite"], (player2["rect"]))

    #draw OL
    screen.blit(OL, (0, 0))
    screen.blit(text_to_img(player1["score"], pixelfont, black, 32, 32), (0*game_scale,0))
    screen.blit(text_to_img(player2["score"], pixelfont, black, 32, 32), (480*game_scale,0))
    screen.blit(text_to_img(timer_to_str(timer), pixelfont, black, 64, 32), (224*game_scale,0))

    #check all collisions
    check_player_collision(player1)
    check_player_collision(player2)

    #gravity
    apply_gravity(player1, delta)
    apply_gravity(player2, delta)

    #controlls
    check_input(player1, delta)
    #check_input(player2, delta)
    
    #jumps
    jump(player1)
    #jump(player2)

    #count cooldown
    if player1["cooldown_count"] > 0:
        player1["cooldown_count"] -= 1

    if player2["cooldown_count"] > 0:
        player2["cooldown_count"] -= 1
    

    update_timer()

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()
    clock.tick(FPS)