# Importation des différents modules

import pygame

pygame.init()

# Déclaration des variables liées à l'écran principal

screen_width = 1080
screen_height = 720
fps = 60
logo = pygame.image.load("Paris_Survival_Games_Logo.png")
main_screen_color = (0, 0, 0)

# Déclaration des variables liées au joueur

mc_image_original = pygame.image.load("images/Image_Main_Character.png")
mc_image = pygame.transform.scale(mc_image_original, (200, 400))
mc_image_x = 0
mc_image_y = 0
velocity = 5
player_life = 5
