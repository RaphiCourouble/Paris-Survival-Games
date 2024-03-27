# Importation des différents modules

from competition_config import *
import pygame
from math import *

pygame.init()

# Création de l'écran principal

pygame.display.set_caption("Paris Survival Games")
pygame.display.set_icon(logo)
main_screen = pygame.display.set_mode((screen_width, screen_height))
main_screen_background_x = 0

# Déclaration de la liste et des variables liées au joueur

mc_image_liste = [mc_image_1, mc_image_2, mc_image_3, mc_image_4]
frame_actuelle = 0
frame_compteur = 0

mc_image_x = 0
mc_image_y = 360


def obstacles(vie, mc_image_x, mc_image_y):

    if 30 < mc_image_x % ((2700/5) - mc_image_x) < 50 and mc_image_y > 280:

        vie -= 1
        mc_image_x = 0
        mc_image_y = 360

    elif 70 < mc_image_x % ((2700/5) - mc_image_x) < 90 and mc_image_y > 280:

        vie -= 1
        mc_image_x = 0
        mc_image_y = 360

    elif 160 < mc_image_x % ((2700/5) - mc_image_x) < 180 and mc_image_y > 280:

        vie -= 1
        mc_image_x = 0
        mc_image_y = 360

    elif 260 < mc_image_x % ((2700/5) - mc_image_x) < 280 and mc_image_y > 280:

        vie -= 1
        mc_image_x = 0
        mc_image_y = 360

    elif 350 < mc_image_x % ((2700/5) - mc_image_x) < 370 and mc_image_y > 280:

        vie -= 1
        mc_image_x = 0
        mc_image_y = 360

    elif 390 < mc_image_x % ((2700/5) - mc_image_x) < 410 and mc_image_y > 280:

        vie -= 1
        mc_image_x = 0
        mc_image_y = 360

    return vie, mc_image_x, mc_image_y

# Boucle du jeu

running = True
fin = False
clock = pygame.time.Clock()

while running:

    clock.tick(fps)

    if mc_image_x < ((2700/5)*3) - mc_image_x:

        main_screen_background_x = - 5 * mc_image_x

    else:

        fin = True

    main_screen.blit(main_screen_background, (main_screen_background_x, 0))
    main_screen.blit(main_screen_background, (2700 + main_screen_background_x, 0))
    main_screen.blit(main_screen_background, (2700*2 + main_screen_background_x, 0))
    main_screen.blit(mc_image_liste[frame_actuelle], (mc_image_x, mc_image_y))

    mouvement = False

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
            pygame.quit()
            print("Le jeu est terminé. Merci d'avoir joué avec nous!")

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:

        # Contrôle des déplacements vers la droite

        mc_image_x += vitesse
        mouvement = True

    elif keys[pygame.K_SPACE]:

        # Contrôle des sauts

        mc_image_x += vitesse/2
        mc_image_y -= 10
        mouvement = True

    if mc_image_y < 360 and not(keys[pygame.K_SPACE]):

        mc_image_y = mc_image_y + 20

    if mouvement:

        frame_compteur += 1

        if frame_compteur % 5 == 0:

            frame_actuelle = (frame_actuelle + 1) % len(mc_image_liste)

    if vie == 5:

        main_screen.blit(vie_5, (mc_image_x, mc_image_y))

    elif vie == 4:

        main_screen.blit(vie_4, (mc_image_x + 65, mc_image_y - 10))

    elif vie == 3:

        main_screen.blit(vie_3, (mc_image_x + 65, mc_image_y - 20))

    elif vie == 2:

        main_screen.blit(vie_2, (mc_image_x + 65, mc_image_y - 20))

    elif vie == 1:

        main_screen.blit(vie_1, (mc_image_x + 65, mc_image_y - 20))

    elif vie == 0:

        fin = True
        print("Le jeu est terminé.")

    if fin:

        main_screen.fill([0, 0, 0])

    # Gestion des obstacles

    if 30 < mc_image_x % abs((2700/5) - mc_image_x) < 50 and mc_image_y > 280:

        vie -= 1
        mc_image_x = 0
        mc_image_y = 360

    elif 70 < mc_image_x % abs((2700/5) - mc_image_x) < 90 and mc_image_y > 280:

        vie -= 1
        mc_image_x = 0
        mc_image_y = 360

    elif 160 < mc_image_x % abs((2700/5) - mc_image_x) < 180 and mc_image_y > 280:

        vie -= 1
        mc_image_x = 0
        mc_image_y = 360

    elif 260 < mc_image_x % abs((2700/5) - mc_image_x) < 280 and mc_image_y > 280:

        vie -= 1
        mc_image_x = 0
        mc_image_y = 360

    elif 350 < mc_image_x % abs((2700/5) - mc_image_x) < 370 and mc_image_y > 280:

        vie -= 1
        mc_image_x = 0
        mc_image_y = 360

    elif 390 < mc_image_x % abs((2700/5) - mc_image_x) < 410 and mc_image_y > 280:

        vie -= 1
        mc_image_x = 0
        mc_image_y = 360

    pygame.display.update()
