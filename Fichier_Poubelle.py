# Importation des différents modules

from config import *
import pygame

pygame.init()

mc_image_originale = pygame.image.load("images/Image-Première-Version.png")
mc_image_scaled = pygame.transform.scale(mc_image_originale, (200, 400))
mc_image_x = 0
mc_image_y = 0


def deplacement_droite(mc_image_x):
    mc_image_x = mc_image_x + velocity

    return mc_image_x


def deplacement_gauche(mc_image_x):
    mc_image_x = mc_image_x - velocity

    return mc_image_x


# Création de l'écran principal

pygame.display.set_caption("Paris Survival Games")
pygame.display.set_icon(logo)
main_screen = pygame.display.set_mode((screen_width, screen_height))

# Boucle du jeu

running = True
clock = pygame.time.Clock()

while running:

    clock.tick(fps)

    # affichage du personnage
    main_screen.blit(mc_image_scaled, (mc_image_x, screen_height - mc_image_scaled.get_height()))
    pygame.display.flip()

    # gestion des evenements
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
            pygame.quit()
            print("Le jeu est terminé.")

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:

                # gestion des collisions vers la droite
                if mc_image_x + velocity < screen_width - 200:  # gestion des collisions vers la droite

                    mc_image_x = deplacement_droite(mc_image_x)
                    main_screen.fill(black)
                    # pygame.draw.rect(main_screen, black, (mc_image_x, mc_image_y, 200, 400))

            elif event.key == pygame.K_LEFT:

                # gestion des collisions vers la gauche
                if mc_image_x + velocity > 0:
                    mc_image_x = deplacement_gauche(mc_image_x)
                    main_screen.fill(black)
                    # pygame.draw.rect(main_screen, black, (mc_image_x, mc_image_y, 200, 400))

    main_screen.blit(logo, (-100, -250))