import pygame
from zoneAffichage import zoneAffichage
from bouton import Button

pygame.init()

screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Scores")

orange = (255, 165, 0)
blanc = (255, 255, 255)
gris = (200, 200, 200)
noir = (0, 0, 0)
rouge = (255, 0, 0)

# Chargement de l'image de fond

background_image = pygame.image.load("volleyball-2.jpg")
background_image = pygame.transform.scale(background_image, (1000,1000))

# Créer des boutons
MoinsGauche = Button(100, 350, 50, 50, gris, gris, rouge, "-", noir)
PlusGauche = Button(250, 350, 50, 50, gris, gris, rouge, "+", noir)
MoinsDroite = Button(700, 350, 50, 50, gris, gris, rouge, "-", noir)
PlusDroite = Button(850, 350, 50, 50, gris, gris, rouge, "+", noir)

# Créer des zones d'affichage avec un score initial de 0
ecranGauche = zoneAffichage(100, 100, 200, 200, blanc, noir, score=0, font_size=200)
ecranDroite = zoneAffichage(700, 100, 200, 200, blanc, noir, score=0, font_size=200)

#Créer les zones d'affichage pour les sets avec un score initial de 0
setGauche = zoneAffichage(350, 175, 75, 75, blanc, noir, score=0)
setDroit = zoneAffichage(575, 175, 75, 75, blanc, noir, score=0)

#Créer les zones d'affichage pour les résultats
résultatsGauche1 = zoneAffichage(400, 300, 75, 75, orange, noir, score="") #voir si on peut laisser les "" ou s'il faut mettre un 0
résultatsGauche2 = zoneAffichage(400, 400, 75, 75, orange, noir, score="")
résultatsGauche3 = zoneAffichage(400, 500, 75, 75, orange, noir, score="")
résultatsGauche4 = zoneAffichage(400, 600, 75, 75, orange, noir, score="")
résultatsGauche5 = zoneAffichage(400, 700, 75, 75, orange, noir, score="")
#rajouter 4 et 5 démerde toi pour les placer ;)
résultatsDroite1 = zoneAffichage(525, 300, 75, 75, orange, noir, score="")
résultatsDroite2 = zoneAffichage(525, 400, 75, 75, orange, noir, score="")
résultatsDroite3 = zoneAffichage(525, 500, 75, 75, orange, noir, score="")
résultatsDroite4 = zoneAffichage(525, 600, 75, 75, orange, noir, score="")
résultatsDroite5 = zoneAffichage(525, 700, 75, 75, orange, noir, score="")
#rajouter 4 et 5 démerde toi pour les placer ;)

running = True
scoreGauche = 0
scoreDroite = 0
scoreSetGauche = 0
scoreSetDroit = 0
nombreSet = 0



# Variable pour éviter les clics multiples
prev_mouse_state = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Récupérer la position de la souris
    mouse_pos = pygame.mouse.get_pos()
    mouse_button = pygame.mouse.get_pressed()[0]  # Vérifier si le bouton gauche de la souris est enfoncé
    
     # Si le bouton est enfoncé et que c'était un nouveau clic (non maintenu)
    if mouse_button and not prev_mouse_state:
        # Vérifier si les boutons sont cliqués et mettre à jour les scores
        if MoinsGauche.is_clicked(mouse_pos, mouse_button):
            scoreGauche -= 1
            ecranGauche.update_score(scoreGauche)  # Met à jour le score de l'écran gauche

        if PlusGauche.is_clicked(mouse_pos, mouse_button):
            scoreGauche += 1
            ecranGauche.update_score(scoreGauche)

        if MoinsDroite.is_clicked(mouse_pos, mouse_button):
            scoreDroite -= 1
            ecranDroite.update_score(scoreDroite)

        if PlusDroite.is_clicked(mouse_pos, mouse_button):
            scoreDroite += 1
            ecranDroite.update_score(scoreDroite)

        # Si la souris n'est pas enfoncée, on réinitialise l'état du clic
    if not mouse_button:
        prev_mouse_state = False
    else:
        prev_mouse_state = True

    # Verification si set gagné
    if scoreGauche >= 25:
        differenceScore = abs(scoreGauche - scoreDroite)
        if differenceScore >= 2:
            scoreSetGauche += 1
            setGauche.update_score(scoreSetGauche)  # Met à jour le score de l'écran gauche
            nombreSet +=1
            if nombreSet == 1:
                résultatsGauche1.update_score(scoreGauche)
                résultatsDroite1.update_score(scoreDroite)
            if nombreSet == 2:
                résultatsGauche2.update_score(scoreGauche)
                résultatsDroite2.update_score(scoreDroite)               
            if nombreSet == 3:
                résultatsGauche3.update_score(scoreGauche)
                résultatsDroite3.update_score(scoreDroite)
            if nombreSet == 4:
                résultatsGauche4.update_score(scoreGauche) # faut rajouter les variable en haut
                résultatsDroite4.update_score(scoreDroite)
            if nombreSet == 5:
                résultatsGauche5.update_score(scoreGauche)
                résultatsDroite5.update_score(scoreDroite)
            
            scoreGauche = 0
            ecranGauche.update_score(scoreGauche)
            scoreDroite = 0
            ecranDroite.update_score(scoreDroite)
            
    if scoreDroite >= 25:
        differenceScore = abs(scoreGauche - scoreDroite)
        if differenceScore >= 2:
            scoreSetDroit += 1
            setDroit.update_score(scoreSetDroit)  # Met à jour le score de l'écran droit
            nombreSet +=1
            if nombreSet == 1:
                résultatsGauche1.update_score(scoreGauche)
                résultatsDroite1.update_score(scoreDroite)
            if nombreSet == 2:
                résultatsGauche2.update_score(scoreGauche)
                résultatsDroite2.update_score(scoreDroite)               
            if nombreSet == 3:
                résultatsGauche3.update_score(scoreGauche)
                résultatsDroite3.update_score(scoreDroite)
            if nombreSet == 4:
                résultatsGauche4.update_score(scoreGauche) # faut rajouter les variable en haut
                résultatsDroite4.update_score(scoreDroite)
            if nombreSet == 5:
                résultatsGauche5.update_score(scoreGauche)
                résultatsDroite5.update_score(scoreDroite)
            scoreGauche = 0
            ecranGauche.update_score(scoreGauche)
            scoreDroite = 0
            ecranDroite.update_score(scoreDroite)
               
    

    # Remplir la fenêtre avec la couleur orange
    screen.blit(background_image, (0, 0))

    # Dessiner les boutons et les zones d'affichage
    MoinsGauche.draw(screen, mouse_pos)
    MoinsDroite.draw(screen, mouse_pos)
    PlusGauche.draw(screen, mouse_pos)
    PlusDroite.draw(screen, mouse_pos)

    ecranGauche.draw(screen)
    ecranDroite.draw(screen)
    setGauche.draw(screen)
    setDroit.draw(screen)

    résultatsGauche1.draw(screen)
    résultatsGauche2.draw(screen)
    résultatsGauche3.draw(screen)
    résultatsGauche4.draw(screen)
    résultatsGauche5.draw(screen)
    résultatsDroite1.draw(screen)
    résultatsDroite2.draw(screen)
    résultatsDroite3.draw(screen)
    résultatsDroite4.draw(screen)
    résultatsDroite5.draw(screen)

    # Mettre à jour l'affichage
    pygame.display.flip()

pygame.quit()
