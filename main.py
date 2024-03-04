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

    # Affichage du personnage
    main_screen.blit(mc_image, (mc_image_x, mc_image_y))

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
            pygame.quit()
            print("Le jeu est terminé.")

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and mc_image_x < screen_width:

        # Contrôle des déplacements vers la droite

        mc_image_x = mc_image_x + velocity

    elif keys[pygame.K_LEFT] and mc_image_x + velocity > 0:

        # Contrôle des déplacements vers la gauche

        mc_image_x = mc_image_x - velocity

    elif keys[pygame.K_UP] and mc_image_y > 0:

        # Contrôle des déplacements vers le haut

        mc_image_y = mc_image_y - velocity

    elif keys[pygame.K_DOWN] and mc_image_y < screen_height:

        # Contrôle des déplacements vers le bas

        mc_image_y = mc_image_y + velocity

    if 200 < mc_image_x < 300 and 200 < mc_image_y < 300:

        # Vérification de la position de l'utilisateur

        player_life = player_life - 1
        mc_image_x = 0
        mc_image_y = 0
        print("Il ne vous reste plus que " + str(player_life) + "vie.")

        if player_life == 0:

            running = False
            pygame.quit()
            print("Le jeu est terminé.")

    main_screen.fill(main_screen_color)
