import pygame


# Couleur du fond de la fenête
COULEUR_FOND = (255, 255, 255)
# Couleur questions - réponses
QUEST_FOND  = (46, 46, 46) 
QUEST_TEXTE = (34, 198, 0)
ORANGE = (237, 127, 16)
WHITE = (255, 255, 255)
pygame.init()


fond = pygame.image.load("fond.jpg")
print("Dimension de l'image du fond", fond.get_size())

# Les dimensions de la fenêtre sont celles de l'image du bambou
LARGEUR, HAUTEUR = fond.get_size()

# Initialisation de la fenêtre pygame
fen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Projet")
fen.fill(COULEUR_FOND)

# Préparation de de l'image du bambou à son utilisation dans pygame
fond = fond.convert()

LARGEUR_REC = 120
HAUTEUR_REC = 50

police = pygame.font.Font("police.ttf", 16)
msg_clic = police.render("Clique ici", True, WHITE)

# Chargement et préparation des images
joueur = pygame.image.load("joueur.png").convert()
petit_joueur = pygame.transform.scale(joueur, (joueur.get_width() // 16, joueur.get_height() // 16))
petit_joueur = petit_joueur.convert_alpha()

regles = pygame.image.load("regles.png").convert()
petit_regles = pygame.transform.scale(regles, (regles.get_width() // 1.6, regles.get_height() // 1.6))
petit_regles = petit_regles.convert_alpha()

etat_jeu = "choix_difficultes"
presentateur = pygame.image.load("presentateur.png").convert()
presentateur.set_colorkey((0, 0, 0))  # Remplace la couleur (0, 0, 0) - Noir en transparence
petit_presentateur = pygame.transform.scale(presentateur, (presentateur.get_width() // 20, presentateur.get_height() // 20))
petit_presentateur = petit_presentateur.convert_alpha()

# Affichage du bambou aux coordonnées précisées en second argument
fen.blit(fond, (0, 0))
fen.blit(petit_joueur, (420, 20))
fen.blit(petit_regles, (40, 140))
fen.blit(petit_presentateur, (120, 20))
# Dessiner les deux rectangles
rect_orange = pygame.draw.rect(fen, ORANGE, [246, 40, LARGEUR_REC, HAUTEUR_REC])
fen.blit(msg_clic, (255,55))
etat_jeu = "debut"
print (etat_jeu)
continuer = True

while continuer:
    for event in pygame.event.get():
        # L'utilisateur veut-il fermer la fenêtre ?
        if event.type == pygame.QUIT:
            continuer = False
        # L'utilisateur a-t-il relâché un bouton de souris
        elif event.type == pygame.MOUSEBUTTONUP:
            print("up", event.pos)
                
            if rect_orange.collidepoint(event.pos):
                print(" --> Orange")
                etat_jeu = "choix_difficultes"
                print (etat_jeu)

                
                
    pygame.display.flip()

pygame.quit()

