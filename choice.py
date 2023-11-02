import pygame

# Définition des couleurs et initialisation de Pygame
COULEUR_FOND = (255, 255, 255)
ORANGE = (237, 127, 16)
RED = (198, 0, 0)
BLUE = (0, 123, 198)
WHITE = (255, 255, 255)
pygame.init()

# Chargement des images et dimensions de la fenêtre
fond = pygame.image.load("fond.jpg")
LARGEUR, HAUTEUR = fond.get_size()
fen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Projet")
fen.fill(COULEUR_FOND)
fond = fond.convert()

LARGEUR_REC_CHOICE = 300
HAUTEUR_REC_CHOICE = 60

# Chargement et préparation des images
joueur = pygame.image.load("joueur.png").convert()
petit_joueur = pygame.transform.scale(joueur, (joueur.get_width() // 16, joueur.get_height() // 16))
petit_joueur = petit_joueur.convert_alpha()

presentateur = pygame.image.load("presentateur.png").convert()
presentateur.set_colorkey((0, 0, 0))
petit_presentateur = pygame.transform.scale(presentateur, (presentateur.get_width() // 20, presentateur.get_height() // 20))
petit_presentateur = petit_presentateur.convert_alpha()

# Textes pour les différentes difficultés
police_choice = pygame.font.Font("police.ttf", 20)
msg_easy = police_choice.render("Easy", True, WHITE)
msg_medium = police_choice.render("Medium", True, WHITE)
msg_hard = police_choice.render("Hard", True, WHITE)

etat_jeu = "choix_difficultes"

# Initialisation des rectangles
rect_blue_choice = pygame.Rect(156, 60, LARGEUR_REC_CHOICE, HAUTEUR_REC_CHOICE)
rect_orange_choice = pygame.Rect(156, 160, LARGEUR_REC_CHOICE, HAUTEUR_REC_CHOICE)
rect_red_choice = pygame.Rect(156, 260, LARGEUR_REC_CHOICE, HAUTEUR_REC_CHOICE)

def afficher_elements_choice():
    fen.blit(petit_joueur, (520, 150))
    fen.blit(petit_presentateur, (20, 150))
    pygame.draw.rect(fen, BLUE, rect_blue_choice)
    pygame.draw.rect(fen, ORANGE, rect_orange_choice)
    pygame.draw.rect(fen, RED, rect_red_choice)
    fen.blit(msg_easy, (280, 80))
    fen.blit(msg_medium, (270, 180))
    fen.blit(msg_hard, (280, 280))


def gerer_evenements_choice():
    global etat_jeu
    continuer = True
    while continuer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
            elif event.type == pygame.MOUSEBUTTONUP:
                if rect_blue_choice.collidepoint(event.pos):
                    etat_jeu = "en_cours_easy"
                    print(" --> Easy")
                    print(etat_jeu)
                elif rect_orange_choice.collidepoint(event.pos):
                    etat_jeu = "en_cours_medium"
                    print(" --> Medium")
                    print(etat_jeu)
                elif rect_red_choice.collidepoint(event.pos):
                    etat_jeu = "en_cours_hard"
                    print(" --> Hard")
                    print(etat_jeu)
        afficher_elements_choice()

def main():
    global etat_jeu
    fen.blit(fond, (0, 0))
    afficher_elements_choice()
    pygame.display.flip()
    gerer_evenements_choice()
    
    pygame.quit()

if __name__ == "__main__":
    main()
