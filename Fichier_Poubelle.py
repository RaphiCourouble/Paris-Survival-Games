# Importation des différents modules

from config import *
import pygame

pygame.init()

# Création des variables d'affichage de personnages

mc_image_originale = pygame.image.load("images/Image_Main_Character.png")
mc_image_scaled = pygame.transform.scale(mc_image_originale, (200, 400))

mc_image_originale2 = pygame.image.load("images/Image_Main_Character2.png")
mc_image_scaled2 = pygame.transform.scale(mc_image_originale2, (180, 380))

mc_image_x = 400
mc_image_y = 200

clock = pygame.time.Clock()

# initialisation de la liste gérant l'animation pendant le déplacement

personnages_images = [mc_image_scaled, mc_image_scaled2]
# personnages_images = [[mc_image_scaled, mc_image_scaled2]]
frame_actuelle = 0
frame_compteur = 0

# Création de l'écran principal

pygame.display.set_caption("Paris Survival Games")
pygame.display.set_icon(logo)
main_screen = pygame.display.set_mode((screen_width, screen_height))

# Boucle du jeu

running = True
while running:

    # mise à jour de l'écran

    main_screen.blit(logo, (-100, -250))
    clock.tick(fps)

    # affichage du personnage et ses vies

    main_screen.blit(personnages_images[frame_actuelle], (mc_image_x, mc_image_y))
    # main_screen.blit(personnages_images[0][frame_actuelle], (mc_image_x, mc_image_y))
    if vies == 4:
        main_screen.blit(quatre_vies_scaled, (mc_image_x - 50, mc_image_y - 150))
    elif vies == 3:
        main_screen.blit(trois_vies_scaled, (mc_image_x - 50, mc_image_y - 150))
    elif vies == 2:
        main_screen.blit(deux_vies_scaled, (mc_image_x - 50, mc_image_y - 150))
    elif vies == 1:
        main_screen.blit(une_vie_scaled, (mc_image_x - 50, mc_image_y - 150))
    pygame.display.flip()

    # gestion des événements

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Le jeu est terminé.")

    # gestion des touches
    mouvement = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        if mc_image_x + velocity < screen_width - 200:
            mc_image_x += velocity
            mouvement = True
    if keys[pygame.K_LEFT] or keys[pygame.K_q]:
        if mc_image_x - velocity > 0:
            mc_image_x -= velocity
            mouvement = True
    if keys[pygame.K_UP] or keys[pygame.K_z]:
        if mc_image_y - velocity > -50:
            mc_image_y -= velocity
            mouvement = True
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        if mc_image_y + velocity < screen_height - 400:
            mc_image_y += velocity
            mouvement = True
    if keys[pygame.K_SPACE]:
        running = False
        pygame.quit()
        print("Le jeu est terminé.")

    # gestion de l'animation

    if mouvement:
        frame_compteur += 1
        if frame_compteur % 10 == 0:  # Ajuster le nombre pour contrôler la vitesse de l'animation
            frame_actuelle = (frame_actuelle + 1) % len(personnages_images)
            # frame_actuelle = (frame_actuelle + 1) % len(personnages_images[0])

    # gestion des vies

    if 200 < mc_image_x < 300 and 200 < mc_image_y < 300:

        # Vérification de la position de l'utilisateur

        vies -= 1
        mc_image_x = 400
        mc_image_y = 200
        if vies > 1:
            print("Il ne vous reste plus que " + str(vies) + " vies")
        elif vies == 1:
            print("Il ne vous reste plus que " + str(vies) + " vie")

        # quitter le jeu si le joueur n'a plus de vies

        if vies == 0:
            running = False
            pygame.quit()
            print("Vous n'avez plus de vies, vous avez perdu")
            print("Le jeu est terminé.")
