# Importation des différents modules

import pygame

pygame.init()

# Déclaration des variables liées à l'écran principal

screen_width = 1080
screen_height = 720
fps = 60
logo = pygame.image.load("images/Paris_Survival_Games_Logo.png")
main_screen_color = (0, 0, 0)

# Déclaration des variables liées au joueur

mc_image_original = pygame.image.load("images/Image_Main_Character.png")
mc_image = pygame.transform.scale(mc_image_original, (200, 400))
mc_image_x = 0
mc_image_y = 0
velocity = 5
player_life = 5
vies = 4
une_vie = pygame.image.load("images/une_vie.png")
deux_vies = pygame.image.load("images/deux_vies.png")
trois_vies = pygame.image.load("images/trois_vies.png")
quatre_vies = pygame.image.load("images/quatre_vies.png")
une_vie_scaled = pygame.transform.scale(une_vie, (320, 320))
deux_vies_scaled = pygame.transform.scale(deux_vies, (320, 320))
trois_vies_scaled = pygame.transform.scale(trois_vies, (320, 320))
quatre_vies_scaled = pygame.transform.scale(quatre_vies, (320, 320))
