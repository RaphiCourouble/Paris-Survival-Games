# Importation des différents modules
from config import *
import pygame

pygame.init()
pygame.font.init()

# Création de l'écran principal

pygame.display.set_caption("Paris Survival Games - Tir a l'arc ! ")
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

    elif (keys[pygame.K_RIGHT] and mc_image_x + vitesse <= screen_width - 500
          or keys[pygame.K_d] and mc_image_x + vitesse <= screen_width - 500):

        # Contrôle des déplacements vers la droite
        main_screen.blit(mc_image_liste[frame_actuelle], (mc_image_x, mc_image_y))
        mc_image_x += vitesse
        mouvement = True

    elif (keys[pygame.K_LEFT] and mc_image_x >= 0
          or keys[pygame.K_q] and mc_image_x >= 0):

        # Contrôle des déplacements vers la gauche
        main_screen.blit(mc_image_liste[frame_actuelle], (mc_image_x, mc_image_y))
        mc_image_x -= vitesse
        mouvement = True

    elif (keys[pygame.K_UP] and mc_image_y >= 0
          or keys[pygame.K_z] and mc_image_y >= 0):

        # Contrôle des déplacements vers le haut
        main_screen.blit(mc_image_liste[frame_actuelle], (mc_image_x, mc_image_y))
        mc_image_y -= vitesse
        mouvement = True

    elif (keys[pygame.K_DOWN] and mc_image_y - vitesse <= screen_height - 210
          or keys[pygame.K_s] and mc_image_y - vitesse <= screen_height - 210):

        # Contrôle des déplacements vers le bas
        main_screen.blit(mc_image_liste[frame_actuelle], (mc_image_x, mc_image_y))
        mc_image_y += vitesse
        mouvement = True

    elif mc_image_y == - 5:
        main_screen.blit(mc_image_liste[frame_actuelle], (mc_image_x, mc_image_y))
        main_screen.blit(text_surface, (180, 220))

    elif mc_image_y == 520:
        main_screen.blit(mc_image_liste[frame_actuelle], (mc_image_x, mc_image_y))
        main_screen.blit(text_surface, (180, 220))

    elif mc_image_x == - 5:
        main_screen.blit(mc_image_liste[frame_actuelle], (mc_image_x, mc_image_y))
        main_screen.blit(text_surface, (180, 220))

    elif mc_image_x == 580:
        main_screen.blit(mc_image_liste[frame_actuelle], (mc_image_x, mc_image_y))
        main_screen.blit(text_surface, (180, 220))

    elif keys[pygame.K_SPACE]:

        fleche_x = mc_image_x + 100
        fleche_y = mc_image_y + 50

        while fleche_x < 980:

            fleche_rect = fleche.get_rect(topleft=(fleche_x, fleche_y))
            cible_rect = cible.get_rect(topleft=(cible_x + 120, cible_y))
            main_screen.fill(main_screen_color)
            main_screen.blit(bg_tir_a_larc, (80, 0))
            main_screen.blit(cible, (cible_x + 120, cible_y))
            main_screen.blit(arc, (mc_image_x + 95, mc_image_y + 40))

            main_screen.blit(mc_image_liste[frame_actuelle], (mc_image_x, mc_image_y))

            fleche_x = fleche_x + 20

            if cible_rect.colliderect(fleche_rect):
                # Collision detected, perform actions here
                score += 1

            main_screen.blit(fleche, (fleche_x, fleche_y))

            if mvt_cible:
                cible_y += vitesse_cible - 1
                if cible_y >= 500:  # Si la cible atteint la limite basse
                    cible_y = 500
                    mvt_cible = False  # Changer la direction
            else:  # Si la cible se déplace vers le haut
                cible_y -= vitesse_cible - 1
                if cible_y <= 0:  # Si la cible atteint la limite haute
                    cible_y = 0
                    mvt_cible = True
            main_screen.blit(cible, (cible_x + 120, cible_y))

            if 49 < score < 59:

                main_screen.blit(vie_5, (750, -65))
                main_screen.blit(text_score, (100, 220))

            elif 39 < score < 49:

                main_screen.blit(vie_4, (775, -60))

            elif 29 < score < 39:

                main_screen.blit(vie_3, (795, -60))

            elif 19 < score < 29:

                main_screen.blit(vie_2, (815, -60))

            elif 9 < score < 19:

                main_screen.blit(vie_1, (835, -60))

            elif score >= 60:

                running = False
                pygame.quit()
                print("Le jeu est terminé.")

            pygame.display.flip()

    # Contrôle de la cible en dehors de l'animation de la flèche

    if mvt_cible:
        cible_y += vitesse_cible
        if cible_y >= 500:  # Si la cible atteint la limite basse
            cible_y = 500
            mvt_cible = False  # Changer la direction
    else:  # Si la cible se déplace vers le haut
        cible_y -= vitesse_cible
        if cible_y <= 0:  # Si la cible atteint la limite haute
            cible_y = 0
            mvt_cible = True
    main_screen.blit(cible, (cible_x + 120, cible_y))
    # Changement d'images selon le mouvement du personnage

    if mouvement:

        frame_compteur += 1

        if frame_compteur % 10 == 0:
            frame_actuelle = (frame_actuelle + 1) % len(mc_image_liste)

    # Contrôle du nombre de vies

    if 49 < score < 59:

        main_screen.blit(vie_5, (750, -65))
        main_screen.blit(text_score, (100, 220))

    elif 39 < score < 49:

        main_screen.blit(vie_4, (775, -60))

    elif 29 < score < 39:

        main_screen.blit(vie_3, (795, -60))

    elif 19 < score < 29:

        main_screen.blit(vie_2, (815, -60))

    elif 9 < score < 19:

        main_screen.blit(vie_1, (835, -60))

    elif score >= 60:

        running = False
        pygame.quit()
        print("Le jeu est terminé.")

    pygame.display.flip()

pygame.quit()