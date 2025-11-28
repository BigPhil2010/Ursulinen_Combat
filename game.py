import pygame    #this project runs on most versions of python 3.10
import time
import characters
import maps

pygame.init()
pygame.mixer.init()

######################### VARIABLES #########################

#start sets
P1 = "RITT"
P2 = "KIEN"
Map = "forum"

#screensize
screen_hight = 256
screen_width = 512
game_scale = 2

#setup screen
screen = pygame.display.set_mode((screen_width*game_scale, screen_hight*game_scale))
pygame.display.set_caption('UrsulinenCombat')



#gamestates
clock = pygame.time.Clock()
run = True

#timer
game_duration = 180
timer = game_duration
start_time = time.time()

#setup FPS & delta time
FPS = 60
last_time = time.time()



#physics preset
speed = 2 * game_scale
gravity = 3 * game_scale

BG = None
BG_scale = 1

plattforms = []

#set maps
BG = maps.maps_list[Map]["background"]
plattforms = maps.maps_list[Map]["plattforms"]
speed = maps.maps_list[Map]["speed"]*game_scale
gravity = maps.maps_list[Map]["gravity"]*game_scale
BG_scale = maps.maps_list[Map]["background_scale"]


#player values
player1 = {}
player2 = {}

#set characters
player1 = characters.character_list[P1]
player2 = characters.character_list[P2]

#set player rects
player1["rect"] = pygame.Rect(player1["start_x"]*game_scale, player1["start_y"]*game_scale, player1["width"]*game_scale, player1["height"]*game_scale)
player2["rect"] = pygame.Rect(player2["start_x"]*game_scale, player2["start_y"]*game_scale, player2["width"]*game_scale, player2["height"]*game_scale)



#preload_colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

#load fonts
pixelfont = pygame.font.Font(r"recources/fonts/Minecraft.ttf", 14*game_scale)

#load images
test_overlay = pygame.image.load(r"recources/images/overlays/png/Test_Overlay.png")
standard_overlay = pygame.image.load(r"recources/images/overlays/png/Standard_Overlay.png")

#load sounds
#sound = pygame.mixer.Sound("")
#sound.play()


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

def can_hit(player, enemy):
    if player["rect"].x < enemy["rect"].x and player["looking_left"] == False and player["rect"].colliderect(enemy["rect"]):
        return True
    elif player["rect"].x > enemy["rect"].x and player["looking_left"] == True and player["rect"].colliderect(enemy["rect"]):
        return True
    else:
        return False

def hit(player):
    enemy = None

    #set enemy
    if player == player1:
        enemy = player2
    elif player == player2:
        enemy = player1

    if player["cooldown_count"] == 0:
        player["damage_done"] = False
        player["cooldown_count"] = player["cooldown"]
        player["hit"] = True
        if can_hit(player, enemy):
            player["damage_done"] = True
            enemy["hp"] -= player1["damage"]
            if enemy["hp"] <= 0:
                game_over(player)

def check_input(player, delta):
    key = pygame.key.get_pressed()
    key_just = pygame.key.get_pressed()
    #key_just_released = pygame.key.get_just_released()

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

def game_over(win):
    if win == None:
        print("Unentschieden")
    if win == player1:
        print("P1 hat gewonnen")
    if win == player2:
        print("P2 hat gewonnen")

def update_timer():
    global timer
    global start_time
    if timer > 0:
        current_time = time.time()
        time_over = current_time-start_time
        timer = round(game_duration-time_over)
    else:
        timer = 0
        game_over(None)

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

    if player["hit"] == True:
        if animation != "jump":
            animation_playing = str("hit_" + str(animation))
    else:
        animation_playing = animation

    animation_fps = player["sprite_sheet_layout"][animation_playing][1]
    addition_per_frame = 1/FPS*animation_fps
    player["frame"] += addition_per_frame

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
BG = get_image(BG, 0, 0, 512, 256, BG_scale*game_scale)
OL = get_image(standard_overlay, 0, 0, 512, 256, game_scale)

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
set_sprites(player2, "hit_run")
set_sprites(player2, "hit_idle")

######################### GAMELOOP #########################

while run:
    #messure delta time
    delta = time.time() - last_time
    delta *= FPS
    last_time = time.time()

    #update player sprites
    update_sprites(player1, player1["animation"])
    update_sprites(player2, player2["animation"])

    #update hp_bar
    player1["hp_bar"] = pygame.Rect(0*game_scale, 0*game_scale, player1["hp"]*game_scale, 16*game_scale)
    player2["hp_bar"] = pygame.Rect((512-player2["hp"])*game_scale, 0*game_scale, player2["hp"]*game_scale, 16*game_scale)

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

    if player2["looking_left"]:
        screen.blit(player2["flipped_sprite"], (player2["rect"]))
    else:
        screen.blit(player2["sprite"], (player2["rect"]))

    #draw OL
    screen.blit(OL, (0, 0))
    screen.blit(text_to_img(timer_to_str(timer), pixelfont, white, 64, 32), (224*game_scale,0))

    #draw healthbar
    pygame.draw.rect(screen, green, player1["hp_bar"])
    pygame.draw.rect(screen, green, player2["hp_bar"])

    #check all collisions
    check_player_collision(player1)
    check_player_collision(player2)

    #gravity
    apply_gravity(player1, delta)
    apply_gravity(player2, delta)

    #controlls
    check_input(player1, delta)
    check_input(player2, delta)

    #jumps
    jump(player1)
    jump(player2)

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
