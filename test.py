import pygame    #this project runs on most versions of python 3.10
import time

pygame.init()

#screensize
screen_hight = 256
screen_width = 512
game_scale = 1
BG = ""

#setup screen
screen = pygame.display.set_mode((screen_width*game_scale, screen_hight*game_scale))
pygame.display.set_caption('UrsulinenCombat')

#gamestates
clock = pygame.time.Clock()
run = True

speed = 2*game_scale
gravity = 3*game_scale
jump_power = 1
jump_frames = 200

#player values
player1 = {
    "sprite": None,
    "rect": None,
    "start_x": 100,
    "start_y": 50,
    "width": 32,
    "height": 32,
    "jump_frames": 0,
    "collision_top": False,
    "collision_bottom": False,
    "collision_left": False,
    "collision_right": False,
    "gravity": 1,
}

player2 = {
    "sprite": None,
    "rect": None,
    "start_x": 100,
    "start_y": 100,
    "width": 32,
    "height": 32,
    "jump_frames": 0,
    "collision_top": False,
    "collision_bottom": False,
    "collision_left": False,
    "collision_right": False
}

#set rects
player1["rect"] = pygame.Rect(player1["start_x"]*game_scale, player1["start_y"]*game_scale, player1["width"]*game_scale, player1["height"]*game_scale)
player2["rect"] = pygame.Rect(player2["start_x"]*game_scale, player2["start_y"]*game_scale, player2["width"]*game_scale, player2["height"]*game_scale)


plattforms = [
    pygame.Rect(62, 129, 379, 32),
    pygame.Rect(0, 250, 500, 20)
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


def check_player_collision(player):
    #keep in screen
    player["rect"].y = max(0, min(player["rect"].y, (screen_hight * game_scale) - (player["rect"].height)))
    player["rect"].x = max(0, min(player["rect"].x, (screen_width * game_scale) - (player["rect"].width)))


    #reset collision
    player["collision_left"] = False
    player["collision_right"] = False
    player["collision_top"] = False
    player["collision_bottom"] = False

    for plattform in plattforms:
        #check collision
        if player["rect"].colliderect(plattform):

            # Berechne die Überlappungen aus Sicht des Spielers
            overlap_left = player["rect"].right - plattform.left
            overlap_right = plattform.right - player["rect"].left
            overlap_top = player["rect"].bottom - plattform.top
            overlap_bottom = plattform.bottom - player["rect"].top

            # Finde die kleinste Überlappung
            min_overlap = min(overlap_left, overlap_right, overlap_top, overlap_bottom)

            # Setze alle Richtungen erstmal zurück
            player["collision_left"] = False
            player["collision_right"] = False
            player["collision_top"] = False
            player["collision_bottom"] = False

            # Bestimme Richtung aus Sicht des Spielers
            if min_overlap == overlap_left:
                player["collision_right"] = True

            elif min_overlap == overlap_right:
                player["collision_left"] = True

            elif min_overlap == overlap_top:
                player["collision_bottom"] = True

            elif min_overlap == overlap_bottom:
                player["collision_top"] = True

def toggle_num(x):
    if x == abs(x):
        print(-x)
        return -x
    else:
        print(abs(x))
        return abs(x)

#gameloop
while run:

    screen.fill(white)
    screen.blit(BG, (0, 0))

    for plattform in plattforms:
        pygame.draw.rect(screen, (0, 0, 0), plattform)

    #testing
    screen.blit(player1["sprite"], (player1["rect"]))
    #screen.blit(player2["sprite"], (player2["x"], player2["y"]))

    #check all collisions
    check_player_collision(player1)
    check_player_collision(player2)

    #gravity
    if player1["collision_bottom"] == False and gravity == abs(gravity):
        player1["rect"].y += gravity
    elif player1["collision_top"] == False and gravity != abs(gravity):
        player1["rect"].y += gravity
    if player2["collision_bottom"] == False:
        player2["rect"].y += gravity

    #controlls
    key = pygame.key.get_pressed() 
    key_just = pygame.key.get_just_pressed() 

    if key_just[pygame.K_w]:
        if player1["collision_top"] == False:
            if player1["collision_bottom"] == True:
                #player1["jump_frames"] = jump_frames
                gravity = toggle_num(gravity)
                player1["jump_frames"] = 20

    elif key[pygame.K_s]:
        if player1["collision_bottom"] == False:
            player1["rect"].y += speed
    elif key[pygame.K_a]:
        if player1["collision_left"] == False:
            player1["rect"].x -= speed
    elif key[pygame.K_d]:
        if player1["collision_right"] == False:
            player1["rect"].x += speed
    
    if key[pygame.K_UP]:
        if player2["collision_top"] == False:
            player2["rect"].y -= 1*speed
    elif key[pygame.K_DOWN]:
        if player2["collision_bottom"] == False:
            player2["rect"].y += 1*speed
    elif key[pygame.K_LEFT]:
        if player2["collision_left"] == False:
            player2["rect"].x -= 1*speed
    elif key[pygame.K_RIGHT]:
        if player2["collision_right"] == False:
            player2["rect"].x += 1*speed
    
    #jumps
    if player1["jump_frames"] > 0:
        player1["jump_frames"] -= 1
        if player1["jump_frames"] == 1:
            gravity = toggle_num(gravity)
    

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if key[pygame.K_ESCAPE]:
        run = False
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit