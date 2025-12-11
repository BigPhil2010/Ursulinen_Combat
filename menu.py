import pygame    #this project runs on most versions of python 3.10
import characters
import maps
import globals as G
import screen as scrn
import game
import settings

pygame.init()
pygame.mixer.init()

def open():
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


    #set btn rects
    P1_btn_left_rect = pygame.Rect(96 * scrn.game_scale, 96 * scrn.game_scale, 16 * 2*scrn.game_scale, 32 * 2*scrn.game_scale)
    P1_btn_right_rect = pygame.Rect(192 * scrn.game_scale, 96 * scrn.game_scale, 16 * 2*scrn.game_scale, 32 * 2*scrn.game_scale)
    P2_btn_left_rect = pygame.Rect(288 * scrn.game_scale, 96 * scrn.game_scale, 16 * 2*scrn.game_scale, 32 * 2*scrn.game_scale)
    P2_btn_right_rect = pygame.Rect(384 * scrn.game_scale, 96 * scrn.game_scale, 16 * 2*scrn.game_scale, 32 * 2*scrn.game_scale)

    start_btn_rect = pygame.Rect(224 * scrn.game_scale, 192 * scrn.game_scale, 64 * scrn.game_scale, 32 * scrn.game_scale)

    settings_btn_rect = pygame.Rect(480 * scrn.game_scale, 0 * scrn.game_scale, 32 * scrn.game_scale, 32 * scrn.game_scale)

    #set btn states
    P1_btn_left = G.btn_left
    P1_btn_right = G.btn_right
    P2_btn_left = G.btn_left
    P2_btn_right = G.btn_right

    start_btn = G.text_btn
    settings_btn = G.settings_btn

    #set charakter
    P1_character = characters.character_list[list(characters.character_list)[P1]]
    P2_character = characters.character_list[list(characters.character_list)[P2]]

    #reset animation
    P1_character["idle"] = []
    P2_character["idle"] = []
    P1_character["animation"] = "idle"
    P2_character["animation"] = "idle"

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
        nonlocal run
        run = False

        game.start(list(characters.character_list)[P1], list(characters.character_list)[P2], maps.random_map(), 119)

    def btn_pressed(btn):
        G.click.play()
        nonlocal P1_btn_left
        nonlocal P1_btn_right
        nonlocal P2_btn_left
        nonlocal P2_btn_right
        nonlocal start_btn
        nonlocal settings_btn

        nonlocal run

        nonlocal P1
        nonlocal P2

        if btn == "P1_left":
            P1_btn_left = G.btn_left_pressed
            P1 = update_character(P1, P2, "left")
        elif btn == "P1_right":
            P1_btn_right = G.btn_right_pressed
            P1 = update_character(P1, P2, "right")

        elif btn == "P2_left":
            P2_btn_left = G.btn_left_pressed
            P2 = update_character(P2, P1, "left")
        elif btn == "P2_right":
            P2_btn_right = G.btn_right_pressed
            P2 = update_character(P2, P1, "right")
        
        elif btn == "start":
            start_btn = G.text_btn_pressed
            start_game()
        
        elif btn == "settings":
            settings_btn = G.settings_btn_pressed
            run = False
            settings.set()


    ######################### LOOP #########################
    while run:
        scrn.screen.fill(G.background_color)
        scrn.screen.blit(G.get_image(G.menu_BG, 0, 0, 256, 128, scrn.game_scale*2), (0,0))

        #draw selection buttons
        scrn.screen.blit(P1_btn_left, P1_btn_left_rect)
        scrn.screen.blit(G.preview_frame, (128 * scrn.game_scale, 96 * scrn.game_scale))
        scrn.screen.blit(P1_btn_right, P1_btn_right_rect)

        scrn.screen.blit(P2_btn_left, P2_btn_left_rect)
        scrn.screen.blit(G.preview_frame, (320 * scrn.game_scale, 96 * scrn.game_scale))
        scrn.screen.blit(P2_btn_right, P2_btn_right_rect)

        #draw start btn
        scrn.screen.blit(start_btn, start_btn_rect)
        scrn.screen.blit(G.text_to_img(G.texts["start"], G.pixelfont, G.btn_txt_color, 64, 32, scrn.game_scale), start_btn_rect)

        #draw settings btn
        scrn.screen.blit(settings_btn, settings_btn_rect)

        #draw title
        scrn.screen.blit(G.text_to_img(G.texts["choose"], G.pixelfont_title, G.black, 512, 64, scrn.game_scale), (0, 32*scrn.game_scale))

        #update players
        P1_character = characters.character_list[list(characters.character_list)[P1]]
        G.set_sprites(P1_character,"idle", 1.5*scrn.game_scale)
        G.update_sprites(P1_character, "idle", FPS)

        P2_character = characters.character_list[list(characters.character_list)[P2]]
        G.set_sprites(P2_character,"idle", player_scale*scrn.game_scale)
        G.update_sprites(P2_character, "idle", FPS)

        #draw players
        scrn.screen.blit(P1_character["sprite"], ((160 - 16*player_scale) * scrn.game_scale, (128 - 16*player_scale) * scrn.game_scale))
        scrn.screen.blit(P2_character["sprite"], ((352 - 16*player_scale) * scrn.game_scale, (128 - 16*player_scale) * scrn.game_scale))

        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            #check mouse input
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
                if settings_btn_rect.collidepoint(event.pos):
                    btn_pressed("settings")

            if event.type == pygame.MOUSEBUTTONUP:
                P1_btn_left = G.btn_left
                P1_btn_right = G.btn_right
                P2_btn_left = G.btn_left
                P2_btn_right = G.btn_right
                start_btn = G.text_btn
                settings_btn = G.settings_btn
        pygame.display.flip()
        clock.tick(FPS)