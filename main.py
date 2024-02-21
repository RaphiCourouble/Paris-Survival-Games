# Importation des différents modules

import pygame
from config import *

pygame.init()

# Création de l'écran principal

pygame.display.set_caption("Paris Survival Games")
main_screen = pygame.display.set_mode((screen_width, screen_height))

# Boucle du jeu

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
            pygame.quit()
            print("Le jeu se termine.")
