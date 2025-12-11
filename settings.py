import pygame    #this project runs on most versions of python 3.10
import json
import globals as G
import screen as scrn
import menu

pygame.init()

def set():
    ######################### VARIABLES #########################
    settings = None

    #load settings
    with open("settings.json", "r", encoding="utf-8") as file:
        settings = json.load(file)

    #gamestates
    clock = pygame.time.Clock()
    run = True

    #setup FPS
    FPS = 60

    pressed_key = None
    key_waiting = None

    #setting heights
    save_height = 8 * scrn.game_scale
    language_height = 59 * scrn.game_scale
    scale_height = 110 * scrn.game_scale
    keys1_height = 161 * scrn.game_scale
    keys2_height = 212 * scrn.game_scale

    #set btn rects
    middle = 288

    save_btn_rect = pygame.Rect(16 * scrn.game_scale, save_height, 64 * scrn.game_scale, 32 * scrn.game_scale)

    keys1_jump_btn_rect = pygame.Rect(118 * scrn.game_scale, keys1_height, 64 * scrn.game_scale, 32 * scrn.game_scale)
    keys1_hit_btn_rect = pygame.Rect(220 * scrn.game_scale, keys1_height, 64 * scrn.game_scale, 32 * scrn.game_scale)
    keys1_left_btn_rect = pygame.Rect(322 * scrn.game_scale, keys1_height, 64 * scrn.game_scale, 32 * scrn.game_scale)
    keys1_right_btn_rect = pygame.Rect(424 * scrn.game_scale, keys1_height, 64 * scrn.game_scale, 32 * scrn.game_scale)

    keys2_jump_btn_rect = pygame.Rect(118 * scrn.game_scale, keys2_height, 64 * scrn.game_scale, 32 * scrn.game_scale)
    keys2_hit_btn_rect = pygame.Rect(220 * scrn.game_scale, keys2_height, 64 * scrn.game_scale, 32 * scrn.game_scale)
    keys2_left_btn_rect = pygame.Rect(322 * scrn.game_scale, keys2_height, 64 * scrn.game_scale, 32 * scrn.game_scale)
    keys2_right_btn_rect = pygame.Rect(424 * scrn.game_scale, keys2_height, 64 * scrn.game_scale, 32 * scrn.game_scale)

    scale_up_btn_rect = pygame.Rect((middle+32) * scrn.game_scale, scale_height, 16 * scrn.game_scale, 32 * scrn.game_scale)
    scale_down_btn_rect = pygame.Rect((middle-32-16) * scrn.game_scale, scale_height, 16 * scrn.game_scale, 32 * scrn.game_scale)
    scale_btn_rect = pygame.Rect((middle-32) * scrn.game_scale, scale_height, 16 * scrn.game_scale, 32 * scrn.game_scale)

    lang_up_btn_rect = pygame.Rect((middle+32) * scrn.game_scale, language_height, 16 * scrn.game_scale, 32 * scrn.game_scale)
    lang_down_btn_rect = pygame.Rect((middle-32-16) * scrn.game_scale, language_height, 16 * scrn.game_scale, 32 * scrn.game_scale)
    lang_btn_rect = pygame.Rect((middle-32) * scrn.game_scale, language_height, 16 * scrn.game_scale, 32 * scrn.game_scale)


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

    scale_up_btn = G.normal_btn_right
    scale_down_btn = G.normal_btn_left
    scale_btn = G.text_btn
    
    lang_up_btn = G.normal_btn_right
    lang_down_btn = G.normal_btn_left
    lang_btn = G.text_btn

    #btn texts
    keys1_jump_txt = G.texts["jump"]
    keys1_hit_txt = G.texts["hit"]
    keys1_left_txt = G.texts["left"]
    keys1_right_txt = G.texts["right"]

    keys2_jump_txt = G.texts["jump"]
    keys2_hit_txt = G.texts["hit"]
    keys2_left_txt = G.texts["left"]
    keys2_right_txt = G.texts["right"]

    scale_txt = str(settings["gamescale"]) + "x"

    lang_txt = str(G.lang_path_to_name(settings["lang"]))

    ######################### FUNCTIONS #########################

    def get_key(key):
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

        nonlocal key_waiting
        nonlocal pressed_key
        nonlocal settings

        if key == "P1_jump":
            keys1_jump_btn = G.text_btn_pressed
            keys1_jump_txt = G.texts["press"]
            key_waiting = key
            if not pressed_key == None:
                keys1_jump_txt = pygame.key.name(pressed_key)
                settings["keysets"]["keyset_P1"]["jump"] = pressed_key
                
                keys1_jump_btn = G.text_btn
                key_waiting = None
                pressed_key = None
        
        if key == "P1_hit":
            keys1_hit_btn = G.text_btn_pressed
            keys1_hit_txt = G.texts["press"]
            key_waiting = key
            if not pressed_key == None:
                keys1_hit_txt = pygame.key.name(pressed_key)
                settings["keysets"]["keyset_P1"]["hit"] = pressed_key
                
                keys1_hit_btn = G.text_btn
                key_waiting = None
                pressed_key = None
        
        if key == "P1_left":
            keys1_left_btn = G.text_btn_pressed
            keys1_left_txt = G.texts["press"]
            key_waiting = key
            if not pressed_key == None:
                keys1_left_txt = pygame.key.name(pressed_key)
                settings["keysets"]["keyset_P1"]["left"] = pressed_key
                
                keys1_left_btn = G.text_btn
                key_waiting = None
                pressed_key = None
        
        if key == "P1_right":
            keys1_right_btn = G.text_btn_pressed
            keys1_right_txt = G.texts["press"]
            key_waiting = key
            if not pressed_key == None:
                keys1_right_txt = pygame.key.name(pressed_key)
                settings["keysets"]["keyset_P1"]["right"] = pressed_key
                
                keys1_right_btn = G.text_btn
                key_waiting = None
                pressed_key = None
        

        if key == "P2_jump":
            keys2_jump_btn = G.text_btn_pressed
            keys2_jump_txt = G.texts["press"]
            key_waiting = key
            if not pressed_key == None:
                keys2_jump_txt = pygame.key.name(pressed_key)
                settings["keysets"]["keyset_P2"]["jump"] = pressed_key
                
                keys2_jump_btn = G.text_btn
                key_waiting = None
                pressed_key = None
        
        if key == "P2_hit":
            keys2_hit_btn = G.text_btn_pressed
            keys2_hit_txt = G.texts["press"]
            key_waiting = key
            if not pressed_key == None:
                keys2_hit_txt = pygame.key.name(pressed_key)
                settings["keysets"]["keyset_P2"]["hit"] = pressed_key
                
                keys2_hit_btn = G.text_btn
                key_waiting = None
                pressed_key = None
        
        if key == "P2_left":
            keys2_left_btn = G.text_btn_pressed
            keys2_left_txt = G.texts["press"]
            key_waiting = key
            if not pressed_key == None:
                keys2_left_txt = pygame.key.name(pressed_key)
                settings["keysets"]["keyset_P2"]["left"] = pressed_key
                
                keys2_left_btn = G.text_btn
                key_waiting = None
                pressed_key = None
        
        if key == "P2_right":
            keys2_right_btn = G.text_btn_pressed
            keys2_right_txt = G.texts["press"]
            key_waiting = key
            if not pressed_key == None:
                keys2_right_txt = pygame.key.name(pressed_key)
                settings["keysets"]["keyset_P2"]["right"] = pressed_key
                
                keys2_right_btn = G.text_btn
                key_waiting = None
                pressed_key = None

    def save():
        with open("settings.json", "w", encoding="utf-8") as file:
            json.dump(settings, file, ensure_ascii=False, indent=4)
        G.load_texts()

    def update_scale(direction):
        nonlocal settings
        nonlocal scale_txt
        
        if direction == "up":
            settings["gamescale"] += 0.25
        if direction == "down" and settings["gamescale"]>=0.5:
            settings["gamescale"] -= 0.25
        scale_txt = str(settings["gamescale"]) + "x"
        
    def update_lang(direction):
        nonlocal settings
        nonlocal lang_txt

        language_count = len(G.language_list)

        # Falls noch keine Sprache gesetzt ist, starte bei Index 0
        if settings["lang"] not in G.language_list:
            current_index = 0
        else:
            current_index = G.language_list.index(settings["lang"])

        if direction == "up":
            new_index = (current_index + 1) % language_count
        elif direction == "down":
            new_index = (current_index - 1) % language_count
        else:
            new_index = current_index  # keine Änderung bei falscher Eingabe

        settings["lang"] = G.language_list[new_index]
        lang_txt = str(G.lang_path_to_name(settings["lang"]))

    def btn_pressed(btn):
        G.click.play()
        nonlocal save_btn
        nonlocal scale_up_btn
        nonlocal scale_down_btn

        nonlocal lang_up_btn
        nonlocal lang_down_btn

        nonlocal run

        if btn == "save":
            save_btn = G.text_btn_pressed
            save()
            run = False
            menu.open()
        
        elif btn == "keys1_jump":
            get_key("P1_jump")
        elif btn == "keys1_hit":
            get_key("P1_hit")
        elif btn == "keys1_left":
            get_key("P1_left")
        elif btn == "keys1_right":
            get_key("P1_right")
        
        elif btn == "keys2_jump":
            get_key("P2_jump")
        elif btn == "keys2_hit":
            get_key("P2_hit")
        elif btn == "keys2_left":
            get_key("P2_left")
        elif btn == "keys2_right":
            get_key("P2_right")

        elif btn == "scale_up":
            scale_up_btn = G.normal_btn_right_pressed
            update_scale("up")
        elif btn == "scale_down":
            scale_down_btn = G.normal_btn_left_pressed
            update_scale("down")
        
        elif btn == "lang_up":
            lang_up_btn = G.normal_btn_right_pressed
            update_lang("up")
        elif btn == "lang_down":
            lang_down_btn = G.normal_btn_left_pressed
            update_lang("down")



    ######################### LOOP #########################
    while run:
        
        scrn.screen.fill(G.background_color)

        #draw btns
        scrn.screen.blit(save_btn, save_btn_rect)
        scrn.screen.blit(G.text_to_img(G.texts["save"], G.pixelfont, G.btn_txt_color, 64, 32, scrn.game_scale), save_btn_rect)

        scrn.screen.blit(keys1_jump_btn, keys1_jump_btn_rect)
        scrn.screen.blit(G.text_to_img(keys1_jump_txt, G.pixelfont, G.btn_txt_color, 64, 32, scrn.game_scale), keys1_jump_btn_rect)
        scrn.screen.blit(keys1_hit_btn, keys1_hit_btn_rect)
        scrn.screen.blit(G.text_to_img(keys1_hit_txt, G.pixelfont, G.btn_txt_color, 64, 32, scrn.game_scale), keys1_hit_btn_rect)
        scrn.screen.blit(keys1_left_btn, keys1_left_btn_rect)
        scrn.screen.blit(G.text_to_img(keys1_left_txt, G.pixelfont, G.btn_txt_color, 64, 32, scrn.game_scale), keys1_left_btn_rect)
        scrn.screen.blit(keys1_right_btn, keys1_right_btn_rect)
        scrn.screen.blit(G.text_to_img(keys1_right_txt, G.pixelfont, G.btn_txt_color, 64, 32, scrn.game_scale), keys1_right_btn_rect)

        scrn.screen.blit(keys2_jump_btn, keys2_jump_btn_rect)
        scrn.screen.blit(G.text_to_img(keys2_jump_txt, G.pixelfont, G.btn_txt_color, 64, 32, scrn.game_scale), keys2_jump_btn_rect)
        scrn.screen.blit(keys2_hit_btn, keys2_hit_btn_rect)
        scrn.screen.blit(G.text_to_img(keys2_hit_txt, G.pixelfont, G.btn_txt_color, 64, 32, scrn.game_scale), keys2_hit_btn_rect)
        scrn.screen.blit(keys2_left_btn, keys2_left_btn_rect)
        scrn.screen.blit(G.text_to_img(keys2_left_txt, G.pixelfont, G.btn_txt_color, 64, 32, scrn.game_scale), keys2_left_btn_rect)
        scrn.screen.blit(keys2_right_btn, keys2_right_btn_rect)
        scrn.screen.blit(G.text_to_img(keys2_right_txt, G.pixelfont, G.btn_txt_color, 64, 32, scrn.game_scale), keys2_right_btn_rect)

        scrn.screen.blit(scale_btn, scale_btn_rect)
        scrn.screen.blit(G.text_to_img(scale_txt, G.pixelfont, G.btn_txt_color, 64, 32, scrn.game_scale), scale_btn_rect)
        scrn.screen.blit(scale_up_btn, scale_up_btn_rect)
        scrn.screen.blit(scale_down_btn, scale_down_btn_rect)

        scrn.screen.blit(lang_btn, lang_btn_rect)
        scrn.screen.blit(G.text_to_img(lang_txt, G.pixelfont, G.btn_txt_color, 64, 32, scrn.game_scale), lang_btn_rect)
        scrn.screen.blit(lang_up_btn, lang_up_btn_rect)
        scrn.screen.blit(lang_down_btn, lang_down_btn_rect)

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
                if scale_up_btn_rect.collidepoint(event.pos):
                    btn_pressed("scale_up")
                if scale_down_btn_rect.collidepoint(event.pos):
                    btn_pressed("scale_down")
                if lang_up_btn_rect.collidepoint(event.pos):
                    btn_pressed("lang_up")
                if lang_down_btn_rect.collidepoint(event.pos):
                    btn_pressed("lang_down")

            if event.type == pygame.MOUSEBUTTONUP:
                save_btn = G.text_btn
                scale_up_btn = G.normal_btn_right
                scale_down_btn = G.normal_btn_left
                lang_up_btn = G.normal_btn_right
                lang_down_btn = G.normal_btn_left
            
            if event.type == pygame.KEYDOWN:
                pressed_key = event.key
                get_key(key_waiting)
            
        pygame.display.flip()
        clock.tick(FPS)