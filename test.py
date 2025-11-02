import pygame

pygame.init()

screen_hight = 256
screen_width = 512

screen = pygame.display.set_mode((screen_width*2, screen_hight*2))
pygame.display.set_caption('UrsulinenCombat')
clock = pygame.time.Clock()

run = True

player1 = pygame.Rect((0, 0, 32, 32))
player2 = pygame.Rect((50, 50, 32, 32))

while run:

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), player1)
    pygame.draw.rect(screen, (0, 0, 255), player2)

    key = pygame.key.get_pressed()

    if key[pygame.K_w]:
        player1.move_ip(0, -1)
    elif key[pygame.K_s]:
        player1.move_ip(0, 1)
    elif key[pygame.K_a]:
        player1.move_ip(-1, 0)
    elif key[pygame.K_d]:
        player1.move_ip(1, 0)
    
    if key[pygame.K_UP]:
        player2.move_ip(0, -1)
    elif key[pygame.K_DOWN]:
        player2.move_ip(0, 1)
    elif key[pygame.K_LEFT]:
        player2.move_ip(-1, 0)
    elif key[pygame.K_RIGHT]:
        player2.move_ip(1, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit
