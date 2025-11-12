import pygame    #this project runs on most versions of python 3.10

pygame.init()

#screensize
screen_hight = 256
screen_width = 512
game_scale = 2.5
BG = ""

#setup screen
screen = pygame.display.set_mode((screen_width*game_scale, screen_hight*game_scale))
pygame.display.set_caption('UrsulinenCombat')

#gamestates
clock = pygame.time.Clock()
run = True

speed = 2*game_scale
gravity = 3*game_scale
jump_power = 0.5
jump_frames = 100

#player values
player1 = {
    "sprite": "",
    "x": 100,
    "y": 100,
    "width": 32,
    "height": 32,
    "jump_frames": 0,
    "collision_top": False,
    "collision_bottom": False,
    "collision_left": False,
    "collision_right": False
}

player2 = {
    "sprite": "",
    "x": 50,
    "y": 50,
    "width": 32,
    "height": 32,
    "jump_frames": 0,
    "collision_top": False,
    "collision_bottom": False,
    "collision_left": False,
    "collision_right": False
}

#plattforms
plattforms = [
    #[x, y, width, height]
    [62, 129, 440, 160]
]
plattforms = [
    {
        "x": 0,
        "y": -1,
        "width": 512,
        "height": 1
    },
    {
        "x": 0,
        "y": 257,
        "width": 512,
        "height": 1
    },
    {
        "x": -1,
        "y": 0,
        "width": 1,
        "height": 256
    },
    {
        "x": 513,
        "y": 0,
        "width": 1,
        "height": 256
    }
]

#colors
black = (0, 0, 0)
white = (255, 255, 255)

#images
test_sprite_sheet_image = pygame.image.load(r"recources/images/sprites/animation.png").convert_alpha()
test_BG = pygame.image.load(r"recources/images/backgrounds/test_BG.png").convert_alpha()


#image processing
def get_image(sheet, sprite_x, sprite_y, width, height, scale):
    image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
    image.blit(sheet, (0, 0), (sprite_x * width, sprite_y * height, sprite_x * width + width, sprite_y * height + height))
    image = pygame.transform.scale(image, (width * scale, height * scale))
    return image

#set BG
BG = get_image(test_BG, 0, 0, 512, 256, game_scale)

#TEMPORARY!!!!!!!!!!!!!
player1["sprite"] = get_image(test_sprite_sheet_image, 0, 0, player1["width"], player1["height"], game_scale)
player2["sprite"] = get_image(test_sprite_sheet_image, 0, 1, player2["width"], player2["height"], game_scale)

def check_collision(obj):
    obj_left = obj["x"]
    obj_right = obj["x"] + obj["width"]
    obj_top = obj["y"]
    obj_bottom = obj["y"] + obj["height"]

    # Initialisiere Kollisionsflags
    obj["collision_top"] = False
    obj["collision_bottom"] = False
    obj["collision_left"] = False
    obj["collision_right"] = False

    for platform in plattforms:
        plat_left = platform["x"]
        plat_right = platform["x"] + platform["width"]
        plat_top = platform["y"]
        plat_bottom = platform["y"] + platform["height"]

        # Prüfe horizontale Überlappung
        horizontal_overlap = obj_right > plat_left and obj_left < plat_right
        vertical_overlap = obj_bottom > plat_top and obj_top < plat_bottom

        # Oben
        if horizontal_overlap and obj_bottom == plat_top:
            obj["collision_bottom"] = True

        # Unten
        if horizontal_overlap and obj_top == plat_bottom:
            obj["collision_top"] = True

        # Links
        if vertical_overlap and obj_right == plat_left:
            obj["collision_right"] = True

        # Rechts
        if vertical_overlap and obj_left == plat_right:
            obj["collision_left"] = True

#gameloop
while run:
    
    #debug
    print(player1["collision_bottom"])

    screen.fill(white)
    screen.blit(BG, (0, 0))

    #testing
    screen.blit(player1["sprite"], (player1["x"], player1["y"]))
    screen.blit(player2["sprite"], (player2["x"], player2["y"]))

    #gravity
    #if player1["collision_bottom"] == False:
    #    player1["y"] += gravity
    if player2["collision_bottom"] == False:
        player2["y"] += gravity

    #controlls
    key = pygame.key.get_pressed() 

    if key[pygame.K_w]:
        if player1["collision_top"] == False:
            player1["jump_frames"] = jump_frames
    elif key[pygame.K_s]:
        if player1["collision_bottom"] == False:
            player1["y"] += 1*speed
    elif key[pygame.K_a]:
        if player1["collision_left"] == False:
            player1["x"] -= 1*speed
    elif key[pygame.K_d]:
        if player1["collision_right"] == False:
            player1["x"] += 1*speed
    
    if key[pygame.K_UP]:
        if player2["collision_top"] == False:
            player2["y"] -= 1*speed
    elif key[pygame.K_DOWN]:
        if player2["collision_bottom"] == False:
            player2["y"] += 1*speed
    elif key[pygame.K_LEFT]:
        if player2["collision_left"] == False:
            player2["x"] -= 1*speed
    elif key[pygame.K_RIGHT]:
        if player2["collision_right"] == False:
            player2["x"] += 1*speed
    
    #jumps
    while player1["jump_frames"] > 0 :
        player1["y"] -= jump_power
        player1["jump_frames"] -= 1
    while player2["jump_frames"] > 0 :
        player2["y"] -= jump_power
        player2["jump_frames"] -= 1

    check_collision(player1)

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if key[pygame.K_ESCAPE]:
        run = False
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit