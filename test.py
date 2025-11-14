import pygame    #this project runs on most versions of python 3.10
import time

pygame.init()


######################### VARIABLES #########################

#screensize
screen_hight = 256
screen_width = 512
game_scale = 1
BG = None

#setup screen
screen = pygame.display.set_mode((screen_width*game_scale, screen_hight*game_scale))
pygame.display.set_caption('UrsulinenCombat')

#gamestates
clock = pygame.time.Clock()
run = True

#movement norms
speed = 2 * game_scale
gravity = 3 * game_scale

#keysets
keyset1 = {
    "left": pygame.K_a,
    "right": pygame.K_d,
    "jump": pygame.K_w
}

keyset2 = {
    "left": pygame.K_LEFT,
    "right": pygame.K_RIGHT,
    "jump": pygame.K_UP
}

#player values
player1 = {
    "sprite": None,
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
    "sprite": None,
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
    "jump_frames": 60,
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

#load images
test_sprite_sheet_image = pygame.image.load(r"recources/images/sprites/animation.png").convert_alpha()
test_BG = pygame.image.load(r"recources/images/backgrounds/test_BG.png").convert_alpha()


######################### FUNCTIONS #########################

#image processing
def get_image(sheet, sprite_x, sprite_y, width, height, scale):
    image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
    image.blit(sheet, (0, 0), (sprite_x * width, sprite_y * height, sprite_x * width + width, sprite_y * height + height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    return image

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

def apply_gravity(object):
    global gravity
    if object["collision_bottom"] == False and gravity*object["gravity"] == abs(gravity*object["gravity"]):
        object["rect"].y += gravity*object["gravity"]
    elif object["collision_top"] == False and gravity*object["gravity"] != abs(gravity*object["gravity"]):
        object["rect"].y += gravity*object["gravity"]

def jump(object):
    if object["jump_frames_count"] > 0:
        object["jump_frames_count"] -= 1
        if object["jump_frames_count"] == 1:
            object["gravity"] = abs(object["gravity"]/object["jump_power"])

def check_input(player):
    key = pygame.key.get_pressed() 
    key_just = pygame.key.get_just_pressed() 

    if key_just[player["keyset"]["jump"]]:
        if player["collision_top"] == False:
            if player["collision_bottom"] == True:
                player["gravity"] = -abs(player["gravity"]*player["jump_power"])
                player["jump_frames_count"] = player["jump_frames"]
    elif key[player["keyset"]["left"]]:
        if player["collision_left"] == False:
            player["rect"].x -= speed*player["speed"]
    elif key[player["keyset"]["right"]]:
        if player["collision_right"] == False:
            player["rect"].x += speed*player["speed"]


#########################  UPDATE #########################

#set BG
BG = get_image(test_BG, 0, 0, 512, 256, game_scale)

#TEMPORARY!!!!!!!!!!!!!
player1["sprite"] = get_image(test_sprite_sheet_image, 0, 0, player1["width"], player1["height"], game_scale)
player2["sprite"] = get_image(test_sprite_sheet_image, 0, 1, player2["width"], player2["height"], game_scale)


######################### GAMELOOP #########################

while run:
    #reset screen
    screen.fill(white)
    screen.blit(BG, (0, 0))

    #draw plattforms
    for plattform in plattforms:
        pygame.draw.rect(screen, (0, 0, 0), plattform)

    #draw players
    screen.blit(player1["sprite"], (player1["rect"]))
    screen.blit(player2["sprite"], (player2["rect"]))

    #check all collisions
    check_player_collision(player1)
    check_player_collision(player2)

    #gravity
    apply_gravity(player1)
    apply_gravity(player2)

    #controlls
    check_input(player1)
    check_input(player2)
    
    #jumps
    jump(player1)
    jump(player2)
    

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit