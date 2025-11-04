import pygame

pygame.init()

#screensize
screen_hight = 256
screen_width = 512

#setup screen
screen = pygame.display.set_mode((screen_width*2, screen_hight*2))
pygame.display.set_caption('UrsulinenCombat')

#gamestates
clock = pygame.time.Clock()
run = True
speed = 0.5

#positions
player1_x = 0
player1_y = 0
player2_x = 50
player2_y = 50

#colors
black = (0, 0, 0)
white = (255, 255, 255)

#images
sprite_sheet_image = pygame.image.load(r"recources/images/sprites/animation.png").convert_alpha()

#objects
player1 = pygame.Rect((0, 0, 32, 32))
player2 = pygame.Rect((50, 50, 32, 32))

#image processing
def get_image(sheet, sprite_x, sprite_y, width, height, scale):
    image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
    image.blit(sheet, (0, 0), (sprite_x*width, sprite_y*height, sprite_x*width+width, sprite_y*height+height))
    image = pygame.transform.scale(image, (width*scale, height*scale))
    return image

frame_0 = get_image(sprite_sheet_image, 7, 1, 32, 32, 2)

#gameloop
while run:

    screen.fill(white)

    #testing
    screen.blit(frame_0, (player1_x, player1_y))

    #pygame.draw.rect(screen, (255, 0, 0), player1)
    pygame.draw.rect(screen, (0, 0, 255), player2)


    #controlls
    key = pygame.key.get_pressed()

    if key[pygame.K_w]:
        player1_y -= 1*speed
    elif key[pygame.K_s]:
        player1_y += 1*speed
    elif key[pygame.K_a]:
        player1_x -= 1*speed
    elif key[pygame.K_d]:
        player1_x += 1*speed
    
    if key[pygame.K_UP]:
        player2.move_ip(0, -1)
    elif key[pygame.K_DOWN]:
        player2.move_ip(0, 1)
    elif key[pygame.K_LEFT]:
        player2.move_ip(-1, 0)
    elif key[pygame.K_RIGHT]:
        player2.move_ip(1, 0)

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit