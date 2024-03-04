# Importation des différents modules

from config import *
import pygame

pygame.init()

mc_image_originale = pygame.image.load("images/Image-Première-Version.png")
mc_image_scaled = pygame.transform.scale(mc_image_originale, (200, 400))
mc_image_x = 400
mc_image_y = 200
clock = pygame.time.Clock()

# Création de l'écran principal

pygame.display.set_caption("Paris Survival Games")
pygame.display.set_icon(logo)
main_screen = pygame.display.set_mode((screen_width, screen_height))

# Boucle du jeu

running = True
while running:

    clock.tick(fps)

    # affichage du personnage

    main_screen.blit(mc_image_scaled, (mc_image_x, mc_image_y))
    pygame.display.flip()

    # gestion des événements

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Le jeu est terminé.")

    # gestion des touches

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        if mc_image_x + velocity < screen_width - 200:
            mc_image_x += velocity
    if keys[pygame.K_LEFT]:
        if mc_image_x - velocity > 0:
            mc_image_x -= velocity
    if keys[pygame.K_UP]:
        if mc_image_y - velocity > -50:
            mc_image_y -= velocity
    if keys[pygame.K_DOWN]:
        if mc_image_y + velocity < screen_height - 400:
            mc_image_y += velocity

    main_screen.blit(logo, (-100, -250))
