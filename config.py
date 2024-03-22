# Importation des différents modules

import pygame

pygame.init()

# Déclaration des variables liées à l'écran principal

screen_width = 1080
screen_height = 720
fps = 60

logo = pygame.image.load("images/Paris_Survival_Games_Logo.png")
rocher = pygame.image.load("images/autres/Rocher.png")
main_screen_color = (34, 139, 34)

# Déclaration des variables liées au joueur

mc_image_face1 = pygame.image.load("images/Main_Character_1.png")
mc_image_face2 = pygame.image.load("images/Main_Character_2.png")
mc_image_face3 = pygame.image.load("images/Main_Character_3.png")
mc_image_profil1 = pygame.image.load("images/Ethan profil-1.png.png")
mc_image_profil2 = pygame.image.load("images/Ethan profil-2.png.png")
mc_image_profil3 = pygame.image.load("images/Ethan profil-3.png.png")
mc_image_profil4 = pygame.image.load("images/Ethan profil-4.png.png")
mc_image_profil1_scaled = pygame.transform.scale_by(mc_image_profil1, 6)
mc_image_profil2_scaled = pygame.transform.scale_by(mc_image_profil2, 6)
mc_image_profil3_scaled = pygame.transform.scale_by(mc_image_profil3, 6)
mc_image_profil4_scaled = pygame.transform.scale_by(mc_image_profil4, 6)

mc_image_x = 0
mc_image_y = 250
vitesse = 5

vie = 5
vie_1 = pygame.image.load("images/autres/Vie 1.png")
vie_2 = pygame.image.load("images/autres/Vie 2.png")
vie_3 = pygame.image.load("images/autres/Vie 3.png")
vie_4 = pygame.image.load("images/autres/Vie 4.png")
vie_5 = pygame.image.load("images/autres/Vie 5.png")

fleche_original = pygame.image.load("images/autres/Fleche.png")
fleche = pygame.transform.scale_by(fleche_original, 2)

bg_tir_a_larc = pygame.image.load("images/tir_a_larc.png")

cible_originale = pygame.image.load("images/target.png")
cible = pygame.transform.scale_by(cible_originale, 6.5)
cible_x = 720
cible_y = 0
