# In this file, all functions that can be used in multiple scripts are stored
import pygame
import json
import screen as scrn

pygame.init()

######################### FUNCTIONS #########################
def get_image(sheet, sprite_x, sprite_y, width, height, game_scale):
    image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
    image.blit(sheet, (0, 0), (sprite_x * width, sprite_y * height, sprite_x * width + width, sprite_y * height + height))
    image = pygame.transform.scale(image, (width * game_scale, height * game_scale))
    return image

def flip_image(image):
    if image == None:
        return None
    else:
        return pygame.transform.flip(image, True, False)

def text_to_img(text, font, color, width, height, game_scale):
    img = pygame.Surface((width * game_scale, height * game_scale), pygame.SRCALPHA).convert_alpha()
    font_img = font.render(str(text), True, color)
    font_width = font_img.get_width()
    font_height = font_img.get_height()
    font_x = (width * game_scale - font_width)/2
    font_y = (height * game_scale - font_height)/2
    img.blit(font_img, (font_x, font_y))
    return img

def set_sprites(player, animation, game_scale):
    sprite_y = player["sprite_sheet_layout"][animation][0][1]
    sprites_x = []
    count = 0
    while count < player["sprite_sheet_layout"][animation][0][2]+1:
        sprites_x.append(count)
        count += 1
    for sprite_x in sprites_x:
        player[animation].append(get_image(player["sprite_sheet"], sprite_x, sprite_y, player["width"], player["height"], game_scale))

def update_sprites(player, animation, FPS):
    animation_playing = animation

    if player["hit"] == True:
        if animation != "jump":
            animation_playing = str("hit_" + str(animation))
    else:
        animation_playing = animation

    animation_fps = player["sprite_sheet_layout"][animation_playing][1]
    addition_per_frame = 1/FPS*animation_fps
    player["frame"] += addition_per_frame

    loop = player["sprite_sheet_layout"][animation_playing][2]

    if player["frame"] >= player["sprite_sheet_layout"][animation_playing][0][2]+1:
        if loop == True:
            player["frame"] = 0
        else:
            player["animation"] = "idle"
            player["frame"] = 0
            player["hit"] = False

    player["sprite"] = player[animation_playing][int(player["frame"])]
    player["flipped_sprite"] = flip_image(player["sprite"])


######################### VARIABLES #########################
#preload_colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
background_color = (200, 200, 200)

#load fonts
pixelfont = pygame.font.Font(r"recources/fonts/Minecraft.ttf", 14*scrn.game_scale)
pixelfont_title = pygame.font.Font(r"recources/fonts/Minecraft.ttf", 22*scrn.game_scale)

#load images
test_overlay = pygame.image.load(r"recources/images/overlays/png/Test_Overlay.png")
standard_overlay = pygame.image.load(r"recources/images/overlays/png/Standard_Overlay.png")

#load btn images
buttons = pygame.image.load(r"recources/images/GUI/png/buttons.png")

btn_left = get_image(buttons, 0, 0, 16, 32, scrn.game_scale*2)
btn_right = get_image(buttons, 1, 0, 16, 32, scrn.game_scale*2)
btn_left_pressed = get_image(buttons, 2, 0, 16, 32, scrn.game_scale*2)
btn_right_pressed = get_image(buttons, 3, 0, 16, 32, scrn.game_scale*2)

preview_frame = get_image(buttons, 0, 1, 32, 32, scrn.game_scale*2)

text_btn = get_image(buttons, 0, 2, 64, 32, scrn.game_scale)
text_btn_pressed = get_image(buttons, 0, 3, 64, 32, scrn.game_scale)

settings_btn = get_image(buttons, 0, 4, 32, 32, scrn.game_scale)
settings_btn_pressed = get_image(buttons, 1, 4, 32, 32, scrn.game_scale)

#load sounds
#sound = pygame.mixer.Sound("")
#sound.play()

#load texts
texts = None

with open("settings.json", "r", encoding="utf-8") as file:
        settigs = json.load(file)
        texts_path = settigs["lang"]

        with open(texts_path, "r", encoding="utf-8") as lang_file:
            lang = json.load(lang_file)
            texts = lang["txt"]