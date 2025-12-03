import pygame    #this project runs on most versions of python 3.10
import time
import global_functions as G
import screen as scrn
import game

pygame.init()
pygame.mixer.init()

#gamestates
clock = pygame.time.Clock()
run = True

#setup FPS & delta time
FPS = 60
last_time = time.time()

x = True

while run:
    #messure delta time
    delta = time.time() - last_time
    delta *= FPS
    last_time = time.time()

    scrn.screen.fill((0, 0, 0))

    if x == True:
        x = False
        game.start("KIEN", "RITT", "klassenzimmer", 18)
        run = False

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
    clock.tick(FPS)