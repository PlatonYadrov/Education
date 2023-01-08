import pygame
import os
my_path = "pictures/"

#Спрайты
normal_images = {
    "running": [pygame.image.load(os.path.join(my_path + "dinos", "DinoRun1.png")), pygame.image.load(os.path.join(my_path + "dinos", "DinoRun2.png"))],

    "jumping": pygame.image.load(os.path.join(my_path + "dinos", "DinoJump.png")),

    "ducking": [pygame.image.load(os.path.join(my_path + "dinos", "DinoDuck1.png")), pygame.image.load(os.path.join(my_path + "dinos", "DinoDuck2.png"))],

    "small_cactus": [pygame.image.load(os.path.join(my_path + "cactus", "SmallCactus1.png")), pygame.image.load(os.path.join(my_path + "cactus", "SmallCactus2.png")), pygame.image.load(os.path.join(my_path + "cactus", "SmallCactus3.png"))],

    "large_cactus": [pygame.image.load(os.path.join(my_path + "cactus", "LargeCactus1.png")), pygame.image.load(os.path.join(my_path + "cactus", "LargeCactus2.png")), pygame.image.load(os.path.join(my_path + "cactus", "LargeCactus3.png"))],

    "ptero": [pygame.image.load(os.path.join(my_path + "pterodactyls", "Bird1.png")), pygame.image.load(os.path.join(my_path + "pterodactyls", "Bird2.png"))],

    "cloud": pygame.image.load(os.path.join(my_path + "other", "Cloud.png")),
    "bg": pygame.image.load(os.path.join(my_path + "other", "Track.png"))
}

revers_images = {
    "running": [pygame.image.load(os.path.join(my_path + "dinos_revers", "DinoRun1_revers.png")), pygame.image.load(os.path.join(my_path + "dinos_revers", "DinoRun2_revers.png"))],

    "jumping": pygame.image.load(os.path.join(my_path + "dinos_revers", "DinoJump_revers.png")),

    "ducking": [pygame.image.load(os.path.join(my_path + "dinos_revers", "DinoDuck1_revers.png")), pygame.image.load(os.path.join(my_path + "dinos_revers", "DinoDuck2_revers.png"))],

    "small_cactus": [pygame.image.load(os.path.join(my_path + "cactus", "SmallCactus1.png")), pygame.image.load(os.path.join(my_path + "cactus", "SmallCactus2.png")), pygame.image.load(os.path.join(my_path + "cactus", "SmallCactus3.png"))],

    "large_cactus": [pygame.image.load(os.path.join(my_path + "cactus", "LargeCactus1.png")), pygame.image.load(os.path.join(my_path + "cactus", "LargeCactus2.png")), pygame.image.load(os.path.join(my_path + "cactus", "LargeCactus3.png"))],

    "ptero": [pygame.image.load(os.path.join(my_path + "pterodactyls_revers", "Bird1_revers.png")), pygame.image.load(os.path.join(my_path + "pterodactyls_revers", "Bird2_revers.png"))],

    "cloud": pygame.image.load(os.path.join(my_path + "other", "Cloud.png")),
    "bg": pygame.image.load(os.path.join(my_path + "other", "Track.png"))
}

sonic_images = {
    "running": [pygame.image.load(os.path.join(my_path + 'sonic', 'running_sonic1.png')), pygame.image.load(os.path.join(my_path + 'sonic', 'running_sonic2.png'))],

    "jumping": pygame.image.load(os.path.join(my_path + 'sonic', 'jumping_sonic.png')),

    "ducking": [pygame.image.load(os.path.join(my_path + 'sonic', 'ducking_sonic1.png')), pygame.image.load(os.path.join(my_path + 'sonic', 'ducking_sonic2.png'))],

    "small_cactus": [pygame.image.load(os.path.join(my_path + "sonic_bird", "Chaotixtailsplane.gif")), pygame.image.load(os.path.join(my_path + "sonic_bird", "BB_Badnik_2-spr.png")), pygame.image.load(os.path.join(my_path + "sonic_bird", "Uniformer-spr.png"))],

    "large_cactus": [pygame.image.load(os.path.join(my_path + "sonic_bird", "BB_Badnik_3-spr.png")), pygame.image.load(os.path.join(my_path + "sonic_bird", "Eggrobo-sprite.png")), pygame.image.load(os.path.join(my_path + "sonic_bird", "Chainspike.png"))],

    "ptero": [pygame.image.load(os.path.join(my_path + "sonic_bird", "Balkiry_sprite_bird.png")), pygame.image.load(os.path.join(my_path + "sonic_bird", "Balkiry2_bird.png"))],

    "cloud": pygame.image.load(os.path.join(my_path + "other", "Cloud.png")),
    "bg": pygame.image.load(os.path.join(my_path + "other", "Track.png"))
}

images = revers_images
# Глобальные переменные
my_path = "pictures/"
win_width = 1100
win_height = 600
direction = 0
hard = 0
win = pygame.display.set_mode((win_width, win_height))
score_and_name_pair = [1, "default"]
all_id = []
game_speed = 10
obstacles = [1,2]
points = 0
