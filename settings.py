import pygame    #this project runs on most versions of python 3.10
import globals as G
import screen as scrn
import menu

pygame.init()
pygame.mixer.init()
def set():
    ######################### VARIABLES #########################

    #gamestates
    clock = pygame.time.Clock()
    run = True

    #setup FPS
    FPS = 60

    #setting heights
    save_height = 8 * scrn.game_scale
    language_height = 59 * scrn.game_scale
    scale_height = 110 * scrn.game_scale
    keys1_height = 161 * scrn.game_scale
    keys2_height = 212 * scrn.game_scale

    #set btn rects
    save_btn_rect = pygame.Rect(16 * scrn.game_scale, save_height, 64 * scrn.game_scale, 32 * scrn.game_scale)

    keys1_jump_btn_rect = pygame.Rect(118 * scrn.game_scale, keys1_height, 64 * scrn.game_scale, 32 * scrn.game_scale)
    keys1_hit_btn_rect = pygame.Rect(220 * scrn.game_scale, keys1_height, 64 * scrn.game_scale, 32 * scrn.game_scale)
    keys1_left_btn_rect = pygame.Rect(322 * scrn.game_scale, keys1_height, 64 * scrn.game_scale, 32 * scrn.game_scale)
    keys1_right_btn_rect = pygame.Rect(424 * scrn.game_scale, keys1_height, 64 * scrn.game_scale, 32 * scrn.game_scale)

    keys2_jump_btn_rect = pygame.Rect(118 * scrn.game_scale, keys2_height, 64 * scrn.game_scale, 32 * scrn.game_scale)
    keys2_hit_btn_rect = pygame.Rect(220 * scrn.game_scale, keys2_height, 64 * scrn.game_scale, 32 * scrn.game_scale)
    keys2_left_btn_rect = pygame.Rect(322 * scrn.game_scale, keys2_height, 64 * scrn.game_scale, 32 * scrn.game_scale)
    keys2_right_btn_rect = pygame.Rect(424 * scrn.game_scale, keys2_height, 64 * scrn.game_scale, 32 * scrn.game_scale)


    #set btn states
    save_btn = G.text_btn

    keys1_jump_btn = G.text_btn
    keys1_hit_btn = G.text_btn
    keys1_left_btn = G.text_btn
    keys1_right_btn = G.text_btn

    keys2_jump_btn = G.text_btn
    keys2_hit_btn = G.text_btn
    keys2_left_btn = G.text_btn
    keys2_right_btn = G.text_btn

    #btn texts
    keys1_jump_txt = G.texts["jump"]
    keys1_hit_txt = G.texts["hit"]
    keys1_left_txt = G.texts["left"]
    keys1_right_txt = G.texts["right"]

    keys2_jump_txt = G.texts["jump"]
    keys2_hit_txt = G.texts["hit"]
    keys2_left_txt = G.texts["left"]
    keys2_right_txt = G.texts["right"]

    ######################### FUNCTIONS #########################

    def btn_pressed(btn):
        nonlocal save_btn
        nonlocal keys1_jump_btn
        nonlocal keys1_hit_btn
        nonlocal keys1_left_btn
        nonlocal keys1_right_btn
        nonlocal keys2_jump_btn
        nonlocal keys2_hit_btn
        nonlocal keys2_left_btn
        nonlocal keys2_right_btn

        nonlocal keys1_jump_txt
        nonlocal keys1_hit_txt
        nonlocal keys1_left_txt
        nonlocal keys1_right_txt

        nonlocal keys2_jump_txt
        nonlocal keys2_hit_txt
        nonlocal keys2_left_txt
        nonlocal keys2_right_txt

        nonlocal run

        if btn == "save":
            newGame_btn = G.text_btn_pressed
            run = False
            menu.open()
        elif btn == "keys1_jump":
            keys1_jump_btn = G.text_btn_pressed
            keys1_jump_txt = G.texts["press"]
        elif btn == "keys1_hit":
            keys1_hit_btn = G



    ######################### LOOP #########################
    while run:
        #print(pygame.key.name(13))
        scrn.screen.fill(G.background_color)

        #draw btns
        scrn.screen.blit(save_btn, save_btn_rect)
        scrn.screen.blit(G.text_to_img(G.texts["save"], G.pixelfont, G.black, 64, 32, scrn.game_scale), save_btn_rect)

        scrn.screen.blit(keys1_jump_btn, keys1_jump_btn_rect)
        scrn.screen.blit(G.text_to_img(keys1_jump_txt, G.pixelfont, G.black, 64, 32, scrn.game_scale), keys1_jump_btn_rect)
        scrn.screen.blit(keys1_hit_btn, keys1_hit_btn_rect)
        scrn.screen.blit(G.text_to_img(keys1_hit_txt, G.pixelfont, G.black, 64, 32, scrn.game_scale), keys1_hit_btn_rect)
        scrn.screen.blit(keys1_left_btn, keys1_left_btn_rect)
        scrn.screen.blit(G.text_to_img(keys1_left_txt, G.pixelfont, G.black, 64, 32, scrn.game_scale), keys1_left_btn_rect)
        scrn.screen.blit(keys1_right_btn, keys1_right_btn_rect)
        scrn.screen.blit(G.text_to_img(keys1_right_txt, G.pixelfont, G.black, 64, 32, scrn.game_scale), keys1_right_btn_rect)

        scrn.screen.blit(keys2_jump_btn, keys2_jump_btn_rect)
        scrn.screen.blit(G.text_to_img(keys2_jump_txt, G.pixelfont, G.black, 64, 32, scrn.game_scale), keys2_jump_btn_rect)
        scrn.screen.blit(keys2_hit_btn, keys2_hit_btn_rect)
        scrn.screen.blit(G.text_to_img(keys2_hit_txt, G.pixelfont, G.black, 64, 32, scrn.game_scale), keys2_hit_btn_rect)
        scrn.screen.blit(keys2_left_btn, keys2_left_btn_rect)
        scrn.screen.blit(G.text_to_img(keys2_left_txt, G.pixelfont, G.black, 64, 32, scrn.game_scale), keys2_left_btn_rect)
        scrn.screen.blit(keys2_right_btn, keys2_right_btn_rect)
        scrn.screen.blit(G.text_to_img(keys2_right_txt, G.pixelfont, G.black, 64, 32, scrn.game_scale), keys2_right_btn_rect)

        #draw setting names
        scrn.screen.blit(G.text_to_img(str(G.texts["lang"])+":", G.pixelfont, G.black, 64, 32, scrn.game_scale), (16 * scrn.game_scale, language_height))
        scrn.screen.blit(G.text_to_img(str(G.texts["scale"])+":", G.pixelfont, G.black, 64, 32, scrn.game_scale), (16 * scrn.game_scale, scale_height))
        scrn.screen.blit(G.text_to_img(str(G.texts["keys1"])+":", G.pixelfont, G.black, 64, 32, scrn.game_scale), (16 * scrn.game_scale, keys1_height))
        scrn.screen.blit(G.text_to_img(str(G.texts["keys2"])+":", G.pixelfont, G.black, 64, 32, scrn.game_scale), (16 * scrn.game_scale, keys2_height))

        
        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            #check mouse input
            if event.type == pygame.MOUSEBUTTONDOWN:
                if save_btn_rect.collidepoint(event.pos):
                    btn_pressed("save")
                if keys1_jump_btn_rect.collidepoint(event.pos):
                    btn_pressed("keys1_jump")
                if keys1_hit_btn_rect.collidepoint(event.pos):
                    btn_pressed("keys1_hit")
                if keys1_left_btn_rect.collidepoint(event.pos):
                    btn_pressed("keys1_left")
                if keys1_right_btn_rect.collidepoint(event.pos):
                    btn_pressed("keys1_right")
                if keys2_jump_btn_rect.collidepoint(event.pos):
                    btn_pressed("keys2_jump")
                if keys2_hit_btn_rect.collidepoint(event.pos):
                    btn_pressed("keys2_hit")
                if keys2_left_btn_rect.collidepoint(event.pos):
                    btn_pressed("keys2_left")
                if keys2_right_btn_rect.collidepoint(event.pos):
                    btn_pressed("keys2_right")

            if event.type == pygame.MOUSEBUTTONUP:
                save_btn = G.text_btn
            
        pygame.display.flip()
        clock.tick(FPS)