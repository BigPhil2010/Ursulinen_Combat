import pygame    #this project runs on most versions of python 3.10
import globals as G
import screen as scrn
import menu

pygame.init()
pygame.mixer.init()
def gameOver(winner):
    ######################### VARIABLES #########################

    #gamestates
    clock = pygame.time.Clock()
    run = True

    #setup FPS
    FPS = 60

    #set btn rects
    newGame_btn_rect = pygame.Rect(128 * scrn.game_scale, 180 * scrn.game_scale, 64 * scrn.game_scale, 32 * scrn.game_scale)
    quit_btn_rect = pygame.Rect(320 * scrn.game_scale, 180 * scrn.game_scale, 64 * scrn.game_scale, 32 * scrn.game_scale)

    #set btn states
    newGame_btn = G.text_btn
    quit_btn = G.text_btn

    title = None

    if winner == None:
        title = G.texts["draw"]
    elif winner == "player1":
        title = G.texts["P1_won"]
    elif winner == "player2":
        title = G.texts["P2_won"]

    ######################### FUNCTIONS #########################

    def btn_pressed(btn):
        nonlocal newGame_btn
        nonlocal quit_btn
        nonlocal run

        if btn == "newGame":
            newGame_btn = G.text_btn_pressed
            run = False
            menu.open()
        elif btn == "quit":
            quit_btn = G.text_btn_pressed
            run = False

    ######################### LOOP #########################
    while run:
        scrn.screen.fill(G.background_color)

        #draw btns
        scrn.screen.blit(newGame_btn, newGame_btn_rect)
        scrn.screen.blit(G.text_to_img(G.texts["new"], G.pixelfont, G.black, 64, 32, scrn.game_scale), newGame_btn_rect)

        scrn.screen.blit(quit_btn, quit_btn_rect)
        scrn.screen.blit(G.text_to_img(G.texts["quit"], G.pixelfont, G.black, 64, 32, scrn.game_scale), quit_btn_rect)

        #draw title
        scrn.screen.blit(G.text_to_img(title, G.pixelfont_title, G.black, 512, 64, scrn.game_scale), (0, 32*scrn.game_scale))

        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            #check mouse input
            if event.type == pygame.MOUSEBUTTONDOWN:
                if newGame_btn_rect.collidepoint(event.pos):
                    btn_pressed("newGame")
                if quit_btn_rect.collidepoint(event.pos):
                    btn_pressed("quit")

            if event.type == pygame.MOUSEBUTTONUP:
                newGame_btn = G.text_btn
                quit_btn = G.text_btn
        pygame.display.flip()
        clock.tick(FPS)