# Importation des différents modules

import pygame

pygame.init()
pygame.font.init()


def jeu_tir_arc():

    """
    Cette procédure contient l'ensemble des variables nécessaires au bon fonctionnement du premier jeu.
    Elle permet notamment de gérer des fonctionnalités importantes comme l'affichage du fond, du personnage, des
    déplacements, du tir, des collisions, du mouvement de la cible et du score.
    Une fois le jeu fini, on appelle ce jeu dans une autre procédure appelée menu().
    """

    # Déclaration des variables liées à l'écran principal

    screen_width = 1080
    screen_height = 720
    fps = 60

    # Chargement du logo et de la couleur de fond

    logo = pygame.image.load("images/Paris_Survival_Games_Logo.png")
    couleur_principale = (34, 139, 34)

    # Déclaration des variables liées au joueur et son apparence

    mc_image = pygame.image.load("images/Main_Character_3.png")
    mc_image_1 = pygame.image.load("images/Ethan Profil_1.png")
    mc_image_1 = pygame.transform.scale_by(mc_image_1, 0.3)
    mc_image_2 = pygame.image.load("images/Ethan Profil_2.png")
    mc_image_2 = pygame.transform.scale_by(mc_image_2, 0.3)
    mc_image_3 = pygame.image.load("images/Ethan Profil_3.png")
    mc_image_3 = pygame.transform.scale_by(mc_image_3, 0.3)
    mc_image_4 = pygame.image.load("images/Ethan Profil_4.png")
    mc_image_4 = pygame.transform.scale_by(mc_image_4, 0.3)

    vitesse = 5

    # Création du système de vies

    vie_1 = pygame.image.load("images/autres/Vie 1.png")
    vie_1 = pygame.transform.scale_by(vie_1, 6)
    vie_2 = pygame.image.load("images/autres/Vie 2.png")
    vie_2 = pygame.transform.scale_by(vie_2, 6)
    vie_3 = pygame.image.load("images/autres/Vie 3.png")
    vie_3 = pygame.transform.scale_by(vie_3, 6)
    vie_4 = pygame.image.load("images/autres/Vie 4.png")
    vie_4 = pygame.transform.scale_by(vie_4, 6)
    vie_5 = pygame.image.load("images/autres/Vie 5.png")
    vie_5 = pygame.transform.scale_by(vie_5, 6)

    # Création des variables liées au tir de la flèche

    fleche = pygame.image.load("images/autres/Fleche.png")
    fleche = pygame.transform.scale_by(fleche, 2)

    background_tir_a_larc = pygame.image.load("images/Tir_à_L'arc.png")

    # Chargement de l'arc

    arc_original = pygame.image.load("images/autres/Arc.png")
    arc = pygame.transform.scale_by(arc_original, 3)

    # Création des variables liées à la cible

    cible = pygame.image.load("images/autres/Cible.png")
    cible = pygame.transform.scale_by(cible, 6.5)

    vitesse_cible = 8
    mouvement_cible = True
    cible_x = 720
    cible_y = 0

    # Création des variables d'affichage de texte

    rouge = (255, 0, 0)
    font = pygame.font.Font(None, 60)
    texte_collisions = font.render("Attention, vous mordez la ligne!", True, rouge)

    # Déclaration du score

    score = 0
    jaune = (255, 255, 0)
    texte_score = font.render("Dernière flèche pour gagner!", True, jaune)

    # Création de l'écran principal

    pygame.display.set_caption("Paris Survival Games - Epreuve de tir à l'arc ! ")
    pygame.display.set_icon(logo)
    main_screen = pygame.display.set_mode((screen_width, screen_height))

    # Liste gérant l'animation pendant le déplacement

    mc_image_liste = [mc_image_1, mc_image_2, mc_image_3, mc_image_4]
    frame_actuelle = 0
    frame_compteur = 0

    mc_image_x = 450
    mc_image_y = 300

    # Boucle du jeu

    running = True
    clock = pygame.time.Clock()

    while running:

        clock.tick(fps)

        main_screen.fill(couleur_principale)
        main_screen.blit(background_tir_a_larc, (80, 0))

        # Gestion des déplacements

        mouvement = False

        keys = pygame.key.get_pressed()

        if all(not key for key in keys):

            main_screen.blit(mc_image, (mc_image_x, mc_image_y))

        elif (keys[pygame.K_RIGHT] and mc_image_x + vitesse <= screen_width - 500
              or keys[pygame.K_d] and mc_image_x + vitesse <= screen_width - 500):

            # Contrôle des déplacements vers la droite

            main_screen.blit(mc_image_liste[frame_actuelle], (mc_image_x, mc_image_y))
            mc_image_x += vitesse
            mouvement = True

        elif keys[pygame.K_LEFT] and mc_image_x >= 0 or keys[pygame.K_q] and mc_image_x >= 0:

            # Contrôle des déplacements vers la gauche

            main_screen.blit(mc_image_liste[frame_actuelle], (mc_image_x, mc_image_y))
            mc_image_x -= vitesse
            mouvement = True

        elif keys[pygame.K_UP] and mc_image_y >= 0 or keys[pygame.K_z] and mc_image_y >= 0:

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

        # Contrôle des collisions

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
                main_screen.fill(couleur_principale)
                main_screen.blit(background_tir_a_larc, (80, 0))
                main_screen.blit(cible, (cible_x + 120, cible_y))
                main_screen.blit(arc, (mc_image_x + 95, mc_image_y + 40))
                main_screen.blit(mc_image_liste[frame_actuelle], (mc_image_x, mc_image_y))

                fleche_x = fleche_x + 20

                if cible_rect.colliderect(fleche_rect):

                    # Collision détectée

                    score += 1

                main_screen.blit(fleche, (fleche_x, fleche_y))

                if mouvement_cible:

                    cible_y += vitesse_cible - 1

                    # Si la cible atteint la limite basse

                    if cible_y >= 500:

                        cible_y = 500
                        mouvement_cible = False  # Changement de directions

                else:

                    cible_y -= vitesse_cible - 1

                    # Si la cible atteint la limite haute

                    if cible_y <= 0:

                        cible_y = 0
                        mouvement_cible = True

                main_screen.blit(cible, (cible_x + 120, cible_y))

                # Vérification des scores

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

        if mouvement_cible:

            cible_y += vitesse_cible

            if cible_y >= 500:  # Si la cible atteint la limite basse

                cible_y = 500
                mouvement_cible = False  # Changement de direction

        else:

            cible_y -= vitesse_cible

            if cible_y <= 0:  # Si la cible atteint la limite haute

                cible_y = 0
                mouvement_cible = True

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

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running = False
                pygame.quit()
                print("Le jeu est terminé.")

        pygame.display.flip()

    menu()


def aide():

    """
    Cette procédure contient tout simplement le texte nécessaire à la page d'aide du menu.
    Une fois le texte généré, on peut l'afficher où l'on souhaite.
    Un bouton 'menu' est aussi affiché pour renvoyer l'utilisateur au menu en appelant la fonction menu()
    """

    screen_width = 1080
    screen_height = 720
    fps = 60

    aide_screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Paris Survival Games - Aide")

    font = pygame.font.Font(None, 36)

    texte_aide1 = font.render(
        "Pour le jeu 1, déplacez vous avec les touches Z-Q-S-D ou les flèches directionnelles.", True,
        (0, 100, 180))

    texte_aide2 = font.render(
        "Pour tirer une flèche, appuyez sur la touche espace. Ne vous déplacez pas en même temps!", True,
        (0, 100, 180))

    texte_aide3 = font.render(
        "Pour le jeu 2, sautez en appuyant sur la touche espace. Évitez les barrières sinon, perdu!", True,
        (0, 100, 180))

    aide_running = True
    clock = pygame.time.Clock()

    while aide_running:

        clock.tick(fps)

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


def jeu_athletisme():

    # Déclaration des variables liées à l'écran principal

    screen_width = 1080
    screen_height = 720
    fps = 60

    logo = pygame.image.load("images/Paris_Survival_Games_Logo.png")
    main_screen_background = pygame.image.load("images/Course.png")

    # Déclaration des variables liées au joueur

    mc_image_1 = pygame.image.load("images/Ethan Profil_1.png")
    mc_image_1 = pygame.transform.scale_by(mc_image_1, 0.3)
    mc_image_2 = pygame.image.load("images/Ethan Profil_2.png")
    mc_image_2 = pygame.transform.scale_by(mc_image_2, 0.3)
    mc_image_3 = pygame.image.load("images/Ethan Profil_3.png")
    mc_image_3 = pygame.transform.scale_by(mc_image_3, 0.3)
    mc_image_4 = pygame.image.load("images/Ethan Profil_4.png")
    mc_image_4 = pygame.transform.scale_by(mc_image_4, 0.3)

    sc_image_1 = pygame.image.load("images/Théo Profil_1.png")
    sc_image_1 = pygame.transform.scale_by(sc_image_1, 3 / 7)
    sc_image_2 = pygame.image.load("images/Théo Profil_2.png")
    sc_image_2 = pygame.transform.scale_by(sc_image_2, 3 / 7)
    sc_image_3 = pygame.image.load("images/Théo Profil_3.png")
    sc_image_3 = pygame.transform.scale_by(sc_image_3, 3 / 7)
    sc_image_4 = pygame.image.load("images/Théo Profil_4.png")
    sc_image_4 = pygame.transform.scale_by(sc_image_4, 3 / 7)

    sc_image_x = 0
    sc_image_y = 250

    # Création du système de vies

    vie = 5
    vie_1 = pygame.image.load("images/autres/Vie 1.png")
    vie_2 = pygame.image.load("images/autres/Vie 2.png")
    vie_3 = pygame.image.load("images/autres/Vie 3.png")
    vie_4 = pygame.image.load("images/autres/Vie 4.png")
    vie_5 = pygame.image.load("images/autres/Vie 5.png")

    # Création de l'écran principal

    pygame.display.set_caption("Paris Survival Games")
    pygame.display.set_icon(logo)
    main_screen = pygame.display.set_mode((screen_width, screen_height))
    main_screen_background_x = 0

    # Déclaration de la liste et des variables liées au joueur

    mc_image_liste = [mc_image_1, mc_image_2, mc_image_3, mc_image_4]
    sc_image_liste = [sc_image_1, sc_image_2, sc_image_3, sc_image_4]
    frame_actuelle_mc = 0
    frame_compteur_mc = 0
    frame_actuelle_sc = 0
    frame_compteur_sc = 0

    mc_image_x = 0
    mc_image_y = 360
    vitesse = 2

    # Boucle du jeu

    running = True
    fin = False
    clock = pygame.time.Clock()

    while running:

        clock.tick(fps)

        # Cette condition nous permet d'animer le background du jeu

        if mc_image_x < ((2700 / 5) * 3) - mc_image_x:

            main_screen_background_x = - 5 * mc_image_x

        else:

            fin = True

        # Ces indications permettent d'afficher les fonds d'écran

        main_screen.blit(main_screen_background, (main_screen_background_x, 0))
        main_screen.blit(main_screen_background, (2700 + main_screen_background_x, 0))
        main_screen.blit(main_screen_background, (2700 * 2 + main_screen_background_x, 0))

        # Ces indications permettent d'afficher les personnages

        main_screen.blit(mc_image_liste[frame_actuelle_mc], (mc_image_x, mc_image_y))
        main_screen.blit(sc_image_liste[frame_actuelle_sc], (sc_image_x, sc_image_y))

        mouvement = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:

            # Contrôle des déplacements vers la droite

            mc_image_x += vitesse
            mouvement = True

        elif keys[pygame.K_SPACE]:

            # Contrôle des sauts

            mc_image_x += vitesse / 2
            mc_image_y -= 10
            mouvement = True

        if mc_image_y < 360 and not (keys[pygame.K_SPACE]):

            # Contrôle de la chute lors des sauts

            mc_image_y = mc_image_y + 20

        sc_image_x += vitesse / 2

        # Gestion de l'animation du joueur principal

        if mouvement:

            frame_compteur_mc += 1

            if frame_compteur_mc % 5 == 0:

                frame_actuelle_mc = (frame_actuelle_mc + 1) % len(mc_image_liste)

        # Gestion de l'animation des joueurs secondaires

        frame_compteur_sc += 1

        if frame_compteur_sc % 10 == 0:

            frame_actuelle_sc = (frame_actuelle_mc + 1) % len(sc_image_liste)

        # Gestion du système de vies

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

        if fin:

            menu()

        # Gestion des obstacles

        verif_pos = mc_image_x % (2700 / 5)

        if 30 < verif_pos < 50 and mc_image_y > 280:

            vie -= 1
            mc_image_x = 0
            mc_image_y = 360

        elif 70 < verif_pos < 90 and mc_image_y > 280:

            vie -= 1
            mc_image_x = 0
            mc_image_y = 360

        elif 160 < verif_pos < 180 and mc_image_y > 280:

            vie -= 1
            mc_image_x = 0
            mc_image_y = 360

        elif 260 < verif_pos < 280 and mc_image_y > 280:

            vie -= 1
            mc_image_x = 0
            mc_image_y = 360

        elif 350 < verif_pos < 370 and mc_image_y > 280:

            vie -= 1
            mc_image_x = 0
            mc_image_y = 360

        elif 390 < verif_pos < 410 and mc_image_y > 280:

            vie -= 1
            mc_image_x = 0
            mc_image_y = 360

        # Gestion de la fermeture de l'écran

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("Le jeu est terminé. Merci d'avoir joué avec nous!")

        pygame.display.update()


def menu():

    """
    Cette procédure génére et affiche tous les éléments du menu.
    Les boutons redirigent respectivement vers : le jeu 1, le jeu 2, l'aide et retour en appelant les différentes
    procédures : jeu_tir_arc(), jeu2(), aide() et menu()
    """

    screen_width = 1080
    screen_height = 720
    fps = 60

    menu_screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Paris Survival Games - Menu")

    font = pygame.font.Font(None, 36)

    logo = pygame.image.load("images/Paris_Survival_Games_Logo.png")

    clock = pygame.time.Clock()

    menu_running = True

    while menu_running:

        clock.tick(fps)
        menu_screen.blit(logo, (-100, -250))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                menu_running = False
                pygame.quit()
                print("Le jeu est terminé.")

            elif event.type == pygame.MOUSEBUTTONDOWN:

                mouse_x, mouse_y = pygame.mouse.get_pos()

                if 450 < mouse_x < 650 and 290 < mouse_y < 340:

                    jeu_tir_arc()

                elif 450 < mouse_x < 650 and 360 < mouse_y < 410:

                    jeu_athletisme()

                elif 450 < mouse_x < 650 and 430 < mouse_y < 480:
                    aide()

                elif 450 < mouse_x < 650 and 500 < mouse_y < 550:
                    pygame.quit()

        # Affichage de personnages (décoration)

        sc_image_1 = pygame.image.load("images/Main_Character_1.png")
        sc_image_1 = pygame.transform.scale_by(sc_image_1, 1.5)
        sc_image_2 = pygame.image.load("images/Gabriel_1.png.png")
        sc_image_2 = pygame.transform.scale_by(sc_image_2, 9)

        menu_screen.blit(sc_image_1, (150, 290))
        menu_screen.blit(sc_image_2, (700, 290))

        # Affichage des boutons

        bouton_jeu1_rect = pygame.Rect(450, 290, 200, 50)
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


menu()
