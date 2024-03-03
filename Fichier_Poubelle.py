# Importation des différents modules

from config import *
import pygame

pygame.init()


mc_image = pygame.image.load("Image Première Version.png")
mc_image_x = 0
mc_image_y = 0
velocity = 5


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

    main_screen.blit(mc_image, (mc_image_x, mc_image_y))

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
            pygame.quit()
            print("Le jeu est terminé.")

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:

                mc_image_x = deplacement_droite(mc_image_x)

            elif event.key == pygame.K_LEFT:

                mc_image_x = deplacement_gauche(mc_image_x)
