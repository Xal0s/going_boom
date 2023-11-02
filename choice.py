import pygame


# Couleur du fond de la fenête
COULEUR_FOND = (255, 255, 255)
# Couleur questions - réponses
QUEST_FOND  = (46, 46, 46) 
QUEST_TEXTE = (34, 198, 0)
ORANGE = (237, 127, 16)
RED = (198, 0, 0)
BLUE = (0, 123, 198)
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

LARGEUR_REC = 300
HAUTEUR_REC = 60

police = pygame.font.Font("police.ttf", 20)
msg_easy = police.render("Easy", True, WHITE)
msg_medium = police.render("Medium", True, WHITE)
msg_hard = police.render("Hard", True, WHITE)

# Chargement et préparation des images
joueur = pygame.image.load("joueur.png").convert()
petit_joueur = pygame.transform.scale(joueur, (joueur.get_width() // 16, joueur.get_height() // 16))
petit_joueur = petit_joueur.convert_alpha()

regles = pygame.image.load("regles.png").convert()
petit_regles = pygame.transform.scale(regles, (regles.get_width() // 1.6, regles.get_height() // 1.6))
petit_regles = petit_regles.convert_alpha()


presentateur = pygame.image.load("presentateur.png").convert()
presentateur.set_colorkey((0, 0, 0))  # Remplace la couleur (0, 0, 0) - Noir en transparence
petit_presentateur = pygame.transform.scale(presentateur, (presentateur.get_width() // 20, presentateur.get_height() // 20))
petit_presentateur = petit_presentateur.convert_alpha()

# Affichage du bambou aux coordonnées précisées en second argument
fen.blit(fond, (0, 0))
fen.blit(petit_joueur, (520, 150))

fen.blit(petit_presentateur, (20, 150))
rect_blue = pygame.draw.rect(fen, BLUE, [156, 60, LARGEUR_REC, HAUTEUR_REC])
rect_orange = pygame.draw.rect(fen, ORANGE, [156, 160, LARGEUR_REC, HAUTEUR_REC])
rect_red = pygame.draw.rect(fen, RED, [156, 260, LARGEUR_REC, HAUTEUR_REC])
fen.blit(msg_easy, (280,80))
fen.blit(msg_medium, (270,180))
fen.blit(msg_hard, (280,280))
etat_jeu = "choix_difficultes"
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
                
            if rect_blue.collidepoint(event.pos):
                print(" --> Easy")
                etat_jeu = "en_cours"
                print (etat_jeu)
            if rect_orange.collidepoint(event.pos):
                print(" --> Medium")
                etat_jeu = "en_cours_medium"
                print (etat_jeu)
            if rect_red.collidepoint(event.pos):
                print(" --> Hard")
                etat_jeu = "en_cours_hard"
                print (etat_jeu)

                
                
    pygame.display.flip()

pygame.quit()


