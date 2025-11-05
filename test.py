import pygame    #this project runs on most versions of python 3.10

pygame.init()

#screensize
screen_hight = 256
screen_width = 512
game_scale = 2.5
player_height = 32
player_width = 32

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
    "x": 0,
    "y": 0,
    "jump_frames": 0,
    "on_floor": False
}

player2 = {
    "sprite": "",
    "x": 50,
    "y": 50,
    "jump_frames": 0,
    "on_floor": False
}

#plattforms
plattforms = [
    #[start_x, end_y, start_y, end_y]

]

#colors
black = (0, 0, 0)
white = (255, 255, 255)

#images
test_sprite_sheet_image = pygame.image.load(r"recources/images/sprites/animation.png").convert_alpha()


#image processing
def get_image(sheet, sprite_x, sprite_y, width, height, scale):
    image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
    image.blit(sheet, (0, 0), (sprite_x*width, sprite_y*height, sprite_x*width+width, sprite_y*height+height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    return image

#TEMPORARY!!!!!!!!!!!!!
player1["sprite"] = get_image(test_sprite_sheet_image, 0, 0, player_width, player_height, game_scale)
player2["sprite"] = get_image(test_sprite_sheet_image, 0, 1, player_width, player_height, game_scale)

#def on_floor(object):


#gameloop
while run:

    screen.fill(white)

    #testing
    screen.blit(player1["sprite"], (player1["x"], player1["y"]))
    screen.blit(player2["sprite"], (player2["x"], player2["y"]))

    #gravity
    player1["y"] += gravity
    player2["y"] += gravity

    #controlls
    key = pygame.key.get_pressed()

    if key[pygame.K_w]:
        player1["jump_frames"] = jump_frames
    elif key[pygame.K_s]:
        player1["y"] += 1*speed
    elif key[pygame.K_a]:
        player1["x"] -= 1*speed
    elif key[pygame.K_d]:
        player1["x"] += 1*speed
    
    if key[pygame.K_UP]:
        player2["y"] -= 1*speed
    elif key[pygame.K_DOWN]:
        player2["y"] += 1*speed
    elif key[pygame.K_LEFT]:
        player2["x"] -= 1*speed
    elif key[pygame.K_RIGHT]:
        player2["x"] += 1*speed
    
    #jumps
    while player1["jump_frames"] > 0 :
        player1["y"] -= jump_power
        player1["jump_frames"] -= 1
    while player2["jump_frames"] > 0 :
        player2["y"] -= jump_power
        player2["jump_frames"] -= 1

    #checks collision        [x = max(a, min(x, b))] --> hält x in einer spanne von a-b
    player1["y"] = max(0, min(player1["y"], (screen_hight * game_scale) - (player_height * game_scale)))
    player1["x"] = max(0, min(player1["x"], (screen_width * game_scale) - (player_width * game_scale)))
    player2["y"] = max(0, min(player2["y"], (screen_hight * game_scale) - (player_height * game_scale)))
    player2["x"] = max(0, min(player2["x"], (screen_width * game_scale) - (player_width * game_scale)))

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if key[pygame.K_ESCAPE]:
        run = False
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit