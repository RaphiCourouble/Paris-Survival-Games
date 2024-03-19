# Importation des différents modules

from config import *
import pygame
import pytmx
# from random import *

pygame.init()

# Création de l'écran principal

pygame.display.set_caption("Paris Survival Games")
pygame.display.set_icon(logo)
main_screen = pygame.display.set_mode((screen_width, screen_height))

# Initialisation gérant animation pendant déplacement

mc_image_liste = [mc_image_1, mc_image_2, mc_image_3]
frame_actuelle = 0
frame_compteur = 0

mc_image_x = 0
mc_image_y = 250

clock = pygame.time.Clock()

tmx_map = pytmx.load_pygame("tilemap_test.tmx")

'''
ennemis = []
'''

# Boucle du jeu

running = True
while running:

    clock.tick(fps)

    for layer in tmx_map.visible_layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, gid in layer:
                tile = tmx_map.get_tile_image_by_gid(gid)
                if tile:
                    main_screen.blit(tile, (x * tmx_map.tilewidth, y * tmx_map.tileheight))

    '''
    if len(ennemis) < 3:
        ennemi_x = randint(0, 750)
        ennemi_y = randint(0, 550)
        direction = choice(["haut", "bas", "gauche", "droite"])
        ennemis.append([ennemi_x, ennemi_y, direction])
    '''

    # Affichage du personnage

    main_screen.blit(mc_image_liste[frame_actuelle], (mc_image_x, mc_image_y))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
            pygame.quit()
            print("Le jeu est terminé.")

    '''
    for ennemi in ennemis:
        if ennemi[2] == "haut":
            ennemi[1] -= 2
            ennemi[0] += 1
        elif ennemi[2] == "bas":
            ennemi[1] += 2
            ennemi[0] += 3
        elif ennemi[2] == "gauche":
            ennemi[0] -= 2
            ennemi[1] -= 4
        elif ennemi[2] == "droite":
            ennemi[0] += 2
            ennemi[1] += 2.5

    for ennemi in ennemis:
        main_screen.blit(mc_image_1, (ennemi[0], ennemi[1], 50, 50))
    '''

    # gestion des déplacements

    mouvement = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] or keys[pygame.K_d] and mc_image_x + vitesse < screen_width - 180:

        # Contrôle des déplacements vers la droite

        mc_image_x += vitesse
        mouvement = True

    elif keys[pygame.K_LEFT] or keys[pygame.K_q] and mc_image_x > 0:

        # Contrôle des déplacements vers la gauche

        mc_image_x -= vitesse
        mouvement = True

    elif keys[pygame.K_UP] or keys[pygame.K_z] and mc_image_y > 0:

        # Contrôle des déplacements vers le haut

        mc_image_y -= vitesse
        mouvement = True

    elif keys[pygame.K_DOWN] or keys[pygame.K_s] and mc_image_y - vitesse < screen_height - 210:

        # Contrôle des déplacements vers le bas

        mc_image_y += vitesse
        mouvement = True

    elif keys[pygame.K_SPACE]:

        fleche_x = mc_image_x + 150
        fleche_y = mc_image_y + 75

        main_screen.blit(fleche, (fleche_x, fleche_y))

        while fleche_x < 1080:

            main_screen.fill(main_screen_color)
            main_screen.blit(rocher, (200, 200))
            main_screen.blit(mc_image_liste[frame_actuelle], (mc_image_x, mc_image_y))

            fleche_x = fleche_x + 2

            main_screen.blit(fleche, (fleche_x, fleche_y))

            pygame.display.flip()

    # Changement d'images selon le mouvement du personnage

    if mouvement:

        frame_compteur += 1

        if frame_compteur % 10 == 0:

            frame_actuelle = (frame_actuelle + 1) % len(mc_image_liste)

    # Contrôle du nombre de vies

    if vie == 5:

        main_screen.blit(vie_5, (mc_image_x + 65, mc_image_y - 10))

    elif vie == 4:

        main_screen.blit(vie_4, (mc_image_x + 65, mc_image_y - 20))

    elif vie == 3:

        main_screen.blit(vie_3, (mc_image_x + 65, mc_image_y - 20))

    elif vie == 2:

        main_screen.blit(vie_2, (mc_image_x + 65, mc_image_y - 20))

    elif vie == 1:

        main_screen.blit(vie_1, (mc_image_x + 65, mc_image_y - 20))

    # Vérification de la position de l'utilisateur

    if 200 < mc_image_x < 360 and 200 < mc_image_y < 360:

        vie -= 1
        mc_image_x = 0
        mc_image_y = 250

        if vie > 1:

            print("Il ne vous reste plus que " + str(vie) + " vies.")

        elif vie == 1:

            print("Il ne vous reste plus que " + str(vie) + " vie.")

        elif vie == 0:

            running = False
            pygame.quit()
            print("Le jeu est terminé.")

    pygame.display.flip()
