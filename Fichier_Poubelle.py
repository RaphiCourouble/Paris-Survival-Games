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

    # affichage du personnage

    main_screen.blit(personnages_images[frame_actuelle], (mc_image_x, mc_image_y))
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
    if keys[pygame.K_RIGHT]:
        if mc_image_x + velocity < screen_width - 200:
            mc_image_x += velocity
            mouvement = True
    if keys[pygame.K_LEFT]:
        if mc_image_x - velocity > 0:
            mc_image_x -= velocity
            mouvement = True
    if keys[pygame.K_UP]:
        if mc_image_y - velocity > -50:
            mc_image_y -= velocity
            mouvement = True
    if keys[pygame.K_DOWN]:
        if mc_image_y + velocity < screen_height - 400:
            mc_image_y += velocity
            mouvement = True

    # gestion de l'animation

    if mouvement:
        frame_compteur += 1
        if frame_compteur % 10 == 0:  # Ajuster le nombre pour contrôler la vitesse de l'animation
            frame_actuelle = (frame_actuelle + 1) % len(personnages_images)
