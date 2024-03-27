def jeu1():

    """
    La fonction jeu1 contient toutes les variables nécessaires au bon fonctionnement du jeu numéro 1.
    Elle gère les fonctionnalités importantes comme l'affichage du fond, du personnage, des déplacements, du tir,
    des collisions, du mouvement de la cible et du score.
    Une fois le jeu fini, on appelle la fonction menu().
    """

    import pygame
    pygame.init()
    pygame.font.init()

    # Déclaration des variables liées à l'écran principal

    screen_width = 1080
    screen_height = 720
    fps = 60

    # Chargement du logo
    logo = pygame.image.load("images/Paris_Survival_Games_Logo.png")

    # Chargement de la couleur de fond
    main_screen_color = (34, 139, 34)

    # Déclaration des variables liées au joueur et son apparence

    # mc_image_face1 = pygame.image.load("images/Main_Character_1.png")
    # mc_image_face2 = pygame.image.load("images/Main_Character_2.png")
    mc_image_face3 = pygame.image.load("images/Main_Character_3.png")
    mc_image_profil1 = pygame.image.load("images/Ethan profil-1.png.png")
    mc_image_profil2 = pygame.image.load("images/Ethan profil-2.png.png")
    mc_image_profil3 = pygame.image.load("images/Ethan profil-3.png.png")
    mc_image_profil4 = pygame.image.load("images/Ethan profil-4.png.png")
    mc_image_profil1_scaled = pygame.transform.scale_by(mc_image_profil1, 6)
    mc_image_profil2_scaled = pygame.transform.scale_by(mc_image_profil2, 6)
    mc_image_profil3_scaled = pygame.transform.scale_by(mc_image_profil3, 6)
    mc_image_profil4_scaled = pygame.transform.scale_by(mc_image_profil4, 6)

    vitesse = 5

    # Déclaration des variables liées au score

    vie_1_originale = pygame.image.load("images/autres/Vie 1.png")
    vie_2_originale = pygame.image.load("images/autres/Vie 2.png")
    vie_3_originale = pygame.image.load("images/autres/Vie 3.png")
    vie_4_originale = pygame.image.load("images/autres/Vie 4.png")
    vie_5_originale = pygame.image.load("images/autres/Vie 5.png")
    vie_1 = pygame.transform.scale_by(vie_1_originale, 6)
    vie_2 = pygame.transform.scale_by(vie_2_originale, 6)
    vie_3 = pygame.transform.scale_by(vie_3_originale, 6)
    vie_4 = pygame.transform.scale_by(vie_4_originale, 6)
    vie_5 = pygame.transform.scale_by(vie_5_originale, 6)

    # Création des variables liées au tir de la flèche

    fleche_original = pygame.image.load("images/autres/Fleche.png")
    fleche = pygame.transform.scale_by(fleche_original, 2)

    bg_tir_a_larc = pygame.image.load("images/tir_a_larc.png")

    # Création des variables liées à la cible

    cible_originale = pygame.image.load("images/target.png")
    cible = pygame.transform.scale_by(cible_originale, 6.5)

    vitesse_cible = 8  # avant: 5
    mvt_cible = True
    cible_x = 720
    cible_y = 0

    # Création des variables d'affichage de texte

    rouge = (255, 0, 0)
    font = pygame.font.Font(None, 60)
    texte_collisions = font.render("Attention, vous mordez la ligne!", True, rouge)

    # Chargement de l'arc

    arc_original = pygame.image.load("images/arc.png")
    arc = pygame.transform.scale_by(arc_original, 3)

    # Déclaration du score

    score = 0
    jaune = (255, 255, 0)
    texte_score = font.render("Dernière flèche pour gagner!", True, jaune)

    # Création de l'écran principal

    pygame.display.set_caption("Paris Survival Games - Tir a l'arc ! ")
    pygame.display.set_icon(logo)
    main_screen = pygame.display.set_mode((screen_width, screen_height))

    # liste gérant l'animation pendant le déplacement

    mc_image_liste = [mc_image_profil1_scaled, mc_image_profil2_scaled, mc_image_profil3_scaled,
                      mc_image_profil4_scaled]
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
            main_screen.blit(texte_collisions, (180, 220))

        elif mc_image_y == 520:
            main_screen.blit(mc_image_liste[frame_actuelle], (mc_image_x, mc_image_y))
            main_screen.blit(texte_collisions, (180, 220))

        elif mc_image_x == - 5:
            main_screen.blit(mc_image_liste[frame_actuelle], (mc_image_x, mc_image_y))
            main_screen.blit(texte_collisions, (180, 220))

        elif mc_image_x == 580:
            main_screen.blit(mc_image_liste[frame_actuelle], (mc_image_x, mc_image_y))
            main_screen.blit(texte_collisions, (180, 220))

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
                    main_screen.blit(texte_score, (100, 220))

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
            main_screen.blit(texte_score, (100, 220))

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
            print("Le jeu est terminé.")

        pygame.display.flip()
    menu()


def aide():

    """
    La fonction aide contient simplement le texte nécessaire à la page 'aide' du menu.
    Une fois le texte généré, on l'affiche où l'on souhaite.
    On affiche également un bouton 'menu' pour nous renvoyer au menu en appelant la fonction menu()
    """

    import pygame

    pygame.init()
    pygame.font.init()

    screen_width = 1080
    screen_height = 720

    aide_screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Paris Survival Games - Aide")

    font = pygame.font.Font(None, 36)

    # logo = pygame.image.load("images/Paris_Survival_Games_Logo.png")

    texte_aide1 = font.render(
        "Pour le jeu 1, déplacez vous avec les touches Z-Q-S-D ou les flèches directionnelles.", True,
        (0, 100, 180))
    texte_aide2 = font.render(
        "Pour tirer une flèche, appuyez sur la touche espace. Ne vous déplacez pas en même temps ! ", True,
        (0, 100, 180))

    texte_aide3 = font.render(
        "Pour le jeu 2, sautez en appuyant sur la touche espace. Évitez les barrières sinon, perdu!  ", True,
        (0, 100, 180))

    clock = pygame.time.Clock()
    clock.tick(60)

    aide_running = True
    while aide_running:

        # aide_screen.blit(logo, (-100, -250))
        aide_screen.fill((255, 203, 96))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                aide_running = False
                pygame.quit()
                print("Le jeu est terminé.")

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if 450 < mouse_x < 650 and 500 < mouse_y < 550:
                    menu()

        aide_screen.blit(texte_aide1, (30, 90))
        aide_screen.blit(texte_aide2, (12, 130))
        aide_screen.blit(texte_aide3, (10, 350))

        bouton_retour_rect = pygame.Rect(450, 500, 200, 50)
        pygame.draw.rect(aide_screen, (255, 220, 120), bouton_retour_rect)
        bouton_retour_texte = font.render("Retour", True, (132, 132, 132))
        aide_screen.blit(bouton_retour_texte, (505, 515))

        pygame.display.flip()
        clock.tick(60)


def menu():

    """
    La fonction menu() génère et affiche tous les éléments du menu.
    Les boutons redirigent respectivement vers : le jeu 1, le jeu 2, l'aide et retour en appelant
    respectivement : jeu1(), jeu2(), aide() et menu()
    """

    import pygame

    pygame.init()
    pygame.font.init()

    screen_width = 1080
    screen_height = 720

    menu_screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Paris Survival Games - Menu")

    font = pygame.font.Font(None, 36)

    logo = pygame.image.load("images/Paris_Survival_Games_Logo.png")

    clock = pygame.time.Clock()
    clock.tick(60)

    menu_running = True
    while menu_running:

        menu_screen.blit(logo, (-100, -250))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_running = False
                pygame.quit()
                print("Le jeu est terminé.")

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                if 450 < mouse_x < 650 and 290 < mouse_y < 340:
                    jeu1()

                elif 450 < mouse_x < 650 and 360 < mouse_y < 410:
                    jeu1()

                elif 450 < mouse_x < 650 and 430 < mouse_y < 480:
                    aide()

                elif 450 < mouse_x < 650 and 500 < mouse_y < 550:
                    pygame.quit()

        # Affichage de personnages (décoration)

        ethan = pygame.image.load("images/Main_Character_1.png")
        gabriel = pygame.image.load("images/Gabriel-1.png.png")

        ethan_scaled = pygame.transform.scale_by(ethan, 1.5)
        gabriel_scaled = pygame.transform.scale_by(gabriel, 9)

        menu_screen.blit(ethan_scaled, (150, 290))
        menu_screen.blit(gabriel_scaled, (700, 290))

        # Affichage des boutons

        bouton_jeu1_rect = pygame.Rect(450, 290, 200, 50)  # --> Rect(left, top, width, height)
        pygame.draw.rect(menu_screen, (255, 203, 96), bouton_jeu1_rect)
        bouton_jeu1_texte = font.render("Jeu 1", True, (132, 132, 132))
        menu_screen.blit(bouton_jeu1_texte, (520, 305))

        bouton_jeu2_rect = pygame.Rect(450, 360, 200, 50)
        pygame.draw.rect(menu_screen, (255, 203, 96), bouton_jeu2_rect)
        bouton_jeu2_texte = font.render("Jeu 2", True, (132, 132, 132))
        menu_screen.blit(bouton_jeu2_texte, (520, 375))

        bouton_jeu3_rect = pygame.Rect(450, 430, 200, 50)
        pygame.draw.rect(menu_screen, (255, 203, 96), bouton_jeu3_rect)
        bouton_jeu3_texte = font.render("Aide", True, (132, 132, 132))
        menu_screen.blit(bouton_jeu3_texte, (520, 445))

        bouton_jeu4_rect = pygame.Rect(450, 500, 200, 50)
        pygame.draw.rect(menu_screen, (255, 203, 96), bouton_jeu4_rect)
        bouton_jeu4_texte = font.render("Quitter", True, (255, 0, 0))
        menu_screen.blit(bouton_jeu4_texte, (505, 515))

        pygame.display.flip()
        clock.tick(60)


menu()
