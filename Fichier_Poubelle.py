# Importation des différents modules
from config import *
import pygame

# from random import *

pygame.init()

# Création de l'écran principal

pygame.display.set_caption("Paris Survival Games")
pygame.display.set_icon(logo)
main_screen = pygame.display.set_mode((screen_width, screen_height))

# Initialisation gérant animation pendant déplacement

mc_image_liste = [mc_image_profil1_scaled, mc_image_profil2_scaled, mc_image_profil3_scaled, mc_image_profil4_scaled]
frame_actuelle = 0
frame_compteur = 0

mc_image_x = 450
mc_image_y = 300

clock = pygame.time.Clock()

# Boucle du jeu

running = True
while running:

    clock.tick(fps)

    main_screen.fill(main_screen_color)
    main_screen.blit(bg_tir_a_larc, (80, 0))

    # Affichage du personnage

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Le jeu est terminé.")

    # gestion des déplacements

    mouvement = False

    keys = pygame.key.get_pressed()

    if all(not key for key in keys):

        main_screen.blit(mc_image_face3, (mc_image_x, mc_image_y))

    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:

        # Contrôle des déplacements vers la droite
        main_screen.blit(mc_image_liste[frame_actuelle], (mc_image_x, mc_image_y))
        mc_image_x += vitesse
        mouvement = True

    elif keys[pygame.K_LEFT] or keys[pygame.K_q]:

        # Contrôle des déplacements vers la gauche
        main_screen.blit(mc_image_liste[frame_actuelle], (mc_image_x, mc_image_y))
        mc_image_x -= vitesse
        mouvement = True

    elif keys[pygame.K_UP] or keys[pygame.K_z]:

        # Contrôle des déplacements vers le haut
        main_screen.blit(mc_image_liste[frame_actuelle], (mc_image_x, mc_image_y))
        mc_image_y -= vitesse
        mouvement = True

    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:

        # Contrôle des déplacements vers le bas
        main_screen.blit(mc_image_liste[frame_actuelle], (mc_image_x, mc_image_y))
        mc_image_y += vitesse
        mouvement = True

    elif keys[pygame.K_SPACE]:

        fleche_x = mc_image_x + 100
        fleche_y = mc_image_y + 50

        while fleche_x < 1080:

            main_screen.fill(main_screen_color)
            main_screen.blit(bg_tir_a_larc, (80, 0))

            main_screen.blit(mc_image_liste[frame_actuelle], (mc_image_x, mc_image_y))

            fleche_x = fleche_x + 20

            main_screen.blit(fleche, (fleche_x, fleche_y))

            pygame.display.flip()

    main_screen.blit(cible, (cible_x, cible_y))

    # Changement d'images selon le mouvement du personnage

    if mouvement:

        frame_compteur += 1

        if frame_compteur % 10 == 0:
            frame_actuelle = (frame_actuelle + 1) % len(mc_image_liste)

    # Contrôle du nombre de vies

    if vie == 5:

        main_screen.blit(vie_5, (mc_image_x + 60, mc_image_y - 10))

    elif vie == 4:

        main_screen.blit(vie_4, (mc_image_x + 62, mc_image_y - 20))

    elif vie == 3:

        main_screen.blit(vie_3, (mc_image_x + 64, mc_image_y - 20))

    elif vie == 2:

        main_screen.blit(vie_2, (mc_image_x + 66, mc_image_y - 20))

    elif vie == 1:

        main_screen.blit(vie_1, (mc_image_x + 60, mc_image_y - 20))

    # Vérification de la position de l'utilisateur

    '''if 200 < mc_image_x < 360 and 200 < mc_image_y < 360:

        vie -= 1
        mc_image_x = 450
        mc_image_y = 300

        if vie > 1:

            print("Il ne vous reste plus que " + str(vie) + " vies.")

        elif vie == 1:

            print("Il ne vous reste plus que " + str(vie) + " vie.")

        elif vie == 0:

            running = False
            pygame.quit()
            print("Le jeu est terminé.")'''

    pygame.display.flip()
