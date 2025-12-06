import pygame    #this project runs on most versions of python 3.10
import characters
import global_functions as G
import screen as scrn
import game

pygame.init()
pygame.mixer.init()

######################### VARIABLES #########################

#gamestates
clock = pygame.time.Clock()
run = True

#setup FPS
FPS = 60

#scale vars
player_scale = 1.5

#character selection
P1 = 0
P2 = 1

P1_character = None
P1_character = None

#load images
buttons = pygame.image.load(r"recources/images/GUI/png/buttons.png")

btn_left = G.get_image(buttons, 0, 0, 16, 32, scrn.game_scale*2)
btn_right = G.get_image(buttons, 1, 0, 16, 32, scrn.game_scale*2)
btn_left_pressed = G.get_image(buttons, 2, 0, 16, 32, scrn.game_scale*2)
btn_right_pressed = G.get_image(buttons, 3, 0, 16, 32, scrn.game_scale*2)

preview_frame = G.get_image(buttons, 0, 1, 32, 32, scrn.game_scale*2)

text_btn = G.get_image(buttons, 0, 2, 64, 32, scrn.game_scale)
text_btn_pressed = G.get_image(buttons, 0, 3, 64, 32, scrn.game_scale)

settings_btn = G.get_image(buttons, 0, 4, 32, 32, scrn.game_scale)
settings_btn_pressed = G.get_image(buttons, 1, 4, 32, 32, scrn.game_scale)

#set btn rects
P1_btn_left_rect = pygame.Rect(96 * scrn.game_scale, 96 * scrn.game_scale, 16 * 2*scrn.game_scale, 32 * 2*scrn.game_scale)
P1_btn_right_rect = pygame.Rect(192 * scrn.game_scale, 96 * scrn.game_scale, 16 * 2*scrn.game_scale, 32 * 2*scrn.game_scale)
P2_btn_left_rect = pygame.Rect(288 * scrn.game_scale, 96 * scrn.game_scale, 16 * 2*scrn.game_scale, 32 * 2*scrn.game_scale)
P2_btn_right_rect = pygame.Rect(384 * scrn.game_scale, 96 * scrn.game_scale, 16 * 2*scrn.game_scale, 32 * 2*scrn.game_scale)

start_btn_rect = pygame.Rect(224 * scrn.game_scale, 192 * scrn.game_scale, 64 * scrn.game_scale, 32 * scrn.game_scale)

#set btn states
P1_btn_left = btn_left
P1_btn_right = btn_right
P2_btn_left = btn_left
P2_btn_right = btn_right

start_btn = text_btn



######################### FUNCTIONS #########################

def update_character(player, player_b, direction):
    character_count = len(characters.character_list)

    if direction == "left":
        player = (player - 1) % character_count
        # Skip if it matches player_b
        if player == player_b:
            player = (player - 1) % character_count

    elif direction == "right":
        player = (player + 1) % character_count
        # Skip if it matches player_b
        if player == player_b:
            player = (player + 1) % character_count

    return player

def start_game():
    global run
    run = False

    game.start(list(characters.character_list)[P1], list(characters.character_list)[P2], "forum", 20)

def btn_pressed(btn):
    global P1_btn_left
    global P1_btn_right
    global P2_btn_left
    global P2_btn_right
    global start_btn

    global P1
    global P2

    if btn == "P1_left":
        P1_btn_left = btn_left_pressed
        P1 = update_character(P1, P2, "left")
    elif btn == "P1_right":
        P1_btn_right = btn_right_pressed
        P1 = update_character(P1, P2, "right")

    elif btn == "P2_left":
        P2_btn_left = btn_left_pressed
        P2 = update_character(P2, P1, "left")
    elif btn == "P2_right":
        P2_btn_right = btn_right_pressed
        P2 = update_character(P2, P1, "right")
    
    elif btn == "start":
        start_btn = text_btn_pressed
        start_game()

while run:
    #draw buttons
    scrn.screen.fill((200, 200, 200))

    scrn.screen.blit(P1_btn_left, P1_btn_left_rect)
    scrn.screen.blit(preview_frame, (128 * scrn.game_scale, 96 * scrn.game_scale))
    scrn.screen.blit(P1_btn_right, P1_btn_right_rect)

    scrn.screen.blit(P2_btn_left, P2_btn_left_rect)
    scrn.screen.blit(preview_frame, (320 * scrn.game_scale, 96 * scrn.game_scale))
    scrn.screen.blit(P2_btn_right, P2_btn_right_rect)

    scrn.screen.blit(start_btn, start_btn_rect)


    P1_character = characters.character_list[list(characters.character_list)[P1]]
    G.set_sprites(P1_character,"idle", 1.5*scrn.game_scale)
    G.update_sprites(P1_character, "idle", FPS)

    P2_character = characters.character_list[list(characters.character_list)[P2]]
    G.set_sprites(P2_character,"idle", player_scale*scrn.game_scale)
    G.update_sprites(P2_character, "idle", FPS)


    scrn.screen.blit(P1_character["sprite"], ((160 - 16*player_scale) * scrn.game_scale, (128 - 16*player_scale) * scrn.game_scale))
    scrn.screen.blit(P2_character["sprite"], ((352 - 16*player_scale) * scrn.game_scale, (128 - 16*player_scale) * scrn.game_scale))

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if P1_btn_left_rect.collidepoint(event.pos):
                btn_pressed("P1_left")
            if P1_btn_right_rect.collidepoint(event.pos):
                btn_pressed("P1_right")
            
            if P2_btn_left_rect.collidepoint(event.pos):
                btn_pressed("P2_left")
            if P2_btn_right_rect.collidepoint(event.pos):
                btn_pressed("P2_right")
            
            if start_btn_rect.collidepoint(event.pos):
                btn_pressed("start")

        if event.type == pygame.MOUSEBUTTONUP:
            P1_btn_left = btn_left
            P1_btn_right = btn_right
            P2_btn_left = btn_left
            P2_btn_right = btn_right
            start_btn = text_btn
    pygame.display.flip()
    clock.tick(FPS)