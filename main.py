# Importation des différents modules

from config import *
import pygame

pygame.init()

# Création de l'écran principal

pygame.display.set_caption("Paris Survival Games")
pygame.display.set_icon(logo)
main_screen = pygame.display.set_mode((screen_width, screen_height))

# Boucle du jeu

running = True
clock = pygame.time.Clock()

while running:

    clock.tick(fps)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
            pygame.quit()
            print("Le jeu se termine.")
